---
title: VG_EC_MouseHand controller
keywords: external-controller
sidebar: main_sidebar_0_10_1
permalink: unity_vg_ec_mousehand.0.10.1.html
folder: mydoc/external_controllers
---

{% include external_controller.html %}

## Description 

This is an external controller class that supports a Mouse controller as an external controller.

There are no requirements to use this controller, so you can use the "MOUSE" option to [AutoSetup](unity_component_myvirtualgrasp.0.10.1.html#autosetup) your VG configuration.

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through the Mouse position in your game window, as well as through the scroll wheel (moving the hands in depth).

### Grab Signals
will be controlled through the Mouse button clicks, left mouse button for left hand, right mouse button for right hand.
