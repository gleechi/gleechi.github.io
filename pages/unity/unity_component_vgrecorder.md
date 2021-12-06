---
title: VG_Recorder Component
#tags: [getting_started]
keywords: component, recorder, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vgrecorder.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_recorder.png" alt="VG Recorder" caption="VG_Recorder Component." %}

## Description

The VirtualGrasp library (VG_Controller) has a couple of [API functions](VirtualGrasp_UnityAPI.html#setprocessbyrecordedframe) 
for recording and replaying {% include tooltip.html tooltip="SensorData" text="sensor data" %}. For convenience, the SDK includes a VG_Recorder {% include tooltip.html tooltip="VGPublicScript" text="public script" %} as a customizable component. 

You can use it to access the major functionalities which are explained in [sensor record and replay](sensor_record_replay.html#sensor-record-replay).

Some example use cases are:
* “replaying entire instruction sequence”.
* “replaying a specific object interaction for instruction”.
* “quick testing of a whole interaction sequence”.

{% include singleton_script.html %}

## How to Record Sensor Data

Pressing the _Recording Key_ during play will toggle between starting and stopping the recording of an interaction sequence.
After a recording is finished, a file with the recorded data will be written, named after the provided _Recording Filename_. 
In the current implementation of VG_Recorder, the recording will be **attached** to the same file, so if you want to separate and keep multiple recordings, 
you have to rename them.

In order to record an interaction sequence:
* press the _Recording Key_ key once, 
* do some interactions in your scene, 
* press the _Recording Key_ another time.

### Important Note on the Files

In order to support recording and replaying {% include tooltip.html tooltip="SensorData" text="sensor data" %} and re-using that information, there will be recording files in each project.

That means that when you record inside your Unity project, and want to use the recordings in a build, you have to manually copy these files to the build directory.

## How to Replay an Interaction Sequence

### Full and scene-specific interaction replay

After you have recorded an {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can fully replay it later. The _Replay Object_ has to be empty (None) for this mode. In this replay mode, the hand movements will be replayed exactly as they were recorded. That means that as soon as you change positions of objects that you did interact with, the replaying hand will grasp empty air. 

This option is very handy when you want to record and replay for example an assembling task where interactions with multiple objects are involved. However you need to guaranttee while replaying all objects are at the same location as when they are recorded.

Pressing the _Replay Sequence Key_ will replay the recording provided in _Recording Filename_ with the avatar provided in _Avatar ID_. To create a different avatar to follow the recording, please follow the [instructions below](#how-to-create-another-pair-of-hands-for-replaying-an-interaction-sequence). In the video below, the green button triggers this replay.

{% include youtube.html id="o5F5tUb8RQM" caption="Record Replay 1." %}

### Full and object-specific interaction replay

If you assign a _Replay Object_, the {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %} will be replayed fully, but in the frame of the provided _Replay Object_. Also all the other objects that your hands have interacted with in the sequence will also be moved into the frame of the provided _Replay Object_. This means that it is assured that the particular object - even after positional changes - will be interacted with as recorded. 

This option is very handy when you want to record and replay for example an assembling task where interactions with multiple objects are involved. And when you replay it you don't want to be restricted by having to place the objects at exact locations when recorded. 

### Partial and object-specific interaction replay

The third replay mode is to replay an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %}. After you have recorded a full {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %}, you can replay a specific part of it - an {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} (specified by the _Segment ID_) - with a specified hand (_Side_) and object (_Replay Object_). 
See [sensor record and replay](sensor_record_replay.html#background) to understand interaction segments.

In the VG_Recoder, pressing the _Replay Segment Key_ will replay a specific 
{% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} of the recording provided in _Recording Filename_ with the replay avatar. In the movie above, the blue button triggers this replay.

{% include warning.html content="The current implementation is still not very user-friendly as you have to
know which interaction combinations (of the “Replay Object” to play on, the avatar, the hand side, and the segment ID) are valid. You will get a list of available interaction segments in the console though that may help you out." %}

This option is handy when you want to record the entire training sequence that involved multiple steps consisting of interaction with multiple objects, and later you just want to extract some individual {% include tooltip.html tooltip="InteractionSegment" text="interaction segment" %} to insert into a training authoring system as one step. 

{% include callout.html content="Note that since this partial replay option can only play interaction on one object by one hand, so when you want to replay two-hands interactions on one object at the same time, or two-hands interactions with multiple objects, you should choose the full replay options earlier. " %}

## How to Query Start Pose of Hand 

You can use [GetReplayStartWristPose](virtualgrasp_unityapi.html#getreplaystartwristpose) to query the start pose of the wrists of the _replay avatar_ when replay is on [full and scene-specific interaction](#full-and-scene-specific-interaction-replay) or [full and object-specific interaction](#full-and-object-specific-interaction-replay). Note this does not work when replay [partial and object-specific interaction](#partial-and-object-specific-interaction-replay).

As shown in the VG_Recorder GUI, _Set Hand Start Pose Key_ S demonstrate how this is done in the script. 

```js
// To use GetReplayStartWristPose, need to first load recording and make sure avatar is enabled for replay.
VG_Controller.LoadRecording(m_recordingFilename);
VG_Controller.SetProcessByRecordedFrame(m_replayingAvatarID, true);
// If m_replayObject is null will be full and scene-specific interaction replay, otherwise object-specific.
VG_Controller.GetReplayStartWristPose(m_replayingAvatarID, m_replayObject, out Vector3 p_left, out Quaternion q_left, out Vector3 p_right, out Quaternion q_right);
````

{% include callout.html content="Note that querying the start pose of hands does not affect later replaying the interaction sequence." %}

## How to Create another Pair of Hands for Replaying an Interaction Sequence

If you replay the whole {% include tooltip.html tooltip="InteractionSequence" text="interaction sequence" %} of {% include tooltip.html tooltip="SensorData" text="sensor data" %} without any changes, the controlled VR hands will be disembodied, which is what you potentially do not want. 

In order to instantiate another pair of hands to be controlled by the replay, 
* add another hand model into the scene (such as by duplicating the hand model you already have), 
* add another element to VG_MainScript→Sensors→Avatars (see below), 
* assign the SkinnedMeshRenderer of your duplicated hand model to the Hand Model slot of the newly added element, and finally 
* change the _AvatarID_ in the VG_Recorder to 2 (meaning that you want to replay the recordings on the second avatar).

{% include image.html file="unity/unity_vg_recorder_avatars.png" alt="VG Recorder Hands" caption="In MyVirtualGrasp: Setup for another avatar to replay recorded data." %}

<!--
## Videos

{% include youtube.html id="7aRCZThEHOE" caption="Record Replay 2" %}
-->

