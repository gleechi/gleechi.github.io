---
title: VG_EC_UnityXRHands controller
keywords: external-controller
sidebar: main_sidebar_1_5_0
permalink: unity_vg_ec_unityxrhands.1.5.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.5.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

 This is an external controller class that supports the Unity XRHands controller as an external controller.
 
{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_XRHANDS_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation)." %}

 The following requirements have to be met to be able to enable the #define VG_USE_XRHANDS_CONTROLLER above and use the controller:
  * You have followed the installation and setup instructions of the [Unity XRHands package](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.1/manual/)

## Controller Profile
If these requirements are met, you will be able to use the **VG_CP_Unity.XRHands** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.5.0.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_unityxrhands_1_4_0.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses

All finger bones are mapped.

Will be controlled through Unity's XRHandSubsystem controller system, such as XRHand.GetJoint().
