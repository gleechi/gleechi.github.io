---
title: VG_Interactable Component
#tags: [getting_started]
keywords: component, interactable
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_vginteractable.html
folder: mydoc
---

To use the VG_Interactable component, you should first understand the meaning of VirtualGrasp's  
[grasp Interaction](grasp_interaction.html#grasp-interaction).


### Global Settings

You can set the default [grasp Interaction](grasp_interaction.html#grasp-interaction) settings for all objects in the scene through:

{% include image.html file="unity/unity_vg_settings.png" alt="VG Settings." caption="VG_Settings" %}

{% include important.html content="We will soon move grasp interaction related parameters out from Sensor setting GUI to have an independent GUI maybe with a name Global Interactables" %}

### Local Settings

If you want some selected objects to have <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Grasp Synthesis</a> method and 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">Interaction Type</a> different from the global settings, 
you can add a VG_Interactable component to the object and set interaction type and synthesis method just for this object.


{% include image.html file="unity/unity_vg_interactable.png" alt="VG interactable." caption="VG_Interactable" %}

{% include tip.html content="All objects without a customized VG_Interactable will follow the global settings (see above), but those with VG_Interactable will follow their local settings." %}