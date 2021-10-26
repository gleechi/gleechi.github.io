---
title: About VirtualGrasp
sidebar: main_sidebar
keywords: virtualgrasp
permalink: virtual_grasp.html
folder: knowledge
toc: true
---

VirtualGrasp (or in short VG) is a software development kit (SDK) developed from over eight years of research in robotics, healthcare and industrial applications.
VG SDK provides a set of useful tools to make hand-object interactions in VR more natural and immersive. The two main **interaction-related features** offered by VG are:
* easy setup of <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behaviors</a> 
of an object (through [object articulation](object_articulation.html)) when hand [grasps](grasp_interaction.html) or [pushes](push_interaction.html) the object, and 
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesis}}">synthesizing</a>
 natural looking <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configurations</a> 
on hands during [grasp interaction](grasp_interaction.html) in a VR application.

Currently, these two features are closely linked to each other. 
To have intuitive object grasp interaction experiences, just synthesizing the natural looking 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configuration</a>
is not enough. How the hand and object moves just before and after the grasp trigger needs to be carefully handled, which is
addressed by using VG's [object articulation](object_articulation.html) feature.

Note that, while the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behavior</a> 
is provided out of the box from the VG SDK, 
to achieve natural looking <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configurations</a> in runtime
requires a preprocessing step called [object baking](object_baking.html).

Besides the above mentioned interaction-related features, one attractive feature of VirtualGrasp is that it is **hardware-agnostic**. VirtualGrasp can create natural grasp interactions 
with any kind of controllers (or sensors), wether it is hand-held VR controllers or finger tracking devices like LeapMotion. This is because unlike 
many physics-based grasp synthesis solutions in the market (Hand Physics Lab, [HPTK](https://github.com/jorgejgnz/HPTK-Sample), [CLAP](https://clapxr.com/) etc) 
that requires accurate finger tracking devices, VirtualGrasp exploits "object intelligence". By analyzing shape and affordances of an object model in VR, 
we can synthesize <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configurations</a> on a hand
with just the knowledge of where the wrist is; and without any dependence of expensive physical simulations. 
To learn how to setup different controllers, see [Controllers](controllers.html) page.
 
