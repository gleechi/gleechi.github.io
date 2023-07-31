---
title: Controllers
sidebar: main_sidebar_1_4_0
version: 1.4.0
keywords: controller, internal, external
permalink: controllers.1.4.0.html
folder: knowledge
toc: true
---
## Background

{% include callout.html content="In VirtualGrasp we use the terms sensor and controller exchangeably since a VR controller is essentially a sensing device for hand poses." %}

VirtualGrasp is hardware-agnostic. 

You can use VirtualGrasp with or without a VR headset and your scene does not need to be a VR-enabled scene. 

In terms of hand control, VirtualGrasp can create natural [grasp interactions](grasp_interaction.1.4.0.html) with any kind of controllers (or {% include tooltip.html tooltip="Sensor" text="sensors" %}), whether it is hand-held VR controllers that gives accurate 6-dof wrist pose, finger tracking devices like Leap Motion or Oculus finger tracking feature, or or even just a computer mouse. 

This is because unlike many physics-based grasp synthesis solutions in the market that require accurate finger tracking, VirtualGrasp exploits "object intelligence". By analyzing shape and affordances of an object model in VR, we can synthesize {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} on a hand with just the knowledge of where the wrist is, and without any dependence of expensive physical simulations. 

## How to Setup


VirtualGrasp allows you to assign upto two types of {% include tooltip.html tooltip="Sensor" text="sensors" %} for an avatar. 
This allows developers to combine two sensors to control avatar's hands. For example you can choose to use a data glove to control avatar's finger pose and grasp triggers, while using an Oculus touch controller to control wrist position and orientation. Though this is not most common setup for today's development use cases, this feature may become useful expecially for research and development of new hand controllers. 

In the majority of use cases only one primary sensor is used. 


Whether it is Unity or Unreal, you can assign your controller input in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html#avatars-and-sensors) → Avatars → Primary and Secondary Sensor Setup. 

{% include image.html file="unity/unity_vg_myvirtualgrasp_1_4_0.png" alt="Avatar and Sensor setup in Unity." caption="Avatar and Sensor setup in Unity." %}

### Controller Profile

Whether it is Unity or Unreal, in Sensor Setup, _Profile_ option allows you to select the "controller profile" for that sensor (primary or secondary). You are able to configure a number of controller-related settings and thereyby allow you to quickly switch between different controller inputs, such as UnityXR (e.g. supporting Quest), LeapMotion, Mouse, and others.

A set of ready-to-use controllers is explained in on the [VG_ExternalControllerManager](http://localhost:4000/unity_component_vgexternalcontrollermanager.1.4.0.html#vg_externalcontroller-class) page. 

{% include image.html file="unity/unity_vg_ec_unityxr.png" alt="VG Controller profile in Unity." caption="VG Controller profile as scriptable object in Unity." %}

 Elements of VG_ControllerProfile are explained in this table: 

<!--{% include image.html file="unity/unity_vg_sensor.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}-->

| Option | Description |
|-------|--------|--------|
| External Type| name of the external controller, as a string, so one can write your own external controller. Note, here we supports adding a list of controller names, separated by ';', in order of priorization. E.g. "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.|  
| Control |  specify what this sensor element controls. If you added two sensors, then one could control wrist position, rotation and  haptics, another controls fingers and grasp for example.| 
| Finger Control Type |  specify how sensor controls the finger motion. See [Finger Control Type](virtualgrasp_unityapi.1.4.0.html#vg_fingercontroltype). | 
| Offset Position<br>Offset Rotation |  when the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust the offset to synchronize them. Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.| 
| Origin Name | set this to the GameObject name that should act as the origin of your controller data. For example, "XRRig" for the default Unity XR Rig (unless you renamed it). If no GameObject with this name is found (or you leave it empty), the origin will be the zero-origin.<br><br>To overwrite this behavior, you can use the [Origin](#origin) field as described below.| 
| Origin Scale | you can add a scale multiplier to the sensor data if you like. The default is (1,1,1). | 
| Hand Mappings | you can find a more detailed documentation on [Controller Axis Mappings](avatars.1.4.0.html#controller-axis-mappings). | 

{% include image.html width = "60" file="knowledge/3D_Cartesian_Coodinate_Handedness.jpg" alt="LHS/RHS" %} <figcaption>The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand.<br>Source: Original by <a href="https://commons.wikimedia.org/wiki/File:3D_Cartesian_Coodinate_Handedness.jpg">PrimalShell</a>, <a href="https://en.wikipedia.org/wiki/en:Creative_Commons">Creative Commons</a> <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">Attribution-Share Alike 3.0 Unported</a> license.</figcaption>


<!--| Finger Control Type | Description |
|-------|--------|
| BY_SENSOR_FULL_DOFS | for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. | 
| BY_SENSOR_LOW_DOFS| for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path | 
| BY_ANIMATION | for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation. | 
| BY_OSCILLATED_ANIMATION | will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (Experimental) | 
| BY_EXTERNAL | only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs. | -->


### Origin

While each VG_ControllerProfile contains an "Origin Name" that should act as the origin of your controller data, you can overwrite the origin by selecting a different transform here. 

<!-- Moved these commented texts from External controller manager page to here. 
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

For Unity, the basic VG_ExternalController "UnityXR" is using Unity's [UnityXR](https://docs.unity3d.com/2019.1/Documentation/Manual/xr_input.1.4.0.html) API to provide the wrist pose and a trigger signal to VG.

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