---
title: VG_Interactable Component
#tags: [getting_started]
keywords: component, interactable
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vginteractable.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_interactable.png" alt="VG interactable." caption="VG_Interactable" %}

{% include callout.html content="All parameters in the VG_Interactable component is explained in 
[grasp interaction](grasp_interaction.html#grasp-interaction)." %}

VG_Interactable component allows you to specify different <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">synthesis method</a> and <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">interaction type</a> for each object by attaching this component to the corresponding game object. 
This will override the global settings for [grasp Interaction](grasp_interaction.html#grasp-interaction) assigned on all objects in the scene (see [global grasp interaction settings](unity_component_myvirtualgrasp.html#grasp-interaction-settings)). 

Adding this component to an object also specifies this object to be <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGInteractable}}">interactable</a> (see [object identifiers](unity_get_started_objects.html#customizing-layers-and-component-names)).
 
{% include tip.html content="All objects without a customized VG_Interactable will follow the global settings,
 but those with VG_Interactable will follow these local settings." %}



