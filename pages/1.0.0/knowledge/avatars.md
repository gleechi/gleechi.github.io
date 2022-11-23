---
title: Avatars
sidebar: main_sidebar_1_0_0
version: 1.0.0
keywords: avatar
permalink: avatars.1.0.0.html
folder: knowledge
toc: true
---
## Background

For any avatar model (skeletal mesh), VirtualGrasp identifies the left and right hands (i.e. wrist bones) among the entire skeleton hierarchy, and create the internal hand representation to control the hand movement and interaction with objects. 

By default, Gleechi provides an avatar model, GleechiRig in VirtualGrasp/Resources/GleechiHands/. In this avatar both left and right hands are included in the single skeleton hierarchy, and there are no bones other than hand bones included. 
However avatars can have non-hand bones such as arm or even full body. VirtualGrasp automatically identifies the hand bones and only controls the hand movement, without influencing any other parts of the skeleton. 
If on the other hand you have two separate skeletal meshes one for left hand and one for right hand, the you can setup two Avatars. 

## Custom Hand Model 

### Hand Model Standard
If developers want to use custom avatars with the Pro version of VirtualGrasp SDK, there are certain conditions on which kind of skeletal meshes are supported, and GleechiRig gives a reference of rigging / model hierarchy of the hands:

* a hand's wrist bone should include 5 fingers as children (no extra bones), and 
* each finger should include 3-4 bones (with or without fingertip). If a fingertip is missing, VirtualGrasp will estimate its position, but it is recommended, and also very easy in Unity to add missing fingertip bones manually, and
* hands with metacarpals for the non-thumb fingers are not fully supported. 

{% include image.html file="vg_hand_model.png" width="100" alt="VG hand model." caption="VG Hand model example with 4 bones (including finger tip) each finger." %}

### Separate Hand Models

Sometimes, developers have a skeleton mesh for one hand (left or right), and create the opposite side by mirroring; or there could be separate skeleton meshes for left and right hands. In such cases VirtualGrasp considers the left and right hand skeleton meshes as two separate Avatars; and you can set it up using same _Hand Profile_ and [sensor setup](unity_get_started_sensors.1.0.0.html). 

Image below shows an example how to set it up in Unity, but it applies to any VG integrated game engines.

{% include image.html file="unity/unity_vg_avatar_sensor_separate_hands_setup.png" width="100" alt="Unity Avatar Sensor setup for two separate hand models." caption="Unity Avatar Sensor setup for two separate hand models." %}

## Axis Mappings

### Controller Axis Mapping

{% include image.html width = "60" file="knowledge/3D_Cartesian_Coodinate_Handedness.jpg" alt="LHS/RHS" %} <figcaption>The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand.<br>Source: Original by <a href="https://commons.wikimedia.org/wiki/File:3D_Cartesian_Coodinate_Handedness.jpg">PrimalShell</a>, <a href="https://en.wikipedia.org/wiki/en:Creative_Commons">Creative Commons</a> <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">Attribution-Share Alike 3.0 Unported</a> license.</figcaption>

### Hand Axis Mappings