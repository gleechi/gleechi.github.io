---
title: VirtualGrasp Onboarding Task3 - Container
#tags: [getting_started]
keywords: casestudy, task2, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_9_6
permalink: unity_vgonboarding_task5.0.9.6.html
redirect_from: unity_vgonboarding_task5.html
folder: mydoc
---

We have a series of VG onboarding tasks to show how to tackle different practical use cases in a VR application.

### Task Description

{% include youtube.html id="SWekpa7OxHI" %}

#### Interaction behaviors wanted

* xxx

#### Tips for VR developers

* xxx

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

is the unity scene showing how ...
and xxx.cs script is attached to xxx.

The steps to achieve the manipulation on the scissors in the video:

* Make a single object that combines the two articulated parts (for scissors the two handles), we call for example **scissor**.
* Make two objects corresponding to the two articulated parts of **scissor**, we call **handle_left** and **handle_right**.
* In Unity set up the object hiearchy such that **scissor** is the parent of the two handles, and the two handles should be in a position overlapping with **scissor**.
* Make **scissor** as a VG interactable object, but deactivate mesh renderer, so it is invisible. 
* Make both **handles** non-interactable with VG, but activate mesh renderer, so they are actually visible.
* Once you have baked the objects, then only the VG interactable object **scissor** is baked, so DG is available on this object.
* Use [VG_GraspStudio](unity_component_vggraspstudio.0.9.6.html#grasp-studio) to create a primary grasp on **scissor** to be suitable for the initial pose for the manipulation.
* Find the position where you want to lerp the fingers when triggering the button and add them to the post animator script
* Add the specific behaviour you want in the post animator script to rotate the handles

```js
//VirtualGrasp/Scenes/onboarding/Scripts/xxx.cs:

to be filled
````
is the script showing how to adapt the public script [VG_PostAnimator](unity_component_vgpostanimator.0.9.6.html) to ...

