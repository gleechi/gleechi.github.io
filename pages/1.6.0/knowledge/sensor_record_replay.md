---
title: Sensor Record and Replay
sidebar: main_sidebar_1_6_0
keywords: interaction_sequence, interaction_segment, sensor_record, sensor_replay, record, replay
permalink: sensor_record_replay.1.6.0.html
folder: knowledge
toc: true
---

### Background

One feature of VirtualGrasp (Pro version) is the ability to pre-record a
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">interaction sequence</a>,
and later replay the whole sequence or individual <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segment</a> on specific objects. 
This is enabled by the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">sensor record and replay</a>
functionality of VirtualGrasp. 

With this functionality, you can start the recording at any moment in runtime interaction inside a VR application . 
The sensor recorder will record the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">sensor data</a>
frame by frame, and also automatically segment the frames into segments (we call <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segment</a>)
 according to which object the hand is interacting with. 
 
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
		   
Above code block shows a display of one recording on an avatar with a pair of left and right humanoid hands. 
You can see in this recording:
* the left hand sensor data has been segmented (automatically during recording) into 10 <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segment</a>, 
with incremental ids starting from #0.  
* segment #0 has 462 frames while hand was not interacting with any object (hence no information of on which object),
* segment #1 has 934 frames while hand was interacting with baseball,
* segment #2 starts when hand stopped interaction with baseball, and back to a state without interacting with any object,
* segment #3 starts when hand started to interact with another object apple, and so on ... 
* however for the right hand, during the entire time of sensor recording (4085 frames), was not interacting with any object, therefore no separated segments.

### Why Segmenting into Interaction Segments?

The reason we segment the sensor data into different <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segments</a> by objects is because we can later replay the sensor data 
* either on the entire recording sequence, 
* or play just one particular interaction segment on a particular object. 

Each option has its use cases. 
For example once you record all the steps to go through a training task, 
* if you want to show the entire steps you can fully replay the whole sequence;
* you can however also replay a specific <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segment</a> on a specific object to show a single step in training.

Either the entire <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">interaction sequence</a> or one specific <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSegment}}">interaction segment</a> can used to suppliment a training authoring system such as Gleechi's step manager.

### What is Recorded Exactly?

What is recorded is the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">sensor data</a> -- wrist position, orientation and grasp trigger signals.
In other words, what we record is user provided control signals on hands -- where a user places hand, and when a user want to grasp and interact with an object. 
And what we DO NOT record is the "result" of these control signals, namely, when a hand grasped an object, which object is grasped, and when and how a hand formed the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configuration</a>.

Therefore, if you want to achieve same interaction behaviors of the avatar during recording, replaying setup need to guarrantee to
1. use the same avatar (mainly same pair of hands skeleton mesh) as the recording, and
2. use the same scene (same set of objects at same locations) as the recording.

To learn more details on how to use <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">sensor record and replay</a> 
in Unity please see [VG_Recorder](unity_component_vgrecorder.1.6.0.html).

