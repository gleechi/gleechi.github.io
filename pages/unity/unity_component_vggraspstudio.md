---
title: VG_GraspStudio Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vggraspstudio.html
folder: mydoc
---

### Background 

VG_GraspStudio is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGPublicScript}}">public script</a>.
It is provided as a component of the VirtualGrasp Unity plugin, and thus only available in Unity for now. 
The MonoBehavior provides a tutorial on the VG API functions for accessing grasps existing in the grasp DB as well as using the labeling interface.

It serves as a high-level visualizing tool in which you can not only review all grasps that you have in a project, but also annotate them.

Some examples of annotations are:

* “deleting grasps that look bad”.
* "adding (dynamic) grasps for an object into the (static) grasp database”
* “choosing only some "primary" grasps for an object”.

{% include tip.html content="If you are more interested in the low-level API or editing features of VirtualGrasp, or interested in implementing similar high-level features in Unreal, we recommend to also have a look at the Grasp Editing API Section of the API. The VirtualGrasp API (VG_Controller) has one single API function called [EditGrasp](VirtualGrasp_UnityAPI.html#editgrasp) to perform different editing actions on an object. Look up the API page as well as the [EditorAction](VirtualGrasp_UnityAPI.html#vg_editoraction) list for more information." %}

### Enabling VirtualGrasp GraspStudio

The preferred way to use GraspStudio is to use the option of automatically creating a separate editor scene (Menu VirtualGrasp → Create VG_Editor Scene).

This will place a new .unity scene next to your existing one in the file system, that you can then open and use.

The new editor scene will be automatically configured by combining information from your current scene (VirtualGrasp, hands and camera components), [debug files](debug_files.html#grasp-editor) (objects) and adding and configuring the GraspStudio component itself (from Prefabs).


### VirtualGrasp Studio GUI

The interface is shown below, with some regions outlined in blue only for this documentation:

{% include image.html file="unity/unity_vg_graspstudio.png" alt="VG GraspStudio" caption="VG_GraspStudio Component." %}

[A] The Grasp View

Here, the current object and the selected grasp is visualized.

[B] The Thumbnail View

Here, a subset of all the current object's grasps is visualized.

[C] The Object Panel

Here, information on the current object and the selected grasp is visualized, together with buttons to step between objects.

[D] The Grasp Panel

Here, information on the selected grasp is visualized, together with buttons to step between grasps as well as to label them.

### Interacting with VirtualGrasp GraspStudio

The interface supports two different modes: 

**Non-VR mode.** You can interact with the interface using the mouse and/or the keyboard when playing the scene. The GUI camera is used, so you will not be able to see your scene.

**VR mode.** You can interact with the interface using your VR controllers when playing the scene. You can do this both using buttons on the controllers as well as by interacting with the GUI.

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
| Label as Primary* | Click ★ in [D] | Push right thumbstick up | P | 
| Label as Disabled* | Click    ⃠     in [D] | Push right thumbstick down | D |  
| Label all as Disabled* | - | - | LShift+D | 
| Scale/Place Interface | - | Push both triggers and move controllers | - | 
| Adding Dynamic grasp | - | see "Adding Grasps" below | - | 

\* Labeling an already selected primary or disabled grasp unlabel it.

### Adding Grasps

Adding grasps can only be done in VR. The scene will have a second hand pair created that can interact with a duplicate of the visualized object, using [dynamic grasping](grasp_interaction.html#grasp-synthesis-method). You can grasp the object until you find a grasp that you would like to add, and while holding then press the top button (usually "X" on the left and "A" on the right controller) to add it as a static grasp. It will then appear as a new entry in the thumbnail section.

### Important Note on the Files

The information on added and edited grasps will be stored in additional files which you will find in each project's root folder by default:

* vg_external.db: keeps manually added grasps
* vg_external.lab: keeps manually edited labels of grasps (such as disabled, primary, etc).

The VirtualGrasp plugin will automatically  

* load these files at initialization (e.g. start the game), and 
* save them at releasing (e.g. stop the game). 

By this follows that:

* All scenes will use the same annotated grasps and labels, since the files are saved in the project.
* When you want to use the labels in a build, you have to manually copy these files to the build directory.
* If you you are using a version control system and want to share the annotated data with others, you have to commit these files to the repository.

