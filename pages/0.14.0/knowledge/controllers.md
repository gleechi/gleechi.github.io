---
title: Controllers
sidebar: main_sidebar_0_14_0
version: 0.14.0
keywords: controller, internal, external
permalink: controllers.0.14.0.html
folder: knowledge
toc: true
---
## Background

{% include callout.html content="In VirtualGrasp we use the terms sensor and controller exchangeably since a VR controller is essentially a sensing device for hand poses." %}

VirtualGrasp is hardware-agnostic. 

You can use VirtualGrasp with or without a VR headset and your scene does not need to be a VR-enabled scene. 

In terms of hand control, VirtualGrasp can create natural [grasp interactions](grasp_interaction.0.14.0.html) with any kind of controllers (or {% include tooltip.html tooltip="Sensor" text="sensors" %}), whether it is hand-held VR controllers that gives accurate 6-dof wrist pose, finger tracking devices like Leap Motion or Oculus finger tracking feature, or or even just a computer mouse. 

This is because unlike many physics-based grasp synthesis solutions in the market that require accurate finger tracking, VirtualGrasp exploits "object intelligence". By analyzing shape and affordances of an object model in VR, we can synthesize {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} on a hand with just the knowledge of where the wrist is, and without any dependence of expensive physical simulations. 

## How to Setup
Whether it is Unity or Unreal, you can assign your controller input in MyVirtualGrasp → Sensors. 
See [AutoSetup & Sensors](unity_component_myvirtualgrasp.0.14.0.html#autosetup--sensors) to learn how to setup your sensors in Unity. A set of ready-to-use controllers is explained in [VG_ExteralController Class](http://localhost:4000/unity_component_vgexternalcontrollermanager.0.14.0.html#vg_externalcontroller-class). 


<!--
{% include image.html file="unity/unity_control_flags.png" alt="VG control flags." caption="VG Control Flags" %}

There are a few controllers that are supported "out of the box" by VirtualGrasp, called INTERNAL_CONTROLLERs, which means that no additional Unity plugins are needed. However in the released VG SDK, INTERNAL_CONTROLLERS option is turned off. EXTERNAL_CONTROLLERs are enabled through separate Unity plugins, and are the default sensor type.

There are a few controllers that are supported "out of the box" by VirtualGrasp, called INTERNAL_CONTROLLERs, which means that no additional engine plugins are needed. 
Since VirtualGrasp internally takes care of them, we call them "internal controllers." All of the sensor options (such as LEAP in the image above), except EXTERNAL_CONTROLLER are internal controllers.

## Internal Controllers

To use some of the supported internal controllers, you will still need to install the main software on your computer (such as Leap SDK for Leap, Oculus App for Oculus, SteamVR for OpenVR, etc), but as a main feature, you will not need to take any further action in your game project.

This is because VG comes on demand with working native libraries for each supported internal controller. VG takes care of extracting input data from the native libraries and directly reflects it on the hand. The data is then represented as hand animation in the engine.

{% include image.html file="knowledge/internal_controllers.png" alt="Internal controllers." caption="Internal controller pipeline." %}

If your version does not support a controller, you will receive an error message like the following:

{% include image.html file="knowledge/controller_not_supported.png" alt="VG control flags." caption="" %}

Sometimes, you may end up in a situation where you cannot use an internal controller:

1. Your input is not available as an internal controller in VG, either because it's not feature-enabled or because it is not integrated.
1. Not all providers provide all configurations of native libraries (for example, LeapMotion does not have Android support).
1. It can be troublesome for platforms to load native library dependencies in runtime (such as Android on Quest).
1. You have proprietary input hardware where native libraries cannot be shared (fallback to problem 1.) or are not available (but rather managed, java, etc).
1. You want to have full control of the input data.

## External Controllers

For these cases, we have enabled a generic EXTERNAL_CONTROLLER interface.

It is called external, because - instead of an internal native library - an external source is feeding VG with the input data. In most cases, this external source is a plugin provided by the hardware manufacturer for your engine of choice.

{% include image.html file="knowledge/external_controllers.png" alt="Internal controllers." caption="External controller pipeline." %}

### Considerations

When installing a controller plugin into your project, the same native libraries will be placed somewhere on your system, most probably as part of the plugin that you installed into your project. With the plugin, a number of components, scripts, tutorials, etc may also be installed. Since you may not use many of them, this may be an **overhead to take**.

Using a component, script, or prefab, the plugin will follow to allow you to control a pair of hands. Often, only a **particular hand model** that comes with the plugin is supported out of the box (with fixed assumptions on the rig), and mostly this hand is directly controlled by the plugin during runtime. 

To provide best usability for full finger control, VG's external controller does not take the raw sensor input as an input (because there is no standard between different plugins), but works as a filter on the bone animation. The plugin will be used to extract the hand bones, and VG will receive and adjust it, before rendering.

Sometimes, the dependencies in the provided scripts/components/prefabs between the hand model, the data, the plugin, the overhead, etc, are so strong, that you might still want to (or have to) write **customized script** just using the plugin API. 

This means that you have to also gather a **holistic understanding**, covering the different APIs (components, scripts, APIs, etc). So, before you actually get up and running, you have to do a bit of reading, and it becomes less plug & play.

Finally, there are a **number of engineering issues** that may decrease plug&play further, such as that you have to

* handle more complex dependencies and runtime issues, such as when to update the hand model, or when to send the data into the library
* maintain potential future changes of the third party plugin provider, such as LeapMotion greatly refactored their API between two major versions 3 and 4, 
* handle very different geometrical representations (some APIs use global poses, some local poses, some angles; some APIs use left hand system, some right hand, ...),
* parameterize or adjust your script for every new hand model, since there is no standard for hand rigging in terms of the geometrical representations mentioned above.

Finally, all plugins are **engine specific**, so if you are using other engines beside Unity, you would have to do all this for both engines separately, at a risk that some plugins may not be available or work differently on different engines.

### VG_ExternalControllerManager

In order to reduce the effect of these considerations, and provide a better plug&play experience for external controller input, we provide a sample script, called VG_ExternalControllerManager and a number of VG_ExternalControllers that can be managed with it.

For Unity, the basic VG_ExternalController "UnityXR" is using Unity's [UnityXR](https://docs.unity3d.com/2019.1/Documentation/Manual/xr_input.0.14.0.html) API to provide the wrist pose and a trigger signal to VG.

<table border="1">
<thead>
<tr class="header">
<th colspan="3">Basic example using a plugin and direct data</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">UnityXR</td>
<td markdown="span">Wrist, trigger</td>
<td markdown="span">Unity XR controller abstraction, included in Unity since 2019.1; used for Quest / Touch</td>
</tr>
</tbody>
</table>

What this means is that the whole sensor processing is done through Unity/UnityXR, and VG is functioning as a filter on that signal between the sensor and the hand motion. No additional native libraries are needed, and since Unity and VG support both Windows and Android, you can run the same project in the Editor, on Windows and on the Quest without adaptations.

We also include integrations for some "full-pose" external controllers (which are those that also communicate finger tracking data) that we have been working with: 

<table border="1">
<thead>
<tr class="header">
<th colspan="4">Expansions dependent on customized hand controller</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">LeapHand</td>
<td markdown="span">Full hand</td>
<td markdown="span">LeapMotion SDK / API used for Finger Tracking.</td>
<td markdown="span">VG_EC_LeapHand.cs</td>
</tr>
<tr>
<td markdown="span">QuestHand</td>
<td markdown="span">Full hand</td>
<td markdown="span">OculusVR plugin / OVRPlugin API used for Quest Finger Tracking.</td>
<td markdown="span">VG_EC_OculusHand.cs</td>
</tr>
</tbody>
</table>

As mentioned earlier, for each of them, you also need to install a specific plugin into Unity (see table). VG then does not take the raw sensor input as an input, but works as a filter on the bone animation. To address some of the considerations mentioned in the section above, we provide mapping components (right column). Using the minimal APIs and some help of the VG plugin, those mapping components are configured automatically, they update the hand bones according to the sensor input, and then provide the full bone configuration to VG, which in turn updates the hand bones once again to the final hand configuration.

{% include important.html content="Due to the different geometric representations in the sensor API and the hand models, all mapping components are made to work with the Oculus hands. If you want to use other hands, you have to adapt the scripts." %}


## Known Issues

Full-hand external controllers do not work when using VirtualGrasp inside a remote package (due to package dependencies). You need to have VirtualGrasp installed inside the project from a .unitypackage.
-->