---
title: VG_Recorder Component (Pro)
#tags: [getting_started]
keywords: component, recorder, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_3
permalink: unity_component_vgrecorder.1.6.3.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_recorder_1_5_0.png" alt="VG Recorder" caption="VG_Recorder Component." %}

## Description

The VirtualGrasp library (VG_Controller) has a couple of [API functions](virtualgrasp_unityapi.1.6.3.html#recording_interface_api-pro) 
for recording and replaying {% include tooltip.html tooltip="SensorData" text="sensor data" %}. For convenience, the SDK includes a VG_Recorder {% include tooltip.html tooltip="VGPublicScript" text="public script" %} as a customizable component. 

You can use it to access the major functionalities which are explained in [sensor record and replay](sensor_record_replay.1.6.3.html).

Some example use cases are:
* “replaying entire instruction sequence”.
* “replaying a specific object interaction for instruction”.
* “quick testing of a whole interaction sequence”.

{% include singleton_script.html %}

## How to Record Sensor Data

In order to record sensor data, a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} needs to be created in [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.6.3.html#avatars). 

Pressing the _Recording Key_ during play will toggle between starting and stopping the recording of an interaction sequence.
After a recording is finished, the recorded data will be kept in the memory. And if _New Recording Path_ is provided, it will be saved as a .sdb file. Note file name has to end with ".sdb", and will be corrected by VG if not upon game launch. 

{% include tip.html content="To make the VG_Recorder react appropriately to keyboard input, the Unity Editor needs to be in focus (by mouse click on the game window once)." %}

## How to Replay Sensor Data

In order to replay the recorded sensor data, a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} needs to be created in [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.6.3.html#avatars), and corresponding skinned mesh renderer should be specified in _Replay Avatars_ entry. 

VG_Recorder allows to assign multiple _Replay Avatars_. This allows you to replay data on a pair of hands that are represented by [separate hand models](avatars.1.6.3.html#separate-hand-models). 

Pressing the _Replay Sequence Key_ or _Replay Segment Key_ during play will replay the recorded sensor data.
* When replay starts, normally sensor data will be loaded from the .sdb assets provided by _Replay Recording_ list. 
* However replay can also happen directly after recording without providing sensor data in _Replay Recording_ list. In such case, replay is using just recorded data in in memory. 

You can replay recorded sensor data in following two ways. 

### Full and scene-specific sequence replay

After you have recorded an {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can fully replay it later. In this replay mode, the hand movements will be replayed exactly as they were recorded in global coordinate frame. That means if you change positions of objects different from when they are during recording, the replaying hand will grasp empty air. 

This option is very handy when you want to record and replay for example an assembling task where interactions with multiple objects are involved. However you need to guaranttee 
1. while replaying all objects are at the same location as when they are recorded,
2. you use {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} with same hand models as the {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} used for recording.

Pressing the _Replay Sequence Key_ will replay the recording provided in _Recording Filename_ from its start with the replay avatar. Pressing _Left Shift + Replay Sequence Key_ will pause and resume the replay. To create a second avatar to follow the recording, please follow the [instructions below](#how-to-create-another-pair-of-hands-for-replaying). 

### Partial and object-specific segment replay

The second replay mode is to replay an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %}. After you have recorded a full {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can replay a specific part of it - an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} (specified by the _Segment ID_) - with a specified hand (_Side_) and object (_Replay Object_). 
See [sensor record and replay](sensor_record_replay.1.6.3.html#background) to understand interaction segments.

In the VG_Recoder, pressing the _Replay Segment Key_ will replay a specific 
{% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} of the recording provided in _Recording Filename_ with the replay avatar. 
Holding the _Left Shift button_ while pressing the _Replay Segment Key_ allows pause and resume of the replay. In the movie above, the blue button triggers this replay.

This option is handy when you want to record the entire training sequence that involved multiple steps consisting of interaction with multiple objects, and later you just want to extract some individual {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} to insert into a training authoring system as one step.

{% include tip.html content="A very useful feature of object-specific segment replay is that the object does not need to be placed at exact same location as when sensor data is recorded, because the recorded wrist pose will always be transformed to be centered around current pose of the replay object." %}

Which segment is to be replayed is configured in _Segment Replay Options_:  

| Option | Description |
|-------|--------|--------|
| Side| to which hand side the segment belongs |  
| Segment ID |  which segment to replay | 
| Replay Object | the transform of the object that has same shape as the object recorded in that segment | 

VG_Recorder image at the beginning of this page is configured to play segment #3 on left hand on object apple on the example recording shown below.




        SensorDB has 2 hand interaction(s):
         humanoid_handLeft1 has 10 interaction segments(s):
           segment #0  has 462/0 frames/states
           segment #1  has 934/0 frames/states, on object baseball
           segment #2  has 169/0 frames/states
           segment #3  has 568/0 frames/states, on object apple
           segment #4  has 178/0 frames/states
           segment #5  has 631/0 frames/states, on object baseball
           segment #6  has 152/0 frames/states
           segment #7  has 593/0 frames/states, on object pear
           segment #8  has 40/0 frames/states
           segment #9  has 358/0 frames/states, on object screwdriver
         humanoid_handRight1 has 1 interaction segment(s):
           segment #0  has 4085/0 frames/states


{% include warning.html content="The current VG_Recorder GUI is still not very user-friendly since you need to visualize the summary of the recorded sensor data as above to pick the valid _Segment Replay Options_. And this summary is only shown in console output when you replay the full sequence once." %}

## How to Create another Pair of Hands for Replaying

If you want a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} co-exist with a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} while playing in a scene, you can instantiate another pair of hands to be controlled by the replay. 
* add another avatar with hands into the scene (such as by duplicating the avatar you already have), 
* add another element to MyVirtualGrasp→Avatars, drag the SkinnedMeshRenderer from scene to _SkeletalMesh_ field and check it as _Replay_ avatar, 
* also assign the SkinnedMeshRenderer to the _Replay Avatar_ slot of the VG_Recorder (meaning that you want to replay the recordings on this avatar).

{% include tip.html content= "Runtime/Resources/Prefabs/ includes two prefabs **SensorAndReplayAvatars** and **SeparateHandsSensorAndReplayAvatars** that give examples of basic VG library setup that enables sensor recording and replaying. The former uses _GleechiRig_ that includes both left and right hands, and the latter uses separate left and right hand models."%} 
 