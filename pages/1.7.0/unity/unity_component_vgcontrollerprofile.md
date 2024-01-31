---
title: VG_ControllerProfile [Scriptable Object]
keywords: component
sidebar: main_sidebar_1_7_0
permalink: unity_component_vgcontrollerprofile.1.7.0.html
folder: mydoc
---

<!--
## Description 

A VG_ExternalController is a base class for different controllers. We call it **external controller**, because an external source or plugin is providing VirtualGrasp with the input data in Unity (but external to VirtualGrasp). In most cases, the source is a plugin provided by the hardware manufacturer for your engine of choice. 

In contrast to external controllers we term **internal controllers** as those that link the controllers native library directly to VirtualGrasp. Internal controllers are by default not supported for the VirtualGrasp SDK, due to third-party distribution regulations.

Thus, whenever we speak of controllers or sensors in this documentation, we refer to external controllers.

{% include image.html file="knowledge/external_controllers.png" alt="Internal controllers." caption="External controller pipeline." %}

## VG_ExternalController Class
-->

## Description

VirtualGrasp provides VG_ControllerProfiles (in Unity as ScriptableObjects) to configure a number of sensor-related settings and thereby allows you to quickly switch between different controllers.

{% include callout.html content="You only need to create a new instance of a VG_ControllerProfile if you integrate a new motion controller plugin into your game. You then need to configure the the mapping rotations for your new VG_ControllerProfile." %}

<!-- {% include image.html file="unity/unity_vg_ec_unityxrhands_1_4_0.png" alt="VG Controller profile in Unity." caption="Example of a VG_ControllerProfile as a scriptable object in Unity." %} -->

Examples for VG_CP_Unity.XRHands and VG_CP_Oculus.OVRLib.HandTracking:

| <img class="docimage" style="width:100%" src="images/unity/unity_vg_ec_unityxrhands_1_4_0.png"/> | <img class="docimage" style="width:100%" src="images/unity/unity_vg_ec_oculus.png"/> |

The elements of a VG_ControllerProfile are explained in this table: 

<!--{% include image.html file="unity/unity_vg_sensor.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}-->

| VG_ControllerProfile Field | Description |
|-------|--------|
| Url | (optional) A URL can be provided to a more detailed documentation of the controller that this VG_ControllerProfile relates to. Press enter twice in the text field to open the URL. |
| Controller Class(es) | name of one or more external controllers, as a string. Note, here we supports adding a list of controller classes (see below), separated by ';', in order of priorization. E.g. "VG_EC_Oculus;VG_EC_UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.|  
| Control | specify what this sensor element controls. If you added two sensors, then one could control wrist position, rotation and  haptics, another controls fingers and grasp for example.| 
| Finger Control Type | specify how sensor controls the finger motion. See [Finger Control Type](virtualgrasp_unityapi.1.7.0.html#vg_fingercontroltype). | 
| Offset Position<br>Offset Rotation |  when the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust the offset to synchronize them. Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.| 
| Origin Name | set this to the GameObject name that should act as the origin of your controller data. For example, "XRRig" for the default Unity XR Rig (unless you renamed it). If no GameObject with this name is found (or you leave it empty), the origin will be the zero-origin.<br><br>To overwrite this behavior, you can use the [Origin](unity_component_myvirtualgrasp.1.7.0.html#origin) field.| 
| Origin Scale | you can add a scale multiplier to the sensor data if you like. The default is (1,1,1). | 
| Rotation Types and Hand Mappings | Rotation Types and Hand Mappings define how this controller deviates in terms of bone pose orientations. You can find a more detailed documentation on these axis mappings [here](axis_mappings.1.7.0.html). |

## Ready-to-Use VG_ControllerProfiles and VG_ExternalController classes

To link together a controller plugin with VG, the VirtualGrasp SDK provides a base class VG_ExternalController. 

The VirtualGrasp SDK also already includes a few ready-to-use child classes for the
controller input methods listed below. For each controller, you will also find a [VG_ControllerProfile](controllers.1.7.0.html#controller-profile) as a scriptable object that enables the respective controller class.

| VG_ExternalController class | VG_ControllerProfile | Control hand motion by |
|-------|--------|--------|
| [VG_EC_Mouse](unity_vg_ec_mouse.1.7.0.html) | VG_CP_Common.Mouse | Mouse input |
| [VG_EC_Script](unity_vg_ec_script.1.7.0.html) | VG_CP_Common.Script | Unity scripts |
| [VG_EC_Leap](unity_vg_ec_leap.1.7.0.html) | VG_CP_UltraLeap.HandTracking | LeapMotion controller; [Ultraleap](https://developer.leapmotion.com/unity) API. |
| [VG_EC_Manus](unity_vg_ec_manus.1.7.0.html) | VG_CP_Manus.HandTracking | Manus Finger Tracking; [Manus Core SDK](https://documentation.manus-meta.com/v2.1.0/unity-plugin/index.html) |
| [VG_EC_Oculus](unity_vg_ec_oculus.1.7.0.html) | VG_CP_Oculus.OVRLib.HandTracking | Oculus Finger Tracking; [Oculus](https://developer.oculus.com/downloads/package/unity-integration/) API |
| [VG_EC_OVR](unity_vg_ec_ovr.1.7.0.html) | VG_CP_Oculus.OVRHand.HandTracking | Oculus Finger Tracking; OVRHand component; [Oculus](https://developer.oculus.com/downloads/package/unity-integration/) |
| [VG_EC_Steam](unity_vg_ec_steam.1.7.0.html) | VG_CP_Steam.HandTracking | OpenXR controllers; [SteamVR](https://valvesoftware.github.io/steamvr_unity_plugin/index.html) API |
| [VG_EC_UnityXR](unity_vg_ec_unityxr.1.7.0.html) | VG_CP_Unity.UnityXR | UnityXR controllers; [UnityXR](https://docs.unity3d.com/Manual/XR.html) API |
| [VG_EC_UnityXRHands](unity_vg_ec_unityxrhands.1.7.0.html) | VG_CP_Unity.XRHands | Unity XR Hands controllers; [Unity XRHands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.1/manual/index.html) API |
| [VG_EC_UnityXRInteraction](unity_vg_ec_unityxrinteraction.1.7.0.html) | VG_CP_Unity.XRInteraction | Unity XR Interaction controllers; [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/xr-controller-action-based.html) API |
| [VG_EC_Generic](unity_vg_ec_generic.1.7.0.html) | VG_CP_Common.Generic | Unity transforms / fallback solution |


<!--
{% include important.html content="The video below shows the old layout of Sensors -> Avatars, while currently is Avatars -> Sensors. However the content regarding the controller profiles are still valid." %}

<br>
{% include youtube.html id="Z-yjd1muM44" caption="Switching between different external controllers using VG_ControllerProfiles." %}
-->
