---
title: VG_HintVisualizer Component
#tags: [getting_started]
keywords: component, HintVisualizer
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vghintvisualizer.html
folder: mydoc
---

VG_HintVisualizer is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGPublicScript}}">public script</a>.
It can be used as a Unity component to visualize some hints such as a selection sphere to debug graspable object selection or a push sphere to guide pushing interactions. The MonoBehavior provides a tutorial on the VG API functions for accessing the push state ([GetPushCircle](virtualgrasp_unityapi.html#getpushcircle)).

{% include image.html file="unity/unity_vg_hint_visualizer.png" alt="VG HintVisualizer" caption="VG_HintVisualizer Component." %}

### Push Hints

If push hints is enabled, for any objects that are setup for push without physics, there will be a push hint drawn on the surface of the selected object in Unity. 

{% include youtube.html id="FX4HQCO_hd8" %}

By default the push hint takes the shape of a circle (see video above), and its size will increase as the finger tip is closer to the object, and decrease as it moves far away.
And when finger tip is too far from the object, or 
if the approach direction deviates too much from the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">push pivot</a>,
this circle will disappear indicating the object is no longer selected for push.

See [push without physics](push_interaction.html#push-without-physics) to learn about the process of pushable object selection.

### Grasp Hints

If grasp hints is enabled, the graspable object selection sphere attached to the hand will show up, and when an object is selected, this sphere will change color.

See [from object selection to grasp synthesis](grasp_interaction.html#from-object-selection-to-grasp-synthesis) to learn about the process of graspable object selection.

### How to Use

When you want to enable either push or grasp hints, it is recommended to add this component on the same GameObject where your MyVirtualGrasp script is.

{% include callout.html content="You should not add this component to individual objects because this is a global setting that is not linked to specific objects." %}
