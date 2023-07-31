---
title: VG_HandProfiles Scriptable Object
keywords: editor, script
sidebar: main_sidebar_1_4_0
permalink: unity_component_vghandprofile.1.4.0.html
folder: mydoc
---

## Description

VirtualGrasp provides VG_HandProfiles (in Unity as ScriptableObjects) to configure a number of hand model-related settings and thereby allows you to quickly switch between different custom hands.

{% include image.html file="unity/unity_vg_ec_handprofile_1_4_0.png" alt="VG_HandProfile in Unity." caption="VG_HandProfile as scriptable object in Unity." %}


## Rotation Mapping

VirtualGrasp controlls wrist and finger rotations assuming an internal coordinate frame used for wrist and finger bones. For wrist the y-axis is pointing towards finger and z-axis is pointing inward to palm direction. For fingers the y-axis is pointing towards distal end, and z-axis is pointing to the palm side of the finger. However for custom hands, the artists may have designed these coordinate frames differently. Therefore to compensate the rotation offset, you can configure VG_HandProfile's **Left Hand Mapping** and **Right Hand Mapping** settings. 


## Finger Bone Mapping

[Gleechi hand model standard](avatars.1.4.0.html#hand-model-standard) shows the requirement of the hiearchical structure of hand bones in order for VG to automatically identify and assign hand bones to VG's internal representation. When your hand model is not following this standard, then identified hand bones may be off: for example the hands may not be identified at all, or even if they are identified, some bones may be mis-represented like the first finger bone (index 0) may be mapped to the metacarpal bone. To fix this, you can manually provide a hand bone map by loading your hand skinned mesh and editing the Left and Right Hand Bone Maps, then click **Assign Hand Bone Indices** to save the map as "hand bone indices" in the hand profile.


Please watch the video below for a tutorial that shows an example of how to configure a VG_HandProfile for your Custom Hand in Unity. In current video **Hand Bone Indices** is not needed because the hand model follows the Gleechi hand model standard. The video was recorded in an earlier version so the profile GUI is outdated. A new video instruction will be added soon.

{% include youtube.html id="UFCitkp39uw" %}