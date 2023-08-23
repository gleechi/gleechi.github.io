---
title: Object Articulation
#tags: [getting_started]
keywords: component, object, affordance, joint
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_4_0
permalink: object_articulation.1.4.0.html
folder: mydoc
---

In VirtualGrasp, we use "Object Articulation" to setup an object's {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behaviors" %} through the combination of [object joint](#object-joint) and [object affordances](#object-affordances), without relying on physical simulations.

## Object Joint

Each object has a {% include tooltip.html tooltip="Joint" text="joint" %} of a given type which determines how it moves in relation to its parent object. Unlike Unity's object physics-based joint systems, VirtualGrasp's joint system is purely kinematic, and allows you to setup common object behaviors like buttons, screws, and sliders, etc very easily. 

| Type | Dofs | Description |
|-------|--------|--------|---------|
| Floating | 6 | unconstrained, freely floating object | 
| Fixed | 0 | constrained, as if an integrated object with its parent | 
| Revolute | 1 | constrained, rotate around an axis through an anchor point (joint center), limited by an angle range | 
| Prismatic | 1 | constrained, move linearly along an axis through an anchor point (joint center), limited by an distance range |
| Planar | 2 | constrained, move on a plane defined by anchor point and anchor's zaxis as plane normal, limited by a rectangular shaped range defined along anchor's x and y axes | 
| Cone | 3 | constrained, rotate around an anchor point limited by a cone limit, parameterized by a swing limit angle that determines the cone size, and twist limit angle that determines how much the object can rotate around the axis (center axis of the cone) |

For any joint type, there are a set of parameters to be used to configure the joint:

| Parameters | Description |
|-------|--------|
| Motion Type | if Free the motion in the joint defined dof(s) will not be constrained by any limits. |
| Min | lower limit of 1-dof joint, i.e. revolute or prismatic joint. |
| Max | upper limit of 1-dof joint, i.e. revolute or prismatic joint. |
| Min x | lower limit of planar joint, along _xaxis_ of anchor transform. |
| Max x| upper limit of planar joint, along _xaxis_ of anchor transform. |
| Min y| lower limit of planar joint, along _yaxis_ of anchor transform. |
| Max y| upper limit of planar joint, along _yaxis_ of anchor transform. |
| Swing | swing angle limit for cone joint. |
| Twist | twist angle limit for cone joint. |
| Screw Rate | only valid for revolute joint, describing how much the object linearly move along the axis given every degree of rotation, in unit (cm/degree). | 
| Discrete States | discrete values for 1-dof joints within the limit boundary. By default [Min, Max]. If provided has to be at least 2 states and in ascending order. | 
| Discrete States x | discrete values for planar joint along _xaxis_ of anchor transform. By default [Min x, Max x]. If provided has to be at least 2 states and in ascending order. | 
| Discrete States y | discrete values for planar joint along _yaxis_ of anchor transform. By default [Min y, Max y]. If provided has to be at least 2 states and in ascending order. | 
| Joint Center | around which position an object is rotating around, specified by the _Anchor_'s position. | 
| Joint Axis | the axis specified by the _Anchor_'s _zaxis_. For revolute joint, this defines rotation axis, for prismatic joint, object move linearly along this axis, for cone joint this defines center of the cone shape limit range, for planar joint, this is normal of the plane. |
| Joint Axis2 | the secondary axis specified by the _Anchor_'s _yaxis_, which defines orientation of planar joint's rectangular shaped limit space. |

### Joint State

If an object has an 1-dof joint (Prismatic or Revolute) or 2-dof joint (Planar), then its complete pose can be determined by a combination of 
* its joint configuration (defined by a set of parameters shown in above table) 
* and a single scalar value -- {% include tooltip.html tooltip="JointState" text="joint state" %} for 1-dof joints, or two values -- ({% include tooltip.html tooltip="JointState" text="joint state" %}, {% include tooltip.html tooltip="SecondaryJointState" text="secondary joint state" %}).

The table below gives some example values of joint state for two 1-dof joints to further clarify its meaning:

| Joint State | Revolute | Prismatic|
|-------|--------|---------|
| 0 | zero pose (initial pose) | zero pose (initial pose) |
| 2.5 (a random value as an example) | 2.5 (degree) rotated around {% include tooltip.html tooltip="JointAxis" text="joint axis" %} (follow right-hand rule) from the zero pose | 2.5 (meter, in Unity) translated along {% include tooltip.html tooltip="JointAxis" text="joint axis" %} direction from the zero pose |
| -2.5 (a random value as an example) | -2.5 (degree) rotated around {% include tooltip.html tooltip="JointAxis" text="joint axis" %} (follow right-hand rule) from the zero pose | -2.5 (meter, in Unity) translated along {% include tooltip.html tooltip="JointAxis" text="joint axis" %} direction from the zero pose |

{% include callout.html content="Note that the joint limit [Min, Max] is essentially the limit range of the joint state; and the discrete states are where the joint state will clamp to when the object is released depending on [object affordances](#object-affordances)." %}

If an object has {% include tooltip.html tooltip="Planar" text="PLANAR" %} joint, then there are {% include tooltip.html tooltip="JointState" text="joint state" %} and {% include tooltip.html tooltip="SecondaryJointState" text="secondary joint state" %} representing the position of object along _xaxis_ and _yaxis_ of the {% include tooltip.html tooltip="Pivot" text="anchor" %} transform. 

{% include tip.html content="You can use [GetObjectJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectjointstate) and [GetObjectSecondaryJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectsecondaryjointstate) to get current joint state and secondary joint state (in the case of PLANAR joint) respectively." %}
 

### Anchor vs. Push Direction

As shown in the joint parameter table above, an object's joint parameters include {% include tooltip.html tooltip="JointCenter" text="joint center" %} and {% include tooltip.html tooltip="JointAxis" text="joint axis" %} (also {% include tooltip.html tooltip="JointAxis2" text="joint axis2" %} in the case of PLANAR joint).
These two parameters are provided in a combined way through an {% include tooltip.html tooltip="Pivot" text="anchor" %} transform in the game engine. 

Then what is **push direction**? 

{% include tooltip.html tooltip="PushPivot" text="Push direction" %} is provided to specify along which direction the hand is allowed to approach and apply push action. 
And this is only relevant for [push without physics](push_interaction.1.4.0.html#push-without-physics) setup for push interaction.

Similar to provide joint axis through anchor transform, we use push direction transform's _zaxis_ to specify this push approach direction. 

{% include callout.html content="Push direction is NOT specifying along which direction object moves, 
but rather specifying a preferred hand approach direction which is only used for [pushable object selection](push_interaction.1.4.0.html#from-object-selection-to-push-without-physics). How object moves is defined by anchor together with other joint parameters." %}

If {% include tooltip.html tooltip="PushPivot" text="push direction" %} is not provided, then it will just inherit from the {% include tooltip.html tooltip="Pivot" text="anchor" %}, i.e. the push direction is same as the joint axis. 

{% include image.html file="unity/unity_button_pivot.png" alt="A Unity button." caption="A Unity button"%}
The image above shows an example of setting up a button object that can be pushed from top by index finger. 
In this case the {% include tooltip.html tooltip="PushPivot" text="push direction" %}
is the same as {% include tooltip.html tooltip="Pivot" text="anchor" %} because the preferred approach direction is same as the button movement direction.

To learn more details of how to setup pushable object see [push interaction](push_interaction.1.4.0.html).


## Object Affordances

“Object Affordance”, in a broader sense, means what kind of action this object can be used for. 
For example a chair affords to be sit upon, a button on the wall affords push, and a handle affords grasp.

In VG library we define a “narrower” sensed set of affordances that determines which kind of hand **interaction** we can have with this object ({% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}), and how the object's **joint state** react in the virtual environment ({% include tooltip.html tooltip="StateAffordance" text="state affordance" %}). 

| Affordances | Description | Object Joint Settings |
|-------|--------|---------|
| Graspable | {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}: Can be grasped | for all joint types | 
| Index Pushable | {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}: Can be pushed by the index finger; only relevant when setup [push interaction without physics](push_interaction.1.4.0.html#push-without-physics).| for all joint types | 
|-------|--------|---------|
| Normal | {% include tooltip.html tooltip="StateAffordance" text="state affordance" %}: Object stay at the pose when hand is released  | for all joint types| 
| Bounce | {% include tooltip.html tooltip="StateAffordance" text="state affordance" %}: When released, bounce to the lowest discrete state | for 1-dof joint | 
| Two Stage | {% include tooltip.html tooltip="StateAffordance" text="state affordance" %}: When released, bounce to the highest and lowest discrete state in an alternating order | for 1-dof joint | 
| Snaps | {% include tooltip.html tooltip="StateAffordance" text="state affordance" %}: When released, snap to the closest discrete state | for 1-dof joint and 2-dof Planar joint| 

## Dual Hands Only

This is a miscellaneous parameter to enforce an object can only be moved when grasped by more than one hands. 

The purpose of this feature is to "simulate" a heavy object that need more hands to be moved. This option applies to both {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} and non-physical objects.

## Graphical User Interface

The image below shows Unity's [VG_Articulation](unity_component_vgarticulation.1.4.0.html) component used to setup all parameters of object articulation.
Note that the VG_Articulation is generic for all other client engines like Unreal.

{% include image.html file="unity/unity_vg_articulation_full_0_11_0.png" alt="VG Articulation" caption="VG_Articulation Component." %}

