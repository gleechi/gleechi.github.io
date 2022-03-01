---
title: VG_EC_UnityXRHand controller
keywords: external-controller
sidebar: main_sidebar_0_10_1
permalink: unity_vg_ec_unityxrhand.0.10.1.html
folder: mydoc/external_controllers
---

{% include external_controller.html %}

## Description 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.0.10.1.html) controller (such as provided by Pico or Oculus integrations) as an external controller.
 
The following requirements have to be met to be able to enable the #define USE_UNITYXR_CONTROLLER above and use the controller:
 * You have the Unity XR Management package installed into your Unity project.

After this, use the "UNITY_XR" option to [AutoSetup](unity_component_myvirtualgrasp.0.10.1.html#autosetup) your VG configuration.

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().