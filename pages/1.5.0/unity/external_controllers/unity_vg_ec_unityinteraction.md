---
title: VG_EC_UnityInteraction controller
keywords: external-controller
sidebar: main_sidebar_1_5_0
permalink: unity_vg_ec_unityinteraction.1.5.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.5.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

The following requirements have to be met to be able to use this controller:

 * You have the Unity XR Management package installed into your Unity project.

This is an external controller class that supports the action-based [Unity XR Interaction toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/xr-controller-action-based.html) controller as an external controller.
 
{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_UNITYINTERACTION_HAND** to your Unity player settings (Project Settings → Player → Script Compilation)." %}

The following requirements have to be met to be able to use the controller:

 * You have the "XR Plugin Management" package installed into your Unity project.
 * You have the "XR Interaction Toolkit" package installed into your Unity project.
 * You have selected "OpenXR" as the Plugin-Provider in Project Settings -> XR Plugin Management
 * if you use Oculus, you use it through "OpenXR" (Oculus -> Tools -> OVR Utilitites Plugin -> Set OVR to OpenXR)

## Controller Profile

If these requirements are met, you will be able to use the **VG_CP_Unity.XRInteraction** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.5.0.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_unityinteraction.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.devicePosition).

### Grab Signals
will be controlled through UnityXR controller system, such as InputDevice.TryGetFeatureValue(CommonUsages.trigger).

### Haptic Signals
will be controlled through UnityXR controller system, such as InputDevice.SendHapticImpulse().