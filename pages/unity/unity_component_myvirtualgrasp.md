---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_myvirtualgrasp.html
folder: mydoc
---

## [THIS PAGE NEEDS TO BE UPDATED]

### Sensor settings

In Unreal or Unity, VG_MyVirtualGrasp has a component where you can specify a number of interaction related options that can significantly change the user experiences when using our VirtualGrasp software. 

The most important options are explained here:

#### Finger control type

This provide the option to choose how sensor controls the finger motion

BY_SENSOR_FULL_DOFS: this means for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. 

BY_SENSOR_LOW_DOFS : this means for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path

BY_ANIMATION: this means for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation.

BY_EXTERNAL: this is only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs.

BY_OSCILLATED_ANIMATION: this will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (remain to be tested in unity when sensor type is External Controller )

#### Interaction type

This provides the option to choose what interaction type we use when grasping objects.

STICKY_HAND: is a type of interaction when grasping, the current hand/finger pose will be applied as the grasp. This simulates the “bad” grasps. When an object is not baked, this grasp will be used on it.

TRIGGER_GRASP: is a type of interaction when grasping, the hand will move smoothly from the sensor position to the grasp position close to the object.

JUMP_GRASP: is a type of interaction when grasping, the object will move smoothly from its current position into the hand.

PREVIEW_GRASP: is a type of interaction once hand is close to object, hand and finger will move to object at currently synthesized grasp, and this pose will update as you move the hand around the object, and object will not be picked up by hand until you push trigger grasp button on controller. This interaction type works best with the DYNAMIC_GRASP synthesis method.

JUMP_PRIMARY_GRASP: is a type of interaction that only applies a single “primary” grasp in the grasp database for a given object and hand.

When the interaction type is set toJUMP_PRIMARY_GRASPfor an object, this object's synthesis method will be forced to be STATIC_GRASP since a database of grasps are needed among which the primary grasp is stored. Also, you should have labeled one of the grasps in the database to be “Primary”, otherwise it will just apply the closest grasp in the database.

### Setup sensor settings

You can set a couple of sensor settings for all objects in the scene, in VG_SensorConfiguration → Settings → Global Grasp Interaction Type:

While finger control type is only specified globally, you can also overwrite the global interaction type and synthesis method for particular objects, by adding a VG_Interactable to the object and setting interaction type and synthesis method.

{% include image.html file="unity/unity_vg_interactable.png" alt="VG Interactable" caption="VG_Interactable Component." %}

Note that all objects without a customized VG_Interactable will follow the global settings (see above), but those with VG_Interactable will follow their local settings.

#### Transition duration

This is specifying how long it takes (e.g. 6 frames) in different transition phases of interaction. And this is a global setting that applies to all hands and all objects. For example

in the case of TRIGGER_GRASP interaction type, it takes e.g. 6 frames for the hand to move from sensor position to the grasp position once the user triggers the grasp button on the controller,

in the case of JUMP_GRASP interaction type, it takes e.g. 6 frames for the object to move from its current position to the hand once the user triggers the grasp button on the controller.

#### Push with index finger or palm

Here either index finger tip or palm pushes an object when it is in contact with the object in the direction of “push_axis”. “push_axis” defines a planar pushable surface on a bounding box of the object. If needed, a “push_circle” can be drawn on any pushable surface of the object as a hint on which object can be pushed, and once the finger tip / palm is in contact with the surface, the object will be moved by the finger / hand motion.

As an example to show the use the push hint when you use physical push, see the pushHint element in the VG_HintVisualizer.cs script (currently only Unity) and the VG_Controller.GetPushCircle(hand.m_avatarID, hand.m_side, out p, out q, out r, out inContact) function. It requests the push hint, which is represented by position p, rotation q, and radius r for drawing the push circle from the library. In the example, you can just assign a 3D sphere to the pushHint in the Unity Editor and it will be placed and shaped to represent the push circle. In the example script, “inContact” is not used, but will tell you if the finger is in contact with the pushable object or not, so you might trigger haptic feedback, for example.

An object can only have one push surface, which is defined by the “push_axis”. By default this axis is same as the joint axis you already specify. But you can also explicitly specify a push_axis that is different from the joint axis, as an example use case for sliding button.

#### Sensor offset

When the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust an offset in each controller setting to synchronize them:

Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.