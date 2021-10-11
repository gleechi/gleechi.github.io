---
title: VirtualGrasp Onboarding Task1 - Light Switch
#tags: [getting_started]
keywords: casestudy, task1, vgonboarding
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_vgonboarding_task1.html
folder: mydoc
---

We have a series of VG onboarding tasks to show how to tackle different practical use cases in a VR application.

### Task Description
<iframe width="560" height="315" src="https://www.youtube.com/embed/_4IFXcsT9ME" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


#### Interaction behaviors wanted

* Push once a button stay in lowered position, light turn on
* Push another time button come back to original position, light turns off

#### Tips for VR developers

* Which <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">Joint Type</a> should be assigned to the button?
* Which <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a> to use to allow button be switch between these two states?
* How to determine when light should be on or off (use **GetObjectState** function)?
* More systemtic understanding can be obtained in explanations of [Push Interaction](push_interaction.html#background).

#### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp\Scenes\onboarding**.

```js
VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity
````
is the unity scene showing how [VG_Articulation](unity_component_vgarticulation.html) component is used to setup this object's articulation settings.

```js
//VirtualGrasp\Scenes\onboarding\Scripts\ToggleLight.cs:

using UnityEngine;
using VirtualGrasp;

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
        float state = VG_Controller.GetObjectJointState(transform);
        if (state == m_articulation.m_min) m_light.enabled = false;
        else if (state == m_articulation.m_max) m_light.enabled = true;
    }
}

````
is the script showing how to use API function GetObjectState() to get the object's
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointState}}">Joint State</a>
 in order to determine when the light is on or off. 

