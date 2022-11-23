---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_0_0
permalink: unity_component_myvirtualgrasp.1.0.0.html
folder: mydoc
---

## Description

MyVirtualGrasp is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} inherited from VG_MainScript, which encodes the main functionality of VirtualGrasp, and is the main component that you need to add and configure in your project to enable VirtualGrasp.

In Unity, VG_MainScript inherits from Monobehavior so you can use it as a component on a GameObject.

On this page, we are going to describe all the major configuration options covered in MyVirtualGrasp.cs.

## Avatars and Sensors

{% include image.html file="unity/unity_vg_myvirtualgrasp_1_0_0.png" alt="Avatar and Sensor setup in Unity." caption="Avatar and Sensor setup in Unity." %}

{% include callout.html content="In VirtualGrasp we use the term sensor and controller exchangeably since a controller is essentially a sensing device for hand poses." %}

### Avatars

VirtualGrasp provides a default avatar model "ThirdParty\VirtualGrasp\Resources\GleechiHands\GleechiRig". 
And if you want to use your own model it is supported in the pro version, see [Avatars page](unity_get_started_avatars.1.0.0.html). 

#### SkeletalMesh

Specify this to provide a reference to the SkinnedMeshRenderer of the avatar model that you have imported in your scene and which should be controlled by VG during runtime.

#### Replay and Physical

There are three avatar types in VirtualGrasp:

* By default an avatar is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, meaning that avatar's hands are directly controlled by the [VG's sensor / controller integration](unity_component_vgexternalcontrollermanager.1.0.0.html) for movement and object interaction. 
* If _Replay_ option is ticked, then an avatar will be registered as {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %}. Such an avatar will be controlled by pre-recorded sensor data (see [Sensor Record and Replay](sensor_record_replay.1.0.0.html) and [VG_Recorder](unity_component_vgrecorder.1.0.0.html)). Note this feature is only available in VirtualGrasp pro version.
* Both {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} and {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} can be created as a {% include tooltip.html tooltip="PhysicalAvatar" text="physical avatar" %} if _Physical_ option is ticked. 

VirtualGrasp allows creating multiple avatars in the interface by modifying _Size_ value. In the example image above, we specified to created two avatars, where first one is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, and second one is a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %}. 


#### Hand Profile

{% include image.html file="unity/unity_vg_ec_handprofile.png" alt="VG Controller profile in Unity." caption="VG Controller profile as scriptable object in Unity." %}

Through hand profiles (which are ScriptableObjects), you are able to configure a number of hand model-related settings and thereyby allow you to quickly switch between different custom hands. Besides the original VG_GleechiHands_Profile you may find some others as part of the VG SDK in __Resources/VG_HandPofiles__. You can find a more detailed documentation on [Hand Axis Mappings](avatars.1.0.0.html#hand-axis-mappings).

### Sensors

VirtualGrasp allows you to assign upto two {% include tooltip.html tooltip="Sensor" text="sensors" %} for an avatar. 
This allows developers to combine two sensors to control avatar's hands. For example you can choose to use a data glove to control avatar's finger pose and grasp triggers, while using an Oculus touch controller to control wrist position and orientation. Though this is not most common setup for today's development use cases, this feature may become useful expecially for research and development of new hand controllers. 

In the majority of use cases only one primary sensor is used. 

#### Controller Profile

{% include image.html file="unity/unity_vg_ec_unityxrhand_1_0_0.png" alt="VG Controller profile in Unity." caption="VG Controller profile as scriptable object in Unity." %}

In each Sensor Setup, _Profile_ option allows you to select the "controller profile" (which are ScriptableObjects) for that sensor (primary or secondary). You are able to configure a number of controller-related settings and thereyby allow you to quickly switch between different controller inputs, such as UnityXR (e.g. supporting Quest), LeapMotion, Mouse, and others. A number of common VG_ControllerProfile are part of the VG SDK and you can find them in __Resources/VG_ControllerProfiles__. Elements of each VG_ControllerProfile are explained in this table: 

<!--{% include image.html file="unity/unity_vg_sensor.png" alt="Sensor configuration options in Unity." caption="Sensor configuration options in Unity." %}-->

| Option | Description |
|-------|--------|--------|
| External Type| name of the external controller, as a string, so one can write your own external controller. Note, here we supports adding a list of controller names, separated by ';', in order of priorization. E.g. "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.|  
| Control |  specify what this sensor element controls. If you added two sensors, then one could control wrist position, rotation and  haptics, another controls fingers and grasp for example.| 
| Finger Control Type |  specify how sensor controls the finger motion. See [Finger Control Type](virtualgrasp_unityapi.1.0.0.html#vg_fingercontroltype). | 
| Offset Position<br>Offset Rotation |  when the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust the offset to synchronize them. Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.| 
| Origin Name | set this to the GameObject name that should act as the origin of your controller data. For example, "XRRig" for the default Unity XR Rig (unless you renamed it). If no GameObject with this name is found (or you leave it empty), the origin will be the zero-origin.<br><br>To overwrite this behavior, you can use the [Origin](#origin) field as described below.| 
| Origin Scale | you can add a scale multiplier to the sensor data if you like. The default is (1,1,1). | 
| Hand Mappings | you can find a more detailed documentation on [Controller Axis Mappings](avatars.1.0.0.html#controller-axis-mapping). | 

<!--| Finger Control Type | Description |
|-------|--------|
| BY_SENSOR_FULL_DOFS | for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. | 
| BY_SENSOR_LOW_DOFS| for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path | 
| BY_ANIMATION | for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation. | 
| BY_OSCILLATED_ANIMATION | will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (Experimental) | 
| BY_EXTERNAL | only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs. | -->


#### Origin

While each VG_ControllerProfile contains an "Origin Name" that should act as the origin of your controller data, you can overwrite the origin by selecting a different transform here. This may be useful since searching for a GameObject name as the VG_ControllerProfile does is error-prone, for example there may be multiple objects with that name.

If you set an "Origin" here instead, this Transform will overwrite the origin potentially detected through the VG_ControllerProfile. If you do not provide an "Origin" here (set it to None), the selected VG_ControllerProfile will try to find a GameObject by name as described above.

## Global Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction_0_15_0.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

After you have setup how your avatar's hands are controlled, you can use the interface to specify [Grasp Button](virtualgrasp_unityapi.1.0.0.html#vg_vrbutton) globally for all of the sensors.

You can set the default [grasp Interaction](grasp_interaction.1.0.0.html#grasp-interaction) parameters for all objects in the scene globally in Global Grasp Interaction Settings.
See detailed explanation of the parameters in page [grasp Interaction](grasp_interaction.1.0.0.html#grasp-interaction).

{% include callout.html content= "Note that Interaction Type, Throw Velocity Scale and Throw Angular Velocity Scale can be set locally for each object by attaching [VG_Interactable](unity_component_vginteractable.1.0.0.html#unity-component-vginteractable) component to the object. These local settings will overwrite the global settings for that object." %} 


<!--### Selection Settings
{% include image.html file="unity/unity_vg_selection_settings.png" alt="VG selection settings." caption="VG selection settings" %}

Selection settings will show up when "Show Advanced" is checked. 

Selection settings provides options to choose how a graspable object is selected and how a grasp is selected
for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">grasp synthesis</a>.

#### Object Selection Method

| Object Selection Method | Description |
|-------|--------|
| INTERNAL_SELECTION | VG inherent graspable object selection method as described in [grasp interaction](grasp_interaction.1.0.0.html#from-object-selection-to-grasp-synthesis) | 
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
| Export Scene in Runtime | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes. (see [create debug files](debug_files.1.0.0.html#creating-debug-files)) | 
| Export Scene in Editor | Alternatively to check "Export Scene in Runtime", pressing Export Scene in Edit will simulate a launch of the VG plugin from the Unity Editor, thus without the need of launching the scene. This option is provided for convenience, but objects that are not in your scene yet will not be included. (see [create debug files](debug_files.1.0.0.html#creating-debug-files))|
| Use Network IDs | (Pro feature) Enabling this will allow you to set network ID for avatar's left/right hand (through [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.0.0.html#sensors--controllers)), and set network ID for object (through [VG_Articulation](unity_component_vgarticulation.1.0.0.html)).|
