---
title: VG_Utility [Scriptable Object]
#tags: [getting_started]
keywords: component, utility
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_0
permalink: unity_component_vgutility.1.6.0.html
folder: mydoc
---

## Description

The ScriptableObject _Runtime/Resources/VG_Utility.asset_ is based on _Runtime/Scripts/VG_Utility.cs_.

It allows to quickly access most [VG API functions](https://docs.virtualgrasp.com/virtualgrasp_unityapi.1.6.0.html) through the UnityEvent system instead of through code.

For a component that has an event slot (see below at the example of a new script with a public UnityEvent), you can drag & drop the VG_Utility into the target slot of the event and assign VG API functions.

{% include image.html file="unity/unity_vg_utility.png" alt="VG Utility" caption="VG_Utility ScriptableObject as event sink." %}