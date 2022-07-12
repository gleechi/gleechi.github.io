---
title: VG_EC_UnityInteractionHand controller
keywords: external-controller
sidebar: main_sidebar_0_15_0
permalink: unity_vg_ec_unityinteractionhand.0.15.0.html
folder: mydoc/external_controllers
---

## Description

{% include external_controller.html %}

## Setup 

{% include image.html file="unity/unity_vg_ec_unityinteractionhand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

This is an external controller class that supports the action-based [Unity XR Interaction toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/xr-controller-action-based.html) controller as an external controller.
 
The following requirements have to be met to be able to enable the #define VG_USE_UNITYINTERACTION_HAND above and use the controller:

 * You have the "XR Plugin Management" package installed into your Unity project.
 * You have the "XR Interaction Toolkit" package installed into your Unity project.
 * You have selected "OpenXR" as the Plugin-Provider in Project Settings -> XR Plugin Management
 * if you use Oculus, you use it through "OpenXR" (Oculus -> Tools -> OVR Utilitites Plugin -> Set OVR to OpenXR)

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().