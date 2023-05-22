---
title: VG_EC_UnityXRHand controller
keywords: external-controller
sidebar: main_sidebar_1_3_0
permalink: unity_vg_ec_unityxrhand.1.3.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.3.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a [UnityXR](https://docs.unity3d.com/Manual/XR.1.3.0.html) controller (such as provided by Pico or Oculus integrations) as an external controller.
 
The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

If these requirements are met, you will be able to use the "VG_EC_UnityXRHand" controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.3.0.html#controller-profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_unityxrhand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().