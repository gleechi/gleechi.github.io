---
title: VG_EC_OVR controller
keywords: external-controller
sidebar: main_sidebar_1_6_1
permalink: unity_vg_ec_ovr.1.6.1.html
folder: mydoc/external_controllers
---

## Description 

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.6.1.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a generic overlay controller for the [OVRHand](https://developer.oculus.com/documentation/unity/unity-handtracking/) class as an external controller.

{% include important.html content="This is an **EXPERIMENTAL** controller only for the OculusIntegration sample. It will not function with VG in terms of grasping because VG updates in FixedUpdate() will be overwritten by OVRHand updates which run in Update(). <br><br>

At the moment, we therefore recommend not to use OVRHand / OVRCustomSkeleton but instead use one of the various finger controllers that come with VirtualGrasp and take the same sensor signal. You can compare the solutions in the OculusIntegration sample." %}

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_OCULUS_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation)." %}
      
The following requirements have to be met to be able to enable the #define VG_USE_OVRHAND_CONTROLLER above and use the controller:

 * You have the [Oculus SDK](https://www.oculus.com/setup/) installed on your computer.
 * You have the [Oculus Integration plugin](https://developer.oculus.com/downloads/package/unity-integration/) imported into your Unity project.
 * You are using a handmodel / rig that is based on the [OVRHand / OVRCustomSkeleton](https://developer.oculus.com/documentation/unity/unity-handtracking/) classes.

## Controller Profile

If these requirements are met, you will be able to use the **VG_CP_Oculus.OVRHand.HandTracking** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.6.1.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_ovr.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
All finger bones are mapped.

All finger bones are generically taken from the Transforms of the hand rig (which is controlled by the OVRHand component).

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
