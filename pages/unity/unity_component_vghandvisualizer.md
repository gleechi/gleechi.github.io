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

VG_HandVisualizer is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.CoreScript}}">Core Script</a>.
It provides a tool to visualize the hand bones in Unity. 
The MonoBehavior provides a tutorial on the VG API functions for accessing specific bones / elements of the hands

<iframe width="560" height="315" src="https://www.youtube.com/embed/FX4HQCO_hd8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The Component

{% include image.html file="unity/unity_vg_hand_visualizer.png" alt="VG HintVisualizer" caption="MyVirtualGrasp script - VG_HintVisualizer Component." %}

Is the ID of the avatar whose hands you want to visualize. 


### How to Use

When you want to enable visualizing the hand, it is recommended to add this component on the same GameObject where your MyVirtualGrasp script is.

{% include important.html content="You should not add this component to individual objects because this is a global setting that is not linked to specific objects." %}
