---
title: Avatars
sidebar: main_sidebar_1_3_0
version: 1.3.0
keywords: avatar
permalink: avatars.1.3.0.html
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

### Separate Hand Models

If you have a skeletal mesh for one hand side and are creating the opposite side by duplicating and mirroring this hand, you can setup two separate avatars with same sensors to control the two hands. In such cases VirtualGrasp considers the left and right hand skeleton meshes as two separate _Avatars_. You can set it up using same _Hand Profile_ and [sensor setup](unity_get_started_sensors.1.3.0.html). 

[VG_HandProfile](unity_component_vghandprofile.1.3.0.html) page gives detailed instruction on how to setup custom hands in Unity.

<!--The image below shows an example of how to set it up in Unity, but it applies to any VG integrated game engine.

{% include image.html file="unity/unity_vg_avatar_sensor_separate_hands_setup.png" width="100" alt="Unity Avatar Sensor setup for two separate hand models." caption="Unity Avatar Sensor setup for two separate hand models." %} -->

## Avatar Types

There are three avatar types in VirtualGrasp:

* By default an avatar is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, meaning that avatar's hands are directly controlled by the [sensors](controllers.1.3.0.html) for movement and object interaction. This is also the avatar used for [recording sensor data](sensor_record_replay.1.3.0.html) (feature available in **Pro version**).
* If the _Replay_ option is ticked, then the avatar will be registered as a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %}. The hands of this avatar will be controlled by pre-recorded sensor data. Note this <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">sensor record and replay</a> feature is only available in VirtualGrasp **Pro version**.
* Both {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} and {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} can be created as a {% include tooltip.html tooltip="PhysicalAvatar" text="physical avatar" %} if _Physical_ option is ticked. 
* Only {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} can be specified to have mirror hand control if _Mirror_ option is ticked. When mirror hand control is enabled, the controller/sensor signal from a user's left hand side will be used to control avatar hand of the right side, vice versa. 

{% include image.html file="unity/unity_hand_model_1_2_0.png" alt="Unity hand model." caption="Hand model references need to be provided in MyVirtualgrasp → Avatars → Skeletal Mesh.<br>Note that \"Replay\" only appears in Pro-versions of VG." %}

{% include callout.html content= "The physical avatar currently is only semi-physical in that only colliders are added to hand bones, no rigid bodies or articulation bodies are used." %} 

