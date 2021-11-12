---
title: VG_BakingClient Component
keywords: component, baking, objectbaking, baking-client
sidebar: main_sidebar
permalink: unity_component_vgbakingclient.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_menu_bakingclient.png" alt="VG_BakingClient menu." caption="VG_BakingClient can be found in the VirtualGrasp/Components menu." %}

## Description

The VG_BakingClient is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that integrates the VirtualGrasp Cloud Baking Service ({% include tooltip.html tooltip="CABVG" text="CABVG" %}) into the Unity editor. 

If you are not familiar with the concept of object baking, please read the [object baking documentation](object_baking.html) first.

Before you can upload the input to the Baking Service, you need to create it by following the instructions on [Debug Files](debug_files).

{% include editor_script.html %}

## Create Input

Enabling "Save Debug Files" in your VG_MainScript and running the application will create a *[APP-IDENTITY].[APP-VERSION].zip* file in your project folder. 

For more information on the content and use cases of the *.zip* file, see [Debug Files Content](#debug-files-content).

## Upload Input

<!--{% include image.html file="unity/unity_vg_baking_client.png" alt="VG Baking Client in Unity." caption="VG_BakingClient" %}-->

{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}

To upload the files for a bake:

* Insert the **SitePath** (provided to you with your license). The site path is the server address.
* Insert the **ApiKey** (provided to you with your license). The api key is an identifier to access the service.
* Enter your **email** address (to which you want to get notifications).
* Click **"Upload"**

Note that as soon as you close the window, your settings will be stored in a file called vg_cabvg_settings.json in your project folder, so you won't have to re-enter them all the time (since when you open the window, the settings will be loaded).

After clicking Upload, the server will receive the package and trigger a bake, and you should get a notification mail.

Now you have to wait (depending on the number of objects and their complexity).

## Download Output

{% include warning.html content="CABVG is currently ongoing maintenance and an upgrade to version 2.0. It is therefore not available and the documentation below deprecated." %}

You can either download the product of the bake - which is an updated *[APP-IDENTITY].[APP-VERSION].db* file -, and sort it in your project folder yourself, or you can copy the download link, paste it in the DownloadURL field of the VG_BakingClient and click "Download." 

This should have finalized the process and you will be able to enjoy natural grasps of your interactable objects.