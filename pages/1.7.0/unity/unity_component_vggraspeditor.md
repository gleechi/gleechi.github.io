---
title: VG_GraspEditor Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_7_0
permalink: unity_component_vggraspeditor.1.7.0.html
folder: mydoc
---

## Description 

{% include image.html file="unity/unity_vg_prefab_graspeditor_prefabview_1_0_0.png" alt="VG Grasp Editor." caption="VG Grasp Editor" %}

VG_GraspEditor is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that provides a tutorial on the minimal VG API functions for accessing grasps existing in the VG grasp database as well as using the labeling interface. 

A VG_GraspEditor Prefab that uses this script (as shown in above image) is added in **VirtualGrasp\Resources\GraspEditor**. This prefab can be added into any unity scene and allows runtime adding, deleting and reviewing {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} (see [Jump Primary Grasp](grasp_interaction.1.7.0.html#grasp-interaction-type)). 

{% include important.html content="Please do all grasp editing in the Unity Editor in order to modify the grasp database. When using VG_GraspEditor on Android, the grasp database is not modified to prevent users from accidentally modifying an application. " %}

{% include youtube.html id="40kYLBKhmqk" %}

## Editing Grasps

Using VG_GraspEditor you can add {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized grasps" %} as {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} into the grasp DB in runtime. 

* The VG_GraspEditor Prefab shows up as an "editing pad" with a number of buttons to allow adding, deleting, deleting all, stepping through {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} and experimenting with the {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interactions on the object.
* This editing pad is also an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object so that it can be grasped and moved close to any object(s) on which grasp editing is needed.
* The grasp editing will be performed on the object currently grasped in one hand. If no object is grasped by any hand, all buttons (currently the text next to it) are grayed out to show there is no valid action on this button.
* Once an object is grasped by a hand, the relevant grasp editing buttons are enabled by showing up the button text (in black).
* When an object's current {% include tooltip.html tooltip="InteractionType" text="interaction type" %} is {% include tooltip.html tooltip="TriggerGrasp" text="Trigger Grasp" %}, {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} or {% include tooltip.html tooltip="PreviewGrasp" text="Preview Grasp" %}, the grasps are {% include tooltip.html tooltip="DynamicGrasp" text="dynamically synthesized" %}. Therefore the **Add grasp** button is enabled to add the current grasp into the grasp db.
* VG_GraspEditor GUI has an option _Editing Interaction Type_ to allow developers to choose the main {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to use when adding primary grasps. The first time pushing Toggle button will switch the grasped object to the selected editing interaction type, and later the Toggle button will toggle between this type and {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} for adding and reviewing added primary grasps respectively. This allows developer to choose most convenient _Editing Interaction Type_ for adding grasps without interfering with the desired project setting for the objects.
* If you want to immediately delete a just added grasp, click the **Delete grasp** button without re-grasping the object. 
* If you want to delete all grasps added on this object with this hand, click the **Delete all grasps** button.
* If you want to experiment with {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interaction with the primary grasps, click **Toggle interaction** button to toggle to {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %} interaction type. When you then re-grasp this object, the primary grasp closest to the current wrist pose will be applied. 
* When the current interaction is {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %}, you can also **step** through to review all the {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} by clicking the **Step grasp** button. 
* By stepping through grasps, you can also click the **Delete grasp** button to delete unwanted grasps.
* Remember to add primary grasps for both left and right hands for a given object, otherwise when the object is set to {% include tooltip.html tooltip="JumpPrimaryGrasp" text="jump primary grasp" %} interaction type, the hand without primary grasps added will not be able to grasp the object.
* There is no need to press any button to save grasps, simply close the application, and the added grasps will be saved into the graspdb used in the project.

{% include important.html content= "Note that during the grasp editing, only edited grasps are saved to the database. The toggled interaction type is not saved in the scene and will not overwrite your project settings for the object." %} 

## Using Grasps in Runtime

To use {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} for an object, you need to set the object's {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to be {% include tooltip.html tooltip="JumpPrimaryGrasp" text="Jump Primary Grasp" %}. To do that you can
* either add a [VG_Interactable](unity_component_vginteractable.1.7.0.html) component to the object and to specify for this object locally, 
* or specify in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.7.0.html#global-grasp-interaction-settings) if you want all objects to be only grasped using added {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %},
* or use the API function [SetInteractionTypeForObject](virtualgrasp_unityapi.1.7.0.html#vg_controllersetinteractiontypeforobject) to change this object to use primary grasp in runtime,
* or use the API function [SetGlobalInteractionType](virtualgrasp_unityapi.1.7.0.html#vg_controllersetglobalinteractiontype) to change all the objects to use primary grasps in runtime.

{% include important.html content= "Once an object uses Jump Primary Grasp as the interaction type, it assumes the hand that want to grasp it has added primary grasps for the object. So if you only added primary grasps on one hand, then the other hand will not be able to grasp the object. The primary grasps added in one hand currently can not be mirrored directly to the other hand side because mirroring of grasps is not as simple as mirroring just hand gesture since it involves accurately detecting the object symmetry as well." %} 

## Important Note on the Files

The information on added grasps will be stored in the grasp .db file that you specified in [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.7.0.html#grasp-db). You do not need to specifically save the added grasps since, 
the VirtualGrasp plugin will load this file at initialization (e.g. start the game), and save it at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same added grasps, since the .db file is saved in and loaded from the project.
* If you you are using a version control system and want to share the data with others, you have to commit the .db file to the repository.

{% include important.html content= "After grasp editing which modifies the grasp .db file, rebaking objects (due to added new objects) will not remove the added grasps. The new baking result saved in Assets/VG_Grasps/grasp-hash.db with a different hash still contains the added grasps. However if you change the shape or scale of the objects on which the primary grasps are added, then rebaking will remove the grasps."%} 
