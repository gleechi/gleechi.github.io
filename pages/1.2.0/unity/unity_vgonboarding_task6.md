---
title: VirtualGrasp Onboarding Task6 - Planar joint 
#tags: [getting_started]
keywords: casestudy, task6, vgonboarding, planar joint,
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_2_0
permalink: unity_vgonboarding_task6.1.2.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="_DcS9Tcfoj8" %}-->

{% include youtube.html id="UZgKsE7FQkc" %}

#### Interaction behaviors wanted

* We want some button objects to stay on the planary surface of a pad simulating touch pad-like behaviors. 

#### Tips for VR developers

* VG_Articulation support creating joints on non-physical objects (objects without Rigidbody or ArticulationBody).
* And the non-physical object with VG_Articulation can be parented to a physical object. 


### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding** see Task6_pad. 

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````
We simply added VG_Articulation component to the two button objects, one cylinder shaped and one cuboid shaped, and set both using PLANAR joint. Then you can interact with it by either pushing with index finger or grasping depending on what kind of {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %} you set. And a rectangular shaped planar limits are set along the joint anchor's x and y axes. 
