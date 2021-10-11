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

### Use cases

Most common use cases of VG_PostAnimator component 
is to create a finger animation on object, for example pushing a button on an electric drill.

Usually you create a grasp using an already created static grasp through [VG_GraspStudio](unity_component_vggraspstudio.html#grasp-studio)

### How to

{% include image.html file="unity/unity_vg_post_animator.png" alt="VG PostAnimator" caption="MyVirtualGrasp script - VG_PostAnimator Component." %}
