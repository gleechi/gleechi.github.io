---
title: BakingClient [EditorWindow]
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar_1_0_0
permalink: unity_component_vgbakingclient.1.0.0.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_menu_1_0_0.png" alt="VG_BakingClient menu." caption="The BakingClient / Bake Grasps method can be found in the VirtualGrasp menu." %}

## Description

The VG_BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of {% include tooltip.html tooltip="ObjectBaking" text="object baking" %}, please read the [object baking documentation](object_baking.1.0.0.html) first.

{% include editor_script.html %}

{% include image.html file="knowledge/baking_pipeline_0_12_0.png" alt="Baking Pipeline." caption="Baking Pipeline." %}


## VG_BakingClient

{% include image.html file="unity/unity_vg_baking_client_1_0_0.png" alt="VG Baking Client in Unity." caption="VG_BakingClient in Unity." %}

<!--{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}-->

### Step 1: Authentication

After signing up to the Cloud Baking Service, you should have received credentials (email address and password). After entering them once, your credentials will be stored in your Unity registry, so you won't have to re-enter them all the time.

Check if your credentials are valid by clicking "Verify credentials".

### Step 2: Preparation

{% include image.html file="unity/unity_vg_baking_client_prepare_project.png" alt="VG Baking Client Prepare Project in Unity." caption="VG_BakingClient Prepare Project in Unity." %}

The preparation step is to create input files needed by the Baking Service. Since these input files can also be used for debugging purposes we refer them to "[Debug Files](debug_files.1.0.0.html#debug-files-content)". 

To prepare project, click _Prepare project_ button in baking client window, and a separate window "Prepare project" shown in above image will pop up. Follow the instruction to prepare the baking input files:
1. At the begining of preparing project, if the listed number of scenes, hand models or objects is non-zero, please click _Clear_ button to clear all so to prevent outdated data from polluting your baking result. 
2. Click _Export_ button will create and fill _Asset/vg_tmp/_ folder with "[Debug Files](debug_files.1.0.0.html#debug-files-content)" generated from the currently opened unity scene. To add more objects from other scenes, close this _Prepare project_ window, open the other scene, open this _Prepare project_ window and _Export_ again. Such process goes on untill you have accumulated all scenes that have {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects. **Note** all objects with [VG_Articulation](unity_component_vgarticulation.1.0.0.html) component will be exported even if this component is disabled.
3. Click _Finish_ button will package all data collected in Asset/vg_tmp/ into "grasps.zip", so you are ready to upload to Gleechi's cloud baking service. 

{% include important.html content="Note there are two ways to create the files depending on the need of your project. Currently, if you want to bake objects that are runtime spawned, _Prepare project_ window does not support it, you need to enable _Export Scene in Runtime_ in Debug Settings. See [Creating Debug Files](debug_files.1.0.0.html#creating-debug-files) for detailed instruction." %}

### Step 3: Baking

Once _Prepare project_ is finished by clicking _Finish_ button, you can come back to main baking client window, and click _Create Grasps for project_ to upload your package to the Gleechi Cloud baking server and trigger a bake. 
A window will appear to inform you about the process. Expect about 1-2 minutes for a common bake. 

Once baking is complete, the grasp baking .db file will be downloaded into your project folder.
Now you can directly play the project and enjoy natural looking grasps dynamically generated on your objects.