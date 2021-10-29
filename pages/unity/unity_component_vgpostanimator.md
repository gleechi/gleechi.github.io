---
title: VG_PostAnimator Component
#tags: [getting_started]
keywords: component, animator, grasp, postanimator
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vgpostanimator.html
folder: mydoc
---

VG_PostAnimator is is a <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.CoreScript}}">Core Script</a>.
It exemplifies how you could overwrite (post-animate) grasp animations that are handled by VirtualGrasp.

{% include image.html file="unity/unity_vg_post_animator.png" alt="VG PostAnimator" caption="VG_PostAnimator Component." %}

{% include youtube.html id="SWekpa7OxHI" %}
<!--
<iframe width="560" height="315" src="https://www.youtube.com/embed/SWekpa7OxHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

Most common use cases of VG_PostAnimator component 
is to create a finger animation on an articulated object, for example manipulating a scissor as shown in above video.

The steps to achieve the manipulation on the scissors in the video:
* Make a single object that combines the two articulated parts (for scissors the two handles), we call for example **scissor**.
* Make two objects corresponding to the two articulated parts of **scissor**, we call **handle_left** and **handle_right**.
* In Unity set up the object hiearchy such that **scissor** is the parent of the two handles, and the two handles should be in a position overlapping with **scissor**.
* Make **scissor** as a VG interactable object, but deactivate mesh renderer, so it is invisible. 
* Make both **handles** non-interactable with VG, but activate mesh renderer, so they are actually visible.
* Once you have baked the objects, then only the VG interactable object **scissor** is baked, so DG is available on this object.
* Use [VG_GraspStudio](unity_component_vggraspstudio.html#grasp-studio) to create a primary grasp on **scissor** to be suitable for the initial pose for the manipulation.
* Find the position where you want to lerp the fingers when triggering the button and add them to the post animator script
* Add the specific behaviour you want in the post animator script to rotate the handles
