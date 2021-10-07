---
title: Knowledge Base - Push Interaction
sidebar: knowledge_sidebar
keywords: affordance, push, index_finger_pushable
permalink: push_interaction.html
folder: knowledge
toc: true
---

### Background

VirtualGrasp not only provides solutions to [Grasp Interaction](grasp_interaction.html#grasp-interaction), 
but also provides solutions for push interactions.

Button push as an action in real world is very simple process due to the very physical laws existing in the nature. 
When the same problem is ported into VR, a realistic button push behavior requires some tedius steps that often needs complex setup of physical properties on 
both button and the hand.

VirtualGrasp provides a solution to make push interaction setup easier and intuitive, through [Object Articulation](object_articulation.html#object-articulation), with and without relying on **physical simulations**.

{% include important.html content="To fully benefit from VG's push interaction, it is important to understand [Object Articulation](object_articulation.html#object-articulation)." %}


### Push Without Physics

#### From Object Selection to Push Without Physics

When push is done with physics, the selection of object is straightforward -- by contact and apply force. 
When push is done without physics, there need to be a way to decide which object is to be pushed. 
VirtualGrasp does this through checking the geometric relation between a 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushAgent}}">Push Agent</a>
and the object to be pushed. 
To allow VR developers to be able to specify for example "This button can not be pushed from below", 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a> is added
onto the object to specify the preferred <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ApproachDirection}}">Approach Direction</a> 
by the push agent for pushing. 

Given that
* The <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushAgent}}">Push Agent</a> has been assigned 
(through set <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> as INDEX_PUSHABLE),
and
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a> is added to the object to be pushed. 

The decision on which of the pushable objects is selected for pushing is done by considering:
* how close is the push agent to the pushable object
and
* how aligned is the push agent's approach direction with the preferred approach direction assigned on the object by 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>. 

{% include image.html file="unity/unity_button_pivot.png" alt="A Unity button." caption="A Unity button"%}

For example image above shows the push pivot transform added to the red button. The blue arrow (Zaxis of this transform) specifies
the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ApproachDirection}}">Approach Direction</a>. 
So when index finger is approaching from bottom to the button, opposite to the blue arrow, the object will not be selected for push.


Once an object is selected, you can turn on the visual hint to show which object is selected for push without physics. 
See [VG_HintVisualizer](unity_component_vghintvisualizer.html#unity-component-vghintvisualizer) to learn how to use it.

#### How to Setup Push Without Physics

Through VirtualGrasp's [Object Articulation](object_articulation.html#object-articulation) feature, a VR developer can setup a pushable object with various behaviors 
simulating real world's button object in any game engine. And this setup does not require the developer to add physical qualities to either objects or hands in the game engine. 

Using Unity game engine as an example, to create a pushable button, 
you add the component [VG_Articulation](unity_component_vgarticulation.html#unity-component-vgarticulation) to the object, 
and the parameters shown in below image create a button that can be pushed by index finger, and will always bounce back when not pushed:

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

* Since button is moving along a single axis linearly, we select the joint type to be PRISMATIC.
* For PRISMATIC joint, we need to provide <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a> which specifies the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointAxis}}">Joint Axis</a> along which object moves.
* For PRISMATIC joint, we also need to provide <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointLimit}}">Joint Limit</a>, i.e. a linear movement range between 0 and 0.014 meter. 
* Since the pushable button's movement direction (by <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a>) is same as the direction we want hand to approach for pushing, so we don't need to specify 
a different <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>.
* For push without physics, you need to select <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> as INDEX_PUSHABLE.
* To let object bounce back when not pushed, you need to set the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>
 to be <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Bounce}}">BOUNCE</a>. 
* To let object bounce back NOT to the lower boundary of the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointLimit}}">Joint Limit</a> 
(i.e. min = 0), but to slightly lower position, we set two <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.DiscreteStates}}">Discrete States</a> with first value 0.004.


{% include important.html content="When BOUNCE affordance is chosen, object' Joint State will bounce back to the smallest value of the Discrete States.
Since by default Discrete States will take the two range values from Joint Limits [min, max], so if Discrete States is not provided, Joint State bounce back to min value. 
If you want Joint State to bounce to a different value from min, you should define Discrete States with first (smallest) value different from Joint Limit's min value, 
as shown in above image, smallest discrete value 0.004 is bigger than Min value 0. Then the Joint State will bounce back to 0.004 not 0." %}



### Push With Physics

VirtualGrasp also supports push through physics, by seamlessly integrating VG's [Object Articulation](object_articulation.html#object-articulation) with the physical simulations already existing 
in the client engines (Unity or Unreal). 

To create a pushable button with physics, besides all the setup in VG_Articulation component as shown in earlier section, you need to:
* Set up the physical properties for the object in the game engine. For example in Unity, you should add RigidBody and Collider to this object. 
* Set up the physical properties for the hand. In Unity, VirtualGrasp automatically setup the hand physical properties (RigidBody and Colliders) if you Enable **Physical** avatars as shown in below image. 

{% include image.html file="unity/unity_vg_avatars.png" alt="VG Avatars" caption="MyVirtualGrasp script - Avatars." %}

### Push Without Physics vs. Physics

To help you set up the push object with or without physics, 
 table below listed how relevant for each of the [Object Articulation](object_articulation.html#object-articulation) parameters:
 
| Object Articulation Param | Push without Physics | Push with Physics |
|-------|--------|---------|
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Joint}}">Joint</a> | Relevant | Relevant | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>| Relevant | Relevant | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> | Relevant | INDEX_PUSHABLE is not needed | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a> | Relevant | Not relevant  | 

Now the question is which one should I choose? 

Which option should be used depends on the requirements of your game and what kind of user experiences is expected:

<table border="1">
<colgroup>
<col width="40%" />
<col width="10%" />
<col width="10%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" style="text-align: right">Push without Physics</th>
<th colspan="2">Push with Physics</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span" colspan="2" style="text-align: right">
**Push without Physics** allows easy, though limited setup of push interaction.<!-- While full baking is needed, it only uses grasp baking results during runtime.are created by a limited set of grasps around an object depending on a pre-baked grasp database.--></td>
<td markdown="span" colspan="2">**Push with Physics** allows more realistic physics-based push interaction.<!--While full baking is currently enabled (so one can switch between static and dynamic grasping per object), it only uses shape baking results. --><!--are unlimited grasps that are generated during runtime.--></td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Easy to setup since no need to specify dynamic properties of a rigid body like mass, drag etc.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Need careful selection of dynamic properties since they influence how object react to push</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Limited in terms of "who" can push the object (now only INDEX_PUSHABLE <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a>.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Anything with RigidBody and Collider can push since it is physics-based.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Can specify preferred hand approach direction through <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>  </td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Can not specify preferred hand direction. </td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Some hand approach direction is not allowed for push if deviate too much from the preferred direction by <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a> </td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Object can be pushed from any direction since it is physics-based.</td>
</tr>
</tbody>
</table>


