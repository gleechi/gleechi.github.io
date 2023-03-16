---
title: VG_AnimationDriver Component
keywords: component, animator, grasp, animationdriver, animation
sidebar: main_sidebar_1_2_0
permalink: unity_component_vganimationdriver.1.2.0.html
folder: mydoc
---

## Description

{% include image.html file="unity/unity_vg_animationdriver.png" alt="VG Animation Driver." caption="VG Animation Driver" %}

VG_AnimationDriver is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that can be used to drive any animation on fingers or objects with specified input through **Action Reference**. Depending on the action reference, **Input Range** could be [0, 1] or other values like [-1, 1]. The driver is only enabled when the left or right hand (specified by **Hand Side**) is holding the **Interactable Object**, because it is designed with the primary intentions to animate in-hand manipulations of grasped objects. 

VG_AnimationDriver provides **On Driven** event that is invoked at each frame to receive input floating values in the **Input Range**. Any animator functions can recieve this input value by listening to the **On Driven** events. The example image above shows the input is driving both VG_FingerAnimator.DriveAnimation(float) and VG_ObjectAnimator.Rotate(float) to animate the in-hand manipulation of the pliers in our [VG onboarding task9](unity_vgonboarding_task9.1.2.0.html). 

{% include important.html content="VG_AnimationDriver is currently relying on the Unity _XR Interaction Toolkit_ package. We thus have a dependency of this system in the current 1.2.0, but will resolve this in the next release so it can also be used with legacy input." %}
 