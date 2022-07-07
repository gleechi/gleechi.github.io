---
title: VG_EC_SteamHand controller
keywords: external-controller
sidebar: main_sidebar_0_15_0
permalink: unity_vg_ec_steamhand.0.15.0.html
folder: mydoc/external_controllers
---

## Description 

{% include external_controller.html %}

## Setup 

This is an external controller class that supports any SteamVR/OpenVR controller as an external controller. Examples are the Valve Knuckles controller or also the Oculus Touch controllers. Note that SteamVR only supports Windows, there is **no Android support for SteamVR**.

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_STEAMVR_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_SteamHand.cs." %}

The following requirements have to be met to be able to use this controller:

 * You have Steam and the corresponding [SteamVR SDK](https://store.steampowered.com/app/250820/SteamVR/) installed on your computer.
 * You have the [SteamVR Unity plugin](https://assetstore.unity.com/packages/tools/integration/steamvr-plugin-32647) imported into your Unity project.
 * You have OpenVR Loader selected in Unity XR Management Project Settings.

### AutoSetup

Finally, you can use the "Steam Hand" option to [AutoSetup](unity_component_myvirtualgrasp.0.15.0.html#autosetup) your VG configuration. For this controller, AutoSetup 

* will set "External" to "SteamHand"
* will set "FingerControlType" to "BY_SENSOR_FULL_DOFS"
* will set "Origin" to the transform called "XRRig"
* will set "Offset" values to rotation (175f, 160f, 210f) and position (-0.06f, -0.1f, -0.01f).

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through Valve.VR controller system, such as SteamVR_Action_Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
