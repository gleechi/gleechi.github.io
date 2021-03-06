---
title: VG_EC_UnityXRHand controller
keywords: external-controller
sidebar: main_sidebar_0_9_5
permalink: unity_vg_ec_unityxrhand.0.9.5.html
folder: mydoc/external_controllers
---

{% include external_controller.html %}

## Description 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.0.9.5.html) controller as an external controller.
 
The following requirements have to be met to be able to enable the #define USE_LEAP_CONTROLLER above and use the controller:
 * You have the Unity XR Management package installed into your Unity project.

After this, use the "QUEST" option to [AutoSetup](unity_component_myvirtualgrasp.0.9.5.html#autosetup) your VG configuration.

{% include note.html content="It is called QUEST since we have mainly tested with Oculus integration of UnityXR, and not with other platforms that UnityXR supports." %}

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().