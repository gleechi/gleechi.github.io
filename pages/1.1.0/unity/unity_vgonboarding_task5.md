---
title: VirtualGrasp Onboarding Task5 - Assemble 
#tags: [getting_started]
keywords: casestudy, task5, vgonboarding, assemble, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_1_0
permalink: unity_vgonboarding_task5.1.1.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="TJ5T67fv6ys" %} -->

{% include youtube.html id="glCwt7WqCS8" %}


#### Interaction behaviors wanted

* We want to close the water bottle with the cap screwed on. 
* Water bottle or cap can be either physical or non-physical, so can not use Unity's physical joint support if they are not {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %}.

#### Tips for VR developers

* VG_Articulation support creating constrained joints on non-{% include tooltip.html tooltip="PhysicalObject" text="physical object" %}.
* When an object's joint is changed in runtime through [ChangeObjectJoint](virtualgrasp_unityapi.1.1.0.html#changeobjectjoint) or [RecoverObjectJoint](virtualgrasp_unityapi.1.1.0.html#vg_controllerrecoverobjectjoint) VG internally handles remove and recover Rigidbody (see page [physical object joint change](unity_component_vgarticulation.1.1.0.html#physical-object-joint-change)).

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

#### Assemble and disassemble cap

{% include image.html file="unity/unity_onboarding_task5_vg_assemble.png" alt="VG Assemble setup for cap." caption="VG Assemble setup for cap." %}

[VG_Assemble](unity_component_vgassemble.1.1.0.html) component is used for assembling and disassembling the cap to the bottle. 
Above image shows the setting for the component on cap. A few things to point out:

* Since when we assemble the cap to the bottle, we want the cap to attach to bottle as bottle's child, we check _Assemble To Parent_ flag. 
* And _Desired Poses_ is **cap_target** transform that is child of the bottle.
* Since the cap is a rotational symetric object, so assemble angle threshold just need to make sure its symetry axis is aligned with desired pose. This axis is represented by the **y-axis** of the cap object itself, since _Assemble Anchor_ is not assigned. Therefore _Asemble Axis_ is set to be (0, 1, 0) to indicate y-axis of the object should match that of **cap_target**.  
* Because when assembled, cap is using  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint with non-zero screw rate to simulate screwing effect of cap in real world. A disabled [VG_Articulation](unity_component_vgarticulation.1.1.0.html) with  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint is added to this game object and drag it to _Assemble Articulation_ entry.
* Because the cap initially is at the disassembled state (attached to radio with {% include tooltip.html tooltip="Floating" text="floating" %} joint), we don't need to assign _Disassemble Articulation_ entry.
* Because the cap initially is at the disassembled state (attached to radio with {% include tooltip.html tooltip="Floating" text="floating" %} joint), if the object initially is {% include tooltip.html tooltip="PhysicalObject" text="physical" %}, when disassembled it will always recover its physical properties automatically handled by VG. Therefore _Force Disassembled Physical_ flag does not need to be checked.