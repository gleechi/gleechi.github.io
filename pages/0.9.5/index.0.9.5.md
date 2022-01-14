---
title: "Welcome to VirtualGrasp Documentations"
sidebar: main_sidebar_0_9_5
permalink: index.html
---

VirtualGrasp (VG) is a software development kit (SDK) developed from over eight years of research in robotics, healthcare and industrial applications.
VG SDK provides a set of tools to make hand-object interactions in VR natural and immersive. The two main benefits of using VG are:
* {% include tooltip.html tooltip="GraspSynthesis" text="synthesizing" %} natural looking {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} on hands during [grasp interaction](grasp_interaction.0.9.5.html) in a VR application, and
* easy setup of {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behaviors" %} of an object (through [object articulation](object_articulation.0.9.5.html)) when hand [grasps](grasp_interaction.0.9.5.html) or [pushes](push_interaction.0.9.5.html) the object. 

These two features are closely linked to each other. 
To have intuitive object grasp interaction experiences, just synthesizing the natural looking 
{% include tooltip.html tooltip="GraspConfiguration" text="grasp configuration" %} is not enough. How the hand and object moves just before and after grasping needs to be carefully handled, which is solved by VG's [object articulation](object_articulation.0.9.5.html) feature.


Note that, while the {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behavior" %} is provided out of the box from the VG SDK, 
to achieve natural looking {% include tooltip.html tooltip="GraspConfiguration" text="grasp configurations" %} in runtime
requires a preprocessing step called [object baking](object_baking.0.9.5.html).

VG is hardware agnostic and can create natural [grasp interactions](grasp_interaction.0.9.5.html) with any kind of controllers (or sensors). 
You can find more details in [controllers](controllers.0.9.5.html) page.

As a general guideline to this site:

* [Tutorials](unity_get_started_installation.0.9.5.html) take you by the hand through a series of steps to learn how to use VirtualGrasp.
* [Explanations](controllers.0.9.5.html) lead you to learn about fundamental concepts in VirtualGrasp.
* [How-To Guides](unity_component_myvirtualgrasp.0.9.5.html) are recipes that guide you through the components involved in addressing key problems and use-cases.
* [References](virtualgrasp_unityapi.0.9.5.html) contain technical reference for VirtualGrasp APIs and components as well as release notes. They describe how it works and how to use it,
 but assume that you have a basic understanding of key concepts in [Explanations](controllers.0.9.5.html).

{% include image.html file="docs_overview.png" alt="Documentation overview." caption="Documentation Overview [source: https://documentation.divio.com]." %}