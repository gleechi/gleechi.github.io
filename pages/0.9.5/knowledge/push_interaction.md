---
title: Push Interaction
sidebar: main_sidebar_0_9_5
keywords: affordance, push, index_finger_pushable
permalink: push_interaction.0.9.5.html
folder: knowledge
toc: true
---

### Background

VirtualGrasp not only provides solutions to [grasp interaction](grasp_interaction.0.9.5.html#grasp-interaction), 
but also for push interactions.

Button push as an action in real world is very simple process due to the very physical laws existing in the nature. 
When the same problem is ported into VR, a realistic button push behavior requires some tedius steps that often needs complex setup of physical properties on 
both button and the hand.

VirtualGrasp provides a solution to make push interaction setup easier and intuitive through [object articulation](object_articulation.0.9.5.html#object-articulation), with and without relying on physical simulations.

{% include callout.html content="Most important concepts relevant to push interaction are explained in [object articulation](object_articulation.0.9.5.html#object-articulation) page." %}

Below we will explain: 
* first how to setup push interaction without adding any physical properties on an object -- [push without physics](#push-without-physics),
* and then how to easily extend this setup to use physical simulation provided by a game engine -- [push with physics](#push-with-physics). 

### Push Without Physics

#### From Object Selection to Push Without Physics

When push is done with physics, the selection of object is straightforward -- by contact and apply force. 
When push is done without physics, there need to be a way to decide which object is to be pushed. 
VirtualGrasp does this through checking the geometric relation between a 
{% include tooltip.html tooltip="PushAgent" text="push agent" %} and the object to be pushed. 
To allow VR developers to be able to specify for example "This button can not be pushed from below", 
{% include tooltip.html tooltip="PushPivot" text="push pivot" %} is added
to the object to specify the preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}
by the {% include tooltip.html tooltip="PushAgent" text="push agent" %} for pushing this object. 

Given that
* the {% include tooltip.html tooltip="PushAgent" text="push agent" %} has been assigned 
(through set {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} as INDEX_PUSHABLE),
and
* {% include tooltip.html tooltip="PushPivot" text="push pivot" %} is added to the object to be pushed, 

the decision on which of the pushable objects is selected for pushing is done by considering:

* how close is the {% include tooltip.html tooltip="PushAgent" text="push agent" %} to the pushable object
and
* how aligned is the {% include tooltip.html tooltip="PushAgent" text="push agent" %}'s {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %} with the preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}. 

{% include image.html file="unity/unity_button_pivot.png" alt="A Unity button." caption="A Unity button"%}

For example image above shows the push pivot transform added to the red button. The blue arrow (zaxis of this transform) specifies
the {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}. 
So when index finger is approaching from bottom to the button, opposite to the blue arrow, the object will not be selected for push.


Once an object is selected, you can turn on the visual hint to show which object is selected for push without physics. 
See [VG_HintVisualizer](unity_component_vghintvisualizer.0.9.5.html#unity-component-vghintvisualizer) to learn how to use it.

#### How to Setup Push Without Physics

Through VirtualGrasp's [object articulation](object_articulation.0.9.5.html#object-articulation) feature, a VR developer can setup a pushable object with various behaviors simulating real world's button object in any game engine. And this setup does not require the developer to add any physical components (such as RigidBody or Colliders) to either objects or hands in the game engine. 

Using Unity game engine as an example, to create a pushable button, 
you add the component [VG_Articulation](unity_component_vgarticulation.0.9.5.html) to the object, and the parameters shown in below image create a button that can be pushed by index finger, and will bounce alternatively to the two <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.DiscreteStates}}">discrete states</a> when push is released (see [affordances](object_articulation.0.9.5.html#object-affordances)):

{% include image.html file="unity/unity_vg_articulation_full.png" alt="VG Articulation" caption="VG_Articulation Component." %}

* Since button is moving along a single axis linearly, we select the joint type to be PRISMATIC.
* For PRISMATIC joint, we need to provide {% include tooltip.html tooltip="Pivot" text="pivot" %} which specifies the {% include tooltip.html tooltip="JointAxis" text="joint axis" %} along which object moves.
* For PRISMATIC joint, we also need to provide {% include tooltip.html tooltip="JointLimit" text="joint limit" %}, i.e. a linear movement range between 0 and 0.014 meter. 
* Since the pushable button's movement direction (by {% include tooltip.html tooltip="Pivot" text="pivot" %}) is same as the direction we want hand to approach for pushing, so we don't need to specify 
a different {% include tooltip.html tooltip="PushPivot" text="push pivot" %}.
* For push without physics, you need to select {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} as INDEX_PUSHABLE.
* To let object bounce back alternatively to two stages when push is release, you need to set the {% include tooltip.html tooltip="StateAffordance" text="state affordance" %} to be {% include tooltip.html tooltip="TwoStage" text="TWO_STAGE" %}. 
* To let object bounce back NOT to the lower boundary of the {% include tooltip.html tooltip="JointLimit" text="joint limit" %} (min = 0), but to slightly lower position, we set two {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} with first value 0.004 (>min).

{% include callout.html content="When TWO_STAGE affordance is chosen, object' joint state will bounce back to the smallest value of the discrete states after the 2nd push.
Since by default discrete states will take the two range values from the joint limits [min, max], so if discrete states is not provided, the joint state will bounce back to the min value. 
If you want it to bounce to a different value from min, you should define the discrete states with first (smallest) value larger than joint limit's min value. As shown in above image, the smallest discrete value 0.004 is bigger than the min value 0." %}

### Push With Physics

<!--{% include warning.html content="The push with physics option is still at the experimental stage." %}-->

VirtualGrasp also supports push through physics, by seamlessly integrating VG's [object articulation](object_articulation.0.9.5.html#object-articulation) feature with the physical simulations already existing 
in the client engines (Unity or Unreal). 

To create a pushable button with physics, besides all the setup in VG_Articulation component as shown in [push without physics](#push-without-physics) section, you only need to:
* set up the physical properties for the object in the game engine. For example in Unity, you should add RigidBody and Collider to this object; and
* set up the physical properties for the hand. In Unity, VirtualGrasp automatically setup the hand physical properties (RigidBody and Colliders) if you enable **Physical** avatars in [Sensors](unity_component_myvirtualgrasp.0.9.5.html#sensors) (see image below).

{% include image.html file="unity/unity_hand_model.png" alt="VG Avatars" caption="MyVirtualGrasp script - Avatars." %}

### Push Without Physics vs. With Physics

To help you set up the push object with physics, most of the [object articulation](object_articulation.0.9.5.html#object-articulation) parameters that applies to without physics situation also will take effect, with very few exceptions:
 
<!--| Object Articulation Param | Push without Physics | Push with Physics |
|-------|--------|---------|
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Joint}}">Joint</a> | Relevant | Relevant | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>| Relevant | Relevant | 
| {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} | Relevant | INDEX_PUSHABLE is not needed | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a> | Relevant | Not relevant  | 
-->

* For push with physics, an object can be pushed by any part of the hands or any object that have physical properties. Therefore setting {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} to be INDEX_PUSHABLE is not relevant because it will not limit the push by only the index finger.
* For push with physics, {% include tooltip.html tooltip="PushPivot" text="push pivot" %} won't take effect to specify a preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}, which can be good or bad depending on the game logic and the desired user experiences.


The table below give some hints and considerations to help you choose which push option to use:

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
<td markdown="span" style="text-align: right">Limited in terms of "who" can push the object (now only INDEX_PUSHABLE).</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Anything with RigidBody and Collider can push since it is physics-based.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Can specify preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %} through {% include tooltip.html tooltip="PushPivot" text="push pivot" %}  </td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Can not specify preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}. </td>
</tr>
<tr>
<td markdown="span" style="text-align: right">From some direction the object cannot be pushed </td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Object can be pushed from any direction since it is physics-based.</td>
</tr>
</tbody>
</table>


