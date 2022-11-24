---
title: VG_Recorder Component
#tags: [getting_started]
keywords: component, recorder, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_0_0
permalink: unity_component_vgrecorder.1.0.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_recorder_1_0_0.png" alt="VG Recorder" caption="VG_Recorder Component." %}

## Description

The VirtualGrasp library (VG_Controller) has a couple of [API functions](virtualgrasp_unityapi.1.0.0.html#recording_interface_api) 
for recording and replaying {% include tooltip.html tooltip="SensorData" text="sensor data" %}. For convenience, the SDK includes a VG_Recorder {% include tooltip.html tooltip="VGPublicScript" text="public script" %} as a customizable component. 

You can use it to access the major functionalities which are explained in [sensor record and replay](sensor_record_replay.1.0.0.html#sensor-record-replay).

Some example use cases are:
* “replaying entire instruction sequence”.
* “replaying a specific object interaction for instruction”.
* “quick testing of a whole interaction sequence”.

{% include singleton_script.html %}

## How to Record Sensor Data

In order to record sensor data, a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} needs to be created (see [Avatar Types](avatars.1.0.0.html#avatar-types)). 

If _Recording Mode_ is "MANUAL", pressing the _Recording Key_ during play will toggle between starting and stopping the recording of an interaction sequence.
If _Recording Mode_ is "RECORD_ON_PLAY" recording will kickoff immediately once play starts.

After a recording is finished, a file with the recorded data will be written, named after the provided _Recording Filename_. 
In the current implementation of VG_Recorder, the recording will be **attached** to the same file, so if you want to separate and keep multiple recordings, 
you have to rename them.
If however _Replay From Memory_ is ticked, then the recorded data will not be written to a file but kept in the memory. 

{% include tip.html content="To make the VG_Recorder react appropriately to keyboard input, the Unity Editor needs to be in focus (by mouse click on the game window once)." %}

### Important Note on the Files

In order to support recording and replaying {% include tooltip.html tooltip="SensorData" text="sensor data" %} and re-using that information, there will be recording files in each project.

## How to Replay an Interaction Sequence

In order to replay the recorded sensor data, a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} needs to be created (see [Avatar Types](avatars.1.0.0.html#avatar-types)). 

If _Recording Mode_ is "MANUAL", pressing the _Replay Sequence Key_ or _Replay Segment Key_ during play will replay the recorded sensor data.
If _Recording Mode_ is "RECORD_ON_PLAY" replay will kickoff immediately once play starts.

When replay starts, normally sensor data will be loaded from the file with recorded data named after the provided _Replay Filename_. 
If however _Replay From Memory_ is ticked, then replay will assume the recording is already done and saved in memory. 

Depending on the options specified in VG_Recorder window, you can replay recorded sensor data in following three ways. 

### Full and scene-specific interaction replay

After you have recorded an {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can fully replay it later. The _Replay Object_ has to be empty (None). In this replay mode, the hand movements will be replayed exactly as they were recorded in global coordinate frame. That means if you change positions of objects different from when they are during recording, the replaying hand will grasp empty air. 

This option is very handy when you want to record and replay for example an assembling task where interactions with multiple objects are involved. However you need to guaranttee 
1. while replaying all objects are at the same location as when they are recorded,
2. you use {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} with same hand models as the {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} used for recording.

Pressing the _Replay Sequence Key_ will replay the recording provided in _Recording Filename_ from its start with the replay avatar. Pressing _Left Shift + Replay Sequence Key_ will pause and resume the replay. To create a different avatar to follow the recording, please follow the [instructions below](#how-to-create-another-pair-of-hands-for-replaying-an-interaction-sequence). 
<!--In the video below, the green button triggers this replay.-->

<!--{% include youtube.html id="o5F5tUb8RQM" caption="Record Replay 1." %}-->

### Full and object-specific interaction replay

If you assign a _Replay Object_, the {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %} will be replayed fully, but in the frame of the provided _Replay Object_. Also all the other objects that your hands have interacted with in the sequence will also be moved into the frame of the provided _Replay Object_. This means that it is assured that the particular object - even after positional changes - will be interacted with as recorded. 

This option is very handy when you want to record and replay for example an assembling task where interactions with multiple objects are involved. And when you replay it you don't want to be restricted by having to place the objects at exact locations when recorded. 

### Partial and object-specific interaction replay

The third replay mode is to replay an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %}. After you have recorded a full {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can replay a specific part of it - an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} (specified by the _Segment ID_) - with a specified hand (_Side_) and object (_Replay Object_). 
See [sensor record and replay](sensor_record_replay.1.0.0.html#background) to understand interaction segments.

In the VG_Recoder, pressing the _Replay Segment Key_ will replay a specific 
{% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} of the recording provided in _Recording Filename_ with the replay avatar. 
Holding the _Left Shift button_ while pressing the _Replay Segment Key_ allows pause and resume of the replay. In the movie above, the blue button triggers this replay.

{% include warning.html content="The current implementation is still not very user-friendly as you have to
know which interaction combinations (of the “Replay Object” to play on, the avatar, the hand side, and the segment ID) are valid. You will get a list of available interaction segments in the console though that may help you out." %}

This option is handy when you want to record the entire training sequence that involved multiple steps consisting of interaction with multiple objects, and later you just want to extract some individual {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} to insert into a training authoring system as one step. 

{% include callout.html content="Note that since this partial replay option can only play interaction on one object by one hand, so when you want to replay two-hands interactions on one object at the same time, or two-hands interactions with multiple objects, you should choose the full replay options earlier. " %}

## How to Query Start Pose of Hands

You can use [GetReplayStartWristPose](virtualgrasp_unityapi.1.0.0.html#vg_controllergetreplaystartwristpose) to query the start pose of the wrists of the _replay avatar_ when replay is on [full and scene-specific interaction](#full-and-scene-specific-interaction-replay) or [full and object-specific interaction](#full-and-object-specific-interaction-replay). Note this does not work when replaying [partial and object-specific interaction](#partial-and-object-specific-interaction-replay).

As shown in the VG_Recorder GUI, _Set Hand Start Pose Key_ "S" demonstrate how this is done in the script:
```js
// Code in VG_Recorder.cs
// To use GetReplayStartWristPose, need to first load recording and make sure avatar is enabled for replay.
VG_Controller.LoadRecording(m_recordingFilename);
// If m_replayObject is null will be full scene-specific replay, otherwise full object-specific replay.
int replayingAvatarInstanceID = GetReplayAvatar();
VG_Controller.GetReplayStartWristPose(replayingAvatarInstanceID, m_replayObject, out Vector3 p_left, out Quaternion q_left, out Vector3 p_right, out Quaternion q_right);
````

{% include callout.html content="Note that querying the start pose of hands does not affect later replaying the interaction sequence." %}

## How to Create another Pair of Hands for Replaying an Interaction Sequence

If you replay the whole {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %} of {% include tooltip.html tooltip="SensorData" text="sensor data" %} without any changes, the controlled VR hands will be disembodied, which is what you potentially do not want. 

In order to instantiate another pair of hands to be controlled by the replay, 
* add another avatar with hands into the scene (such as by duplicating the avatar you already have), 
* add another element to VG_MainScript→Avatars, drag the SkinnedMeshRenderer from scene to _SkeletalMesh_ field and check it as _Replay_ avatar (see below), 
* also assign the SkinnedMeshRenderer to the _Replaying avatar_  slot of the VG_Recorder (meaning that you want to replay the recordings on this avatar).

{% include image.html file="unity/unity_vg_myvirtualgrasp_1_0_0.png" alt="In MyVirtualGrasp: Setup for another avatar to replay recorded data." caption="In MyVirtualGrasp: Setup for another avatar to replay recorded data." %}

<!--
## Videos

{% include youtube.html id="7aRCZThEHOE" caption="Record Replay 2" %}
-->

## Sensor Recording for a built Android app

All recordings performed by the user while in Editor mode are stored under "StreamingAssets/VG_Recordings" followed by the user selected filename (optionally combined with some parent folders). During the phase of building the application for Android all recordings are copied and stored inside the zipped apk file. After installation of the application to an Android device and while initialization, all recordings will be copied over to Android persistent data folder for quick access. 
    
**Recording directly from the Android application is allowed but user should pay attention:**
    
* If the recording provided by the user for the new recording matches one that already exists it will temporarily replace it, until the next initialization of the application when the shipped recording will be restored. 
* Application reinstallation/update/data cleaning may likely lead to lose of the previously recorded data from Android.
* App sharing could also introduce some problems with the recording on Android.
    

{% include tip.html content="In order for the user to overcome these problems, an option is to keep all the recordings performed on Android into a desired cloud storage (e.g., AWS S3 bucket). So everytime a recording is performed it should be uploaded to the desired remote target destination using the corresponding API functions of the cloud service. User should also download all the Android recordings after VG has initialized. " %}

