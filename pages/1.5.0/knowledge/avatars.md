---
title: Avatars
sidebar: main_sidebar_1_5_0
version: 1.5.0
keywords: avatar
permalink: avatars.1.5.0.html
folder: knowledge
toc: true
---
## Background

For any avatar model (skeletal mesh), VirtualGrasp identifies hand bones among the entire skeleton hierarchy, and creates the internal hand representation to control the hand movement and interaction with objects. 

The VG SDK includes an avatar model called GleechiRig (in VirtualGrasp/Resources/GleechiHands/) which is also used in the onboarding scene. In this avatar, both a left and a right hand are included in a single skeleton hierarchy.

However, avatars can have non-hand bones such as elbows, shoulders, or even full body bones. VirtualGrasp automatically identifies the hand bones and only controls the hand movement, but does not influence any optional other parts of the skeleton.

## Custom Hand Models 

### Hand Model Standard

The image below shows GleechiRig's left hand model. The labeled wrist and finger bones represent the hand bones whose movement VirtualGrasp controls. 

If you want to use a custom avatar (enabled in the Pro version of the VirtualGrasp SDK), the recommended minimum conditions to be met related to the skeletal hand structure are:
* A hand's wrist bone should include 5 fingers as children,
* with 3 bones in each finger whose movement VG controls, and
* for thumb, the 3 bones correspond to the first metacarpal and the 2 phalanges, and
* for non-thumb fingers, the 3 bones correspond to the 3 phalanges in human hand anatomy. 

Additionally, 

* The last transform (4th bone) at finger tip (thumb3_L for example) is recommended to be provided to give an accurate representation of the last bone's dimension. If a fingertip is missing, VirtualGrasp will estimate its position, but this may result in finger tip penetration when pushing or grasping objects. Note it is very easy in Unity to add missing fingertip bones manually.
* VirtualGrasp also supports custom hands with the 4 metacarpals connecting the non-thumb fingers, however it does not control the movement of them. 

{% include image.html file="vg_hand_model.png" width="100" alt="VG hand model." caption="VG Hand model example with 4 bones (including finger tip) each finger." %}

{% include tip.html content= "[VG_HandProfile](unity_component_vghandprofile.1.5.0.html) page gives detailed instruction on how to setup custom hands in Unity."%} 

### Separate Hand Models

If you have a skeletal mesh for one hand side and are creating the opposite side by duplicating and mirroring this hand, you can setup two separate avatars with same sensors to control the two hands. In such cases VirtualGrasp considers the left and right hand skeleton meshes as two separate _Avatars_.

In _Runtime/Resources/Prefabs/_ of the Unity SDK, two prefabs for basic avatar setup are included to showcase how to setup VG avatars using separate hand models:
* **SeparateHandsSensorAvatar** is a prefab setting up the {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} with separate left and right hand models (using a singular Gleechi left hand model _Runtime/Resources/GleechiHands/GleechiLeftHand.fbx_).  

* **SeparateHandsSensorAndReplayAvatars** is a prefab varient of **SeparateHandsSensorAvatar**, which shows how to setup VG library for sensor recording and replaying with separate hand models. 

<!--The image below shows an example of how to set it up in Unity, but it applies to any VG integrated game engine.

{% include image.html file="unity/unity_vg_avatar_sensor_separate_hands_setup.png" width="100" alt="Unity Avatar Sensor setup for two separate hand models." caption="Unity Avatar Sensor setup for two separate hand models." %} -->


