---
title: About VirtualGrasp
sidebar: main_sidebar
keywords: virtualgrasp
permalink: virtual_grasp.html
folder: knowledge
toc: true
---



Besides the above mentioned interaction-related features, one attractive feature of VirtualGrasp is that it is **hardware-agnostic**. VirtualGrasp can create natural grasp interactions 
with any kind of controllers (or sensors), wether it is hand-held VR controllers or finger tracking devices like LeapMotion. This is because unlike 
many physics-based grasp synthesis solutions in the market (Hand Physics Lab, [HPTK](https://github.com/jorgejgnz/HPTK-Sample), [CLAP](https://clapxr.com/) etc) 
that requires accurate finger tracking devices, VirtualGrasp exploits "object intelligence". By analyzing shape and affordances of an object model in VR, 
we can synthesize <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspConfiguration}}">grasp configurations</a> on a hand
with just the knowledge of where the wrist is; and without any dependence of expensive physical simulations. 
To learn how to setup different controllers, see [Controllers](controllers.html) page.
 
