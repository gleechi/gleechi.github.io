---
title: VG_EC_Manus controller
keywords: external-controller
sidebar: main_sidebar_1_4_0
permalink: unity_vg_ec_manus.1.4.0.html
folder: mydoc/external_controllers
---

## Description 

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.4.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports a generic overlay controller for the [Manus Glove](https://www.manus-meta.com/knowledge-articles/quantum-metagloves-first-time-setup) class as an external controller.

{% include important.html content="This is an **EXPERIMENTAL** controller only for the Manus sample. It will not function with VG in terms of grasping because there are some changes needed inside the Manus SDK. Necessary changes will be described on this page at a later stage." %}

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_MANUS_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation)." %}
      
The following requirements have to be met to be able to enable the #define VG_USE_MANUS_CONTROLLER above and use the controller:
 * You have the corresponding [Manus Core SDK](https://resources.manus-meta.com/downloads) installed on your computer.
 * You have the [Unity Plugin for Manus Core](https://resources.manus-meta.com/downloads) imported into your Unity project.
 * You have a Manus Pro License assigned to your SDK to use the Unity Plugin.

## Controller Profile

If these requirements are met, you will be able to use the **VG_CP_Manus.HandTracking** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_manus.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
All finger bones are mapped.

All finger bones are generically taken from the Transforms of the hand rig.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
