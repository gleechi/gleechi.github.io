---
title: VG_BakingClient Component
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar_0_9_6
permalink: unity_component_vgbakingclient.0.9.6.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_menu_bakingclient.png" alt="VG_BakingClient menu." caption="VG_BakingClient can be found in the VirtualGrasp/Components menu." %}

## Description

The VG_BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of object baking, please read the [object baking documentation](object_baking.0.9.6.html) first.

Before you can upload the input to the Baking Service, you need to create it by following the instructions on [Debug Files](debug_files.0.9.6.html).

{% include editor_script.html %}

{% include image.html file="knowledge/baking_pipeline.png" alt="Baking Pipeline." caption="Baking Pipeline" %}

## VG_BakingClient

{% include image.html file="unity/unity_vg_baking_client.png" alt="VG Baking Client in Unity." caption="VG_BakingClient in Unity." %}

<!--{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}-->

### Step 1: Authentication

After signing up to the Cloud Baking Service, you should have received credentials (email address and password). After entering them once, your credentials will be stored in a file called vg_cabvg_settings.json in your project folder, so you won't have to re-enter them all the time.

Check if your credentials are valid by trying to "Login." If successful, a window will appear telling you that you logged in successfully.

### Step 2: Preparation

Clicking "Prepare Project" will mainly verify that you have the necessary input data prepared for an upload. If the input is valid, a window will appear telling you how many objects are going to be baked.

### Step 3: Baking

Clicking "Create Grasps for project" will upload your package to the Gleechi Cloud baking server and trigger a bake. A window will appear to inform you about the process. Expect about 1-2 minutes for a common bake. After finishing, the grasp baking .db file will be downloaded into your project folder.