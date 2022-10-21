---
title: VG_EC_OculusHand controller
keywords: external-controller
sidebar: main_sidebar_1_0_0
permalink: unity_vg_ec_oculushand.1.0.0.html
folder: mydoc/external_controllers
---

## Description 

{% include external_controller.html %}

## Setup 

This is an external controller class that supports the Oculus Finger Tracking controller as an external controller.

{% include important.html content="After assuring that the following conditions are met, you have to add the scripting define symbol **VG_USE_OCULUS_CONTROLLER** to your Unity player settings (Project Settings → Player → Script Compilation) OR activate the same define in VG_EC_OculusHand.cs." %}

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

If these requirements are met, you will be able to use the "VG_EC_OculusHand" controller profile to setup your [MyVirtualGrasp](unity_component_myvirtualgrasp.1.0.0.html#controller-profile) configuration (otherwise an error will appear on the console).

{% include image.html file="unity/unity_vg_ec_oculushand.png" alt="VG Controller profile in Unity." caption="VG Controller profile in Unity." %}

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through OVR controller system, such as OVRPlugin.Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
