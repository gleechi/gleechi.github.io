---
title: VG_Assemble Component
#tags: [getting_started]
keywords: component, assemble, disassemble, interaction
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_2_0
permalink: unity_component_vgassemble.1.2.0.html
folder: mydoc
---

## Description 

{% include image.html file="unity/unity_vg_assemble.png" alt="VG Assemble." caption="VG Assemble component handles assemble and disassemble using VG joint" %}

VG_Assemble is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provides a tutorial on the minimal VG API functions for assembling and disassembling objects through VG joint changes. 

This is a mono behavior and is used as a component to attach to the Game Object which you want to assemble or disassemble from some other objects.  

Several examples in VG_Onboarding scene in VirtualGrasp\Scenes\onboarding are using this script to achieve various assembling tasks (see [task2 radio disassemble](unity_vgonboarding_task2.1.2.0.html), [task5 bottle](unity_vgonboarding_task5.1.2.0.html), [task7 chain assemble](unity_vgonboarding_task7.1.2.0.html) and [task8 screw assemble](unity_vgonboarding_task8.1.2.0.html)). 

## Parameters

| Name | Description | Comment |
| Assemble To Parent | If current object will be reparented to the desired pose's parent. | See examples in [task5 bottle](unity_vgonboarding_task5.1.2.0.html) and [task8 screw assemble](unity_vgonboarding_task8.1.2.0.html).|
| Desired Poses | The transform(s) specifying the desired pose of this object or this object's _Assemble Anchor_.| Usually these transforms are the child of the object this object is attached to after assembling. |
| Assemble Distance | The distance (m) threshold (between object or its _Assemble Anchor_ to the desired poses) below which the assembling can be triggered. | Both linear distance and angular distance have to reach the thresholds to trigger assembling. |
| Assemble Angle | The angular distance (deg) threshold (between object or its _Assemble Anchor_ to the desired poses) below which the assembling can be triggered.  | Both linear distance and angular distance have to reach the thresholds to trigger assembling.  |
| Assemble Axis | Along which axis the _Assemble Angle_ threshold is measuring the rotational difference. For rotational symetric object, sometimes we only need to align the rotation axis to the desired pose. If (0,0,0), then requires whole rotation match to the desired pose. |  |
| Assemble Anchor | The transform representing the anchor on this object to be attached to the _Desired Poses_. If not assigned, then the anchor will be this object's origin.| This transform has to be the child of this object. |
| Disassemble Distance | The distance (m) threshold (between object or its _Assemble Anchor_ to the desired poses) above which the disassembling is triggered.  | Tune this value up if assembled object directly disassembles. |
| Disassemble On Zero State | If triggering disassembling also requires the object current joint state is zero. This is simulating the situation when disassembling screw joint requires screw being fully loosened. | See examples when disassembling cap from bottle in [task5 bottle](unity_vgonboarding_task5.1.2.0.html) and disassembling screws from the box [task8 screw assemble](unity_vgonboarding_task8.1.2.0.html). |
| Assemble Articulation | The [VG_Articulation](unity_component_vgarticulation.1.2.0.html) of a non-Floating {% include tooltip.html tooltip="JointType" text="joint type" %} the object switches to (from Floating type) when assembled. If not provided, the object will switch to {% include tooltip.html tooltip="Fixed" text="fixed" %} joint type.  | You can add a [VG_Articulation](unity_component_vgarticulation.1.2.0.html) component with desired joint type to the object and drag it to this entry.|
| Disassemble Articulation | The [VG_Articulation](unity_component_vgarticulation.1.2.0.html) of {% include tooltip.html tooltip="Floating" text="floating" %} joint type. Must be provided if object initially is non-{% include tooltip.html tooltip="Floating" text="floating" %} joint type.| See examples in [task2 radio disassemble](unity_vgonboarding_task2.1.2.0.html).|
| Force Disassembled Physical | If checked will make sure when an object is disassembled (switched to {% include tooltip.html tooltip="Floating" text="floating" %} joint) rigidbody and collider is added to make this object physical. | This is only relevant when object initially is at an assembled state (initial joint is non-{% include tooltip.html tooltip="Floating" text="floating" %}). See examples in [task2 radio disassemble](unity_vgonboarding_task2.1.2.0.html).  |
| On Assembled | Event triggered when object is assembled. |  |
| On disassembled | Event triggered when object is disassembled.|  |

