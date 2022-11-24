---
title: VG_EC_OculusHand controller
keywords: external-controller
sidebar: main_sidebar_0_13_0
permalink: unity_vg_ec_oculushand.0.13.0.html
folder: mydoc/external_controllers
---

## Description 

{% include callout.html content="This class represents a child class of VG_ExternalController.<br><br> If you haven't yet, have a short look at [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.0.13.0.html) on the purpose of a VG_ExternalController." %}

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

### AutoSetup

Finally, you can use the "OCULUS_FT" option to [AutoSetup](unity_component_myvirtualgrasp.0.13.0.html#autosetup) your VG configuration. For this controller, AutoSetup 

* will set "External" to "OculusHand"
* will set "FingerControlType" to "BY_SENSOR_FULL_DOFS"
* will set "Origin" to the transform called "XRRig"
* will set all "Offset" values to 0.

## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through OVR controller system, such as OVRPlugin.Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
