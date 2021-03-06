---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_15_0
permalink: unity_component_myvirtualgrasp.0.15.0.html
folder: mydoc
---

## Description

MyVirtualGrasp is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} inherited from VG_MainScript, which encodes the main functionality of VirtualGrasp, and is the main component that you need to add and configure in your project to enable VirtualGrasp.

In Unity, VG_MainScript inherits from Monobehavior so you can use it as a component on a GameObject.

On this page, we are going to describe all the major configuration options covered in MyVirtualGrasp.cs.

## Sensors & Controllers

{% include callout.html content="In VirtualGrasp we use the term sensor and controller exchangeably since a controller is essentially a sensing device for hand poses." %}

VirtualGrasp allows you to configure multiple {% include tooltip.html tooltip="Sensor" text="sensors" %} in an application. 

This allows developers to combine two sensors to control avatar's hands. For example you can choose to use a data glove to control avatar's finger pose and grasp triggers, while using an Oculus touch controller to control wrist position and orientation. Though this is not most common setup for today's development use cases, this feature may become useful expecially for research and development of new hand controllers. 

In the majority of use cases only 1 single sensor is used. 

As you can see in MyVirtualGrasp, **Sensors** is a list in the interface. The first sensor element is listed as **Element 0**. All of the sensor elements will share the same interface, so in the descriptions below, we will focus on the importance of each element for each Sensor.

{% include image.html file="unity/unity_vg_myvirtualgrasp_0_15_0.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}

<!--
{% include callout.html content="Pay attention to the Console in case there is anything you may need to take care of manually to complete the auto-setup process." %}

{% include important.html content="No matter if Sensors Size is 1 or 2, all the components under Control list should be checked by the combined sensors, and if 2 sensor elements are used, they should not both control same component. For example two sensors should not both control position of the hand." %}
-->

<!--
<div class="panel-group" id="accordion1">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapseOne1">Show Image</a>
            </h4>
        </div>
        <div id="collapseOne1" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <img src="/images/unity/unity_vg_myvirtualgrasp_0_10_1.png">
            </div>
        </div>
    </div>
</div>
-->

### Avatars

For each sensor, you can assign multiple avatars, though in most cases you will have only one avatar per sensor.

<!--{% include image.html file="unity/unity_vg_myvirtualgrasp_avatar.png" alt="Avatar configuration options in Unity." caption="Avatar configuration options in Unity." %}-->

| Option | Description | Supported VG Version|
|-------|--------|--------|
| Model | should be HUMANOID_HAND in most application use cases. There could also be robotic hand options, but they will not be discussed here. | All Versions|
| SkeletalMesh| used to provide a reference to the SkinnedMeshRenderer of the avatar that you have imported in your scene and which should be controlled by VG during runtime. | All Versions |
| Replay | enable this if you want to use this avatar for replay recorded sensor data, as explained in [Sensor Record and Replay](sensor_record_replay.0.15.0.html), or the [VG_Recorder Component](unity_component_vgrecorder.0.15.0.html). This is a feature that is not available in the free version. | Pro Version|
| Remote | This is a placeholder for advanced multiplayer support for hand interaction that we are working on towards a stable version.  This is a feature that is not available in the free version. | Pro Version |
| Physical | enable this if you want VG to create colliders for this avatar and enable the hand for physical interactions. NOTE: at the moment, this option is experimental and should not be used apart from testing.| All Versions |


<!--enable this if you want to use this avatar to reflect networked data (i.e. listening to another client over network in a multiplayer scenario), as explained in [Multiplayer Interaction](multiplayer_interaction.0.15.0.html), or the [VG_Networking Component](unity_component_vgnetworing.0.15.0.html).-->
<!--Check the **Replay** option if you want to use this avatar not for runtime-control, but for replaying recorded sensor data, as explained in [Sensor Record and Replay](sensor_record_replay.0.15.0.html), or the [VG_Recorder Component](unity_component_vgrecorder.0.15.0.html).-->

### Controller Profile

{% include image.html file="unity/unity_vg_ec_unityxrhand.png" alt="VG Controller profile in Unity." caption="VG Controller profile as scriptable object in Unity." %}

Through controller profiles (which are ScriptableObjects), you are able to configure a number of controller-related settings and thereyby allow you to quickly switch between different controller inputs, such as UnityXR (e.g. supporting Quest), LeapMotion, Mouse, and others. A number of common VG_ControllerProfile are part of the VG SDK and you can find them in __Resources/ExternalControllers__. Elements of each VG_ControllerProfile are explained in this table: 

<!--{% include image.html file="unity/unity_vg_sensor.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}-->

| Option | Description |
|-------|--------|--------|
| External Type| name of the external controller, as a string, so one can write your own external controller. Note, here we supports adding a list of controller names, separated by ';', in order of priorization. E.g. "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.|  
| Control |  specify what this sensor element controls. If you added two sensors, then one could control wrist position, rotation and  haptics, another controls fingers and grasp for example.| 
| Finger Control Type |  specify how sensor controls the finger motion. See [Finger Control Type](virtualgrasp_unityapi.0.15.0.html#vg_fingercontroltype). | 
| Offset |  when the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust the offset to synchronize them. Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.| 
| Origin Name | Set this to the GameObject name that should act as the origin of your controller data. For example, "XRRig" for the default Unity XR Rig (unless you renamed it). If no GameObject with this name is found (or you leave it empty), the origin will be the zero-origin. | 
| Origin Scale | You can add a scale multiplier to the sensor data if you like. The default is (1,1,1). | 

<!--| Finger Control Type | Description |
|-------|--------|
| BY_SENSOR_FULL_DOFS | for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. | 
| BY_SENSOR_LOW_DOFS| for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path | 
| BY_ANIMATION | for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation. | 
| BY_OSCILLATED_ANIMATION | will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (Experimental) | 
| BY_EXTERNAL | only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs. | -->

{% include image.html width = "60" file="knowledge/3D_Cartesian_Coodinate_Handedness.jpg" alt="LHS/RHS" %} <figcaption>The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand.<br>Source: Original by <a href="https://commons.wikimedia.org/wiki/File:3D_Cartesian_Coodinate_Handedness.jpg">PrimalShell</a>, <a href="https://en.wikipedia.org/wiki/en:Creative_Commons">Creative Commons</a> <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">Attribution-Share Alike 3.0 Unported</a> license.</figcaption>

<!--
## Object Identifiers

{% include image.html file="unity/unity_vg_object_identifiers.png" alt="VG object identifiers." caption="VG object identifiers" %}

VirtualGrasp is using names to identify which objects are marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. You can customize component and layer names in MyVirtualGrasp ??? Object Identifiers. 
[VG_Articulation](unity_component_vgarticulation.0.15.0.html) component is a default entry, but this method also allows you to quickly adjust your project if you already have a layer or a component that marks your {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects.

Once an object is marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}, it will be supported by VG's [grasp](grasp_interaction.0.15.0.html) and [push](push_interaction.0.15.0.html) interactions. 
-->

## Global Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction_0_15_0.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

After you have setup how your avatar's hands are controlled, you can use the interface to specify [Grasp Button](virtualgrasp_unityapi.0.15.0.html#vg_vrbutton) globally for all of the sensors.

You can set the default [grasp Interaction](grasp_interaction.0.15.0.html#grasp-interaction) parameters for all objects in the scene globally in Global Grasp Interaction Settings.
See detailed explanation of the parameters in page [grasp Interaction](grasp_interaction.0.15.0.html#grasp-interaction).

{% include callout.html content= "Note that Interaction Type, Throw Velocity Scale and Throw Angular Velocity Scale can be set locally for each object by attaching [VG_Interactable](unity_component_vginteractable.0.15.0.html#unity-component-vginteractable) component to the object. These local settings will overwrite the global settings for that object." %} 


<!--### Selection Settings
{% include image.html file="unity/unity_vg_selection_settings.png" alt="VG selection settings." caption="VG selection settings" %}

Selection settings will show up when "Show Advanced" is checked. 

Selection settings provides options to choose how a graspable object is selected and how a grasp is selected
for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">grasp synthesis</a>.

#### Object Selection Method

| Object Selection Method | Description |
|-------|--------|
| INTERNAL_SELECTION | VG inherent graspable object selection method as described in [grasp interaction](grasp_interaction.0.15.0.html#from-object-selection-to-grasp-synthesis) | 
| EXTERNAL_SELECTION| This allows VR developers to implement their own object selection method, and call VG's **SelectObject** api function to select object for grasp interaction |


#### Grasp Selection Method

Grasp selection method is only relevant for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StaticGrasp}}">Static Grasp</a>
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Synthesis Method</a> 
to how to choose a grasp in the database that is **closest** to avatar wrist. How **closeness** is measured differenciate the grasp selection methods.

| Grasp Selection Method | Description |
|-------|--------|
| POS_ROT_COMBINED | choose the grasp closest to wrist combining both position and rotation | 
| MIN_POS| choose the grasp closest to wrist in terms of position |
| MIN_ROT| choose the grasp closest to wrist in terms of rotation |


| Parameters | Description |
|-------|--------|
| Pos Weight | for POS_ROT_COMBINED method, the importance weight on position (as opposed to rotation distance) in range [0.0, 1.0]. If 1.0 is equivalent to MIN_POS; if 0.0 is equivalent to MIN_ROT | 
| Grasp Rot Dist Threshold | rotation distance threshold above which a grasp in DB will not be selected for grasp synthesis | 
| Grasp Pos Dist Threshold | position distance threshold above which a grasp in DB will not be selected for grasp synthesis | 

-->

## Debug Settings

{% include image.html file="unity/unity_vg_debug_settings_0_15_0.png" alt="VG Debug Settings." caption="VG debug settings." %}

| Parameters | Description |
|-------|--------|
| Export Scene in Runtime | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes. (see [create debug files](debug_files.0.15.0.html#creating-debug-files)) | 
| Export Scene in Editor | Alternatively to check "Export Scene in Runtime", pressing Export Scene in Edit will simulate a launch of the VG plugin from the Unity Editor, thus without the need of launching the scene. This option is provided for convenience, but objects that are not in your scene yet will not be included. (see [create debug files](debug_files.0.15.0.html#creating-debug-files))|
| Use Network IDs | (Pro feature) Enabling this will allow you to set network ID for avatar's left/right hand (through [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.0.15.0.html#sensors--controllers)), and set network ID for object (through [VG_Articulation](unity_component_vgarticulation.0.15.0.html)).|
