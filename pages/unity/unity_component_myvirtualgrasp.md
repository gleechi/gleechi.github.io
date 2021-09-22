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

## [THIS PAGE NEEDS TO BE UPDATED]

{% include image.html file="unity/unity_vg_settings.png" alt="VG Settings." caption="VG_Settings" %}


### Sensor settings

In Unreal or Unity, VG_MyVirtualGrasp has a component where you can specify a number of interaction related options that can significantly change the user experiences when using our VirtualGrasp software. 

The most important options are explained here:

#### Finger control type

This provide the option to choose how sensor controls the finger motion

BY_SENSOR_FULL_DOFS: this means for sensor that can provide full dofs hand tracking like Leap Motion, the avatar hand will follow your own hand on all dofs. 

BY_SENSOR_LOW_DOFS : this means for sensor that can only provide one dof for each finger, like some data gloves, the avatar hand finger will be bended by just one value for each finger following a predefined animation path

BY_ANIMATION: this means for all sensor types which all provide a single value, grabbing strength, range between 0.0 and 1.0, all fingers will follow a predefined path in animation.

BY_EXTERNAL: this is only relevant for External Controller sensor type, finger will be set by an externally specified finger dofs.

BY_OSCILLATED_ANIMATION: this will let hand animated a little bit when not interacting with any object to avoid "rigid hand" feeling. (remain to be tested in unity when sensor type is External Controller )

#### Grasp Interaction Settings

You can set the default [grasp Interaction](grasp_interaction.html#grasp-interaction) settings for all objects in the scene globally. 


#### Sensor offset

When the virtual hands do not match to the position or rotation of your real hands holding the controllers, you can adjust an offset in each controller setting to synchronize them:

Note that the hand coordinate system's axes, XYZ, are defined like you strech out three axes with thumb, index, and middle finger (i.e. X is thumb up, Y is index forward, and Z is middle inward) of each hand. In other words, with a fully flat hand, all finger point along the positive Y axis, and your palm faces the positive Z axis.