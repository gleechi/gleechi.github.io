---
title: VG_EC_Oculus controller
keywords: external-controller
sidebar: main_sidebar_1_6_0
permalink: unity_vg_ec_oculus.1.6.0.html
folder: mydoc/external_controllers
---

## Description 

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.6.0.html) on the purpose of a VG_ExternalController." %}

## Setup 

This is an external controller class that supports the Oculus Finger Tracking controller as an external controller.

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_OCULUS_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation)." %}

The following requirements have to be met to be able to use this controller:

 * You have the [Oculus SDK](https://www.oculus.com/setup/) installed on your computer.
 * You have the [Oculus Integration Plugin](https://developer.oculus.com/downloads/package/unity-integration/) imported into your Unity project.
 * You have the same Oculus Integration plugin version as the one on your headset and the Oculus App.
 * You use Oculus through "Legacy OVR" (Oculus -> Tools -> OVR Utilitites Plugin -> Set OVR to Legacy LibOVR). 
 * You have setup the AndroidManifest.xml properly, i.e. it needs to include<br>
 
	```js
	<uses-permission android:name="com.oculus.permission.HAND_TRACKING" />
	<uses-feature android:name="oculus.software.handtracking" android:required="false" />
	````
* You may optionally also add the following into the AndroidManifest.xml to use V2.0 of Oculus finger tracking:
	```js
	<meta-data android:name="com.oculus.handtracking.version" android:value="V2.0" />
	````

## Controller Profile

If these requirements are met, you will be able to use the **VG_CP_Oculus.OVRLib.HandTracking** controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.6.0.html#profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_oculus.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through OVR controller system, such as OVRPlugin.Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
