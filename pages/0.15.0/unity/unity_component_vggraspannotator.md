---
title: VG_GraspAnnotator Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_15_0
permalink: unity_component_vggraspannotator.0.15.0.html
folder: mydoc
---

## Description 

VG_GraspAnnotator is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %}.
It is provided as a component of the VirtualGrasp Unity plugin, and thus only available in Unity for now. 

VG_GraspAnnotator provides a tutorial on the minimal VG API functions for accessing grasps existing in the grasp database as well as using the labeling interface.

Some examples of annotations are:

* "adding manually annotated grasps for an object”
* “choosing only some "primary" grasps for an object”.

## Adding Grasps

## Using Grasps in Runtime


## Important Note on the Files

The information on added and edited grasps will be stored in the grasp .db file which you will find in each project's StreamingAssets/VG_Grasps folder by default.

The VirtualGrasp plugin will automatically load this file at initialization (e.g. start the game), and save it at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same annotated grasps and labels, since the .db file is saved in and loaded from the project.
* If you you are using a version control system and want to share the annotated data with others, you have to commit the .db file to the repository.

