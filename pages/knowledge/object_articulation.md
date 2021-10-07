---
title: Knowledge Base - Object Articulation
#tags: [getting_started]
keywords: component, object, affordance, joint
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: knowledge_sidebar
permalink: object_articulation.html
folder: mydoc
---

In VirtualGrasp, we use "Object Articulation" to setup an object's 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behaviors</a> through a combination of
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Joint}}">object joint</a> and
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Affordance}}">object affordance</a>,
without relying on physical simulations.

### Object Joint

Each object has a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Joint}}">joint</a> of a given type which determines how it moves in relation to its parent object.
Unlike Unity's object physics-based joint systems, VirtualGrasp's joint system is purely kinematic, and allows you to setup common object behaviors like buttons, screws, and sliders, etc very easily. 
   

| Type | Dofs | Description |
|-------|--------|--------|---------|
| Floating | 6-dof | unconstrained, freely floating object | 
| Fixed | 0-dof | constrained, as if an integrated object with its parent | 
| Revolute (or <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ScrewJoint}}">Screw</a>) | 1-dof | constrained, rotate around an axis through a pivot point (joint center), limited by an angle range | 
| Prismatic | 1-dof | constrained, move linearly along an axis through a pivot point (joint center), limited by an distane range | 
| Cone | 3-dof | constrained, rotate around a pivot point limited by a cone limit, parameterized by a swing limit angle that determines the cone size, and twist limit angle that determines how much the object can rotate around the axis (center axis of the cone) |

For any joint type, there are a set of parameters to be used to configure the joint:

| Parameters | Description | Additional features |
|-------|--------|---------|
| Min / Swing | lower limit of 1-dof joint, for cone joint, this is swing angle limit | if angular limit, unit in (degree)|
| Max / Twist | upper limit of 1-dof joint, for cone joint, this is twist angle limit | if angular limit, unit in (degree) |
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ScrewRate}}">Screw Rate</a> | only valid for Revolute joint, describing how much the object linearly move along the axis given every degree of rotation | In unit (cm/degree) | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.DiscreteStates}}">Discrete States</a> | discrete values in the 1-dof joint's limit boundary. By default same as [min, max]. If provided has to be at least 2 states and in ascending order. | Same unit as the limits | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointCenter}}">Joint Center</a> | around which position an object is rotating around, specified by the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a> transform's position | E.g. for cone joint, object will rotate round this point | 
| <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointAxis}}">Joint Axis</a> | the axis specified by the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a> transform's **Zaxis** | E.g. for prismatic joint, object will move linearly along this axis | 

### Joint State

If an object has an 1-dof joint, then its complete pose can be determined by a combination of 
* its joint configuration (defined by a set of parameters shown in above table) 
* and a single scalar value -- <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointState}}">Joint State</a>. 

The table below gives some example values of joint state to further clarify its meaning:

| Joint State | Revolute | Prismatic|
|-------|--------|---------|
| 0 | zero pose (initial pose) | zero pose (initial pose) |
| 2.5 (a random value as an example) | 2.5 (degree) rotated around joint axis (follow right-hand rule) from the zero pose | 2.5 (meter, in Unity) translated along joint axis direction from the zero pose |
| -2.5 (a random value as an example) | -2.5 (degree) rotated around joint axis (follow right-hand rule) from the zero pose | -2.5 (meter, in Unity) translated along joint axis direction from the zero pose |

{% include tip.html content="Note that the joint limit [Min, Max] is essentially the limit range of the Joint State; and the Discrete States are 
 where the Joint State will clamp to when the object is released depending on [Object Affordances](#object-affordances)." %}


### Pivot vs. Push Pivot

As shown in the joint parameter table above, an object's joint parameters include 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointCenter}}">Joint Center</a> and
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointAxis}}">Joint Axis</a>.
These two parameters are provided in a combined way through a 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a> transform in the game engine. 

Then what is **Push Pivot**? 

Push Pivot is provided to specify along which direction the hand is allowed to approach and apply push action. 
And this is only relevant for Push without Physics setup when object's <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> 
to INDEX_PUSHABLE (details see [Push Interaction](push_interaction.html#push-articulation)).

Similar to provide joint axis through Pivot transform, we use Push Pivot transform's **Zaxis** to specify this push approach direction. 

{% include important.html content="Push Pivot is NOT specifying along which direction object moves, 
but rather specifying a preferred hand approach direction which is only used for object selection for
push interaction. How object moves is defined by Pivot together with other joint parameters." %}

If <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>
 is not provided in the [the graphical user interface](#graphical-user-interface), then the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>
 just inherit from the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a>,
i.e. the push direction is same as the joint axis. 

{% include image.html file="unity/unity_button_pivot.png" alt="A Unity button." caption="A Unity button"%}
The image above shows an example of setting up a button object that can be pushed from top by index finger. 
In this case the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>
is the same as <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a>
because the preferred approach direction is same as the button movement direction.

To learn more details of how to setup pushable object see [Push Interaction](push_interaction.html#push-without-physics).


### Object Affordances

“Object Affordance”, in a broader sense, means what kind of action this object can be used for. 
For example a chair affords to be sit upon, a button on the wall affords push, and a handle affords grasp.

In VG library we define a “narrower” sensed set of affordances that determines which kind of hand **interaction** we can have with this object,
 and how the object's **state** react in the virtual environment. 

| Affordances | Description | Object Joint Settings |
|-------|--------|---------|
| Graspable | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a>: Can be grasped | for all joint types | 
| Index Pushable | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a>: Can be pushed by the index finger; only relevant when setup [push interaction without physics](push_interaction.html#push-without-physics).| for all joint types | 
|-------|--------|---------|
| Normal | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>: Object stay at the pose when hand is released  | for all joint types| 
| Bounce | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>: When released, bounce to the lowest discrete state | for 1-dof joint | 
| Two Stage | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>: When released, bounce to the highest and lowest discrete state in an alternating order | for 1-dof joint | 
| Snaps | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>: When released, snap to the closest discrete state | for 1-dof joint | 

### Dual Hands Only

This is a miscellaneous parameter to enforce an object can only be moved when grasped by two hands. 

The purpose of this feature is to simulate a heavy object that need more hands to be moved. 

Note since there is no physical simulation involved, this does not take into account of the physical properties such as
mass or inertia specified in the game engine. 

### Graphical User Interface

The image below shows Unity's VG_Articulation component as an example for the GUI of Object Articulation.

Note that the VirtualGrasp's object articulation is generic for all other client engines like Unreal.

To learn more details of Unity implementation see [VG_Articulation](unity_component_vgarticulation.html#unity-component-vgarticulation).

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

