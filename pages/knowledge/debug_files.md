---
title: Debug Files
sidebar: main_sidebar
keywords: vg_tmp
permalink: debug_files.html
folder: knowledge
toc: true
---

{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG Debug Settings." caption="Debug Settings." %}

Enabling "Save Debug Files" and running the application will create a **vg_tmp** subdirectory in your project and save sources that are used for different purposes. The full debug files process is only in effect in development mode (i.e. using the Unity Editor), but not in builds.

{% include important.html content="Each creation of debug files is scene-dependent, meaning that it only relates to the **current** Unity scene. Thus, to complement debug files from multiple scenes, you have to run these scenes separately." %}

### Content

Whenever you start the scene, the following data will be saved in the "vg_tmp" folder (which will be created if it does not yet exist):
* **1 .OBJ** file for each interactable object, i.e. raw 3D mesh data in uniform scale,
* **1 .BIN** file for each hand configuration.

While you are running the scene, the following data will be saved in the "vg_tmp" folder:
* **1 .LOG** file with VG log data (the same that also appears on the Console) for the scene that you are running.

Whenever you stop the scene, the following data will be saved:
* **1 .DB** & **1 .LAB** file carrying data created with [VirtualGrasp Studio](unity_component_vggraspstudio.html),
* **1 .SCN** & **1 .SCN.OBJRIG** file for each scene, including scene configuration data.
* Finally, from all this content, **1 .ZIP** file named "PROJECT_NAME".zip will be generated in your project folder.

{% include important.html content="Accordingly, it is recommended to delete the vg_tmp folder whenever you start with a new debug file creation process, since existing and potentially outdated data will not be deleted (only potentially overwritten)." %}

<!--
### Creating the Debug Files
If properly setup, you will see similar info as below in your console:

{% include image.html file="unity/unity_vg_debug_console.png" alt="VG Baking Debug Console." caption="Console Output after Saving Debug Files." %}
-->

### Usecases

#### Baking

The **.ZIP** file of all the content is the input that is needed for [Grasp Baking](grasp_baking.html#upload-input).

#### Grasp Editor

The **.OBJ** files of all the objects are used for the automatic generation of the [Grasp Studio](unity_component_vggraspstudio.html) scene.