---
title: Knowledge Base - Grasp Interaction
sidebar: knowledge_sidebar
keywords: grasp, static_grasp, dynamic_grasp, jump_grasp, trigger_grasp, preview_grasp, preview_only, sticky_hand
permalink: grasp_interaction.html
folder: knowledge
toc: true
---

### Background
To create immersive interactive experiences in a virtual environment is difficult because physical constraints and haptic sensations can not 
be fully reproduced with today's VR software and hardware technology. 
This is especially challenging when we want to have hand presence in VR while grasping and manipulating objects. 

For example, when a user places the avatar hand close to an object and triggers the grasp button to initiate grasp interaction, he or she can not guarrantee
that the wrist is perfectly placed so that just closing fingers around the object can generate a natural-looking grasp configuration on the 
selected object. While in real life such a problem is trivial since we can always rely on our fast and advanced sensory-motor feedback
loop to correct our hand and finger poses, in VR such a feedback does not exist. 

VirtualGrasp fills in the gaps of lacking sensory-motor feedback, and uses a generative grasp synthesis algorithm to 
create immersive grasp interacting experiences in VR.

In this page we first describe the process of how VG create hand object grasp interaction,
* From Object Selection to Grasp Synthesis

and then explain a set of parameters to configure and fine-tune the grasp interaction experiences in your VR application.
* Grasp Synthesis Method, or in short, Synthesis Method 
* Grasp Interaction Type, or in short, Interaction Type
* Grasp Speed and Release Speed

### From Object Selection to Grasp Synthesis

In VR, grasp interaction consists of two consecutive processes:
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ObjectSelection}}">Object Selection</a>
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Grasp Synthesis</a>

VirtualGrasp provides an <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ObjectSelection}}">Object Selection</a>
mechanism through checking collision between a grasp selection sphere attached to the hand and the objects,
and choose the "closest" object for grasp. Note this process is done in VirtualGrasp library,
not through physical collision detection in any client engines. 

And once an object is selected by a hand, it is ready for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Grasp Synthesis</a>. 
In a typical <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">Interaction Type</a> (like 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.TriggerGrasp}}">Trigger Grasp</a>, or
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JumpGrasp}}">Jump Grasp</a> ), Grasp Synthesis on an object only happens if
the user triggers grasp while this hand has selected this object. 

### Grasp Synthesis Method

<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Grasp Synthesis</a>
refers to the runtime process of creating hand grasping configuration -- the wrist and fingers pose  w.r.t the object -- when an user triggers grasp with VR controllers.
The method for grasp synthesis refers to how this process is done. 

VG provides two alternative methods for grasp synthesis <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StaticGrasp}}">Static Grasp</a> (SG) 
and <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.DynamicGrasp}}">Dynamic Grasp</a> (DG). 

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
**Static Grasp** (SG) creates grasping configuration from one of N grasps stored in a grasp database.<!-- While full baking is needed, it only uses grasp baking results during runtime.are created by a limited set of grasps around an object depending on a pre-baked grasp database.--></td>
<td markdown="span" colspan="2">**Dynamic Grasp** (DG) computes grasping configuration at the moment of grasp triggering.<!--While full baking is currently enabled (so one can switch between static and dynamic grasping per object), it only uses shape baking results. --><!--are unlimited grasps that are generated during runtime.--></td>
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
<td markdown="span">Some overhead during runtime (generative algorithm)</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Hand-sensor-immersion breaks due to sparse grasps.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Hand-sensor-immersion does not break.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Can use GraspStudio to add primary grasps so can ensure high quality grasps through 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JumpPrimaryGrasp}}">Jump Primary Grasp</a></td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Not possible to control grasp quality since it is computed in runtime by an algorithm</td>
</tr>
<!--
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

### Grasp Interaction Type

As we mentioned in [Background](#background) section, when a user triggers grasp, the wrist may not be at a good pose w.r.t. the object.
VG's grasp synthesis algorithm will "correct" this "mis-placement" of wrist, and create a grasp configuration
with a wrist pose different from the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorPose}}">Sensor Pose</a> at the moment of grasp triggering. 
Because of this difference, there are different alternative solutions to pose the object-hand grasp ensemble that will create different user experiences: 


| Interaction Type | Description | Considerations |
|-------|--------|---------|
| Trigger Grasp | when user triggers grasp, hand moves to the wrist pose in the synthesized grasp configuration around the object | since hand moves away from <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorPose}}">Sensor Pose</a>, this could break sensor-motor immersion| 
| Jump Grasp | when user triggers grasp, object jumps to the grasped position in the hand | object directly moves upon grasp triggering, which may not be suitable for performing some tasks requiring physical stability (e.g. play Jenga game)  | 
| Jump Primary Grasp | when user triggers grasp, object jumps to the grasped position in the hand, using the labeled primary grasp(s) in the grasp DB | using primary grasp(s) is needed particularly in situations when an object should be grasped in one or more particular ways, e.g. how to grasp a gun| 
| Preview Grasp | once user selected an object, the grasp configuration is previewed on the object, so that user can push the trigger button to pick up the object if the grasp is satisfactory | since grasp synthesis process is running at every frame when object is selected, when computationally heavy DG is used, this can be slow | 
| Preview Only | once user selected an object, the grasp configuration is previewed on the object, and the grasp trigger won't take effect to pick up object | since grasp synthesis process is running at every frame when object is selected, when computationally heavy DG is used, this can be slow | 
| Sticky Hand | a fall-back grasp interaction type when object is not baked, where the grasp configuration is directly taken from the hand pose at the moment of grasp triggering as if hand is stick to the object.  | the fall back solution will be active when interactable objects have not been baked | 


### Choosing Synthesis Method and Interaction Type

As explained in the previous sections, selecting different combinitions of synthesis method and interaction type will create different user experiences. 
Due to the nature of each option, there may be preferences of how to combine the two parameters. The table below gives some hints: 


| Interaction Type | Synthesis Method | Evaluation |
|-------|--------|---------|
| Trigger Grasp | DG | &#x2611; Good since DG create grasp pose that is close to <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorPose}}">Sensor Pose</a>, so hand will not move so much.  | 
| Trigger Grasp | SG |  &#x2612; Not recommended since when there is sparse grasps in DB, hand will move far away from <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorPose}}">Sensor Pose</a>, breaking immersion | 
| Jump Grasp | DG | &#x2611; Good since DG create grasp pose that is close to <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorPose}}">Sensor Pose</a>, so object will not jump too much.  | 
| Jump Grasp | SG | &#x2611; Ok as long as the object's big jump is not a problem a the moment of grasping.  | 
| Jump Primary Grasp | DG | &#x2612; Not possible since <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PrimaryGrasp}}">Primary Grasp</a> is grasp(s) in the DB which is only used during SG synthesis| 
| Preview Grasp | DG | &#x2611; Good and recommend to be used in Grasp Studio when adding grasps in to DB through DG synthesis | 
| Preview Grasp | SG | &#x2612; Not recommended since at preview phase hand will be very jumpy due to sparse grasps in DB | 
| Preview Only | DG | &#x2611; Good and recommend to be used in Grasp Studio when adding grasps in to DB through DG synthesis | 
| Preview Only | SG | &#x2612; Not recommended since at preview phase hand will be very jumpy due to sparse grasps in DB | 
| Sticky Hand | -- | -- | 


### Grasp Speed and Release Speed

{% include image.html file="unity/unity_vg_global_grasp_interaction.png" alt="VG Global Grasp Interaction Settings" caption="MyVirtualGrasp script - Global Grasp Interaction Settings" %}
As shown in above image, you can set the default synthesis methods and interaction type for all objects in the scene globally. 

Besides those, there are two parameters <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSpeed}}">Grasp Speed</a> and 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ReleaseSpeed}}">Release Speed</a>
that can also significantly affect the user experience because they determines how fast the hand forms grasp and releases from grasp respectively.
{% include tip.html content="For grasp speed, lower value means faster grasp, for release speed, lower value means faster release." %}

To learn more details on how to setup your objects' grasp interaction in practice, please see [VG_Interactable](unity_component_vginteractable.html#unity-component-vginteractable).

