---
title: VirtualGrasp Onboarding Task7 - Chain Assemble 
#tags: [getting_started]
keywords: casestudy, task7, vgonboarding, assemble, disassemble, VG_Assemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_3_0
permalink: unity_vgonboarding_task7.1.3.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

{% include youtube.html id="cSMZGtcdwMo" %}

#### Interaction behaviors wanted

* We want to assemble a set of objects (chain loops in this example) into a chain connected through VG joint (used {% include tooltip.html tooltip="Cone" text="cone" %} joint), while able to freely determine who is the parent and who is the child. 


### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

#### Assemble and disassemble chain loops to each other

{% include image.html file="unity/unity_onboarding_task7_vg_assemble.png" alt="VG Assemble setup for a chain loop." caption="VG Assemble setup for a chain loop." %}

[VG_Assemble](unity_component_vgassemble.1.3.0.html) component is used for assembling and disassembling the chain loop to each other to form a chain. 
Above image shows the setting for the component on one of the 4 chain loops. A few things to point out:

* Since when we assemble the chain loop to each other, we want the loop to attach to another loop as its child, we check _Assemble To Parent_ flag. 
* Since we have totally 4 chain loops, and each one can assemble to the other 3 loops, we have 3 _Desired Poses_ **anchor_target** transforms as children of the other 3 loops respectively. 
* Since each chain loop is a rotational symmetric object, so assemble angle threshold just need to make sure its symmetry axis is aligned with desired pose. This axis is represented by the **z-axis** of the _Assemble Anchor_ on the loop. Therefore _Assemble Axis_ is set to be (0, 0, 1) to indicate z-axis of the **anchor** should match that of **anchor_target**.  
* Because when assembled, the chain loop is using  {% include tooltip.html tooltip="Cone" text="cone" %} joint,  a disabled [VG_Articulation](unity_component_vgarticulation.1.3.0.html) with  {% include tooltip.html tooltip="Cone" text="cone" %} joint is added to this game object and drag it to _Assemble Articulation_ entry.
* Because the chain loop initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), we don't need to assign _Disassemble Articulation_ entry.
* Because the chain loop initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), if the object initially is {% include tooltip.html tooltip="PhysicalObject" text="physical" %}, when disassembled it will always recover its physical properties automatically handled by VG. Therefore _Force Disassembled Physical_ flag does not need to be checked.
