---
title: VG_EC_MouseHand controller
keywords: external-controller
sidebar: main_sidebar_1_4_0
permalink: unity_vg_ec_mousehand.1.4.0.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.4.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

{% include image.html file="unity/unity_vg_ec_mousehand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

This is an external controller class that supports a Mouse controller as an external controller.

There are no requirements to use this controller, so you can use the "VG_EC_MouseHand" controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html#controller-profile) configuration.

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through the Mouse position in your game window, as well as through the scroll wheel (moving the hands in depth).

### Grab Signals
will be controlled through the Mouse button clicks, left mouse button for left hand, right mouse button for right hand.
