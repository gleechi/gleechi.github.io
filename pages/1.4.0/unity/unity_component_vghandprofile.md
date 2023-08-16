---
title: VG_HandProfile [Scriptable Object]
keywords: editor, script
sidebar: main_sidebar_1_4_0
permalink: unity_component_vghandprofile.1.4.0.html
folder: mydoc
---

## Description

VirtualGrasp provides VG_HandProfiles (in Unity as ScriptableObjects) to configure a number of hand model-related settings and thereby allows you to quickly switch between different hand models.

{% include callout.html content="You only need to create a new instance of a VG_HandProfile if you import a new hand model into your game that deviates from a hand model that you already have. You then need to configure the hand bone mapping as well as potentially the mapping rotations (see below) for your new VG_HandProfile." %}

{% include image.html file="unity/unity_vg_ec_handprofile_1_4_0.png" alt="VG_HandProfile in Unity." caption="Example of a VG_HandProfile as a scriptable object in Unity." %}

## Hand Mapping Rotations

For various hand models, the artists may have designed the coordinate frames differently. To compensate for these rotation offset, you have configure VG_HandProfile's **Left Hand Mapping** and **Right Hand Mapping** settings. Rotation Types and Hand Mappings define how the hand model deviates in terms of bone pose orientations. See [Axis mappings](axis_mappings.1.4.0.html) for a more detailed explanation. 

## Hand Bone Mapping

The [Gleechi hand model standard](avatars.1.4.0.html#hand-model-standard) shows the requirement of the hiearchical structure of hand bones in order for VG to automatically identify and assign hand bones to VG's internal representation. When your hand model is not following this standard, then identified hand bones may be off. For example, the hands may not be identified at all, or even if they are identified, some bones may be mis-represented like the first finger bone (index 0) may be mapped to the metacarpal bone. To fix this, you can manually provide a hand bone map by loading your hand skinned mesh and editing the Left and Right Hand Bone Maps, then click **Assign Hand Bone Indices** to save the map as "hand bone indices" in the hand profile.

## Tutorial

Please watch the video below for a tutorial that shows an example of how to configure a VG_HandProfile for your Custom Hand in Unity. In current video **Hand Bone Indices** is not needed because the hand model follows the Gleechi hand model standard. The video was recorded in an earlier version so the profile GUI is outdated. A new video instruction will be added soon.

{% include youtube.html id="UFCitkp39uw" %}