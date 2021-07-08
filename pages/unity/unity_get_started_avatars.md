---
title: Getting Started in Unity - Avatars
series: "Getting Started in Unity series"
weight: 2
sidebar: unity_sdk_sidebar
keywords: hand, object, avatar, install, quickstart
permalink: unity_get_started_avatars.html
folder: mydoc
toc: false
---

## A First Look at the Hand Model

After importing a hand model into your scene (such as the provided OculusRig_3), link it into its place under Sensors → Avatars → Skeletal Mesh. For example, by dragging and dropping Rhand.001 (which you can find directly under OculusRig_3 in the Hierarchy) into this slot.

{% include image.html file="unity/unity_hand_model.png" alt="Unity hand model." caption="" %}

You can replace this model by any other skinned mesh renderer that you import into the scene, but note that there are restrictions on which kind of skeletons are supported. 

As a rule of thumb, the rigging / model hierarchy should be same as the model in the project:

* 1 avatar / skeletal mesh should include 2 hands, 
* 1 hand should include 5 fingers (no extra bones), and 
* 1 finger should include 3-4 bones (with or without fingertip). If a fingertip is missing, the plugin will guess its position, but it is recommended, and also very easy in Unity to add missing fingertip bones.

You can see that VG has successfully initialized the avatar when messages like these appear:

{% include image.html file="unity/unity_avatar_init.png" alt="Unity avatar init." caption="" %}

{% include tip.html content="Enable \"Update When Offscreen\" for your models to always show the hands." %}


{% include custom/series_acme_next.html %}