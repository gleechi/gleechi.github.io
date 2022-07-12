---
title: VG_EC_LeapHand controller
keywords: external-controller
sidebar: main_sidebar_0_15_0
permalink: unity_vg_ec_leaphand.0.15.0.html
folder: mydoc/external_controllers
---

## Description

{% include external_controller.html %}

## Setup 

{% include image.html file="unity/unity_vg_ec_leaphand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

This is an external controller class that supports the LeapMotion controller as an external controller.

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_LEAP_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_LeapHand.cs." %}

The following requirements have to be met to be able to use this controller:

 * You have a [Core Assets](https://developer.leapmotion.com/releases) plugin imported into your Unity project.
 * Note that Core Assets > 4.4.0 are for LeapMotion SDK 4 or higher, and the older Core Assets are for LeapMotion SDK 3 (lastest CA 4.3.4).
 * You have the corresponding [LeapMotion SDK](https://developer.leapmotion.com/sdk-leap-motion-controller/) installed on your computer.

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through Leap controller system, such as Leap.Fingers.Bones.

### Grab Signals
Will be controlled through Leap controller system, such as Leap.Hand.GrabStrength.
