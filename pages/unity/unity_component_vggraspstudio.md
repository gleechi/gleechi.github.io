---
title: VG_GraspStudio Component
#tags: [getting_started]
keywords: component, editor, studio, grasp
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_vggraspstudio.html
folder: mydoc
---

VirtualGrasp Studio is provided as a component of the VirtualGrasp Unity plugin, and thus only available in Unity for now. 

At the moment, it serves as a high-level visualizing tool in which you can not only review all grasps that you have in a project, but also label them.

Some example use cases are:

* “deleting grasps that look bad”.
* "add (dynamic) grasps into the (static) grasp database”
* “only choose one primary grasp to use for this object”.

If you are more interested in the low-level API or editing features of VirtualGrasp, or interested in implementing similar high-level features in Unreal, we recommend to also have a look at the Grasp Editing API Section at the bottom of this page.

### Enabling VirtualGrasp GraspStudio

There are multiple ways to enable the grasp editor into your project:

#### Raw Prefab

In VirtualGrasp/Resources/GraspStudio/ you will find a Prefab "GraspStudio" that contains the grasp studio plug and play component.

You could simply drag and drop the prefab into your scene if it is setup with VG. While running GraspStudio, you need to set the controller mode (in Sensors→ Sensor to NO_CONTROLLER) - otherwise the hands will follow the controller and not the objects in the grasp editor. You also need to configure another hand when you want to add dynamic grasps.

#### Auto-generated editor scene

In order to not pollute your scene with the grasp editor,  and to avoid configuring the VG components, you can generate an editor scene from your main scene (Menu VirtualGrasp→ Create VG_Editor Scene). This will place a new .unity scene next to your existing one in the file system, and setup VG, GraspStudio, hands, objects, light, camera, etc, in it. 

You can then use this scene to label, and since labels are files saved in the project,  the main scene will simply use the same labels.

You can even use a build of that scene to create the labels.

[It is tested to be working well with a default VG integration. It is not considering various potential alternatives of your main scene setup (for example, if there is no VG in it from the beginning). ] 

#### Auto-filled editor scene

The earlier modes will use your main scene to copy object models into the editor scene. Which means, if you have 10 apples, you will have 10 apples in the grasp editor. You can obviously remove the redundant objects manually.

When using the VG export function ("Save Debug Files") you know that .obj files will be exported into your Assets/vg_tmp folder (to be used for the automatic baking pipeline). If you have used this function, you can import the .obj files into your editor scene (Menu VirtualGrasp→ Load assets from vg_tmp).

  

### VirtualGrasp Studio GUI

The interface is shown below, with some regions outlined in blue only for this documentation:

{% include image.html file="unity/unity_vg_graspstudio.png" alt="VG GraspStudio" caption="VG_GraspStudio Component." %}

[A] The Grasp View

Here, the current object and the selected grasp is visualized.

[B] The Thumbnail View

Here, a subset of all the current object's grasps are visualized.

[C] The Object Panel

Here, information on the current object and the selected grasp is visualized, together with buttons to step between objects.

[D] The Grasp Panel

Here, information on the selected grasp is visualized, together with buttons to step between grasps as well as to label them.

#### Interacting with VirtualGrasp GraspStudio

The interface supports two different modes: 

VR mode: you can interact with the interface using VR controllers when playing the scene. The main camera is used, so you can walk through your scene while using the editor.

Non-VR mode: you can interact with the interface using the mouse when playing the scene.The GUI camera is used, so you will not be able to see your scene.

You are free to choose after your own preference, but (1) not all features are possible in Non-VR mode; (2) there may appear problems in VR mode when you already have / are using the controller for other interactions (such as teleportation, etc). 

In the latter, we recommended to create a complete empty scene and copy VG and your objects into it. It is a task on the TODO list to create this scene automatically.

#### Actions

The following table describes the actions and how to achieve them in the two modes:

| Action(s) | Non-VR (Mouse) | VR (Controller) | Both (Keyboard)| 
|-------|--------|---------|---------|
| Previous/Next Object | Click Prev/Next in [C] | Push left thumbstick down/up | PgDown/PgUp | 
| Previous/Next Grasp(next page will be triggered automatically) | - | Push left thumbstick left/right | ArrowLeft/ArrowRight | 
| Select Grasp | Click a thumbnail in [B] | - | - | 
| Previous/Next Page | Click Prev/Next in [D] | - | ArrowUp/ArrowDown | 
| Rotate object(s)(main and thumbnails) | Drag Mouse in [A] | Rotate left controller | - | 
| Switch Hand | Click Icon above [A] | Push grip button of hand to switch to | -| 
| Label as Primary* | Click ★ in [D] | Push right thumbstick up | P | 
| Label as Disabled* | Click    ⃠     in [D] | Push right thumbstick down | D |  
| Label all as Disabled* | - | - | LShift+D | 
| Scale/Place Interface | - | Push both triggers and move controllers | - | 
| Adding Dynamic grasp | - | see "Adding Grasps" below | - | 

* since only one grasp can be Primary, picking a different grasp as primary will unselect an already selected primary grasp. Labeling an already selected primary grasp will unlabel it.

* labeling an already selected disabled grasp will unlabel it.

### Adding Grasps

Adding grasps can only be done in VR. The scene will have a second hand pair created that can interact with a duplicate of the visualized object, using dynamic grasping.You can grasp the object until you find a grasp that you would like to add, and then press the right "A" button on your controller to add it as a static grasp. It will then appear as a new entry in the thumbnails.

### Important Note on the Files

The information on added and edited grasps will be stored in additional files which you will find in each project's root folder by default:

* vg_external.db: keeps manually added grasps
* vg_external.lab: keeps manually edited labels of grasps (such as disabled, primary, etc).

The VirtualGrasp plugin will automatically  

* load these files at initialization (e.g. start the game), and 
* save them at releasing (e.g. stop the game). 

That means that when you label inside a game engine, and want to use the labels in a build, you have to manually copy these files to the build directory.

Also, if you you are using a project repository and want to share the annotated data, you have to commit these files to the repository to do so.


### Grasp Editing API

The VirtualGrasp API (VG_Controller) has one single API function called [EditGrasp](VirtualGrasp_UnityAPI.html#editgrasp) to perform different editing actions on an object. Look up the API page as well as the [EditorAction](VirtualGrasp_UnityAPI.html#vg_editoraction) list for more information.