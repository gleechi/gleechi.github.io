---
title: Axis Mappings
sidebar: main_sidebar_1_6_1
version: 1.6.1
keywords: controller, internal, external
permalink: axis_mappings.1.6.1.html
folder: knowledge
toc: true
---

## Background Problem

An axis mapping relates to a deviation in terms of bone pose orientation(s) between two coordinate frame representations. 

At the moment, such rotation deviations appear in two places: 
 
- in terms of **hand models** (a deviation in the standard of how hand models are rigged), and 
- in terms of **raw sensor data** (a deviation in the standard of how a sensor model is defined). 

For example: 

- in terms of **hand models**, one hand model may have all hand joints aligned along the Y axes, another may have the wrist aligned along the Z axis, and all the finger bones aligned along the X axis.
- in terms of **raw sensor data**, one sensor API may provide all hand joints aligned along the Y axes, another may provide the wrist aligned along the Z axis, and all the finger bones aligned along the X axis.

This is a problem of rotations only. Positions of bones are "clear" without a standard, but rotations need a standard to be interpreted correctly.

It is important to recognize that many controller plugins for Unity (e.g., LeapMotion, Oculus, Steam) come with their own hand models which are almost always adjusted to their own controller data standard. It is thus not possible (or at least highly complicated) to simply and freely combine a raw hand model of one plugin (e.g Oculus hand model) with the controller data of another plugin (e.g. Leap API). What makes it more complicated is that while some APIs properly document the rotation standard of their data (such as [LeapMotion here](https://developer-archive.leapmotion.com/documentation/cpp/api/Leap.Bone.html#cppclass_leap_1_1_bone_1a4ff50b291a30106f8306ba26d55ada76)), others provide no such documentation and leave us for trial-and-error.

It is also important to understand that in the VirtualGrasp SDK, all [VG_ExternalController](unity_component_vgcontrollerprofile.1.6.1.html#ready-to-use-vg_controllerprofiles-and-vg_externalcontroller-classes) classes extract raw controller data from the original APIs to compute hand poses (as matrices) that are then sent to VG which then adjusts the Unity Transforms. First using plugin-specific components to adjust the Unity transforms, then extracting their data and sending them to VirtualGrasp, which then adjusts the Unity transforms another time, is inefficient and error-prone.

## Solution Approach

In order to allow free combination of random hand models and random sensor data sources, both [VG_HandProfiles](unity_component_vghandprofile.1.6.1.html) and [VG_ControllerProfiles](controllers.1.6.1.html#controller-profile) allow the setup of rotational "Hand Mappings."

Examples for VG_HP_OculusHands (a [VG_HandProfile](unity_component_vghandprofile.1.6.1.html), left) and VG_CP_Oculus.OVRLib.HandTracking (a [VG_ControllerProfile](controllers.1.6.1.html#controller-profile), right):

| <img class="docimage" style="width:100%" src="images/unity/unity_vg_ec_handprofile_1_4_0.png"/> | <img class="docimage" style="width:100%" src="images/unity/unity_vg_ec_oculus.png"/> |

As you can see, the shared fields are the _Rotation Types_, _Left Hand Mapping_, and _Right Hand Mapping_. 

Through the _Rotation Types_ dropdown, you can select which rotation mappings should be enabled for this hand/controller in _Left Hand Mapping_, and _Right Hand Mapping_: Wrist, Finger, and Thumb. 

{% include image.html file="unity/unity_axis_mapping.png" alt="Axis mapping section in Unity." caption="An axis mapping section as it can be found in both VG_HandProfiles and VG_ControllerProfiles." %}

The reason for this three sections is that we have noticed that in the same hand model or the same controller API, deviations may not only be inconsistent between the left and the right hand, but even inconsistent over different bones. 

Some designers/controllers use a different orientation standard for the wrist than for the fingers, some an even different standard for the thumb (e.g., Mixamo uses a different standard for the thumb than for all the other fingers). Therefore, the interface allows you to define various rotation deviations for: wrist, finger bones, and thumb bones. 

Note that if you have not enabled "Thumb" as a rotation type (and thus "Thumb Rotation" does not show), the thumb also undergoes the "Finger Rotation" (being one of the fingers).

## Solution Result

Once each hand model / [VG_HandProfiles](unity_component_vghandprofile.1.6.1.html) or sensor API / [VG_ControllerProfile](controllers.1.6.1.html#controller-profile) has been properly configured in terms of these axis rotation mapping, that means you can combine freely any hand model with any sensor controller input.

It is important to mention that you only need to do this work in either of the following two cases:

- when you want to use a hand model that follows a rigging standard that is not also represented by any of the other [VG_HandProfiles](unity_component_vghandprofile.1.6.1.html); or 
- when you want to take on the task to integrate a new, unsupported controller plugin with VG. Note that all the [VG_ControllerProfiles](controllers.1.6.1.html#controller-profile) and the related VG_ExternalControllers have been setup by our team already and cover many of the most common controller inputs and we are ready to help for any new hardware endavours.

Please watch the video below for a tutorial that shows an example of how to adjust axis mappings when configuring a new VG_HandProfile for a new hand model in Unity. The video was recorded in an earlier version so the profile GUI is outdated. A new video instruction will be added soon.

{% include youtube.html id="UFCitkp39uw" %}