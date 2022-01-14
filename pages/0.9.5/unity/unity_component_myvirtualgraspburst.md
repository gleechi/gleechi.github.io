---
title: MyVirtualGraspBurst Component
#tags: [getting_started]
keywords: component, main, myvirtualgrasp, burst
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_9_5
permalink: unity_component_myvirtualgraspburst.0.9.5.html
folder: mydoc
---

## Description

MyVirtualGrasp is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} inherited from VG_MainScript, which encodes the main functionality of VirtualGrasp.

In contrast to [MyVirtualGrasp](unity_component_myvirtualgrasp.0.9.5.html), this component uses Burst Jobs to isolate VG updates on seperate threads.

<!--{% include note.html content="The use of Burst is experimental and has not shown much of performance improvement in tested applications." %}-->

## Burst Configuration

The only additional element to to the standard GUI elements is the "Burst Parameters" section.

{% include image.html file="unity/unity_vg_myvirtualgraspburst.png" alt="VG_MyVirtualGraspBurst Settings." caption="\"Save Debug Files\" must be enabled Debug Settings to prepare the files." %}

As you can see in the MyVirtualGraspBurst.cs script, you can control the behavior by selecting your number of threads as follows:

* If the number of threads is 0, VirtualGrasp will run on the MainThread. That means the behavior is exactly equal to MyVirtualGrasp.cs.
* If the number of threads is 1, VirtualGrasp will spawn a SingleWorkerThread with Burst. You need to have Burst installed and the define enabled in MyVirtualGraspBurst.cs.
* If the number of threads is N>1, VirtualGrasp will spawn N MultipleWorkerThreads with Burst. You need to have Burst installed and the define enabled in MyVirtualGraspBurst.cs.

{% include note.html content="Since VG itself is not multi-threaded itself, using N MultipleWorkerThreads does not make much sense. You should only use 1 SingleWorkerThread to test with Burst, or 0 for comparison to test without Burst." %}

## Burst Communication with VG

VirtualGrasp works in mainly three steps: 

1. send incoming data from Unity to VirtualGrasp,
2. compute the hand and object animations in VirtualGrasp,
3. send outgoing data from VirtualGrasp back to Unity and reflect it there. 

Therefore, the API offers isolated functions specifically for multi-threading for those three steps:

1. [IsolatedUpdateDataIn](virtualgrasp_unityapi.0.9.5.html#isolatedupdatedatain)
2. [IsolatedUpdate](virtualgrasp_unityapi.0.9.5.html#isolatedupdate)
3. [IsolatedUpdateDataOut](virtualgrasp_unityapi.0.9.5.html#isolatedupdatedataout)

While 1. and 3. are merely data transfer tasks, 2. is the "heavy" lifting and the main blocker on Unity's main thread.

In MyVirtualGraspBurst.cs 1. and 3. are therefore called in the FixedUpdate() loop, while 2. is placed on a separate thread.
