---
title: VG_ObjectAnimator Component
keywords: component, animator, grasp, objectanimator
sidebar: main_sidebar_1_5_0
permalink: unity_component_vgobjectanimator.1.5.0.html
folder: mydoc
---

## Description

{% include image.html file="unity/unity_vg_objectanimator.png" alt="VG Object Animator." caption="VG Object Animator" %}

VG_ObjectAnimator is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that can be used to animate an object. 
The component is designed to simply specify how much the object is to rotate around an **Axis** a target **Angle**, or translate along the axis to a **Distance** from the initial pose. 

VG_ObjectAnimator.Rotate(float) and Translate(float) public functions are provided to enable dynamically driving object animation. For example, the VG_ObjectAnimator.Rotate(float) can listen to the **On Driven** event of [VG_AnimationDriver](unity_component_vganimationdriver.1.5.0.html) to rotate object through a controller input.

[VG onboarding task9](unity_vgonboarding_task9.1.5.0.html) shows a detailed tutorial of how to enable in-hand manipulation of pliers using this component together with [VG_FingerAnimator](unity_component_vgfingeranimator.1.5.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.5.0.html).