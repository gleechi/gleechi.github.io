---
title: VG_GraspStudio Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_12_0
permalink: unity_component_vggraspstudio.0.12.0.html
folder: mydoc
---

## Description 

VG_GraspStudio is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %}.
It is provided as a component of the VirtualGrasp Unity plugin, and thus only available in Unity for now. 

VG_GraspStudio provides a tutorial on the VG API functions for accessing grasps existing in the grasp database as well as using the labeling interface.

It serves as a high-level visualizing tool in which you can not only review all grasps that you have in a project, but also annotate them.

Some examples of annotations are:

* "adding manually annotated grasps for an object”
* “choosing only some "primary" grasps for an object”.

<!--
{% include tip.html content="If you are more interested in the low-level API or editing features of VirtualGrasp, or interested in implementing similar high-level features in Unreal, we recommend to also have a look at the Grasp Editing API Section of the API. The VirtualGrasp API (VG_Controller) has one single API function called [EditGrasp](VirtualGrasp_UnityAPI.0.12.0.html#editgrasp) to perform different editing actions on an object. Look up the API page as well as the [EditorAction](VirtualGrasp_UnityAPI.0.12.0.html#vg_editoraction) list for more information." %}-->

## Enabling VirtualGrasp GraspStudio

The preferred way to use GraspStudio is to use the option of automatically creating a separate editor scene (Menu VirtualGrasp → Asset Functions → Create VG_Editor Scene).

This will place a new .unity scene next to your existing one in the file system, that will then be opened automatically.

The new editor scene will be automatically configured by combining information from your current scene (VirtualGrasp, hands and camera components), [debug files](debug_files.0.12.0.html#grasp-editor) (objects) and adding and configuring the GraspStudio component itself (from Prefabs).


## VirtualGrasp Studio GUI

The interface is shown below, with some regions outlined in blue only for this documentation.

Note that when starting in VR mode, form a grab with both hands and move them (e.g., press both controller triggers and move them when using controllers) to place and adjust the GUI in front of you.

{% include image.html file="unity/unity_vg_graspstudio.png" alt="VG GraspStudio" caption="VG_GraspStudio Component." %}

[A] The Grasp View

Here, the current object and the selected grasp is visualized.

[B] The Thumbnail View

Here, a subset of all the current object's grasps is visualized.

[C] The Object Panel

Here, information on the current object and the selected grasp is visualized, together with buttons to step between objects.

[D] The Grasp Panel

Here, information on the selected grasp is visualized, together with buttons to step between grasps as well as to label them.

## Interacting with VirtualGrasp GraspStudio

The interface supports two different modes: 

**Non-VR mode.** You can interact with the interface using the mouse and/or the keyboard when playing the scene. The GUI camera is used, so you will not be able to see your scene.

**VR mode.** You can interact with the interface using your controllers when playing the scene. You can do this both using buttons on the controllers (if they have any) as well as by interacting with the GUI.

You are free to choose after your own preference, but notice that not all features are possible in Non-VR mode.

The following table describes the actions and how to achieve them in the two modes:

| Action(s) | Non-VR (Mouse) | VR (Controller) | Both (Keyboard)| 
|-------|--------|---------|---------|
| Previous/Next Object | Click Prev/Next in [C] | Push left thumbstick down/up | PgDown/PgUp | 
| Previous/Next Grasp(next page will be triggered automatically) | - | Push left thumbstick left/right | ArrowLeft/ArrowRight | 
| Select Grasp | Click a thumbnail in [B] | - | - | 
| Previous/Next Page | Click Prev/Next in [D] | - | ArrowUp/ArrowDown | 
| Rotate object(s) (main and thumbnails) | Drag Mouse in [A] | Rotate left controller | - | 
| Switch Hand | Click Icon above [A] | Push grip button of hand to switch to | -| 
| Label as Primary* | Click ★  | Push right thumbstick up | P | 
| Label as Disabled** | Click    ⃠       | Push right thumbstick down | D |  
| Label all as Disabled* | - | - | LShift+D | 
| Delete Grasp** |  |  | |  
| Scale/Place Interface | - | Grasp with both hands in air and move them apart | - | 
| Adding Dynamic grasp | - | see "Adding Grasps" below | A | 

\* Labeling an already selected primary grasp unlabel it.

\** Disabling an already selected disabled grasp deletes it.

## Adding Grasps

Adding grasps can only be done in VR. The scene will have a second hand pair created that can interact with a duplicate of the visualized object, using [dynamic grasping](grasp_interaction.0.12.0.html#grasp-synthesis-method). You can grasp the object until you find a grasp that you would like to add, and while holding then press the top button (usually "X" on the left and "A" on the right controller) to add it as a static grasp. It will then appear as a new entry in the thumbnail section.

## Using Grasps in Runtime

In order to use your annotated grasps instead of the default, dynamic grasps during runtime, you need to change an object's [grasp synthesis method](https://docs.gleechi.com/grasp_interaction.0.12.0.html#grasp-synthesis-method) to STATIC_GRASP, and optionally adjust its [interaction types](https://docs.gleechi.com/grasp_interaction.0.12.0.html#grasp-interaction-type). 

Unless you want all objects to behave the same (and use the [global interaction settings](https://docs.gleechi.com/unity_component_myvirtualgrasp.0.12.0.html#grasp-interaction-settings)), you need to add a [VG_Interactable](https://docs.gleechi.com/unity_component_vginteractable.0.12.0.html) on your object to adjust these parameters only for this object.

## Important Note on the Files

The information on added and edited grasps will be stored in an additional .db file which you will find in each project's StreamingAssets/VG_Grasps folder by default.

The VirtualGrasp plugin will automatically load this file at initialization (e.g. start the game), and save it at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same annotated grasps and labels, since the .db file is saved in and loaded from the project.
* If you you are using a version control system and want to share the annotated data with others, you have to commit the .db file to the repository.

