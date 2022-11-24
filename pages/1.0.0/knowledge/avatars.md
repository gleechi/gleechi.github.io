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
If on the other hand you have two separate skeletal meshes one for left hand and one for right hand, the you can setup two Avatars with same sensors to control them
(see [separate hand models](#separate-hand-models)). 

## Custom Hand Model 

### Hand Model Standard
If developers want to use custom avatars with the Pro version of VirtualGrasp SDK, there are certain conditions on which kind of skeletal meshes are supported, and GleechiRig gives a reference of rigging / model hierarchy of the hands:

* a hand's wrist bone should include 5 fingers as children (no extra bones), and 
* each finger should include 3-4 bones (with or without fingertip). If a fingertip is missing, VirtualGrasp will estimate its position, but it is recommended, and also very easy in Unity to add missing fingertip bones manually, and
* hands with metacarpals for the non-thumb fingers are not fully supported. 

{% include image.html file="vg_hand_model.png" width="100" alt="VG hand model." caption="VG Hand model example with 4 bones (including finger tip) each finger." %}

### Separate Hand Models

Sometimes, developers have a skeleton mesh for one hand side, and create the opposite side by mirroring hence a separate skeleton mesh. In such cases VirtualGrasp considers the left and right hand skeleton meshes as two separate _Avatars_; and you can set it up using same _Hand Profile_ and [sensor setup](unity_get_started_sensors.1.0.0.html). 

Image below shows an example how to set it up in Unity, but it applies to any VG integrated game engines.

{% include image.html file="unity/unity_vg_avatar_sensor_separate_hands_setup.png" width="100" alt="Unity Avatar Sensor setup for two separate hand models." caption="Unity Avatar Sensor setup for two separate hand models." %}

## Hand Profile

VirtualGrasp provides "hand profile" to configure a number of hand model-related settings and thereyby allows you to quickly switch between different custom hands. 

{% include image.html file="unity/unity_vg_ec_handprofile.png" alt="VG Controller profile in Unity." caption="VG Controller profile as scriptable object in Unity." %}

(Editing of this section is in progress.)

### Hand Axis Mappings

### Controller Axis Mappings

<!-- Moved these commented texts from External controller manager page to here. 
## Modifying or Writing a Controller

The following we describe technical considerations that you may have when you modify or write your own VG_ExternalController. You may especially end up here if you try to use your own, customized hand model for your application. Note that "SDK" in this case refers to the particular controller plugin (such as Oculus SDK, Ultraleap SDK, etc.).

### Initialization and Mapping

Each VG_ExternalController has to include a VG_ExternalControllerMapping that maps the bone indices provided by the SDK to VirtualGrasp. The VG_ExternalControllerMapping includes variables for 16 bones (1 wrist + 5 * 3 finger bones). The VG_ExternalControllerMapping should be initialized in the VG_ExternalController Initialization function.

### Coordinate-Frame Corrections

If you use a custom hand rig different than the GleechiRig provided in the SDK, you may find the fingers of the hand bending along the wrong axis.

The reason for the mismatch is that each finger controller (for example, VG_EC_OculusHands.cs) is adjusting the raw finger orientations that come directly from the controller API (for example, from the Oculus Integration plugin) to match the hand model representation that is provided with the SDK.

In this case you have two options:

1. you can base or adjust your hand rig to the existing hand rig, keeping the coordinate-frame definition (e.g., y along the finger bone, x to the right, z towards the palm) as in the provided rig. This is some work for a 3D artist.

2. in the controller (such as VG_EC_OculusHands.cs), in the Compute() function, you will see that all the raw finger orientations are processed through the modifyPose() function. Each pose matrix is modified to a new rotation based on if it is wrist or finger and if it is left and right hand (these were the changes we needed for the provided hand model). This is some work for a programmer.

    1. In the optimal case that your hand model is aligned with finger tracking sensor data, just remove the two lines where modifyPose() is called.
    2. If that does not work that means your hand model is not aligned with the finger tracking sensor data and that you have to update the modifyPose() function. Enabling the DebugDraw() call just below the modifyPose() can help you by visualizing the skeleton and rotations.
-->

## Avatar Types

There are three avatar types in VirtualGrasp:

* By default an avatar is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, meaning that avatar's hands are directly controlled by the [sensors](controllers.1.0.0.html) for movement and object interaction. This is also the avatar used for [recording sensor data](sensor_record_replay.1.0.0.html) (feature available in **Pro version**).
* If _Replay_ option is ticked, then the avatar will be registered as a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %}. The hands of this avatar will be controlled by pre-recorded sensor data. Note this <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">sensor record and replay</a> feature is only available in VirtualGrasp **Pro version**.
* Both {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} and {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} can be created as a {% include tooltip.html tooltip="PhysicalAvatar" text="physical avatar" %} if _Physical_ option is ticked. 

{% include image.html file="unity/unity_hand_model_1_0_0.png" alt="Unity hand model." caption="Hand model references need to be provided in MyVirtualgrasp → Avatars → Skeletal Mesh.<br>Note that \"Replay\" only appears in Pro-versions of VG." %}

