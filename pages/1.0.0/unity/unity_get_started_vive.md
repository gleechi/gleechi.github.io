---
title: Getting Started in Unity - Vive Setup
#series: "Getting Started in Unity series 1.0.0"
#weight: 1
sidebar: main_sidebar_1_0_0
permalink: unity_get_started_vive.1.0.0.html
folder: mydoc
toc: false
---

To use the Vive Focus with VG in your project, we recommend to use the [Wave XR Plugin](https://hub.vive.com/storage/docs/en-us/UnityXR/UnityXRGettingStart.html) for Unity, which will connect to [UnityXR](https://docs.unity3d.com/Manual/XR.html). We also recommend to use Wave XR's [DirectPreview](https://hub.vive.com/storage/docs/zh-tw/UnityXR/UnityXRDirectPreview.html) which allows you to run your project with VR in the Unity Editor without the need of building an apk (like Oculus Link).

We will guide you through the main steps to set this up:

## Setup a scoped registry to register the Wave XR Plugin server

Got to "Edit -> Project Settings -> Package Manager" and add a scoped registry as below.
{% include image.html file="unity/vive/vive_1_package.png" alt="Vive scoped registry." caption="Setup a scoped registry in Unity." %}

## Install the Wave XR Plugin

Navigate to "Window -> Package Manager" and choosing "My Registries." You will now see a number of packages that are now available through the scoped registry. Install the "Vive Wave XR Plugin".
{% include image.html file="unity/vive/vive_2_install.png" alt="Installing the Wave XR Plugin" caption="Install WaveXR for Unity." %}

## Enable the Wave XR Plugin

Navigate to "Edit -> Project Settings -> XR Plug-in Management." You will now see "WaveXR" as a plugin provider for UnityXR. Enable it both for Windows as well as on the Android tab.
{% include image.html file="unity/vive/vive_3_xrplugin.png" alt="Enable WaveXR" caption="Enable WaveXR as a plugin provider for UnityXR." %}

## Configure the Wave XR Plugin

During the earlier steps the Wave XR configuration dialog should have popped up. Accept All. 

If the dialog did not pop up, you have probably selected the Windows platform. Navigate to "File -> Build Setting," select "Android" as your platform and click "Switch Platform." Now the dialog should appear. Accept All. 
{% include image.html file="unity/vive/vive_4_config.png" alt="Configure WaveXR" caption="Configure the WaveXR plugin for Unity." %}

## Configure and Use DirectPreview

Under "Wave -> Direct Preview" enable "DirectPreview." Then, open the "ControlPanel."

If you have a cable connected your Vive headset with a USB cable to your computer, select USB, then:

{% include image.html file="unity/vive/vive_5_directpreview.png" alt="Setup DirectPreview" caption="Setup DirectPreview to test WaveXR in Unity Editor." %}

1. "Install the Device APK" onto your headset (you only need to do this once). This will install the "DirectPreviewUnity" app on your headset.
2. When you want to start your app, "Start the Device APK" in the ControlPanel. In your headset it will show "Connecting."
3. Quickly after (the headset may timeout otherwise), start your Unity project. You will not see anything in the headset, but you need to cover the proximity sensor to keep the apk running.

## Using VirtualGrasp

When using VirtualGrasp, assure that in your "MyVirtualGrasp" script, you are using the "VG_EC_UnityXRHand" controller profile, and you will able to use VirtualGrasp with your Vive headset.

{% include image.html file="unity/vive/vive_6_play.png" alt="VirtualGrasp" caption="VirtualGrasp running with WaveXR plugin and DirectPreview in Unity." %}
