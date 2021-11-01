---
title: VG_HandVisualizer Component
#tags: [getting_started]
keywords: component, HandVisualizer
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vghandvisualizer.html
folder: mydoc
---

VG_HandVisualizer is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGScript}}">VG script</a> that provides a tool to visualize the hand bones in Unity. 
The MonoBehavior script examplifies how to use the VG API functions for accessing specific bones / elements of the hands

{% include image.html file="unity/unity_vg_hand_visualizer.png" alt="VG HandVisualizer" caption="VG_HandVisualizer Component." %}

@kai please add a video here.

<!--{% include youtube.html id="FX4HQCO_hd8" %}-->

### How to Use
 
When you want to enable visualizing the hand, it is recommended to add this component on the same GameObject where your MyVirtualGrasp script is.

{% include callout.html content="You should not add this component to individual objects because this is a global setting that is not linked to specific objects." %}
