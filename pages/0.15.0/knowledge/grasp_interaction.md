---
title: Grasp Interaction
sidebar: main_sidebar_0_15_0
keywords: grasp, static_grasp, dynamic_grasp, jump_grasp, trigger_grasp, preview_grasp, preview_only, sticky_hand
permalink: grasp_interaction.0.15.0.html
folder: knowledge
toc: true
---

### Background
To create immersive interactive experiences in a virtual environment is difficult because physical constraints and haptic sensations can not be fully reproduced with today's VR software and hardware technology. 
This is especially challenging when we want to have hand presence in VR while grasping and manipulating objects. 

For example, when a user places the avatar hand close to an object and triggers the grasp button to initiate grasp interaction, he or she can not guarantee that the wrist is perfectly placed so that just closing fingers around the object can generate a natural-looking {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} on the selected object. While in real life such a problem is trivial since we can always rely on our fast sensory-motor feedback loop to correct our hand and finger poses, in VR such a feedback does not exist. 

VirtualGrasp fills in the gaps of lacking sensory-motor feedback, and uses a generative grasp synthesis algorithm to 
create immersive grasp interacting experiences in VR.

VG enables robust grasp interactions. Compared to many physics-based grasp synthesis solutions in the market VG takes a different approach by exploiting “object intelligence”. By analyzing shape and affordances of an object model in VR, we can synthesize grasp configurations on a hand with just the knowledge of where the wrist is, and without any dependence of expensive physical simulations. As a result,
* there is no dependency on accurate finger tracking controllers (see [controllers](controllers.0.15.0.html)), and
* users don't need to spend a lot of cognitive load to carefully place the fingers around the object.

In this page we first describe the process of how VG creates object grasp interaction,
* [From Object Selection to Grasp Synthesis](#from-object-selection-to-grasp-synthesis)

and then explain a set of parameters to configure and fine-tune the grasp interaction experiences in your VR application:
* [Grasp Button](l#grasp-button)
* [Grasp Synthesis Method](#grasp-synthesis-method)
* [Grasp Interaction Type](#grasp-interaction-type)
* [Grasp Speed and Release Speed](#grasp-speed-and-release-speed)
* [Throw Velocity and Angular Velocity Scales](#throw-velocity-scale-and-throw-angular-velocity-scale)

{% include image.html file="unity/unity_vg_global_grasp_interaction_0_15_0.png" alt="VG Global Grasp Interaction Settings" caption="MyVirtualGrasp script - Global Grasp Interaction Settings (Unity)" %}

### From Object Selection to Grasp Synthesis

In VR, grasp interaction consists of two consecutive processes:
1. {% include tooltip.html tooltip="ObjectSelection" text="object selection" %}, and
2. {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %}

VirtualGrasp provides an object selection mechanism through checking collisions between a grasp selection sphere attached to the hand and the objects, and choosing the "closest" object for grasping. 
Note this process is done in the VirtualGrasp library, and no collider setup or physical simulation is needed in any client engines. 

And once an object is selected by a hand, it is ready for grasp synthesis. 

<!--In a typical <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">interaction type</a> (like <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.TriggerGrasp}}">trigger grasp</a>, or <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JumpGrasp}}">jump grasp</a> ), grasp synthesis on an object happens if the user triggers grasp while this hand has selected this object. 
-->

### Grasp Button

When a hand-held VR controller is used (as opposed to finger tracking devices), you can control which button on the controller to use for grasp triggering.

| Button | Description |
|-------|--------|
| TRIGGER | The trigger button will be used to trigger grasp. | 
| GRIP | The grip button will be used to trigger grasp. | 
| GRIP OR TRIGGER | Either the grip or trigger button can be used to trigger grasp. | 

### Grasp Synthesis Method

Grasp synthesis refers to the runtime process of creating hand {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} -- the wrist and fingers pose  w.r.t the object -- when an user triggers grasp with VR controllers. 
There are two alternative grasp synthesis methods -- {% include tooltip.html tooltip="StaticGrasp" text="static grasp" %} (SG) and {% include tooltip.html tooltip="DynamicGrasp" text="dynamic grasp" %} (DG). 
{% include tooltip.html tooltip="StaticGrasp" text="Static grasp" %} is an easy alternative since it simply searches for the closest {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} in a grasp database, and apply it to the hand. However it is also a very rigid approach so that each object can only be grasped in a few limited ways. 
Therefore, VirtualGrasp offers a much more advanced, flexible grasp synthesis method -- {% include tooltip.html tooltip="DynamicGrasp" text="Dynamic grasp" %} -- which compute the {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} dynamically in runtime. To speed this process up to meet the runtime {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} requirement, we need to [bake the object](object_baking.0.15.0.html#object-baking).
The baking output of objects is a grasp database which will enable DG for any humanoid hands.

In the situations when you do want to grasp an object with a set of fixed ways, [VG_GraspAnotator](unity_component_vggraspstudio.0.15.0.html) can be used to add {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasp" %} into the grasp DB. 

{% include important.html content="From this VG version (0.15.0), Grasp Synthesis Method is not exposed as a parameter for grasp interaction setting to avoid confusion caused by how to combine with Grasp Interaction Type. So whenever Jump Primary Grasp is selected as Grasp Interaction Type, Grasp Synthesis Method will be switched to Static Grasp internally in VG, otherwise by default Dynamic Grasp Synthesis Method is used." %}

### Grasp Interaction Type

As we mentioned in [background](#background) section, when a user triggers grasp, the wrist may not be at a good pose w.r.t. the object. VG's grasp synthesis algorithm will "correct" this "mis-placement" of wrist, and create a {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} with a wrist pose different from the {% include tooltip.html tooltip="SensorPose" text="sensor pose" %} at the moment of grasp triggering. 
Because of this difference, there are different alternative solutions to pose the object-hand grasp ensemble, which will create different user experiences: 


| Interaction Type | Description | Considerations |
|-------|--------|---------|
| Trigger Grasp | when user triggers grasp, hand moves to the wrist pose in the {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized" %} {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} around the object.  | since hand moves away from {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}, this could break hand-sensor immersions if synthesized grasp is far away. However since {% include tooltip.html tooltip="DynamicGrasp" text="dynamic grasp" %} is used, the distance is small.| 
| Jump Grasp | when user triggers grasp, object jumps to the {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized" %} grasped position in the hand. | object directly moves upon grasp triggering, which may not be suitable for performing some tasks requiring physical stability (e.g. play a Jenga game).  | 
| Jump Primary Grasp | when user triggers grasp, object jumps to the {% include tooltip.html tooltip="StaticGrasp" text="statically synthesized" %}  grasp position in the hand, using the added primary grasp(s) in the grasp DB | using primary grasp(s) is needed particularly in situations when an object should be grasped in some particular ways (e.g. how to grasp scissors). **Note**: to use this interaction type, you should have added some primary grasps in to grasp DB through [VG_GraspAnotator](unity_component_vggraspstudio.0.15.0.html#grasp-studio). If no primary grasps added, interaction will fall back to Jump Grasp.| 
| Preview Grasp | once user selected an object, the {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} is previewed on the object, so that user can push the trigger button to pick up the object if the grasp is satisfactory. | since {% include tooltip.html tooltip="DynamicGrasp" text="dynamical" %} {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} is running at every frame when object is selected, it can result in low frame rate. | 
| Preview Only | once user selected an object, the {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} is previewed on the object, and the grasp trigger won't take effect to pick up object. | since {% include tooltip.html tooltip="DynamicGrasp" text="dynamical" %} {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} is running at every frame when object is selected, it can result in low frame rate. | 
| Sticky Hand | a fall-back solution when object is not baked, so the grasp configuration is directly taken from the hand pose at the moment of grasp triggering, as if the hand is sticking to the object.  | this allows VR developers to setup the {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behaviors" %} through [object articulation](object_articulation.0.15.0.html) before baking objects. | 


### Grasp Animation Speed and Release Animation Speed

{% include tooltip.html tooltip="GraspSpeed" text="Grasp animation speed" %} and {% include tooltip.html tooltip="ReleaseSpeed" text="release animation speed" %} determines how fast the hand forms grasp and releases from grasp respectively, hence also significantly affect the user experiences when interacting with an object. 

The unit of these values are in (second), so if {% include tooltip.html tooltip="GraspSpeed" text="grasp animation speed" %} is 0.1, it means it takes 0.1 second starting from grasp triggering for the hand to form a complete {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} on the object.
If {% include tooltip.html tooltip="ReleaseSpeed" text="release animation speed" %} is 0.1, it means it takes 0.1 second starting from release triggering for the hand to move from {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} on the object back to its {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}.

{% include tip.html content="For grasp animation speed, lower value means faster grasp, for release animation speed, lower value means faster release." %}

{% include important.html content="For both grasp and release animation speed, there is a minimum allowed value. So any value specified in the GUI that is smaller than the min value will be clamped to this min value." %}

### Throw Velocity Scale and Throw Angular Velocity Scale

The two velocity scales allow you to scale up and down throwing power when an object is released from all grasping hands. 
Throw Velocity Scale is to scale how fast object translate, while throw angular velocity scale is to scale how fast object rotate. 