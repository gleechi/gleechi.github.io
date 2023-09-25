---
title: VG_EC_Script controller
keywords: external-controller
sidebar: main_sidebar_1_6_3
permalink: unity_vg_ec_script.1.6.3.html
folder: mydoc/external_controllers
---

## Description

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.6.3.html) on the purpose of a VG_ExternalController." %}

## Setup 

{% include image.html file="unity/unity_vg_ec_script.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

This is an external controller class that supports a Script controller as an external controller. 

## Controller Profile
There are no requirements to use this controller, so you can use the **VG_CP_Common.Script** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.6.3.html#profile) configuration.

Providing the VG_EC_Script controller profile will allow you to access controller signals (for now grab strength and wrist pose) through public variables from other scripts in your project.

## Functionality

### Hand Poses
Only the wrists are mapped.

Will be controlled through your interactions with the wrist transform from other scripts.

### Grab Signals
will be controlled through your interactions with the grab strength from other scripts.
