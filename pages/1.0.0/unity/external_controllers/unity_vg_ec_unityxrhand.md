---
title: VG_EC_UnityXRHand controller
keywords: external-controller
sidebar: main_sidebar_1_0_0
permalink: unity_vg_ec_unityxrhand.1.0.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.0.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.html) controller (such as provided by Pico or Oculus integrations) as an external controller.
 
<!--{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_UNITYXR_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_UnityXRHand.cs." %}-->

The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

If these requirements are met, you will be able to use the "VG_EC_UnityXRHand" controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.0.0.html#controller-profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_unityxrhand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().