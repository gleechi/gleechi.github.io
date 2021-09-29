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

The VG_HintVisualizer component can be used to visualize in Unity the hints for pushable object selection (see Push without Physics in [Push Interaction](push_interaction.html#push-interaction))
and for graspable object selection (see [Grasp Interaction](grasp_interaction.html#grasp-interaction)). 

### Push Hints

If push hints is enabled, for any objects that are setup for push without physics, there will be a push hint drawn on the surface of the selected object in Unity. 

By default the push hint takes the shape of a circle, and its size will increase as the finger tip is closer to the object, and decrease as it moves far away.
And when finger tip is too far from the object, or if the approach direction deviates too much from the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.PushPivot}}">Push Pivot</a>.

### Grasp Hints

If grasp hints is enabled, the grasp selection sphere attached to the hand will show up, and when an object is selected, this sphere will change color.

