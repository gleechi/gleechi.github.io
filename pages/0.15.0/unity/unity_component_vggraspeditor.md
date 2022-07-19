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

VG_GraspEditor is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provide a tutorial on the minimal VG API functions for accessing grasps existing in the grasp database as well as using the labeling interface. A corresponding VG_GraspEditor prefab as shown above is added in **VirtualGrasp\Resources\onboarding**. This prefab can be added into any unity scene and allows runtime adding, deleting and reviewing {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} (see [Jump Primary Grasp](grasp_interaction.0.15.0.html#grasp-interaction-type)). 

{% include important.html content="VG_GraspEditor is a new version of grasp editing tool provided since this VG version (0.15.0). This replaces the [VG_GraspStudio](unity_component_vggraspstudio.0.14.0.html) in earlier versions, and provides a much simpler interface that can be used in runtime in any client's unity project.
VG_GraspEditor is added into the VG_onboarding scene for you to experiment with the grasp editing process. " %}

{% include youtube.html id="cAiS-uSTxJk" %}

## Edit Grasps

Using VG_GraspEditor you can add {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized grasps" %} as {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} into the StreamingAssets/VG_Grasps/grasps.db in runtime. 

* VG_GraspEditor prefab shows up as an "editing pad" with a number of buttons to allow adding, deleting, deleting all, step through {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} and experiment the {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interactions on the object.
* This editing pad and buttons are also {% include tooltip.html tooltip="VGInteractable" text="VG interactable" %} so that it can be grasped and moved close to any object(s) on which grasp editing is needed.
* The grasp editing is on the object currently grasped in one hand. So if no object is grasped by any hands, all buttons (currently the text next to it) is grayed out to show there is no valid action on this button.
* Once an object is grasped by a hand, the relevant grasp editing buttons are enabled by showing up the button text (black). 
* When an object's current {% include tooltip.html tooltip="InteractionType" text="interaction type" %} is {% include tooltip.html tooltip="TriggerGrasp" text="Trigger Grasp" %} or {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %}, that means the grasps are {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized" %}. Therefore **Add grasp** button is enabled to add current grasp into the grasp db.
* If you want to immediately delete just added grasp, click **Delete grasp** button. 
* If you want to delete all grasps added on this object with this hand, click **Delete all grasps** button.
* If you want to experiment with {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interaction with the primary grasps, click **Toggle interaction** button to toggle to {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interaction type. Then when you regrasp this object the primary grasp closes to the current wrist pose will be applied. 
* When current interaction is {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %}, you can also **step** through all the {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} by clicking **Step grasp** button. 
* By steping through grasps, you can also click **Delete grasp** button to delete unwanted grasps.
* To save grasps there is no need to press any button, simply close the application, the added grasps will be saved into StreamingAssets/VG_Grasps/grasps.db in your project folder. Note only grasps are saved, and the toggled interaction type will not be saved into the project setting on this object. 

## Using Grasps in Runtime

## Important Note on the Files

The information on added grasps will be stored in the grasp .db file which you will find in each project's StreamingAssets/VG_Grasps folder by default.

The VirtualGrasp plugin will automatically load this file at initialization (e.g. start the game), and save it at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same annotated grasps and labels, since the .db file is saved in and loaded from the project.
* If you you are using a version control system and want to share the annotated data with others, you have to commit the .db file to the repository.
