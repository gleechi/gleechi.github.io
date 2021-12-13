---
title: VG_ExternalControllerManager Component
keywords: component, external-controller manager
sidebar: main_sidebar
permalink: unity_component_vgexternalcontrollermanager.html
folder: mydoc
---

## Description 

VG_ExternalControllerManager is a static class representing the controller abstraction towards VirtualGrasp. 

It should be used in any VG_MainScript, such as [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.html), where it is initialized after the VG_Controller itself initialized:

```js
override public void Awake()
{
    base.Awake();
    VG_Controller.Initialize();
    VG_ExternalControllerManager.Initialize(this);
}
````

VG_ExternalControllerManager.cs is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} so that is is extendable, for example to add more controllers or functionalities.

In most cases, the source is a plugin provided by the hardware manufacturer for your engine of choice.

The VG_ExternalControllerManager is managing different VG_ExternalControllers. 
<!-- For more background information, please refer to the [Controller](controllers.html) explanation. -->
We call it **external controllers**, because an external source or plugin is providing VirtualGrasp with the input data in Unity (but external to VirtualGrasp). In contrast to this are **internal controllers** that link the native library directly to VirtualGrasp. Internal controllers are by default not supported for the VirtualGrasp SDK, due to third-party distribution regulations.

Thus, whenever we speak of controllers or sensors in this documentation, we refer to external controllers.

{% include image.html file="knowledge/external_controllers.png" alt="Internal controllers." caption="External controller pipeline." %}

## VG_ExternalController Class

To link together a controller plugin with VG, the VirtualGrasp SDK provides a base class 
VG_ExternalController together with a few ready-to-use child classes for the following
controllers:

* [VG_MouseHand](unity_vg_ec_mousehand.html) for Mouse control.
* [VG_UnityXRHand](unity_vg_ec_unityxrhand.html) for all XR controllers that are supported through [UnityXR](https://docs.unity3d.com/Manual/XR.html).
* [VG_OculusHand](unity_vg_ec_oculushand.html) for Oculus Finger Tracking which is supported through the Oculus SDK.
* [VG_MouseHand](unity_vg_ec_leaphand.html) for LeapMotion controller which is supported through the Ultraleap SDK.
* [VG_GenericHand](unity_vg_ec_generichand.html) as a fallback solution.

While all these classes can serve as tutorials to understand how a VG_ExternalController can be setup, please refer to each particular page for further details on just that particular controller.

<br>

{% include youtube.html id="hNa2o7ngctU" caption="Switching between different external controllers using the VGs AutoSetup functionality." %}

## Modifying or Writing a Controller

The following we describe technical considerations that you may have when you modify or write your own VG_ExternalController. You may especially end up here if you try to use your own, customized hand model for your application. Note that "SDK" in this case refers to the particular controller plugin (such as Oculus SDK, Ultraleap SDK, etc.).

### Initialization and Mapping

Each VG_ExternalController has to include a VG_ExternalControllerMapping that maps the bone indices provided by the SDK to VirtualGrasp. The VG_ExternalControllerMapping includes variables for 16 bones (1 wrist + 5 * 3 finger bones). The VG_ExternalControllerMapping should be initialized in the VG_ExternalController Initialization function.

### Computation

### Coordinate-Frame Corrections
