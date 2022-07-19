---
title: VG_GraspEditor Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_15_0
permalink: unity_component_vggraspeditor.0.15.0.html
folder: mydoc
---

## Description 

{% include image.html file="unity/unity_vg_prefab_graspeditor_prefabview.png" alt="VG Grasp Editor." caption="VG Grasp Editor" %}

VG_GraspEditor is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provide a tutorial on the minimal VG API functions for accessing grasps existing in the grasp database as well as using the labeling interface. A corresponding VG_GraspEditor prefab as shown above is added in **VirtualGrasp\Resources\onboarding**. This prefab can be added into any unity scene and allows runtime adding, deleting and reviewing primary grasps (see [Jump Primary Grasp](grasp_interaction.0.15.0.html#grasp-interaction-type)). 

{% include important.html content="VG_GraspEditor is a new version of grasp editing tool provided since this VG version (0.15.0). This replaces the [VG_GraspStudio](unity_component_vggraspstudio.0.14.0.html) in earlier versions, and provides a much simpler interface that can be used in runtime in any client's unity project.
VG_GraspEditor is added into the VG_onboarding scene for you to experiment with the grasp editing process. " %}

{% include youtube.html id="cAiS-uSTxJk" %}

## Adding Grasps

## Using Grasps in Runtime

## Important Note on the Files

The information on added and edited grasps will be stored in the grasp .db file which you will find in each project's StreamingAssets/VG_Grasps folder by default.

The VirtualGrasp plugin will automatically load this file at initialization (e.g. start the game), and save it at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same annotated grasps and labels, since the .db file is saved in and loaded from the project.
* If you you are using a version control system and want to share the annotated data with others, you have to commit the .db file to the repository.

