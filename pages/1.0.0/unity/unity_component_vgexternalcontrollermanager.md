---
title: VG_ExternalControllerManager Component
keywords: component, external-controller manager
sidebar: main_sidebar_1_0_0
permalink: unity_component_vgexternalcontrollermanager.1.0.0.html
folder: mydoc
---

## Description 

VG_ExternalControllerManager is a static class representing the controller abstraction towards VirtualGrasp. 

It should be used in any VG_MainScript, such as [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.1.0.0.html), where it is initialized after the VG_Controller itself initialized:

```js
override public void Awake()
{
    base.Awake();
    VG_Controller.Initialize();
    VG_ExternalControllerManager.Initialize(this);
}
````

VG_ExternalControllerManager.cs is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} so that it is extendable, for example to add more controllers or functionalities.

The VG_ExternalControllerManager is managing different VG_ExternalControllers. We call it **external controller**, because an external source or plugin is providing VirtualGrasp with the input data in Unity (but external to VirtualGrasp). In most cases, the source is a plugin provided by the hardware manufacturer for your engine of choice. 

In contrast to external controllers we term **internal controllers** as those that link the controllers native library directly to VirtualGrasp. Internal controllers are by default not supported for the VirtualGrasp SDK, due to third-party distribution regulations.

Thus, whenever we speak of controllers or sensors in this documentation, we refer to external controllers.

{% include image.html file="knowledge/external_controllers.png" alt="Internal controllers." caption="External controller pipeline." %}

## VG_ExternalController Class

To link together a controller plugin with VG, the VirtualGrasp SDK provides a base class 
VG_ExternalController. The VirtualGrasp SDK already includes a few ready-to-use child classes for the
controllers listed below. For each controller, you will also find its [VG_ControllerProfile](unity_component_myvirtualgrasp.1.0.0.html#profile), among others to configure its [Controller Axis Mapping](axis_mappings.1.0.0.html#controller-axis-mapping).


* [VG_EC_MouseHand](unity_vg_ec_mousehand.1.0.0.html) for Mouse control.
* [VG_EC_UnityXRHand](unity_vg_ec_unityxrhand.1.0.0.html) for all XR controllers that are supported through the [UnityXR](https://docs.unity3d.com/Manual/XR.1.0.0.html) API.
* [VG_EC_UnityInteractionHand](unity_vg_ec_unityinteractionhand.1.0.0.html) for all XR controllers that are supported through the [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/xr-controller-action-based.html) API.
* [VG_EC_SteamHand](unity_vg_ec_steamhand.1.0.0.html) for all XR controllers that are supported through [SteamVR](https://valvesoftware.github.io/steamvr_unity_plugin/index.html) API.
* [VG_EC_OculusHand](unity_vg_ec_oculushand.1.0.0.html) for Oculus Finger Tracking which is supported through the [Oculus](https://developer.oculus.com/downloads/package/unity-integration/) API.
* [VG_EC_LeapHand](unity_vg_ec_leaphand.1.0.0.html) for LeapMotion controller which is supported through the [Ultraleap](https://developer.leapmotion.com/unity) API.
* [VG_EC_GenericHand](unity_vg_ec_generichand.1.0.0.html) as a fallback solution.

While all these classes can serve as tutorials to understand how a VG_ExternalController can be setup, please refer to each particular page for further details on just that particular controller.

<br>
{% include youtube.html id="Z-yjd1muM44" caption="Switching between different external controllers using VG_ControllerProfiles." %}

<!--
## Modifying or Writing a Controller

The following we describe technical considerations that you may have when you modify or write your own VG_ExternalController. You may especially end up here if you try to use your own, customized hand model for your application. Note that "SDK" in this case refers to the particular controller plugin (such as Oculus SDK, Ultraleap SDK, etc.).

### Initialization and Mapping

Each VG_ExternalController has to include a VG_ExternalControllerMapping that maps the bone indices provided by the SDK to VirtualGrasp. The VG_ExternalControllerMapping includes variables for 16 bones (1 wrist + 5 * 3 finger bones). The VG_ExternalControllerMapping should be initialized in the VG_ExternalController Initialization function.

### Coordinate-Frame Corrections

If you use a custom hand rig different than the GleechiRig provided in the SDK, you may find the fingers of the hand bending along the wrong axis.

The reason for the mismatch is that each finger controller (for example, VG_EC_OculusHands.cs) is adjusting the raw finger orientations that come directly from the controller API (for example, from the Oculus Integration plugin) to match the hand model representation that is provided with the SDK.

In this case you have two options:

1. you can base or adjust your hand rig to the existing hand rig, keeping the coordinate-frame definition (e.g., y along the finger bone, x to the right, z towards the palm) as in the provided rig. This is some work for a 3D artist.

2. in the controller (such as VG_EC_OculusHands.cs), in the Compute() function, you will see that all the raw finger orientations are processed through the modifyPose() function. Each pose matrix is modified to a new rotation based on if it is wrist or finger and if it is left and right hand (these were the changes we needed for the provided hand model). This is some work for a programmer.

    1. In the optimal case that your hand model is aligned with finger tracking sensor data, just remove the two lines where modifyPose() is called.
    2. If that does not work that means your hand model is not aligned with the finger tracking sensor data and that you have to update the modifyPose() function. Enabling the DebugDraw() call just below the modifyPose() can help you by visualizing the skeleton and rotations.
-->