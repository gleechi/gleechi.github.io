---
title: VG_HandVisualizer Component
keywords: component, HandVisualizer
#last_updated: July 16, 2016
sidebar: main_sidebar_1_5_0
permalink: unity_component_vghandvisualizer.1.5.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_hand_visualizer.png" alt="VG HandVisualizer" caption="VG_HandVisualizer Component." %}

## Description

VG_HandVisualizer is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provides a tool to visualize the VirtualGrasp representation of hand bones for debugging purposes. To see the skeleton, you should either choose a transparent shader for your hands or disable the skinned mesh renderer. 

The MonoBehavior script exemplifies how to use the VG API functions for accessing specific bones / elements of the hands, such as [GetBone()](virtualgrasp_unityapi.1.5.0.html#vg_controllergetbone) and [GetFingerBone()](virtualgrasp_unityapi.1.5.0.html#vg_controllergetfingerbone).

{% include singleton_script.html %}

{% include youtube.html id="pK1LxrrbHW4" caption="The VG_HandVisualizer visualizes the hand skeleton of each hand. In this example, the hands were made transparent to show the skeleton, and a finger tracking device was used to show the full movement of the hand." %}
