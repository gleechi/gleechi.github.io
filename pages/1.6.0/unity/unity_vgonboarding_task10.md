---
title: VirtualGrasp Onboarding Task10 - Symmetric Assemble 
#tags: [getting_started]
keywords: casestudy, task10, vgonboarding, assemble, disassemble, VG_Assemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_0
permalink: unity_vgonboarding_task10.1.6.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

{% include youtube.html id="22jiFTPS-eE" %}

#### Interaction behaviors wanted

* Objects whose shapes have different levels of symmetry demand different types of rotaional matching when assembling to a target pose. 
* This task showcases how these different symmetric shapes could be assembled with a set of generic parameters in the provided [VG_Assemble](unity_component_vgassemble.1.6.0.html) component. 
* As shown in the above video, the assembling behaviors we want are:
    * for the sphere, just positional match is needed since it is rotational symmetric around the centriod;
    * for the cone, matching of a rotational axis is needed, and around this axis it is completely rotational symmetric;
    * for the hexagonal prism, matching of a rotational axis in either direction is needed, and around this axis it is rotational symmetric but at 6 discrete angles around the 360 deg range;
    * for the pyramid, matching of a rotational axis is needed, and around this axis it is rotational symmetric but at 4 discrete angles around the 360 deg range;
    * for the curved bar, matching of a rotational axis is needed, and around this axis it is rotational symmetric but at 2 discrete angles around the 360 deg range;
    * for the apple, which is completely assymetric object, we need full rotational match. 

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**. 

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

#### Assemble and disassemble object with different level of symmetric properties

{% include image.html file="unity/unity_onboarding_task10_vg_assemble.png" alt="VG Assemble setup for a set of symmetric objects." caption="VG Assemble setup for a set of symmetric objects." %}

[VG_Assemble](unity_component_vgassemble.1.6.0.html) component is used for assembling and disassembling object with any type of symmetric properties. 
Above image shows the setting for assembling the curved bar object in the video. The table below explains the key parameters for all the shapes in the video. 

| Object | Described As being | Assemble Axis | Assemble Symmetric Steps| Comments |
|-------|--------|---------|---------|
| Sphere |rotational symmetric around  a centroid (No Axis) | No Axis | - | No Axis means no need to match the roation, and Steps parameter can be anything |
| Cone |rotational symmetric around an axis | Y Axis| 0 | Y Axis is the rotational axis of the Cone shape, 0 Steps means can rotate around this axis at any angle |
|-------|---------|--------|---------|---------|
| Hexagon Prism |6-step rotational symmetric around a symmetric axis | Y Axis Symmetric  | 6 | Y Axis Symmetric is chosen because the shape is symmetric in either direction of the Y Axis. And 6 Steps is chosen because hexagon requres matching of rotation at 6 discrete steps around the Y Axis |
| Pyramid |4-step rotational symmetric around an axis | Y Axis | 4 | Y Axis the rotational axis of the Pyramid. And 4 Steps is chosen because Pyramid requres matching of rotation at 4 discrete steps around the Y Axis |
| Curved Bar |2-step rotational symmetric around an axis  | Z Axis | 2 | Z Axis of assigned Assemble Anchor is chosen because the Curved Bar is symmetric around this axis. And 2 Steps is chosen because around Z Axis matching could happen with 180 degree of flip, i.e. 2 discrete steps around the Z axis |
| Apple |1-step rotational symmetric around an axis (i.e. non-symmetric) | X Axis | 1 | Apple is an assymetric object, so any unsymmetric Assemble Axis can be chosen (X, Y, or Z Axis), and 1 Step is chosen because it is only allowed to match of one angle around this X axis.|


