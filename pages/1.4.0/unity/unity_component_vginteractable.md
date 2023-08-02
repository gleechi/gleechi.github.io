---
title: VG_Interactable Component
#tags: [getting_started]
keywords: component, interactable
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_4_0
permalink: unity_component_vginteractable.1.4.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_interactable_0_15_0.png" alt="VG interactable." caption="VG_Interactable" %}

## Description

The VG_Interactable component allows you to specify object specific {% include tooltip.html tooltip="InteractionType" text="interaction type" %}, and two throw velocity scales. All parameters in the VG_Interactable component are explained in [grasp interaction](grasp_interaction.1.4.0.html).

 {% include callout.html content= "Interaction Type, Throw Velocity Scale and Throw Angular Velocity Scale can be set globally in MyVirtualGrasp script [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings). This VG_Interactable local settings will overwrite the global settings for that object. I.e. all objects without a customized VG_Interactable will follow the global settings, but those with VG_Interactable will follow the local settings." %} 


{% include multiple_script.html %}



