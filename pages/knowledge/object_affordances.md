---
title: Knowledge Base - Object Affordances
#tags: [getting_started]
keywords: component, object, affordance, joint
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: knowledge_sidebar
permalink: object_affordances.html
folder: mydoc
---

### Object Joint Types

This internal object tree is the key that determines the object-to-object interaction patterns:

Each object has a joint of a given type (specified in VG_Articulation see Figure 1 below) which determines how it moves in relation to its parent object.

If an object's joint is of an “unconstrained” type, meaning it is freely “floating”, then when you grasp this object, it will follow your hands movement freely.

If an object's joint is of a “constrained” type, meaning it is NOT freely “floating”, then when you grasp this object, it will not follow your hands movement, instead it constrain your hand movement.

If an object's joint is of a “constrained” type, then when you move its parent, this object will follow the parent.

If an object's joint is of a “constrained” type, and its parent object is not “fixed”, then when you move this constrained child object, its parent object will also be affected and moved.


| Type | Description | Additional features |
|-------|--------|---------|
| Floating | unconstrained, 6-dof joint, freely floating object | In VG_Articulation if check Set fix floating then when it is not grasped, will behave like a “fixed” object |
| Fixed | constrained, 0-dof joint, as if an integrated object with its parent | – |
| Revolute | constrained, 1-dof joint, rotate around an axis through a pivot point, limited by an angle range | In VG_Articulation [min, max] specifies the angle (degree) range; and if screw rate is >0, then when rotate will also linearly move along the axis like a “screw”. Discrete states (size > 1) can be set for some special affordances. | 
| Prismatic | constrained, 1-dof joint, move linearly along an axis through a pivot point, limited by an distane range | In VG_Articulation [min, max] specifies the distance range. Discrete states (size > 1) can be set for some special affordances. | 
| Cone | constrained, 3-dof joint, rotate around a pivot point limited by a cone limit, parameterized by a swing limit angle that determines the cone size, and twist limit angle that determines how much the object can rotate around the axis (center axis of the cone) | In VG_Articulation [min, max] specifies [swingLimit, twistLimit] (degree) respectively | 

### Object Affordances

“Object Affordance”, in a broader sense, means what kind of action this object can be used for. For example a chair affords to be sit upon, a button on the wall affords push, and a handle affords grasp.

In VG library we define a “narrower” sensed set of affordances that determines which kind of hand interaction we can have with this object in the virtual environment. 

| Affordances | Description | Object Joint Settings |
|-------|--------|---------|
| Graspable | Can be grasped | valid for all joint types | 
| Finger Pushable | Can be pushed by the index finger | valid for all joint types | 
| Normal | Object stay at the pose when hand is released  | valid for all kinds of joints | 
| Bounces | When released, bounce to the lowest discrete state | only valid for 1-dof joint, and has to provide >1 discrete states in VG_Articulation | 
| Bounces two stage | When released, bounce to the highest and lowest discrete state in an alternating order | only valid for 1-dof joint, and has to provide >1 discrete states in VG_Articulation | 
| Snaps | When released, snap to the closest discrete state | only valid for 1-dof joint, and has to provide >1 discrete states in VG_Articulation | 



{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

