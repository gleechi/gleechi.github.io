---
title: VG_HandVisualizer Component
keywords: component, HandVisualizer
#last_updated: July 16, 2016
sidebar: main_sidebar
permalink: unity_component_vghandvisualizer.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_hand_visualizer.png" alt="VG HandVisualizer" caption="VG_HandVisualizer Component." %}

## Description

VG_HandVisualizer is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGPublicScript}}">public script</a> that provides a tool to visualize the VirtualGrasp representation of hand bones. 

The MonoBehavior script exemplifies how to use the VG API functions for accessing specific bones / elements of the hands, such as [VG_Controller.GetBone()](virtualgrasp_unityapi.html#getbone) and [VG_Controller.GetFingerBone()](virtualgrasp_unityapi.html#getfingerbone).

{% include singleton_script.html %}

{% include youtube.html id="pK1LxrrbHW4" caption="The VG_HandVisualizer visualizes the hand skeleton of each hand. In this example, the hands were made transparent to show the skeleton, and a finger tracking device was used to show the full movement of the hand." %}
