---
title: VG_EC_OculusHand controller
keywords: external-controller
sidebar: main_sidebar_0_10_1
permalink: unity_vg_ec_oculushand.0.10.1.html
folder: mydoc/external_controllers
---

{% include external_controller.html %}

## Description 

This is an external controller class that supports the Oculus Finger Tracking controller as an external controller.

The following requirements have to be met to be able to enable the #define USE_OCULUS_CONTROLLER in the VG_EC_OculusHand.cs file and use the controller:
 * You have the [Oculus SDK](https://www.oculus.com/setup/) installed on your computer.
 * You have the [Oculus Integration Plugin](https://developer.oculus.com/downloads/package/unity-integration/) imported into your Unity project.
 * You have the same Oculus Integration plugin version as the one on your headset AND Oculus App.
 * You have setup the AndroidManifest.xml properly, i.e. they need to include<br>
 
	```js
 		\<uses-permission android:name="com.oculus.permission.HAND_TRACKING" /\><br>
 		\<uses-feature android:name="oculus.software.handtracking" android:required="false" /\>
	````

After this, use the "OCULUS_FT" option to [AutoSetup](unity_component_myvirtualgrasp.0.10.1.html#autosetup) your VG configuration.
 
## Functionality

### Hand Poses
All finger bones are mapped.

Will be controlled through OVR controller system, such as OVRPlugin.Skeleton.

### Grab Signals
will be controlled through the finger configuration (i.e. their state of bending).
