---
title: VG_BakingClient Component
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar_0_11_1
permalink: unity_component_vgbakingclient.0.11.1.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_menu_bakingclient_0_12_0.png" alt="VG_BakingClient menu." caption="VG_BakingClient can be found in the VirtualGrasp/Components menu." %}

## Description

The VG_BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of object baking, please read the [object baking documentation](object_baking.0.11.1.html) first.

{% include editor_script.html %}

{% include image.html file="knowledge/baking_pipeline.png" alt="Baking Pipeline." caption="Baking Pipeline" %}

## VG_BakingClient

{% include image.html file="unity/unity_vg_baking_client_0_12_0.png" alt="VG Baking Client in Unity." caption="VG_BakingClient in Unity." %}

<!--{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}-->

### Step 1: Authentication

After signing up to the Cloud Baking Service, you should have received credentials (email address and password). After entering them once, your credentials will be stored in a file called vg_cabvg_settings.json in your project folder, so you won't have to re-enter them all the time.

Check if your credentials are valid by trying to "Login." If successful, a window will appear telling you that you logged in successfully.

### Step 2: Preparation

{% include image.html file="unity/unity_vg_baking_client_prepare_project.png" alt="VG Baking Client Prepare Project in Unity." caption="VG_BakingClient Prepare Project in Unity." %}

Preparation step is to create input files needed by the Baking Service. Since these input files can also be used for debugging purposes we refer them to "[Debug Files](debug_files.0.11.1.html#debug-files-content)". 

To prepare project, click _Prepare project_ button in baking client window, and a separate window "Prepare project" shown in above image will pop up. Follow the instruction to prepare the baking input files.

{% include important.html content="Note there are two ways to create the files depending on the need of your project. Currently, if you want to bake objects that are runtime spawned, _Prepare project_ window does not support it, you need to enable _Export Scene in Runtime_ in Debug Settings. See [Creating Debug Files](debug_files.0.11.1.html#creating-debug-files) for detailed instruction." %}

 
### Step 3: Baking

Once _Prepare project_ is finished by clicking _Finish_ button, you can come back to main baking client window, and click "Create Grasps for project" to upload your package to the Gleechi Cloud baking server and trigger a bake. A window will appear to inform you about the process. Expect about 1-2 minutes for a common bake. After finishing, the grasp baking .db file will be downloaded into your project folder.