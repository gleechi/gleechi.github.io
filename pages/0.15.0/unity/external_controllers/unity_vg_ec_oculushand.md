---
title: VG_EC_OculusHand controller
keywords: external-controller
sidebar: main_sidebar_0_15_0
permalink: unity_vg_ec_oculushand.0.15.0.html
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
 * You have setup the AndroidManifest.xml properly, i.e. it needs to include<br>
 
	```js
	<uses-permission android:name="com.oculus.permission.HAND_TRACKING" />
	<uses-feature android:name="oculus.software.handtracking" android:required="false" />
	````
* You may optionally also add the following into the AndroidManifest.xml to use V2.0 of Oculus finger tracking:
	```js
	<meta-data android:name="com.oculus.handtracking.version" android:value="V2.0" />
	````

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through OVR controller system, such as OVRPlugin.Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
