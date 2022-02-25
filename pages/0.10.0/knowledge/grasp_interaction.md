---
title: Grasp Interaction
sidebar: main_sidebar_0_10_0
keywords: grasp, static_grasp, dynamic_grasp, jump_grasp, trigger_grasp, preview_grasp, preview_only, sticky_hand
permalink: grasp_interaction.0.10.0.html
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
* there is no dependency on accurate finger tracking controllers (see [controllers](controllers.0.10.0.html)), and
* users don't need to spend a lot of cognitive load to carefully place the fingers around the object.

In this page we first describe the process of how VG creates object grasp interaction,
* [From Object Selection to Grasp Synthesis](#from-object-selection-to-grasp-synthesis)

and then explain a set of parameters to configure and fine-tune the grasp interaction experiences in your VR application:
* [Grasp Synthesis Method](#grasp-synthesis-method)
* [Grasp Interaction Type](#grasp-interaction-type)
* [Grasp Speed and Release Speed](#grasp-speed-and-release-speed)

### From Object Selection to Grasp Synthesis

In VR, grasp interaction consists of two consecutive processes:
1. {% include tooltip.html tooltip="ObjectSelection" text="object selection" %}, and
2. {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %}

VirtualGrasp provides an object selection mechanism through checking collisions between a grasp selection sphere attached to the hand and the objects, and choosing the "closest" object for grasping. 
Note this process is done in the VirtualGrasp library, and no collider setup or physical simulation is needed in any client engines. 

And once an object is selected by a hand, it is ready for grasp synthesis. 

<!--In a typical <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">interaction type</a> (like <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.TriggerGrasp}}">trigger grasp</a>, or <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JumpGrasp}}">jump grasp</a> ), grasp synthesis on an object happens if the user triggers grasp while this hand has selected this object. 
-->

### Grasp Synthesis Method

Grasp synthesis refers to the runtime process of creating hand {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} -- the wrist and fingers pose  w.r.t the object -- when an user triggers grasp with VR controllers.

VG provides two alternative methods for grasp synthesis {% include tooltip.html tooltip="StaticGrasp" text="static grasp" %} (SG) and {% include tooltip.html tooltip="DynamicGrasp" text="dynamic grasp" %} (DG). 

<table border="1">
<colgroup>
<col width="40%" />
<col width="10%" />
<col width="10%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" style="text-align: right">Static Grasp</th>
<th colspan="2">Dynamic Grasp</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span" colspan="2" style="text-align: right">
**Static Grasp** (SG) creates grasp configurations from one of N grasps stored in a grasp database.<!-- While full baking is needed, it only uses grasp baking results during runtime.are created by a limited set of grasps around an object depending on a pre-baked grasp database.--></td>
<td markdown="span" colspan="2">**Dynamic Grasp** (DG) computes grasp configurations at the moment of grasp triggering.<!--While full baking is currently enabled (so one can switch between static and dynamic grasping per object), it only uses shape baking results. --><!--are unlimited grasps that are generated during runtime.--></td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Limited number of and sparse grasps unless parameterized to be denser</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Infinite, flexible grasps</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">No overhead during runtime (simple DB access)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Some negligible overhead during runtime (generative algorithm)</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Hand-sensor-immersion breaks due to sparse grasps.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Hand-sensor-immersion does not break.</td>
</tr>
<!--
<tr>
<td markdown="span" style="text-align: right">Can use GraspStudio to add primary grasps so can ensure high quality grasps through 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JumpPrimaryGrasp}}">Jump Primary Grasp</a></td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Not possible to control grasp quality since it is computed in runtime by an algorithm</td>
</tr>

<tr>
<td markdown="span" style="text-align: right">Difficult to transfer animation signals tuned for one hand to another (needs motion retargeting)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Potentially no need to transfer animation signals tuned for one hand to another.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Difficult to re-use the results of one hand with another (grasp transfer)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">No need to re-use the results of one hand with another.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Grasp baking time</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Only shape baking time</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Potentially high baking time dependent on object complexity.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Low baking time if only dynamic grasps are needed.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Higher baking time dependent on number of grasp types supported</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Grasp types are more freely chosen by the user and our internal algorithms, depending on how the user places wrist/fingers around an object.</td>
</tr>
-->
</tbody>
</table>


To create natural-looking {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} during {% include tooltip.html tooltip="GraspSynthesisMethod" text="grasp synthesis" %}, we need to [bake the object](object_baking.0.10.0.html#object-baking).
The baking output of objects is a grasp database which will enable DG for any humanoid hands.

In the situations when you need to use SG (see section [choosing synthesis method and interaction type](#choosing-synthesis-method-and-interaction-type)), 
[grasp studio](unity_component_vggraspstudio.0.10.0.html#grasp-studio) can be used to add grasps into database through DG. 

### Grasp Interaction Type

As we mentioned in [background](#background) section, when a user triggers grasp, the wrist may not be at a good pose w.r.t. the object. VG's grasp synthesis algorithm will "correct" this "mis-placement" of wrist, and create a {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} with a wrist pose different from the {% include tooltip.html tooltip="SensorPose" text="sensor pose" %} at the moment of grasp triggering. 
Because of this difference, there are different alternative solutions to pose the object-hand grasp ensemble, which will create different user experiences: 


| Interaction Type | Description | Considerations |
|-------|--------|---------|
| Trigger Grasp | when user triggers grasp, hand moves to the wrist pose in the synthesized {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} around the object | since hand moves away from {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}, this could break hand-sensor immersions| 
| Jump Grasp | when user triggers grasp, object jumps to the grasped position in the hand | object directly moves upon grasp triggering, which may not be suitable for performing some tasks requiring physical stability (e.g. play a Jenga game)  | 
| Jump Primary Grasp | when user triggers grasp, object jumps to the grasped position in the hand, using the labeled primary grasp(s) in the grasp DB | using primary grasp(s) is needed particularly in situations when an object should be grasped in some particular ways (e.g. how to grasp scissors)| 
| Preview Grasp | once user selected an object, the {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} is previewed on the object, so that user can push the trigger button to pick up the object if the grasp is satisfactory | since {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} is running at every frame when object is selected, when DG is used can leads to low frame rate | 
| Preview Only | once user selected an object, the {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} is previewed on the object, and the grasp trigger won't take effect to pick up object | since grasp synthesis process is running at every frame when object is selected, when DG is used can leads to low frame rate | 
| Sticky Hand | a fall-back solution when object is not baked, so the grasp configuration is directly taken from the hand pose at the moment of grasp triggering, as if hand is stick to the object.  | this allows VR developers to setup the {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behaviors" %} through [object articulation](object_articulation.0.10.0.html) before baking objects | 


### Choosing Synthesis Method and Interaction Type

As explained in the previous sections, selecting different combinations of {% include tooltip.html tooltip="GraspSynthesisMethod" text="synthesis method" %} and {% include tooltip.html tooltip="InteractionType" text="interaction type" %} will create different user experiences. 
Due to the nature of each option, there may be preferences of how to combine the two parameters. The table below gives some hints: 

| Interaction Type | Synthesis Method | Evaluation |
|-------|--------|---------|
| Trigger Grasp | DG | &#x2611; Good since DG create grasp pose with the wrist close to {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}, so hand will not move so much. | 
| Trigger Grasp | SG |  &#x2612; Not recommended since when there is sparse grasps in DB, hand will move far away from {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}, breaking the hand-sensor immersion. | 
| Jump Grasp | DG | &#x2611; Good since DG create grasp pose that is close to {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}, so object will not jump too much.  | 
| Jump Grasp | SG | &#x2611; Ok as long as the object's big jump is not a problem at the moment of grasping.  | 
| Jump Primary Grasp | DG | &#x2612; Not possible since {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasp" %} is grasp(s) in the DB which is only used during SG synthesis.| 
| Preview Grasp | DG | &#x2611; Good and recommend to be used in Grasp Studio when adding grasps to the DB through DG. | 
| Preview Grasp | SG | &#x2612; Not recommended since at preview phase hand will be very jumpy due to sparse grasps in the DB. | 
| Preview Only | DG | &#x2611; Good and recommend to be used in Grasp Studio when adding grasps to the DB through DG. | 
| Preview Only | SG | &#x2612; Not recommended since at preview phase hand will be very jumpy due to sparse grasps in the DB. | 
| Sticky Hand | -- | Sticky Hand is a fall back solution when objects are not baked, so no SG or DG is relevant. | 


### Grasp Animation Speed and Release Animation Speed

{% include image.html file="unity/unity_vg_global_grasp_interaction_0.10.0.png" alt="VG Global Grasp Interaction Settings" caption="MyVirtualGrasp script - Global Grasp Interaction Settings" %}
In global grasp interaction settings, you can set the default {% include tooltip.html tooltip="GraspSynthesisMethod" text="synthesis method" %} and {% include tooltip.html tooltip="InteractionType" text="interaction type" %} for all objects in the scene globally. 
The other two parameters -- {% include tooltip.html tooltip="GraspSpeed" text="grasp animation speed" %} and {% include tooltip.html tooltip="ReleaseSpeed" text="release animation speed" %} -- also significantly affect the user experiences because they determines how fast the hand forms grasp and releases from grasp respectively. 

The unit of these values are in (second), so if {% include tooltip.html tooltip="GraspSpeed" text="grasp animation speed" %} is 0.1, it means it takes 0.1 second starting from grasp triggering for the hand to form a complete {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} on the object.

If {% include tooltip.html tooltip="ReleaseSpeed" text="release animation speed" %} is 0.1, it means it takes 0.1 second starting from release triggering for the hand to move from {% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} on the object back to its {% include tooltip.html tooltip="SensorPose" text="sensor pose" %}.

{% include tip.html content="For grasp animation speed, lower value means faster grasp, for release animation speed, lower value means faster release." %}

{% include important.html content="For both grasp and release animation speed, there is a minimum allowed value. So any value specified in the GUI that is smaller than the min value will be clamped to this min value." %}

### Throw Velocity Scale and Throw Angular Velocity Scale

The two velocity scales allow you to scale up and down throwing power when an object is released from all grasping hands. 
Throw Velocity Scale is to scale how fast object translate, while throw angular velocity scale is to scale how fast object rotate. 