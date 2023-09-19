---
title: VG_Assemble Component
#tags: [getting_started]
keywords: component, assemble, disassemble, interaction
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_1
permalink: unity_component_vgassemble.1.6.1.html
folder: mydoc
---

## Description 

{% include image.html file="unity/unity_vg_assemble_1_6_0.png" alt="VG Assemble." caption="VG Assemble component handles assemble and disassemble using VG joint" %}

VG_Assemble is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provides a tutorial on the minimal VG API functions for assembling and disassembling objects through VG joint changes. 

This is a mono behavior and is used as a component to attach to the Game Object which you want to assemble or disassemble from some other objects.  

Several examples in VG_Onboarding scene in VirtualGrasp\Scenes\onboarding are using this script to achieve various assembling tasks (see [task2 radio disassemble](unity_vgonboarding_task2.1.6.1.html), [task5 bottle](unity_vgonboarding_task5.1.6.1.html), [task7 chain assemble](unity_vgonboarding_task7.1.6.1.html), [task8 screw assemble](unity_vgonboarding_task8.1.6.1.html), and [task10 symmetric assemble](unity_vgonboarding_task10.1.6.1.html)). 

## Parameters

| Name | Description | Comment |
| Assemble To Parent | If current object will be reparented to the desired pose's parent. | See examples in [task5 bottle](unity_vgonboarding_task5.1.6.1.html) and [task8 screw assemble](unity_vgonboarding_task8.1.6.1.html).|
| Desired Poses | The transform(s) specifying the desired pose of this object or this object's _Assemble Anchor_.| Usually these transforms are the child of the object this object is attached to after assembling. |
| Assemble Distance | The distance (m) threshold (between object or its _Assemble Anchor_ to the desired poses) below which the assembling can be triggered. | Both linear distance and angular distance have to reach the thresholds to trigger assembling. |
| Assemble Angle | The angular distance (deg) threshold (between object or its _Assemble Anchor_ to the desired poses) below which the assembling can be triggered.  | Both linear distance and angular distance have to reach the thresholds to trigger assembling.  |
| Assemble Axis | Around which axis an object is to be rotational symmetrically assembled. The assembling is to match the selected axis on the _Assemble Anchor_ to the same axis of the closest _Desired Pose_. If the assembling is also symmetric along this axis (e.g. a cylinder), then choose "X/Y/Z Axis Symmetric". If rotational match is not needed (e.g. a sphere), then select "No Axis". | The axis is defined on the _Assemble Anchor_. If _Assemble Anchor_ is not asigned then it is on the object.|
| Assemble Symmetry Steps | Given a chosen Assemble Axis, how many discrete steps of rotation across 360 degrees is to be matched. 0 means smoothly rotational symmetric like for a cone or cylinder, 1 means not rotational symmetric at all around the axis, 2 can be used for rectangular prism, 6 for hexagon prism, etc. | This, together with _Assemble Axis_, are the two parameters that define rotation match for any symmetric or asymmetric objects. See [task 10](unity_vgonboarding_task10.1.6.1.html) to see a range of symmetric conditions.|
| Assemble Anchor | The transform representing the anchor on this object to be attached to the _Desired Poses_. If not assigned, then the anchor will be this object's origin.| This transform has to be the child of this object. |
| Disassemble Distance | The distance (m) threshold (between object or its _Assemble Anchor_ to the desired poses) above which the disassembling is triggered.  | Tune this value up if assembled object directly disassembles. |
| Disassemble On Zero State | If triggering disassembling also requires the object current joint state is zero. This is simulating the situation when disassembling screw joint requires screw being fully loosened. | See examples when disassembling cap from bottle in [task5 bottle](unity_vgonboarding_task5.1.6.1.html) and disassembling screws from the box [task8 screw assemble](unity_vgonboarding_task8.1.6.1.html). |
| Assemble Articulation | The [VG_Articulation](unity_component_vgarticulation.1.6.1.html) of a non-Floating {% include tooltip.html tooltip="JointType" text="joint type" %} the object switches to (from Floating type) when assembled. If not provided, the object will switch to {% include tooltip.html tooltip="Fixed" text="fixed" %} joint type.  | You can add a [VG_Articulation](unity_component_vgarticulation.1.6.1.html) component with desired joint type to the object and drag it to this entry.|
| Disassemble Articulation | The [VG_Articulation](unity_component_vgarticulation.1.6.1.html) of {% include tooltip.html tooltip="Floating" text="floating" %} joint type. Must be provided if object initially is non-{% include tooltip.html tooltip="Floating" text="floating" %} joint type.| See examples in [task2 radio disassemble](unity_vgonboarding_task2.1.6.1.html).|
| Force Disassembled Physical | If checked will make sure when an object is disassembled (switched to {% include tooltip.html tooltip="Floating" text="floating" %} joint) rigidbody and collider is added to make this object physical. | This is only relevant when object initially is at an assembled state (initial joint is non-{% include tooltip.html tooltip="Floating" text="floating" %}). See examples in [task2 radio disassemble](unity_vgonboarding_task2.1.6.1.html).  |
| On Before Assembled | Event triggered when object is to be assembled (satisfying assembling criterior but before joint and parent change). |  |
| On Assembled | Event triggered when object is assembled. | E.g. If target is indicated with a transparent object, this event can hook to _VG_Assemble.SetTargetTransformActive_ to be false to make the matched target disappear once the object is assembled. |
| On Disassembled | Event triggered when object is disassembled.| E.g. If target is indicated with a transparent object, this event can hook to _VG_Assemble.SetTargetTransformActive_ to be true to make the matched target reappear once the object is disassembled. |

