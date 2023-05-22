---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_3_0
permalink: unity_component_myvirtualgrasp.1.3.0.html
folder: mydoc
---

## Description

MyVirtualGrasp is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} inherited from VG_MainScript, which encodes the main functionality of VirtualGrasp, and is the main component that you need to add and configure in your project to enable VirtualGrasp.

In Unity, VG_MainScript inherits from Monobehavior so you can use it as a component on a GameObject.

On this page, we are going to describe all the major configuration options covered in MyVirtualGrasp.cs.

## Avatars and Sensors

{% include image.html file="unity/unity_vg_myvirtualgrasp_1_2_0.png" alt="Avatar and Sensor setup in Unity." caption="Avatar and Sensor setup in Unity." %}

{% include callout.html content="In VirtualGrasp we use the term sensor and controller exchangeably since a controller is essentially a sensing device for hand poses." %}

### Avatars

VirtualGrasp provides a default avatar model "ThirdParty\VirtualGrasp\Resources\GleechiHands\GleechiRig". 
And if you want to use your own model it is supported in the **Pro version**, see [Avatars page](avatars.1.3.0.html). 

#### SkeletalMesh

Specify this to provide a reference to the SkinnedMeshRenderer of the avatar model that you have imported in your scene and which should be controlled by VG during runtime.

#### Replay and Physical

There are three avatar types in VirtualGrasp (see [Avatar Types](avatars.1.3.0.html#avatar-types)).
By default an avatar is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}. If _Replay_ is ticked, the avatar becomes {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %} (Pro version only). And both sensor and replay avatars can be {% include tooltip.html tooltip="PhysicalAvatar" text="physical avatars" %}.

VirtualGrasp allows creating multiple avatars in the interface by modifying _Size_ value. In the example image above, we specified to created two avatars, where first one is a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, and second one is a {% include tooltip.html tooltip="ReplayAvatar" text="replay avatar" %}. 

#### Hand Profile

In Unity, VirtualGrasp provides "hand profiles" as ScriptableObjects. You are able to configure a number of hand model-related settings and thereby  quickly switch between different custom hands. Besides the original VG_GleechiHands profile you may find some others as part of the VG SDK in __Resources/VG_HandPofiles__. You can find a more detailed documentation on [Hand Profiles](avatars.1.3.0.html#hand-profiles).

### Sensors

VirtualGrasp allows you to assign upto two {% include tooltip.html tooltip="Sensor" text="sensors" %} for an avatar, which allows developers to combine two sensors to control avatar's hands. However in the majority of use cases only one primary sensor is used. Detailed background can be found in [Controllers](controllers.1.3.0.html) page. 

#### Controller Profile

In each Sensor Setup, _Profile_ option allows you to select the "controller profile" for that sensor (primary or secondary). You are able to configure a number of controller-related settings and thereyby allow you to quickly switch between different controller inputs, such as UnityXR (e.g. supporting Quest), LeapMotion, Mouse, and others. A number of common VG_ControllerProfile are part of the VG SDK and you can find them in __Resources/VG_ControllerProfiles__. 

To learn how to create your custom controller profile see [Controller Profile](controllers.1.3.0.html#controller-profile). 

#### Origin

While each VG_ControllerProfile contains an "Origin Name" that should act as the origin of your controller data, you can overwrite the origin by selecting a different transform here. This may be useful since searching for a GameObject name as the VG_ControllerProfile does is error-prone, for example there may be multiple objects with that name.

If you set an "Origin" here instead, this Transform will overwrite the origin potentially detected through the VG_ControllerProfile. If you do not provide an "Origin" here (set it to None), the selected VG_ControllerProfile will try to find a GameObject by name as described above.

## Global Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction_0_15_0.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

After you have setup how your avatar's hands are controlled, you can use the interface to specify [Grasp Button](virtualgrasp_unityapi.1.3.0.html#vg_vrbutton) globally for all of the sensors.

You can set the default [grasp Interaction](grasp_interaction.1.3.0.html#grasp-interaction) parameters for all objects in the scene globally in Global Grasp Interaction Settings.
See detailed explanation of the parameters in page [grasp Interaction](grasp_interaction.1.3.0.html#grasp-interaction).

{% include callout.html content= "Note that Interaction Type, Throw Velocity Scale and Throw Angular Velocity Scale can be set locally for each object by attaching [VG_Interactable](unity_component_vginteractable.1.3.0.html#unity-component-vginteractable) component to the object. These local settings will overwrite the global settings for that object." %} 

## Grasp DB

{% include image.html file="unity/unity_vg_graspdb.png" alt="VG grasp database." caption="VG grasp database" %}
Once you have baked grasps for your current project using [VG_BakingClient](unity_component_vgbakingclient.1.3.0.html#step-3-baking), the saved grasp db can be dragged into _Grasp DB_ entry to be utilized. 


<!--### Selection Settings
{% include image.html file="unity/unity_vg_selection_settings.png" alt="VG selection settings." caption="VG selection settings" %}

Selection settings will show up when "Show Advanced" is checked. 

Selection settings provides options to choose how a graspable object is selected and how a grasp is selected
for <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">grasp synthesis</a>.

#### Object Selection Method

| Object Selection Method | Description |
|-------|--------|
| INTERNAL_SELECTION | VG inherent graspable object selection method as described in [grasp interaction](grasp_interaction.1.3.0.html#from-object-selection-to-grasp-synthesis) | 
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

{% include image.html file="unity/unity_vg_debug_settings_1_2_0.png" alt="VG Debug Settings." caption="VG debug settings." %}

| Parameters | Description |
|-------|--------|
| Export EC DebugDraw | Enabling this will show the raw sensor skeleton of the external controller data that the hand(s) are using. This is useful if you are creating or debugging [external controller data](unity_component_vgexternalcontrollermanager.1.3.0.html). | 
| Export Scene in Runtime | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes. (see [create debug files](debug_files.1.3.0.html#creating-debug-files)). | 
| Export Scene in Editor | Alternatively to check "Export Scene in Runtime", pressing Export Scene in Edit will simulate a launch of the VG plugin from the Unity Editor, thus without the need of launching the scene. This option is provided for convenience, but objects that are not in your scene yet will not be included. (see [create debug files](debug_files.1.3.0.html#creating-debug-files)). |
| Use Network IDs | (Pro feature) Enabling this will allow you to set network ID for avatar's left/right hand (through [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.3.0.html#sensors--controllers)), and set network ID for object (through [VG_Articulation](unity_component_vgarticulation.1.3.0.html)). |
