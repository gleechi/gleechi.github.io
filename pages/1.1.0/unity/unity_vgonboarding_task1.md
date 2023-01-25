---
title: VirtualGrasp Onboarding Task1 - Light Switch
#tags: [getting_started]
keywords: casestudy, task1, vgonboarding
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_1_0
permalink: unity_vgonboarding_task1.1.1.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="_4IFXcsT9ME" %}-->

{% include youtube.html id="BnoPclLBHCQ" %}

#### Interaction behaviors wanted

* We want to implement a button without using any physical components, but only use VirtualGrasp's kinematic {% include tooltip.html tooltip="Joint" text="joints" %}.
* Push once a button stay in lowered position, light turn on.
* Push another time button come back to original position, light turns off.

#### Tips for VR developers

* Which {% include tooltip.html tooltip="JointType" text="joint type" %} should be assigned to the button?
* Which {% include tooltip.html tooltip="StateAffordance" text="state affordance" %} to use to allow button be switch between these two states?
* How to determine when light should be on or off (use [GetObjectJointState](virtualgrasp_unityapi.1.1.0.html#getobjectjointstate) function)?
* More systemtic understanding can be obtained in [push interaction](push_interaction.1.1.0.html#background).

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
[LIBVIRTUALGRASP_UNITY_SCRIPT]
[HelpURL("https://docs.virtualgrasp.com/unity_vgonboarding_task1.html")]
public class ToggleLight : MonoBehaviour
{
    public GameObject m_light = null;
    public GameObject m_light2 = null;
    private VG_Articulation m_articulation = null;

    public AudioSource m_audioSourceOn;
    public AudioSource m_audioSourceOff;

    private float m_state;
    private bool m_binState = false;


    void Start()
    {
        if (TryGetComponent<VG_Articulation>(out m_articulation))
        {
            VG_Controller.GetObjectJointState(transform, out m_state);
            EvaluateState(m_state);
        }
    }

    void Update()
    {
        VG_Controller.GetObjectJointState(transform, out float newState);
        if (newState != m_state)
            EvaluateState(newState);
        m_state = newState;
    }

    void EvaluateState(float state)
    {
        if (state == m_articulation.m_min && m_binState)
        {
            m_binState = false;
            m_light.SetActive(false);
            m_light2.SetActive(false);
            m_audioSourceOff.Play();
        }
        else if (state == m_articulation.m_max && !m_binState)
        {
            m_binState = true;
            m_light.SetActive(true);
            m_light2.SetActive(true);
            m_audioSourceOn.Play();
        }
    }
}

````
is the script showing how to use API function [GetObjectJointState](virtualgrasp_unityapi.1.1.0.html#getobjectjointstate) to get the object's {% include tooltip.html tooltip="JointState" text="joint state" %} in order to determine when the light is on or off. 

