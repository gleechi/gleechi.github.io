---
title: VirtualGrasp Onboarding Task1 - Light Switch
#tags: [getting_started]
keywords: casestudy, task1, vgonboarding
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_12_0
permalink: unity_vgonboarding_task1.0.12.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

{% include youtube.html id="_4IFXcsT9ME" %}

#### Interaction behaviors wanted

* We want to implement a button without using any physical components, but only use VirtualGrasp's kinematic {% include tooltip.html tooltip="Joint" text="joints" %}.
* Push once a button stay in lowered position, light turn on.
* Push another time button come back to original position, light turns off.

#### Tips for VR developers

* Which {% include tooltip.html tooltip="JointType" text="joint type" %} should be assigned to the button?
* Which {% include tooltip.html tooltip="StateAffordance" text="state affordance" %} to use to allow button be switch between these two states?
* How to determine when light should be on or off (use [GetObjectJointState](virtualgrasp_unityapi.0.12.0.html#getobjectjointstate) function)?
* More systemtic understanding can be obtained in [push interaction](push_interaction.0.12.0.html#background).

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp\Scenes\onboarding**.

```js
VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity
````

```js
//VirtualGrasp\Scenes\onboarding\Scripts\ToggleLight.cs:

using UnityEngine;
using VirtualGrasp;

/** 
 * ToggleLight shows as a tutorial on a non-physical two-stage button setup 
 * through VG_Articulation and how to use VG_Controller.GetObjectJointState to toggle light on and off. 
 */
public class ToggleLight : MonoBehaviour
{
    public Light m_light = null;
    private VG_Articulation m_articulation = null;

    void Start()
    {
        m_articulation = GetComponent<VG_Articulation>();
    }

    void Update()
    {
        float state;
        VG_Controller.GetObjectJointState(transform, out state);

        float disable_state = (m_articulation.m_discreteStates.Count == 0) ? m_articulation.m_min : m_articulation.m_discreteStates[0];
        if (state == disable_state) 
            m_light.enabled = false;
        else if (state == m_articulation.m_max)
            m_light.enabled = true;
    }
}

````
is the script showing how to use API function [GetObjectJointState](virtualgrasp_unityapi.0.12.0.html#getobjectjointstate) to get the object's {% include tooltip.html tooltip="JointState" text="joint state" %} in order to determine when the light is on or off. 

