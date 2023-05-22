---
title: BakingClient [EditorWindow]
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar_1_3_0
permalink: unity_component_vgbakingclient.1.3.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_menu_1_0_0.png" alt="BakingClient menu." caption="The BakingClient / Bake Grasps method can be found in the VirtualGrasp menu." %}

## Description

The BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of {% include tooltip.html tooltip="ObjectBaking" text="object baking" %}, please read the [object baking documentation](object_baking.1.3.0.html) first.

{% include editor_script.html %}

## Tutorial

{% include tip.html content="An in-editor tutorial \"VG Object Baking\" is included in VG to lead you through the steps of baking. You need to have [Unity's Tutorial Framework Package](https://docs.unity3d.com/Packages/com.unity.learn.iet-framework@3.1/manual/index.html) in your project to access the tutorial. You can easily install it through the VirtualGrasp->Welcome menu." %}

## BakingClient

<!--{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}-->

### Step 1: Authentication

After [signing up to the VG Cloud Baking Service](https://www.virtualgrasp.com/download), you should have received credentials (email address and password). After entering them once in the Login tab of the Baking Client Window, your credentials will be stored in your Unity registry, so you won't have to re-enter them all the time.

Check if your credentials are valid by clicking "Verify credentials".

{% include image.html file="unity/unity_vg_baking_client_1_2_0b.png" alt="Baking Client in Unity - Login Tab." caption="BakingClient in Unity - Login Tab." %}

### Step 2: Packaging

{% include image.html file="unity/unity_vg_baking_client_1_2_0a.png" alt="Baking Client in Unity - Bake Tab." caption="BakingClient in Unity - Bake Tab." %}

The Packaging step is to create input files needed by the Baking Service. Since these input files can also be used for debugging purposes we refer them to "[Debug Files](debug_files.1.3.0.html#debug-files-content)". 

Follow the instruction to prepare the baking input files:
1. At the beginning of preparing a project, if the listed number of scenes, hand models or objects is non-zero, please click _Clear_ button to clear all data to prevent outdated data from polluting your baking result. 
2. Click _Export_ button will create and fill the _Assets/vg_tmp/_ folder with "[Debug Files](debug_files.1.3.0.html#debug-files-content)" generated from the currently opened unity scene. To add more objects from other scenes, close this _Prepare project_ window, open the other scene, open this _Prepare project_ window and _Export_ again. Such process goes on untill you have accumulated all scenes that have {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects. **Note:** all objects with [VG_Articulation](unity_component_vgarticulation.1.3.0.html) component will be exported even if this component is disabled.
3. Click _Finish_ button will package all data collected in _Assets/vg_tmp/_ into "bake-job.zip", so you are ready to upload to Gleechi's cloud baking service. 

{% include important.html content="Note there are two ways to create the files depending on the need of your project. Currently, if you want to bake objects that are runtime spawned, _Prepare project_ window does not support it, you need to enable _Export Scene in Runtime_ in Debug Settings. See [Creating Debug Files](debug_files.1.3.0.html#creating-debug-files) for detailed instruction." %}

### Step 3: Baking

Once you have packaged clicking _Package_, you can click _Create Grasps for project_ to upload your package to the Gleechi Cloud baking server and trigger a bake. 
A window will appear to inform you about the process. Expect about 1-2 minutes for a common bake. 

Once the baking is complete, a console message will be displayed to show the newly baked grasp db (as .db) file is saved as "Assets/VG_Grasps/grasp-[hash].db" with a randomly generated hash. You need to drag this file into [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.3.0.html#grasp-db) to use it in your project.

Now you can directly play the project and enjoy natural looking grasps dynamically generated on your objects.

{% include callout.html content="Any .db file is recognized as a grasp db when it is placed in the Assets folder. "%}

## Baking Architecture

{% include image.html file="knowledge/baking_pipeline_0_12_0.png" alt="Baking Pipeline." caption="Baking Pipeline." %}
