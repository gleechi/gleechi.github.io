---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_myvirtualgrasp.html
folder: mydoc
---

MyVirtualGrasp is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.CoreScript}}">Core Script</a>

It inherits from VG_MainScript, which encodes the main functionality of VirtualGrasp, and is the main component that you need to add and configure in your project to enable VirtualGrasp.

In Unity, VG_MainScript inherits from Monobehavior so you can use it as a component on a GameObject.<br><br>
<!-- All the API functions you want to use in your own scripts can be accessed through VG_Controller. -->

On this page, we are going to describe all the major configuration options.

<!--On this page, we are going to describe all the major configuration options, divided into the following sections:

* [AutoSetup & Sensors](#sensor-setup)
* [Sensor Settings](#sensor-settings)
* [Object Identifiers](#object-identifiers)
* [Grasp Interaction Settings](#grasp-interaction-settings)
* [Advanced Settings - Debug Settings](#debug-settings)
-->
### AutoSetup & Sensors

{% include image.html file="unity/unity_vg_myvirtualgrasp.png" alt="Sensor configuration options (as part of VG_MainScript) in Unity." caption="Sensor configuration options (as part of VG_MainScript) in Unity." %}

**AutoSetup** will auto-configure a number of controller-related settings in your VG_MainScript component and thereyby allow you to quickly switch between different controller inputs, such as Quest, LeapMotion, Mouse, and others.

Select an [VG_AutoSetup](/virtualgrasp_unityapi.html#vg_autosetup) option from the dropdown menu, then click "Setup" to automatically adjust the following fields:
* Sensor, External, Origin, Offset, and SensorSettings:FingerControlType.

Pay attention to the Console in case there is anything you may need to take care of manually to complete the auto-setup process.

The integer value (0 in the image) relates to the element of the Sensors list that you want to auto-configure.
In most cases you will have only one avatar in your scene that is controlled by a single controller, so 0 is the default. However, if you use multiple sensor elements, you can also quickly auto-configure them by modifying the integer value.

{% include callout.html content="**Sensors** is a list that allows you to add multiple elements if you like. All of them will share the same interface, so in the descriptions below, we will focus on the importance of each element for each Sensor." type="primary" %} 

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

### Sensors

#### Avatars

For each sensor, you can assign multiple avatars, though in most cases you will have only one avatar per sensor.

{% include image.html file="unity/unity_vg_myvirtualgrasp_avatar.png" alt="Avatar configuration options (as part of VG_MainScript) in Unity." caption="Avatar configuration options (as part of VG_MainScript) in Unity." %}

The **Model** should be HUMANOID_HAND in your usecase. There are robotic hand options as well, but they will not be discussed here.

Under **SkeletalMesh** you provide a reference to the SkinnedMeshRenderer of the avatar that you have imported in your scene and which should be controlled by VirtualGrasp during runtime.

Check the **Replay** option if you want to use this avatar not for runtime-control, but for replaying recorded sensor data, as explained in [Sensor Record and Replay](sensor_record_replay.html), or the [VG_Recorder Component](unity_component_vgrecorder.html).

Check the **Remote** option if you want to use this avatar for reflecting networked data (i.e. listening to another client over network in a multiplayer scenario), as explained in [Multiplayer Interaction](multiplayer_interaction.html), or the [VG_Networking Component](unity_component_vgnetworing.html).
{% include important.html content="Documentation is missing here and links do not work." %}

Check the **Physical** option if you want VirtualGrasp to create colliders for this avatar and enable the hand for physical interactions (remember VG is an animation engine that is not dependent on physics).
{% include important.html content="At the moment, this option is experimental and should not be used apart from testing." %}

### Sensor Offset

When the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust an offset in each controller setting to synchronize them:

Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.

{% include image.html file="knowledge/lhs_rhs.png" alt="LHS/RHS" caption="The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand." %}

### Sensor Settings

{% include image.html file="unity/unity_vg_sensor_settings.png" alt="VG sensor settings." caption="VG sensor settings" %}

#### Finger control type

This provides the option to choose how sensor controls the finger motion

| Finger Control Type | Description |
|-------|--------|
| BY_SENSOR_FULL_DOFS | for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. | 
| BY_SENSOR_LOW_DOFS| for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path | 
| BY_ANIMATION | for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation. | 
| BY_OSCILLATED_ANIMATION | will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (Remain to be tested in unity when sensor type is External Controller ) | 
| BY_EXTERNAL | only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs. | 


#### Trigger Button

This provides the option to choose which button on a hand-held VR controller you want to use to trigger [grasp interactions](grasp_interaction.html#background).

| Trigger Button | Description |
|-------|--------|
| TRIGGER | the VR controller's trigger button usually placed under index finger. | 
| GRIP| the VR controller's grip button usually placed under middle and ring fingers | 

### Object Identifiers
{% include image.html file="unity/unity_vg_object_identifiers.png" alt="VG object identifiers." caption="VG object identifiers" %}

The object identifiers let you decide which Unity component(s) (by name) can be used to specify an object to be interactable. 
If any of these components are added to a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GameObject}}">game object</a>,
this object will be supported by VG's [grasp](grasp_interaction.html) and [push](push_interaction.html) interactions.

By default VG uses 2 components: [VG_Articulation](unity_component_vgarticulation.html) and [VG_Interactable](unity_component_vginteractable.html).

### Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

See explanation of the parameters in [grasp Interaction](grasp_interaction.html#grasp-interaction). 
You can set the default grasp interaction parameters for all objects in the scene globally. 
And <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Synthesis Method</a> and 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">Interaction Type</a> can be set "locally" for each object by using
[VG_Interactable](unity_component_vginteractable.html#unity-component-vginteractable) component.

<!--### Selection Settings
{% include image.html file="unity/unity_vg_selection_settings.png" alt="VG selection settings." caption="VG selection settings" %}

Selection settings will show up when "Show Advanced" is checked. 

Selection settings provides options to choose how a graspable object is selected and how a grasp is selected
for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">grasp synthesis</a>.

#### Object Selection Method

| Object Selection Method | Description |
|-------|--------|
| INTERNAL_SELECTION | VG inherent graspable object selection method as described in [grasp interaction](grasp_interaction.html#from-object-selection-to-grasp-synthesis) | 
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
### Debug Settings
{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG debug settings." caption="VG debug settings" %}

Debug settings will show up when "Show Advanced" is checked. 

#### Save Debug Files

| Parameters | Description |
|-------|--------|
| Save Debug Files | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes (see [Debug Files](debug_files.html)). | 
| Physics Default Contact Offset | Overwrite Unity physics contact offset for more accurate collision detection. | 

