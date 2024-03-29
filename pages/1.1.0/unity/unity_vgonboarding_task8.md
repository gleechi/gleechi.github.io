---
title: VirtualGrasp Onboarding Task8 - Screw Assemble 
#tags: [getting_started]
keywords: casestudy, task8, vgonboarding, assemble, disassemble, VG_Assemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_1_0
permalink: unity_vgonboarding_task8.1.1.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

{% include youtube.html id="oTKGq1XSd-c" %}

#### Interaction behaviors wanted

* We want to be able to use a screw driver to assemble two screws onto a screw-box (a box with two screw holes).
* Basically we can form a chain of objects: screw-box --> screw --> screw driver, with "-->" pointing to the child.

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**. 

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

#### Assemble and disassemble screw driver to screws

{% include image.html file="unity/unity_onboarding_task8_vg_assemble.png" alt="VG Assemble setup for screw driver." caption="VG Assemble setup for screw driver." %}

[VG_Assemble](unity_component_vgassemble.1.1.0.html) component is used for assembling and disassembling the screw driver to the head of screw. 
Above image shows the setting for the component on the screw driver. A few things to point out:

* Since when we assemble the screw driver to the screw, we want the driver to attach to the screw as its child, we check _Assemble To Parent_ flag. 
* Since we have 2 screws, 2 _Desired Poses_ **tool_anchor_target** transforms are assigned, and each is a child of one of the two screws. 
* Since the screw driver is a rotational symmetric object, so assemble angle threshold just need to make sure its symmetry axis is aligned with desired pose. This axis is represented by the **z-axis** of the _Assemble Anchor_ on the driver. Therefore _Assemble Axis_ is set to be (0, 0, 1) to indicate z-axis of the **anchor** should match that of **tool_anchor_target**.  
* Because when assembled, the screw driver is to be fixed on the screw head, so we don't need to assign _Assemble Articulation_ entry since by default assembling switches the object joint to the {% include tooltip.html tooltip="Fixed" text="fixed" %} joint type.
* Because the screw driver initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), we don't need to assign _Disassemble Articulation_ entry.
* Because the screw driver  initially is at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), if the object initially is {% include tooltip.html tooltip="PhysicalObject" text="physical" %}, when disassembled it will always recover its physical properties automatically handled by VG. Therefore _Force Disassembled Physical_ flag does not need to be checked.


#### Assemble and disassemble screws to screw box

{% include image.html file="unity/unity_onboarding_task8_vg_assemble_screw.png" alt="VG Assemble setup for screws." caption="VG Assemble setup for screws." %}

[VG_Assemble](unity_component_vgassemble.1.1.0.html) component is also used for assembling and disassembling the screw to the screw box. 
Above image shows the setting for the component on each of the two screws. A few things to point out:

* Since when we assemble the screw to the screw box, we want the screw to attach to box as box's child, we check _Assemble To Parent_ flag. 
* And there are two _Desired Poses_  **screw_target1** and **screw_target2** transforms that are children of the screw box.
* Since the screw is a rotational symmetric object, so assemble angle threshold just need to make sure its symmetry axis is aligned with desired pose. This axis is represented by the **z-axis** of the screw object itself, since _Assemble Anchor_ is not assigned. Therefore _Assemble Axis_ is set to be (0, 0, 1) to indicate z-axis of the object should match that of the two screw targets.
* Because when assembled, the screw is using  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint with non-zero screw rate to simulate screwing effect in the real world. A disabled [VG_Articulation](unity_component_vgarticulation.1.1.0.html) with  {% include tooltip.html tooltip="Revolute" text="revolute" %} joint is added to this game object and drag it to _Assemble Articulation_ entry.
* Because when disassembling a screw in the real world, we need to unscrew to loosen it, this requirement is simulated by checking _Disassemble On Zero State_ flag.
* Because the screws initially are at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), we don't need to assign _Disassemble Articulation_ entry.
* Because the screws initially are at the disassembled state ({% include tooltip.html tooltip="Floating" text="floating" %} joint), if the object initially is {% include tooltip.html tooltip="PhysicalObject" text="physical" %}, when disassembled it will always recover its physical properties automatically handled by VG. Therefore _Force Disassembled Physical_ flag does not need to be checked.