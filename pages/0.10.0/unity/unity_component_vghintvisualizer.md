---
title: VG_HintVisualizer Component
#tags: [getting_started]
keywords: component, HintVisualizer
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_10_0
permalink: unity_component_vghintvisualizer.0.10.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_hint_visualizer.png" alt="VG HintVisualizer" caption="VG_HintVisualizer Component." %}

## Description

VG_HintVisualizer is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %}.
It can be used as a Unity component to visualize some hints such as a selection sphere to debug graspable object selection or a push sphere to guide pushing interactions.

The MonoBehavior provides a tutorial on the VG API functions for accessing the push state ([GetPushCircle](virtualgrasp_unityapi.0.10.0.html#getpushcircle)).

{% include singleton_script.html %}

## Push Hints

If push hints are enabled, a circle will be visualized on the surface of the selected object if that object is setup for push without physics. 

The circle's size will increase as the finger tip is closer to the object, and decrease as it moves farther away.

When the finger tip is too far from the object, or if the approach direction deviates too much from the {% include tooltip.html tooltip="PushPivot" text="push pivot" %}, this circle will disappear indicating the object is no longer selected for pushing.

See [push without physics](push_interaction.0.10.0.html#push-without-physics) to learn about the process of pushable object selection.

{% include youtube.html id="FX4HQCO_hd8" caption="If Push Hints are enabled, a circle will show up on the pushable object." %}

## Grasp Hints

If grasp hints are enabled, an object selection sphere will be visualized for each hand. When no object is selected, the sphere will be red; when an object is selected, the sphere will change color to green.

See [from object selection to grasp synthesis](grasp_interaction.0.10.0.html#from-object-selection-to-grasp-synthesis) to learn about the process of graspable object selection.


<!-- {% include image.html file="gifs/hintvisualizer.gif" width="100%" alt="VG_HintVisualizer" caption="Selection hint spheres for each hand will change color based on selection." %}  -->

{% include youtube.html id="Xi1Ew04_qMs" caption="Selection hint spheres for each hand will change color based on selection." %}
 
