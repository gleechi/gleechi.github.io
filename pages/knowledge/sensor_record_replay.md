---
title: Sensor Record and Replay
sidebar: main_sidebar
keywords: interaction_sequence, sensor_record, sensor_replay, record, replay
permalink: sensor_record_replay.html
folder: knowledge
toc: true
---

### Background

One very useful feature of VirtualGrasp is the ability to pre-record 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>(s),
and later replay the whole sequences or individual ones on specific objects. 
This is enabled by the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">Sensor Record and Replay</a>
functionality of VirtualGrasp. 

With this functionality, you can start the recording at any moment in runtime interaction inside a VR application . 
The sensor recorder will record <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">Sensor Data</a>
frame by frame, and also automatically segment the frames into segments (we call <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>)
 according to which object the hand is interacting with. 
 
        SensorDB has 2 hand interaction(s):
         humanoid_handLeft1 has 10 sequence(s):
           interaction #0  has 462/462 frames/states
           interaction #1  has 934/934 frames/states, on object baseball
           interaction #2  has 169/169 frames/states
           interaction #3  has 568/568 frames/states, on object apple
           interaction #4  has 178/178 frames/states
           interaction #5  has 631/631 frames/states, on object baseball
           interaction #6  has 152/152 frames/states
           interaction #7  has 593/593 frames/states, on object pear
           interaction #8  has 40/40 frames/states
           interaction #9  has 358/358 frames/states, on object screwdriver
         humanoid_handRight1 has 1 sequence(s):
           interaction #0  has 4085/4085 frames/states
		   
Above code block shows a display of one recording on an avatar with a pair of left and right humanoid hands. 
You can see in this recording:
* the left hand sensor data has been segmented (automatically during recording) into 10 <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionSequence}}">Interaction Sequence</a>s, 
with incremental ids starting from #0.  
* sequence #0 has 462 frames while hand was not interacting with any object (hence not information of on which object),
* sequence #1 has 934 frames while hand was interacting with object baseball,
* sequence #2 starts when hand stopped interaction with baseball, and back to a state without interacting with any object,
* sequence #3 starts when hand started to interact with another object apple, and so on ... 
* however for the right hand, during the entire time of sensor recording (4085 frames), was not interacting with any object, therefore no segmented sequences.

### Why Segmenting into Interaction Sequences?

The reason we segment the sensor data into different interaction sequences by objects is because we can later replay the sensor data 
* either on the entire recording, 
* or play just one particular sequence on a particular object. 

Each option has its use cases. 
For example once you record all the steps to go through a training task, 
* if you want to show the entire steps you can fully replay all sequences;
* you can however also replay a specific interaction with any specific object to show a single step in training.

In latter case such a interaction sequence can be picked out to suppliment a training authoring system such as Gleechi's step manager.

### What is Recorded Exactly?

What is recorded is <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorData}}">Sensor Data</a> -- wrist position, orientation and grasp trigger signals.
In other words, what we record is user provided control signals on hands -- where a user places hand, and when a user want to grasp and interact with an object -- 
 through hand sensors, whether it is hand-held VR controllers (like Oculus Touch) or 
full hand tracking devices like LeapMotion or Oculus hand tracking system.
And what we DO NOT record is the "result" of these control signals, namely, when and how hand formed the 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">Grasp Configuration</a>.

As a result, for example, if you recorded a set of sensor data on a particular scene with a set of objects placed at specific locations,
and later you play this sensor data on a different scene with either same set of objects placed at different places, or with different
set of objects, the resulting interaction will NOT be the same. 




To learn more details on how to use <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SensorRecordAndReplay}}">Sensor Record and Replay</a> 
in Unity please see [VG_Recorder](unity_component_vgrecorder.html#unity-component-vgrecorder).

