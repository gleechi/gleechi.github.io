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


{% include important.html content="To use the VG_Recorder component, you should first learn about VirtualGrasp's  [Sensor Record and Replay](sensor_record_replay.html#sensor-record-replay)." %}


### Use cases

An example use case is “replaying entire instruction sequences”.

Another example use case is “replaying a specific object interaction for instruction”.

Another example use case is “quick testing of a whole interaction sequences”.

{% include youtube.html id="o5F5tUb8RQM" caption="Record Replay 1." %}

{% include youtube.html id="7aRCZThEHOE" caption="Record Replay 2" %}


### How to Record Sensor Data

The VirtualGrasp library (VG_Controller) has a couple of [API functions](VirtualGrasp_UnityAPI.html#setprocessbyrecordedframe) for recording and replaying 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">Sensor Data</a>. 
For convenience, the plugin includes a VG_Recorder script that you can use to access the major functionalities of the sensor recording.

{% include image.html file="unity/unity_vg_recorder.png" alt="VG Recorder" caption="VG_Recorder Component." %}

In the current VG_Recorder, pressing R (KeyCode.R) will toggle between starting recording and stopping recording. 
When you stop recording, a file with the recorded data will be written, named after the filename you provided in the “Recording Filename”. 
Note that in the current implementation of VG_Recorder, the recording will be attached to the same file, so if you want to separate and keep multiple recordings, 
you have to rename them yourself.

So to record, just press the R key once, do some interactions in your scene, and press R another time.In order to allow you to have this interaction from the VR headset,
 it has also been implemented that you can start a recording with the "B" button of the right VR controller, and replay it with the "A" button.

### How to Create another Pair of Hands for Replay

If you replay the whole sequences of <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">Sensor Data</a>
 without any changes, your own VR hands will be disembodied, which is what you potentially do not want. 
 In order to instantiate just another pair of hands to be controlled by a replay, do the following steps:

<!-- {% include image.html file="unity/unity_vg_recorder.png" alt="VG Recorder" caption="VG_Recorder Component." %} -->

In VG_SensorConfiguration→SensorSetup→HandIDs where you should already have one element, add another HandID with the same index. 
This will instantiate a copy of the hands when VirtualGrasp initializes.

In order to specify the hand that should be controlled by replay, set “Use Replay” to 1 (which is the index of the hand in HandIDs that should be reserved for replay).

When now restarting the scene, you should find two pairs of hands in the scene.

### How to Replay an Interaction Sequence

#### Full and scene-specific interaction replay
A whole recorded sensor data (usually contain multiple <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequences</a>)
 will be replayed, for example you once record all the steps to go through a training sequence, and you can fully replay it later. 
However, when you change positions of objects that you interacted with, the replay hand will grasp empty air. 

In the movie above, the green button triggers this replay.

In the current VG_Recorder, pressing T will replay the recording provided in “Recording Filename” with the pair of replay hands. 
If using VR controllers, clicking the left controller's touchpad has the same effect.

#### Partial and object-specific interaction replay
A specific <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>
 on an object can be replayed, for example you once record all the steps to go through a training, 
and you can then replay a specific <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>
(identified by the interaction id) with a specific object. 

In the movie above, the blue button triggers this replay.

In the current VG_Recorder, pressing Y will replay a specific 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>
of the recording provided in “Recording Filename” with the pair of replay hands. The current implementation is still not very user-friendly as you have to
know which interaction combinations (of the “Replay Object” to play on, the avatar, the hand side, and the interaction ID) are valid. 
You will get a list of available interactions in the console though that may help you out.
 
{% include tip.html content="See [Sensor Record and Replay](sensor_record_replay.html#background) to understand segmented interaction sequences and interaction id." %}

If using VR controllers, clicking the left touchpad in its center has the same effect. However, if you click the touchpad on the right side, 
VG_Recorder will increase the interaction ID until it finds a valid one. Clicking on the left side will decrease the interaction ID until it finds a valid one.

{% include important.html content="Note that right now the partial and object-specific replay is replaying the sequence with the same object name. 
Since objects with same name could possibly have different mesh (size and shape), this is not entirely correct. We are going to fix this in next release." %}


### Important Note on the Files

In order to support recording and replaying <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">Sensor Data</a>
 and re-using that information, there will be recording files in each project 
(dependent on how you name them, but default in VG_Recorder for now is for example recording.sdb).

That means that when you record inside a game engine, and want to use the recordings in a build, you have to manually copy these files to the build directory.

Also, if you you are using a project repository and want to share the annotated data, you have to commit these files to the repository to do so.