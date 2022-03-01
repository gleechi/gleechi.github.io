---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_10_1
permalink: unity_component_myvirtualgrasp.0.10.1.html
folder: mydoc
---

## Description

MyVirtualGrasp is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} inherited from VG_MainScript, which encodes the main functionality of VirtualGrasp, and is the main component that you need to add and configure in your project to enable VirtualGrasp.

In Unity, VG_MainScript inherits from Monobehavior so you can use it as a component on a GameObject.

In the VirtualGrasp SDK, you can find the Prefab “GleechiLib” from the ThirdParty/VirtualGrasp/Resources directory that has been configured with the MyVirtualGrasp component. You can simply drag and drop this into your scene. In your Hierarchy view, you will see the instantiated GameObject -- GleechiLib.

On this page, we are going to describe all the major configuration options covered in MyVirtualGrasp.cs.

## AutoSetup & Sensors

{% include callout.html content="In VirtualGrasp we use the term sensor and controller exchangeably since a controller is essentially a sensing device for hand poses." %}

VirtualGrasp allows you to configure multiple {% include tooltip.html tooltip="Sensor" text="sensors" %} in an application. 

This allows developers to combine two sensors to control avatar's hands. For example you can choose to use a data glove to control avatar's finger pose and grasp triggers, while using an Oculus touch controller to control wrist position and orientation. Though this is not most common setup for today's development use cases, this feature may become useful expecially for research and development of new hand controllers. 

In the majority of use cases only 1 single sensor is used. 

As you can see in MyVirtualGrasp, **Sensors** is a list in the interface. The first sensor element is listed as **Element 0**. All of the sensor elements will share the same interface, so in the descriptions below, we will focus on the importance of each element for each Sensor.

{% include image.html file="unity/unity_vg_myvirtualgrasp.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}

### AutoSetup

AutoSetup will auto-configure a number of controller-related settings and thereyby allow you to quickly switch between different controller inputs, such as UnityXR (e.g. supporting Quest), LeapMotion, Mouse, and others.

Select an [VG_AutoSetup](virtualgrasp_unityapi.0.10.1.html#vg_autosetup) option from the dropdown menu, then click "Setup" to automatically adjust the [Sensor options](#sensor) and [SensorSetting:FingerControlType](#finger-control-type)). 

{% include callout.html content="Pay attention to the Console in case there is anything you may need to take care of manually to complete the auto-setup process." %}

The integer value (0 in the image) relates to the element of the Sensors list that you want to auto-configure.
In most cases you will have only one avatar in your scene that is controlled by a single sensor, so 0 is the default. However, if you use multiple sensor elements, you can also quickly auto-configure them by modifying the integer value.

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
                <img src="/images/unity/unity_vg_myvirtualgrasp.png">
            </div>
        </div>
    </div>
</div>
-->

### Avatars

For each sensor, you can assign multiple avatars, though in most cases you will have only one avatar per sensor.

<!--{% include image.html file="unity/unity_vg_myvirtualgrasp_avatar.png" alt="Avatar configuration options in Unity." caption="Avatar configuration options in Unity." %}-->

| Option | Description |
|-------|--------|
| Model | should be HUMANOID_HAND in most application use cases. There could also be robotic hand options, but they will not be discussed here. | 
| SkeletalMesh| used to provide a reference to the SkinnedMeshRenderer of the avatar that you have imported in your scene and which should be controlled by VG during runtime. | 
| Remote | enable this if you want to use this avatar to reflect networked data (i.e. listening to another client over network in a multiplayer scenario), as explained in [Multiplayer Interaction](multiplayer_interaction.0.10.1.html), or the [VG_Networking Component](unity_component_vgnetworing.0.10.1.html).| 
| Physical | enable this if you want VG to create colliders for this avatar and enable the hand for physical interactions. NOTE: at the moment, this option is experimental and should not be used apart from testing.| 

<!--Check the **Replay** option if you want to use this avatar not for runtime-control, but for replaying recorded sensor data, as explained in [Sensor Record and Replay](sensor_record_replay.0.10.1.html), or the [VG_Recorder Component](unity_component_vgrecorder.0.10.1.html).-->

### Sensor

<!--{% include image.html file="unity/unity_vg_sensor.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}-->

| Option | AutoSetup | Description |
|-------|--------|--------|
| Sensor | supported | will always be External Controller for the VG SDK. | 
| External| supported | name of the external controller, as a string, so one can write your own external controller.|  
| Finger Control Type | supported | specify how sensor controls the finger motion. See [Finger Control Type](virtualgrasp_unityapi.0.10.1.html#vg_fingercontroltype). | 
| Control | not supported | specify what this sensor element controls. If you added two sensors, then one could control wrist position, rotation and  haptics, another controls fingers and grasp for example.| 
| Origin | supported | the origin of sensor where the sensor data is interpreted. | 
| Offset | supported | when the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust the offset to synchronize them. Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.| 

<!--| Finger Control Type | Description |
|-------|--------|
| BY_SENSOR_FULL_DOFS | for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. | 
| BY_SENSOR_LOW_DOFS| for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path | 
| BY_ANIMATION | for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation. | 
| BY_OSCILLATED_ANIMATION | will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (Experimental) | 
| BY_EXTERNAL | only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs. | -->

{% include image.html width = "60" file="knowledge/3D_Cartesian_Coodinate_Handedness.jpg" alt="LHS/RHS" %} <figcaption>The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand.<br>Source: Original by <a href="https://commons.wikimedia.org/wiki/File:3D_Cartesian_Coodinate_Handedness.jpg">PrimalShell</a>, <a href="https://en.wikipedia.org/wiki/en:Creative_Commons">Creative Commons</a> <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">Attribution-Share Alike 3.0 Unported</a> license.</figcaption>

## Sensor Settings

{% include image.html file="unity/unity_vg_sensor_settings.png" alt="Sensor settings in Unity." caption="Sensor settings in Unity." %}
After you have setup how your avatar's hands are controlled, you can use the Sensor Settings interface to specify [Trigger Button](virtualgrasp_unityapi.0.10.1.html#vg_vrbutton) globally for all of the sensors.

<!--
## Object Identifiers

{% include image.html file="unity/unity_vg_object_identifiers.png" alt="VG object identifiers." caption="VG object identifiers" %}

VirtualGrasp is using names to identify which objects are marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. You can customize component and layer names in MyVirtualGrasp → Object Identifiers. 
[VG_Articulation](unity_component_vgarticulation.0.10.1.html) component is a default entry, but this method also allows you to quickly adjust your project if you already have a layer or a component that marks your {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects.

Once an object is marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}, it will be supported by VG's [grasp](grasp_interaction.0.10.1.html) and [push](push_interaction.0.10.1.html) interactions. 
-->

## Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction_0.10.1.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

You can set the default [grasp Interaction](grasp_interaction.0.10.1.html#grasp-interaction) parameters for all objects in the scene globally in Grasp Interaction Settings.
See detailed explanation of the parameters in page [grasp Interaction](grasp_interaction.0.10.1.html#grasp-interaction).

{% include callout.html content= "Note that Synthesis Method and Interaction Type can be set locally for each object by attaching [VG_Interactable](unity_component_vginteractable.0.10.1.html#unity-component-vginteractable) component to the object. These local settings will overwrite the global settings for that object." %} 


<!--### Selection Settings
{% include image.html file="unity/unity_vg_selection_settings.png" alt="VG selection settings." caption="VG selection settings" %}

Selection settings will show up when "Show Advanced" is checked. 

Selection settings provides options to choose how a graspable object is selected and how a grasp is selected
for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">grasp synthesis</a>.

#### Object Selection Method

| Object Selection Method | Description |
|-------|--------|
| INTERNAL_SELECTION | VG inherent graspable object selection method as described in [grasp interaction](grasp_interaction.0.10.1.html#from-object-selection-to-grasp-synthesis) | 
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
{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG debug settings." caption="VG debug settings" %}

Debug settings will show up when "Show Advanced" is checked. 

### Save Debug Files

| Parameters | Description |
|-------|--------|
| Save Debug Files | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes (see [debug files](debug_files.0.10.1.html)). | 
| Physics Default Contact Offset | Overwrite Unity physics contact offset for more accurate collision detection. Currently only relevant for the experimental feature [push with physics](push_interaction.0.10.1.html#push-with-physics).| 

