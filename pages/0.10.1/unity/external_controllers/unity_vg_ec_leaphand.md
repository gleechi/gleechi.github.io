---
title: VG_EC_LeapHand controller
keywords: external-controller
sidebar: main_sidebar_0_10_1
permalink: unity_vg_ec_leaphand.0.10.1.html
folder: mydoc/external_controllers
---

{% include external_controller.html %}

## Description 

This is an external controller class that supports the LeapMotion controller as an external controller.
Please refer to [External Controllers](unity_component_vgexternalcontrollermanager.0.10.1.html) for the definition of an external controller for VG.

The following requirements have to be met to be able to enable the #define USE_LEAP_CONTROLLER in the VG_EC_LeapHand.cs file and use the controller:
 * You have a [Core Assets](https://developer.leapmotion.com/releases) plugin imported into your Unity project.
 * Note that Core Assets > 4.4.0 are for LeapMotion SDK 4, older are for LeapMotion SDK 3 (lastest CA 4.3.4).
 * You have the corresponding [LeapMotion SDK](https://developer.leapmotion.com/sdk-leap-motion-controller/) installed on your computer.
 
 After this, use the "LEAP_EXT" option to [AutoSetup](unity_component_myvirtualgrasp.0.10.1.html#autosetup) your VG configuration.
 
### Hand Poses
All finger bones are mapped.

Will be controlled through Leap controller system, such as Leap.Fingers.Bones.

### Grab Signals
Will be controlled through Leap controller system, such as Leap.Hand.GrabStrength.
