---
title: Push Interaction
sidebar: main_sidebar_1_3_0
keywords: affordance, push, index_finger_pushable
permalink: push_interaction.1.3.0.html
folder: knowledge
toc: true
---

### Background

VirtualGrasp not only provides solutions to [grasp interaction](grasp_interaction.1.3.0.html), 
but also for push interactions.

Button push as an action in real world is very simple process due to the very physical laws existing in the nature. 
When the same problem is ported into VR, a realistic button push behavior requires some tedius steps that often needs complex setup of physical properties on 
both button and the hand.

VirtualGrasp provides a solution to make push interaction setup easier and intuitive through [object articulation](object_articulation.1.3.0.html), without relying on physical simulations.

{% include callout.html content="Most important concepts relevant to push interaction are explained in [object articulation](object_articulation.1.3.0.html) page." %}

Below we will explain how to setup push interaction without adding any physical properties on an object -- [push without physics](#push-without-physics), 

### Push Without Physics

#### From Object Selection to Push Without Physics

When push is done with physics, the selection of object is straightforward -- by contact and apply force. 
When push is done without physics, there need to be a way to decide which object is to be pushed. 
VirtualGrasp does this through checking the geometric relation between a 
{% include tooltip.html tooltip="PushAgent" text="push agent" %} and the object to be pushed. 
To allow VR developers to be able to specify for example "This button can not be pushed from below", 
{% include tooltip.html tooltip="PushPivot" text="push direction" %} is added
to the object to specify the preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}
by the {% include tooltip.html tooltip="PushAgent" text="push agent" %} for pushing this object. 

Given that
* the {% include tooltip.html tooltip="PushAgent" text="push agent" %} has been assigned 
(through set {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} as INDEX_PUSHABLE),
and
* {% include tooltip.html tooltip="PushPivot" text="push direction" %} is added to the object to be pushed, 

the decision on which of the pushable objects is selected for pushing is done by considering:

* how close is the {% include tooltip.html tooltip="PushAgent" text="push agent" %} to the pushable object
and
* how aligned is the {% include tooltip.html tooltip="PushAgent" text="push agent" %}'s {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %} with the preferred {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}. 

{% include image.html file="unity/unity_button_pivot.png" alt="A Unity button." caption="A Unity button"%}

For example image above shows the push direction transform added to the red button. The blue arrow (zaxis of this transform) specifies
the {% include tooltip.html tooltip="ApproachDirection" text="approach direction" %}. 
So when index finger is approaching from bottom to the button, opposite to the blue arrow, the object will not be selected for push.

{% include callout.html content="Note that a pushable object is selected before the finger tip touches the object, and the selection can be visualized by using [VG_HintVisualizer](unity_component_vghintvisualizer.1.3.0.html)." %}

Once an object is selected, a push on the object will be triggered when the finger tip touches the pushing surface. The pushable object's movement is then controlled by sensor controlled finger tip position through joint articulation. In other words, the finger tip is "dragging" the object to move to the allowed direction by joint articulation setup. This way an object (like a button) can be "pushed down", or "slided" on a surface as shown on the rectangular button with planar joint (see [pad with planar joint buttons](unity_vgonboarding_task6.1.3.0.html)).

#### How to Setup Push Without Physics

Through VirtualGrasp's [object articulation](object_articulation.1.3.0.html) feature, a VR developer can setup a pushable object with various behaviors simulating real world's button object in any game engine. And this setup does not require the developer to add any physical components (such as RigidBody or Colliders) to either objects or hands in the game engine. 

Using Unity game engine as an example, to create a pushable button, 
you add the component [VG_Articulation](unity_component_vgarticulation.1.3.0.html) to the object, and the parameters shown in below image create a button that can be pushed by index finger, and will bounce alternatively to the two <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.DiscreteStates}}">discrete states</a> when push is released (see [affordances](object_articulation.1.3.0.html#object-affordances)):

{% include image.html file="unity/unity_vg_articulation_push_button.png" alt="VG Articulation" caption="VG_Articulation Component." %}

* Since button is moving along a single axis linearly, we select the joint type to be PRISMATIC.
* For PRISMATIC joint, we need to provide {% include tooltip.html tooltip="Pivot" text="anchor" %} which specifies the {% include tooltip.html tooltip="JointAxis" text="joint axis" %} along which object moves.
* For PRISMATIC joint, we also need to provide {% include tooltip.html tooltip="JointLimit" text="joint limit" %}, i.e. a linear movement range between 0 and 0.014 meter. 
* Since the pushable button's movement direction (by {% include tooltip.html tooltip="Pivot" text="anchor" %}) is same as the direction we want hand to approach for pushing, so we don't need to specify a different {% include tooltip.html tooltip="PushPivot" text="push direction" %}.
* For push without physics, you need to select {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} as INDEX_PUSHABLE.
* To let object bounce back alternatively to two stages when push is release, you need to set the {% include tooltip.html tooltip="StateAffordance" text="state affordance" %} to be {% include tooltip.html tooltip="TwoStage" text="TWO_STAGE" %}. 
* To let object bounce back NOT to the lower boundary of the {% include tooltip.html tooltip="JointLimit" text="joint limit" %} (min = 0), but to slightly lower position, we set two {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} with first value 0.004 (>min).

{% include callout.html content="When TWO_STAGE affordance is chosen, object' joint state will bounce back to the smallest value of the discrete states after the 2nd push.
Since by default discrete states will take the two range values from the joint limits [min, max], so if discrete states is not provided, the joint state will bounce back to the min value. 
If you want it to bounce to a different value from min, you should define the discrete states with first (smallest) value larger than joint limit's min value. As shown in above image, the smallest discrete value 0.004 is bigger than the min value 0." %}