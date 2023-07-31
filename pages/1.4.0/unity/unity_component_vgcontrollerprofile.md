---
title: VG_ControllerProfile
keywords: component
sidebar: main_sidebar_1_4_0
permalink: unity_component_vgcontrollerprofile.1.4.0.html
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

To link together a controller plugin with VG, the VirtualGrasp SDK provides a base class VG_ExternalController. 

The VirtualGrasp SDK already includes a few ready-to-use child classes for the
controllers listed below. For each controller, you will also find its [VG_ControllerProfile](controllers.1.4.0.html#controller-profile) as a scriptable object.

* [VG_EC_Mouse](unity_vg_ec_mouse.1.4.0.html) for Mouse control.
* [VG_EC_Script](unity_vg_ec_script.1.4.0.html) for control from other scripts.
* [VG_EC_Leap](unity_vg_ec_leap.1.4.0.html) for LeapMotion controller which is supported through the [Ultraleap](https://developer.leapmotion.com/unity) API.
* [VG_EC_Manus](unity_vg_ec_manus.1.4.0.html) for Manus Finger Tracking which is supported through the [Manus Core SDK](https://documentation.manus-meta.com/v2.1.0/unity-plugin/index.html).
* [VG_EC_Oculus](unity_vg_ec_oculus.1.4.0.html) for Oculus Finger Tracking which is supported through the [Oculus](https://developer.oculus.com/downloads/package/unity-integration/) API.
* [VG_EC_OVR](unity_vg_ec_ovr.1.4.0.html) for Oculus Finger Tracking which is supported through the OVRHand component of the [Oculus](https://developer.oculus.com/downloads/package/unity-integration/).
* [VG_EC_Steam](unity_vg_ec_steam.1.4.0.html) for all XR controllers that are supported through [SteamVR](https://valvesoftware.github.io/steamvr_unity_plugin/index.html) API.
* [VG_EC_UnityXR](unity_vg_ec_unityxr.1.4.0.html) for all XR controllers that are supported through the [UnityXR](https://docs.unity3d.com/Manual/XR.1.4.0.html) API.
* [VG_EC_UnityXRHands](unity_vg_ec_unityxrhands.1.4.0.html) for all XR controllers that are supported through the [Unity XRHands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.1/manual/index.html) API.
* [VG_EC_UnityInteraction](unity_vg_ec_unityinteraction.1.4.0.html) for all XR controllers that are supported through the [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/xr-controller-action-based.html) API.
* [VG_EC_Generic](unity_vg_ec_generic.1.4.0.html) as a fallback solution.

While all these classes can serve as tutorials to understand how a VG_ExternalController can be setup, please refer to each particular page for further details on just that particular controller.

<!--
{% include important.html content="The video below shows the old layout of Sensors -> Avatars, while currently is Avatars -> Sensors. However the content regarding the controller profiles are still valid." %}

<br>
{% include youtube.html id="Z-yjd1muM44" caption="Switching between different external controllers using VG_ControllerProfiles." %}
-->
