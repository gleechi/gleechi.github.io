---
title: VG_HighLighter Component
#tags: [getting_started]
keywords: component, HighLighter
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_12_0
permalink: unity_component_vghighlighter.0.12.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_highlighter.png" alt="VG HighLighter" caption="VG_HighLighter Component." %}

## Description

VG_HighLighter is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %}.
The MonoBehavior script exemplifies how you could enable object highlighting based on the current hand status; 
and provides a tutorial on the VG API functions for some of the VG_Controller event functions, 
such as [OnObjectSelected](virtualgrasp_unityapi.0.12.0.html#onobjectselected) and [OnObjectDeselected](virtualgrasp_unityapi.0.12.0.html#onobjectdeselected).

{% include singleton_script.html %}

<!--{% include youtube.html id="FX4HQCO_hd8" %}-->

## Selection Highlighting

When the component is in the scene, selecting an object will highlight the selected object using the assigned Unity *Shader*.

When selecting the object with a left hand, the *Left Hand Color* will be used, and when selecting the object with a right hand, the *Right Hand Color* will be used.

{% include youtube.html id="4D4bbfif2YI" caption="Selection Highlighting when selecting objects with both hands." %}

## Bake Highlighting

When playing the scene in the Unity Editor, you can also use the Highlighter to visualize the object baking state of the objects in your scene. 
Please read more on [object baking](object_baking.0.12.0.html) if you are not familiar with the terminology.

There are three options you can enable by clicking on the respective buttons:

* **No Bakes:** Highlight all objects that are not baked in red. You will only get [Sticky Hand](grasp_interaction.0.12.0.html#grasp-interaction-type) grasps on those objects.

* **Dynamic Grasps:** Highlight all objects that are baked in green. You can use [Dynamic Grasps](grasp_interaction.0.12.0.html#grasp-synthesis-method) on those objects.

* **Static Grasps:** Highlight all objects that have static grasps assigned to them in cyan. These objects are usually baked and special grasps were assigned to them using [VG Grasp Studio](unity_component_vggraspstudio.0.12.0.html). You can use [Dynamic and Static Grasps](grasp_interaction.0.12.0.html#grasp-synthesis-method) on those objects.

{% include youtube.html id="lFa1gn3Cu6c" caption="Bake Highlighting in the Unity Editor. Note that most of the objects in the scene are baked, but not the small apple. Thus, grasping the big apple results in Dynamic Grasps, grasping the small apple results in Sticky Hand grasps." %}

