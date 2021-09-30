---
title: VG_HintVisualizer Component
#tags: [getting_started]
keywords: component, HintVisualizer
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_vghintvisualizer.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_hint_visualizer.png" alt="VG HintVisualizer" caption="MyVirtualGrasp script - VG_HintVisualizer Component." %}

The VG_HintVisualizer component can be used to visualize in Unity the hints for pushable object selection 
and for graspable object selection . 

### Push Hints

If push hints is enabled, for any objects that are setup for push without physics, there will be a push hint drawn on the surface of the selected object in Unity. 

By default the push hint takes the shape of a circle, and its size will increase as the finger tip is closer to the object, and decrease as it moves far away.
And when finger tip is too far from the object, or 
if the approach direction deviates too much from the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>,
this circle will disappear indicating the object is no longer selected for push.

See Push without Physics section in [Push Interaction](push_interaction.html#push-interaction) to learn about the process of pushable object selection.

### Grasp Hints

If grasp hints is enabled, the grasp selection sphere attached to the hand will show up, and when an object is selected, this sphere will change color.

See [Grasp Interaction](grasp_interaction.html#grasp-interaction) to learn about the process of graspable object selection.

### How to Use

When you want to enable either push or grasp hints, it is recommended to add this component on the same GameObject where your MyVirtualGrasp script is.

{% include important.html content="You should not add this component to individual objects because this is a global setting that is not linked to specific objects." %}
