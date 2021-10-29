---
title: VG_BakingClient Component
#tags: [getting_started]
keywords: component, baking, objectbaking, baking-client
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vgbakingclient.html
folder: mydoc
---

@kai update regarding output will not be dll anymore, but encripted db.

### VG_BakingClient 

You will be able to request [object baking](object_baking.html) by connecting to Gleechi's 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.CABVG}}">CABVG</a> 
 server through a GUI interface -- VG_BakingClient -- that is part of the SDK. You can find it in the VirtualGrasp menu:

{% include image.html file="unity/unity_vg_baking_client.png" alt="VG Baking Client in Unity." caption="VG_BakingClient" %}

### Upload Input

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

### Target Platform

Selecting **"Windows"** as the target platform is the default. "Download" will provide you with a .DLL file and enable natural grasps in your Editor, as well as in Windows builds.

Select **"Android"** as the target platform if you have tested your Windows solution properly. "Download" will provide you with an .SO file to download and enable natural grasps in your Android builds (such as for Quest, Pico, etc.).


### Download Output

You can either download the product of the bake, rename it and sort it in the Unity plugin folder yourself, or you can copy the download link, paste it in the DownloadURL field of the VG_BakingClient and click "Download." 

The VG_BakingClient will identify itself how to rename and where to place the file.

* An .SO file (for Android/Quest) should become Plugins/Android/libvirtualgrasp-selection.so
* A .DLL file (Windows) should become Plugins/x86_64/virtualgrasp-selection.dll

This should have finalized the process and you will be able to enjoy natural grasps of your interactable objects.