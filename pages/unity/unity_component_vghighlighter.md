---
title: VG_HighLighter Component
#tags: [getting_started]
keywords: component, HighLighter
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vghighlighter.html
folder: mydoc
---

VG_HighLighter is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGPublicScript}}">public script</a>.
The MonoBehavior script exemplifies how you could enable object highlighting based on the current hand status; 
and provides a tutorial on the VG API functions for some of the VG_Controller event functions, 
such as OnObjectSelected and OnObjectDeselected.

{% include image.html file="unity/unity_vg_highlighter.png" alt="VG HighLighter" caption="VG_HighLighter Component." %}

@kai please add a video to here.

<!--{% include youtube.html id="FX4HQCO_hd8" %}-->

### How to Use

When you want to enable highlighting, it is recommended to add this component on the same GameObject where your MyVirtualGrasp script is.

{% include callout.html content="You should not add this component to individual objects because this is a global setting that is not linked to specific objects." %}
