---
title: VG_Interactable Component
#tags: [getting_started]
keywords: component, interactable
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_12_0
permalink: unity_component_vginteractable.0.12.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_interactable.png" alt="VG interactable." caption="VG_Interactable" %}

## Description

The VG_Interactable component allows you to specify object specific {% include tooltip.html tooltip="GraspSynthesisMethod" text="synthesis method" %}, {% include tooltip.html tooltip="InteractionType" text="interaction type" %}, and two throw velocity scales. 

All parameters in the VG_Interactable component are explained in [grasp interaction](grasp_interaction.0.12.0.html#grasp-interaction).

Adding VG_Interactable to an object will override the [global grasp interaction settings](unity_component_myvirtualgrasp.0.12.0.html#global-grasp-interaction-settings) for that particular object. 

All objects without a customized VG_Interactable will follow the global settings, but those with VG_Interactable will follow the local settings.

{% include multiple_script.html %}



