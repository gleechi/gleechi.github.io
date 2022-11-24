---
title: VG_EC_UnityXRHand controller
keywords: external-controller
sidebar: main_sidebar_0_13_0
permalink: unity_vg_ec_unityxrhand.0.13.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.0.13.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.0.13.0.html) controller (such as provided by Pico or Oculus integrations) as an external controller.
 
<!--{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_UNITYXR_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_UnityXRHand.cs." %}-->

The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

### AutoSetup

Finally, you can the "UNITY_XR" option to [AutoSetup](unity_component_myvirtualgrasp.0.13.0.html#autosetup) your VG configuration.

For this controller, AutoSetup 

* will set "External" to "UnityXR"
* will set "FingerControlType" to "BY_ANIMATION"
* will set "Origin" to the transform called "XRRig"
* will set "Offset-Position" to (-0.045, -0.1, -0.03) and "Offset-Rotation" to (23.7, 91.63, 92.7)

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().