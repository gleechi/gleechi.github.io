---
title: VirtualGrasp Onboarding Task2 - Radio Disassemble and Reassemble
#tags: [getting_started]
keywords: casestudy, task2, vgonboarding, assemble, disassemble, VG_Assemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_2_0
permalink: unity_vgonboarding_task2.1.2.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="x9emKcJleCk" %}-->

{% include youtube.html id="kMjdAaeFivE" %}

#### Interaction behaviors wanted

* Radio's body is physically reacting to the environment and gravity
* Radio's antenna should rotate in a cone-shaped joint range (using VG_Articulation {% include tooltip.html tooltip="Cone" text="cone joint" %}).
* Radio's two knobs are to be rotated like as a revolute joint with certain angular range (using VG_Articulation {% include tooltip.html tooltip="Revolute" text="revolute joint" %}).
* When one hand grasp the radio body, the other hand should be able to easily grasp knobs (NOTE this is a challenging object selection problem when a smaller object like knobs are close with a bigger radio object).  
* Can dissembling the antenna and two knobs from the radio body when hand grasping on them and pulling farther away. 
* After the antenna or two knobs are dissembled, they should also physically react to the environment and gravity.
* Can assemble the disassembled parts back to the radio.

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp\Scenes\onboarding**.

```js
VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity
````
#### Disassemble and re-assemble knobs and antenna

{% include image.html file="unity/unity_onboarding_task2_vg_assemble.png" alt="VG Assemble setup for antenna." caption="VG Assemble setup for antenna." %}

[VG_Assemble](unity_component_vgassemble.1.2.0.html) component is used for disassembling and re-assembling the two knobs and the antenna from the radio. 
Above image shows the setting for the component on antenna. A few things to point out:

* Since when we re-assemble the antenna to the radio, we want the antenna to attach to radio as radio's child, we check _Assemble To Parent_ flag. 
* And _Desired Poses_ is **antenna_anchor_target** transform that is radio's child.
* Since the antenna is a rotational symmetric object, so assemble angle threshold just need to make sure this symmetry axis is aligned with the desired pose. This axis is represented by the **z-axis** of the assigned _Assemble Anchor_ **anchor** transform. Therefore _Assemble Axis_ is set to be (0, 0, 1) to indicate z-axis of **anchor** should match that of **antenna_anchor_target**.  
* Because the antenna initially is at the assembled state (attached to the radio with {% include tooltip.html tooltip="Cone" text="cone" %} joint), we need to add a disabled [VG_Articulation](unity_component_vgarticulation.1.2.0.html) with  {% include tooltip.html tooltip="Floating" text="floating" %} joint to this game object and drag it to _Disassemble Articulation_ entry. (If an object initially is floating joint type, this is not needed.)
* Since initially the antenna is attached to the radio with a constrained joint type -- {% include tooltip.html tooltip="Cone" text="cone" %} joint, the object can not be {% include tooltip.html tooltip="PhysicalObject" text="physical" %}. Therefore if we want the object to become physical when it is disassembled, we need to check _Force Disassembled Physical_ flag. 

#### Change selection weight to make knobs easily selected

```js
//VirtualGrasp\Scenes\onboarding\Scripts\ChangeSelectionWeight.cs:

using UnityEngine;
using VirtualGrasp;

/** 
 * ChangeSelectionWeight shows as a tutorial on how to runtime change object
 * selection weight to affect how easy an object can be selected for interaction with VG.
 */
public class ChangeSelectionWeight : MonoBehaviour
{
    public Transform m_dependent_object;
    public float m_releasedWeight = 1.0f;
    public float m_graspedWeight = 20.0f;

    void Start()
    {
        VG_Controller.OnObjectFullyReleased.AddListener(ObjectReleased);
        VG_Controller.OnObjectGrasped.AddListener(ObjectGrasped);

        if (m_dependent_object == null)
            m_dependent_object = transform.parent;
    }

    void ObjectReleased(VG_HandStatus hand)
    {
        if (hand.m_selectedObject == m_dependent_object)
            VG_Controller.SetObjectSelectionWeight(transform, m_releasedWeight);
    }

    void ObjectGrasped(VG_HandStatus handStatus)
    {
        if (handStatus.m_selectedObject == m_dependent_object)
            VG_Controller.SetObjectSelectionWeight(transform, m_graspedWeight);        
    }
}

````
is the script showing how to use API function 
[SetObjectSelectionWeight](virtualgrasp_unityapi.1.2.0.html#vg_controllersetobjectselectionweight) to tune up and down the selection weight in runtime. 
This script is attached to the two knobs, and the main radio body would be **m_dependent_object**; as a result, once the radio is grasped by one hand, the selection weight of the two knobs will be tuned up to **m_graspedWeight** so that the knobs can be easily selected for grasping by the other hand. The logic may not be perfect, however the main goal in this script is to show the use cases of {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %}.

Note, in this example, even when we don't tune up selection weights on the knobs, the selection still works well. 



