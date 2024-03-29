---
title: VG_EC_SteamHand controller
keywords: external-controller
sidebar: main_sidebar_1_0_0
permalink: unity_vg_ec_steamhand.1.0.0.html
folder: mydoc/external_controllers
---

## Description 

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.0.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports any SteamVR/OpenVR controller as an external controller. Examples are the Valve Knuckles controller or also the Oculus Touch controllers. Note that SteamVR only supports Windows, there is **no Android support for SteamVR**.

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_STEAMVR_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_SteamHand.cs." %}

The following requirements have to be met to be able to use this controller:

 * You have Steam and the corresponding [SteamVR SDK](https://store.steampowered.com/app/250820/SteamVR/) installed on your computer.
 * You have the [SteamVR Unity plugin](https://assetstore.unity.com/packages/tools/integration/steamvr-plugin-32647) imported into your Unity project.
 * You have OpenVR Loader selected in Unity XR Management Project Settings.

If these requirements are met, you will be able to use the "VG_EC_SteamHand" controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.0.0.html#controller-profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_steamhand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through Valve.VR controller system, such as SteamVR_Action_Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
