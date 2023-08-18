---
title: VG_EC_UnityXR controller
keywords: external-controller
sidebar: main_sidebar_1_5_0
permalink: unity_vg_ec_unityxr.1.5.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.5.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.html) controller (such as provided by Pico or Oculus integrations) as an external controller.
 
The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

## Controller Profile

If these requirements are met, you will be able to use the **VG_CP_Unity.UnityXR** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.5.0.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_unityxr.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().