---
title: VG_Locomotion Component
#tags: [getting_started]
keywords: component, locomotion
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_3
permalink: unity_component_vglocomotion.1.6.3.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_locomotion.png" alt="VG Locomotion" caption="VG_Locomotion Component." %}

## Description

VG_Locomotion does not depend on VirtualGrasp library. It is provided as a simple Monobehavior to give a convenience tool for locomotion. 

The locomotion supported is of smooth movement with input from 

* Joystick control
* Keyboard control (Q-W-E-A-S-D)

{% include singleton_script.html %}

All the sensor and replay avatar setup prefabs in  _Runtime/Resources/Prefabs/_ include this component to support the smooth locomotion. 
