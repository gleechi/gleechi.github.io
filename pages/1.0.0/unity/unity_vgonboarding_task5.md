---
title: VirtualGrasp Onboarding Task5 - Assemble 
#tags: [getting_started]
keywords: casestudy, task5, vgonboarding, assemble, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_0_0
permalink: unity_vgonboarding_task5.1.0.0.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="TJ5T67fv6ys" %} -->

{% include youtube.html id="glCwt7WqCS8" %}


#### Interaction behaviors wanted

* We want to close the water bottle with the cap screwed on. 
* Neither the water bottle nor the cap are physical object, so can not use Unity's physical joint support.

#### Tips for VR developers

* VG_Articulation support creating joints on non-physical objects (objects without Rigidbody or ArticulationBody).


### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

```js
//VirtualGrasp/Scenes/onboarding/Scripts/AssembleVGArticulation.cs:

using UnityEngine;
using VirtualGrasp;
using System.Collections.Generic;

/** 
 * AssembleVGArticulation shows as a tutorial on how to use the VG_Controller.ChangeObjectJoint function for
 * assemble and dissemble non-physical objects (objects without rigid body or articulation body).
 */
public class AssembleVGArticulation : MonoBehaviour
{
    public Transform m_newParent = null;
    public Transform m_desiredPose = null;
    public float m_assembleDistance = 0.05f;
    public float m_disassembleDistance = 0.5f;
    public VG_Articulation m_assembleArticulation = null;

    private float timeAtDisassemble = 0.0F;
    private float assembleDelay = 1.0F;

    void Start()
    {
        
    }

    void Update()
    {
        assembleByJointChange();
        dessembleByJointChange();
    }

    void assembleByJointChange()
    {
        if ((Time.realtimeSinceStartup - timeAtDisassemble) > assembleDelay
           && (m_desiredPose.position - this.transform.position).magnitude < m_assembleDistance
           && VG_Controller.GetObjectJointType(this.transform, false) == VG_JointType.FLOATING)
        {
            m_desiredPose.gameObject.SetActive(false);
            this.transform.SetPositionAndRotation(m_desiredPose.position, m_desiredPose.rotation);

            if (m_newParent != null)
                this.transform.SetParent(m_newParent);

            VG_Controller.ChangeObjectJoint(transform, m_assembleArticulation);
        }
    }

    void dessembleByJointChange()
    {
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            if (hand.m_selectedObject == transform && hand.IsHolding()
                && VG_Controller.GetObjectJointType(transform) != VG_JointType.FLOATING)
            {
                VG_Controller.GetSensorPose(hand.m_avatarID, hand.m_side, out Vector3 sensor_pos, out Quaternion sensor_rot);
               
                if (VG_Controller.GetObjectJointState(transform) == 0.0f
                    && (sensor_pos - hand.m_hand.position).magnitude > m_disassembleDistance)
                {
                    m_desiredPose.gameObject.SetActive(true);
                    VG_Controller.RecoverObjectJoint(transform);
                    transform.SetParent(m_newParent.parent);

                    timeAtDisassemble = Time.realtimeSinceStartup;
                }
            }
        }
    }
}

````

is the script showing how to use API function [ChangeObjectJoint](virtualgrasp_unityapi.1.0.0.html#changeobjectjoint) and [RecoverObjectJoint](virtualgrasp_unityapi.1.0.0.html#recoverobjectjoint) to attach and unattach the cap on to the bottle. 