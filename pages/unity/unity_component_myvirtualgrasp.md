---
title: MyVirtualGrasp Component
#tags: [getting_started]
keywords: component, main
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_myvirtualgrasp.html
folder: mydoc
---

### Sensor setup
{% include image.html file="unity/unity_vg_myvirtualgrasp.png" alt="VG Sensors." caption="VG Sensors" %}

#### Sensor offset

When the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust an offset in each controller setting to synchronize them:

Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.

{% include image.html file="knowledge/lhs_rhs.png" alt="LHS/RHS" caption="The offset is applied in LHS (left hand system) for the left and RHS (right hand system) for the right hand." %}


### Sensor settings

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


### Grasp Interaction Settings

{% include image.html file="unity/unity_vg_global_grasp_interaction.png" alt="VG global grasp interaction settings." caption="VG global grasp interaction settings" %}

You can set the default [grasp Interaction](grasp_interaction.html#grasp-interaction) settings for all objects in the scene globally. 

And note that <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Synthesis Method</a> and 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionType}}">Interaction Type</a> can be set "locally" for each object by using
[VG_Interactable](unity_component_vginteractable.html#unity-component-vginteractable) component.

### Selection Settings
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


### Debug Settings
{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG debug settings." caption="VG debug settings" %}

Debug settings will show up when "Show Advanced" is checked. 

#### Save Debug Files

| Parameters | Description |
|-------|--------|
| Save Debug Files | Enabling this and running the application will create a vg_tmp subdirectory in your project and save sources that are used for different purposes; read [Debug Files knowledge page](debug_files.html) to learn more. | 
| Use Object IK | Enabling this will activate object IK; NOTE this is not supported anymore. | 
| Physics Default Contact Offset | Overwrite Unity physics contact offset for more accurate collision detection. | 

