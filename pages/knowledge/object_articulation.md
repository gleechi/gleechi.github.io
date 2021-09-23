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

In VirtualGrasp, we use "Object Articulation" to setup complex object behaviors through a combinition of **object joint** settings and **object affordances**.


### Object Joint

Each object has a joint of a given type which determines how it moves in relation to its parent object.

| Type | Dofs | Description |
|-------|--------|--------|---------|
| Floating | 6-dof | unconstrained, freely floating object | 
| Fixed | 0-dof | constrained, as if an integrated object with its parent | 
| Revolute | 1-dof | constrained, rotate around an axis through a pivot point (joint center), limited by an angle range | 
| Prismatic | 1-dof | constrained, move linearly along an axis through a pivot point (joint center), limited by an distane range | 
| Cone | 3-dof | constrained, rotate around a pivot point limited by a cone limit, parameterized by a swing limit angle that determines the cone size, and twist limit angle that determines how much the object can rotate around the axis (center axis of the cone) |


Unlike Unity's object physics-based joint systems, VirtualGrasp's joint system is purely kinematic. 

If an object's joint is of an “unconstrained” type, meaning it is freely “floating”, then when you grasp this object, it will follow your hands movement freely.

If an object's joint is of a “constrained” type, meaning it is NOT freely “floating”, then when you interact with (grasp or push) this object, it will not follow your hands movement freely, 
but be constrained according to its joint configuration. 

For any joint type, there are a set of parameters to be used to configure the joint:

| Parameters | Description | Additional features |
|-------|--------|---------|
| **Min** | lower limit of 1-dof joint, for cone joint, this is swing angle limit | if angular limit, unit in (degree)|
| **Max** | upper limit of 1-dof joint, for cone joint, this is twist angle limit | if angular limit, unit in (degree) |
| **Screw Rate** | only valid for Revolute joint, describing how much the object linearly move along the axis given every degree of rotation | In unit (cm/degree) | 
| **Discrete States** | discrete values in the 1-dof joint's limit boundary. By default same as [min, max]. If provided has to be at least 2 states and in ascending order. | Same unit as the limits | 
| Joint Center | around which position an object is rotating around, specified by the **Pivot** transform's position | E.g. for cone joint, object will rotate round this point | 
| Joint Axis | what is the joint axis, specified by the **Pivot** transform's Zaxs | E.g. for prismatic joint, object will move linearly along this axis | 

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

{% include tip.html content="Note that the joint limit [Min, Max] is essentially the limit range of the Joint State." %}


### Pivot vs. Push Pivot

As shown in the joint parameter table above, an object's joint parameter need to specify its joint center point and joint axis. 
These two parameters are provided in a combined way through a **Pivot** transform in the game engine. 

Then what is **Push Pivot**? 

Push Pivot is provided to specify the object push direction when we assign its interaction affordance to be "Index Pushable". 
Similar to provide joint axis through Pivot transform, we use Push Pivot transform's Zaxis to specify this push direction. 

And if Push Pivot is not provided in the VG_Articulation component (see image blow), then the Push Pivot just inherit from the Pivot, 
i.e. the push direction is same as the joint axis. 

The effect of this push pivot is to say: your finger is not allowed to push the object along the direction that deviate too much from this push direction.

### Object Affordances

“Object Affordance”, in a broader sense, means what kind of action this object can be used for. For example a chair affords to be sit upon, a button on the wall affords push, and a handle affords grasp.

In VG library we define a “narrower” sensed set of affordances that determines which kind of hand **interaction** we can have with this object, and how the object's **state** react in the virtual environment. 

| Affordances | Description | Object Joint Settings |
|-------|--------|---------|
| Graspable | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a>: Can be grasped | for all joint types | 
| Index Pushable | <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a>: Can be pushed by the index finger | for all joint types | 
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

The image below shows Unity's VG_Articulation component as an example for the GUI of Object Artiulation.

Note that the VirtualGrasp's object articulation is generic for all other client engines like Unreal.

To learn more details of Unity implementation see [VG_Articulation](unity_component_vgarticulation.html#unity-component-vgarticulation).

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}
