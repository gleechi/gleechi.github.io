---
title: VirtualGrasp Onboarding Task5 - Assemble 
#tags: [getting_started]
keywords: casestudy, task5, vgonboarding, assemble, disassemble, VG_Assemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_0
permalink: unity_vgonboarding_task5.1.6.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="TJ5T67fv6ys" %} -->

{% include youtube.html id="glCwt7WqCS8" %}


#### Interaction behaviors wanted

* We want to close the water bottle with the cap screwed on. 
* We want be able to have bottle-cap system either completely non-physical or physical. That means for non-physical bottle-cap setup, we can't use Unity's physical joint support for this assembling task.

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

#### Assemble and disassemble cap

{% include image.html file="unity/unity_onboarding_task5_vg_assemble_1_6_0.png" alt="VG Assemble setup for cap." caption="VG Assemble setup for cap." %}

[VG_Assemble](unity_component_vgassemble.1.6.0.html) component is used for assembling and disassembling the cap to the bottle. 
Above image shows the setting for the component on cap. And note that the same setting of VG_Assemble works on both physical cap or non-physical cap. 
A few things to point out:

* Since when we assemble the cap to the bottle, we want the cap to attach to the bottle as its child, we check _Assemble To Parent_ flag. 
* And _Desired Poses_ is **cap_target** transform that is the bottle's child.
* Since the cap is a rotational symmetric object, so assemble angle threshold just need to make sure its symmetry axis is aligned with desired pose. This axis is represented by the **Y Axis** of the cap object itself, since _Assemble Anchor_ is not assigned. Therefore  _Assemble Axis_ is set to be "Y Axis" to indicate y-axis of the object should match that of **cap_target**. Since any rotation angle around the axis is fine, _Assemble Symmetry Steps_ is set to be 0.     
* Because when assembled, cap is using  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint with non-zero screw rate to simulate screwing effect of cap in the real world, a disabled [VG_Articulation](unity_component_vgarticulation.1.6.0.html) with  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint is added to this game object and drag it to _Assemble Articulation_ entry.
* Because when disassembling a cap in the real world, we need to unscrew to loosen it, this requirement is simulated by checking _Disassemble On Zero State_ flag.
* Because the cap initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), we don't need to assign _Disassemble Articulation_ entry.
* Because the cap initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), if the object initially is {% include tooltip.html tooltip="PhysicalObject" text="physical" %}, when disassembled it will always recover its physical properties automatically handled by VG. Therefore _Force Disassembled Physical_ flag does not need to be checked.