---
title: VG_BakingClient Component
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar
permalink: unity_component_vgbakingclient.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_statevisualizer_menu.png" alt="VG_BakingClient menu." caption="VG_BakingClient can be found in the VirtualGrasp/Components menu." %}

{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}

## Description

The VG_BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of object baking, please read the [object baking documentation](object_baking.html) first.

{% include image.html file="unity/unity_vg_baking_client.png" alt="VG Baking Client in Unity." caption="VG_BakingClient" %}

{% include editor_script.html %}

## Upload Input

To upload the files for a bake:

* First, create a package of the necessary inputs for the bake (this is equivalent to creating the [debug files](debug.files)).
* Insert the **SitePath** (provided to you with your license). The site path is the server address.
* Insert the **ApiKey** (provided to you with your license). The api key is an identifier to access the service.
* Enter your **email** address (to which you want to get notifications).
* Select the target **platform**.
* Click **"Upload"**

Note that as soon as you close the window, your settings will be stored in a file called vg_cabvg_settings.json in your project folder, so you won't have to re-enter them all the time (since when you open the window, the settings will be loaded).

After clicking Upload, the server will receive the package and trigger a bake, and you should get a notification mail.

Now you have to wait (depending on the number of objects and their complexity).

## Target Platform

Selecting **"Windows"** as the target platform is the default. "Download" will provide you with a .DLL file and enable natural grasps in your Editor, as well as in Windows builds.

Select **"Android"** as the target platform if you have tested your Windows solution properly. "Download" will provide you with an .SO file to download and enable natural grasps in your Android builds (such as for Quest, Pico, etc.).


## Download Output

You can either download the product of the bake, rename it and sort it in the Unity plugin folder yourself, or you can copy the download link, paste it in the DownloadURL field of the VG_BakingClient and click "Download." 

The VG_BakingClient will identify itself how to rename and where to place the file.

* An .SO file (for Android/Quest) should become Plugins/Android/libvirtualgrasp-selection.so
* A .DLL file (Windows) should become Plugins/x86_64/virtualgrasp-selection.dll

This should have finalized the process and you will be able to enjoy natural grasps of your interactable objects.