---
title: VG_EC_Mouse controller
keywords: external-controller
sidebar: main_sidebar_1_6_3
permalink: unity_vg_ec_mouse.1.6.3.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.6.3.html) on the purpose of a VG_ExternalController." %}

## Setup 

{% include image.html file="unity/unity_vg_ec_mouse.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

This is an external controller class that supports a Mouse controller as an external controller.

## Controller Profile
There are no requirements to use this controller, so you can use the **VG_CP_Common.Mouse** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.6.3.html#profile) configuration.

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through the Mouse position in your game window, as well as through the scroll wheel (moving the hands in depth).

### Grab Signals
will be controlled through the Mouse button clicks, left mouse button for left hand, right mouse button for right hand.
