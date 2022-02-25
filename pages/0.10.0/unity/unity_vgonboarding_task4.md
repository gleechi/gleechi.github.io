---
title: VirtualGrasp Onboarding Task4 - Assemble-Dissemble with Articulation Body
#tags: [getting_started]
keywords: casestudy, task4, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_10_0
permalink: unity_vgonboarding_task4.0.10.0.html
folder: mydoc
---

We have a series of VG onboarding tasks to show how to tackle different practical use cases in a VR application.

### Task Description

{% include youtube.html id="85btM4KdeNM" %}

#### Interaction behaviors wanted

* Initially the valve is a free moving physical object with Articulation Body component.
* When user grasp and moves it to a target desired position (indicated by the transparent valve), it will be assembled to this position and becomes a rotatable valve around the center.
* When user grasp the assembled valve and pull out to certain distance, the valve will become dissembled and freely movable again. 

#### Tips for VR developers

* This task is mainly to showcase VirtualGrasp's support on interaction with ArticulationBody. 

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

```js
//VirtualGrasp/Scenes/onboarding/Scripts/AssembleArticulationBody.cs:

using UnityEngine;
using VirtualGrasp;
using System.Collections.Generic;

/** 
 * AssembleArticulationBody shows as a tutorial on how to use VG to
 * assemble and dissemble objects through Unity's ArticulationBody.
 */
public class AssembleArticulationBody : MonoBehaviour
{
    public Transform m_newParent = null;
    public Transform m_desiredPose = null;
    public float m_assembleDistance = 0.05f;
    public float m_disassembleDistance = 0.5f;

    public ArticulationJointType m_jointType = ArticulationJointType.FixedJoint;
    public Vector3 m_anchorPosition = Vector3.zero;
    public Vector3 m_anchorRotation = new Vector3(90, 90, 0);
    public Vector3 m_parentAnchorPosition = new Vector3(0.298f, 0.158f, 0.268f);
    public Vector3 m_parentAnchorRotation = new Vector3(90, 90, 0);

    private ArticulationBody m_this_ab;
    private ArticulationBody m_parent_ab;

    private float timeAtDisassemble = 0.0F;
    private float assembleDelay = 1.0F;

    void Start()
    {
        gameObject.TryGetComponent<ArticulationBody>(out m_this_ab);
        if (m_newParent != null)
        {

            if(!m_newParent.TryGetComponent<ArticulationBody>(out m_parent_ab))
            {
                Debug.LogWarning("New parent " + m_newParent.name + " should have Articulation Body component, will add one in script");
                m_parent_ab = m_newParent.gameObject.AddComponent<ArticulationBody>();
            }
        }
        else
            Debug.LogError("Need to specify assembling New Parent!");
    }

    void Update()
    {
        assembleArticulationBody();
        dissembleArticluationBody();
    }

    void assembleArticulationBody()
    {
        if(m_this_ab == null || m_parent_ab == null)
        {
            Debug.LogError("Object do no have articulation body, so can't do articulation body based assembling!");
            return;
        }

        if ((Time.realtimeSinceStartup - timeAtDisassemble) > assembleDelay
            && (m_desiredPose.position - transform.position).magnitude < m_assembleDistance
            && transform.parent != m_newParent)
        {
            m_desiredPose.gameObject.SetActive(false);
            transform.SetPositionAndRotation(m_desiredPose.position, m_desiredPose.rotation);
            transform.SetParent(m_newParent);
            m_this_ab.jointType = m_jointType;
            m_this_ab.matchAnchors = false;
            m_this_ab.anchorPosition = m_anchorPosition;
            m_this_ab.anchorRotation = Quaternion.Euler(m_anchorRotation);
            m_this_ab.parentAnchorPosition = m_parentAnchorPosition;
            m_this_ab.parentAnchorRotation = Quaternion.Euler(m_parentAnchorRotation);
        }
    }

    void dissembleArticluationBody()
    {
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            if (hand.m_selectedObject == transform && hand.IsHolding() && transform.parent == m_newParent)
            {
                VG_Controller.GetSensorPose(hand.m_avatarID, hand.m_side, out Vector3 sensor_pos, out Quaternion sensor_rot);
                if ((sensor_pos - hand.m_hand.position).magnitude > m_disassembleDistance ) 
                {
                    m_desiredPose.gameObject.SetActive(true);
                    transform.SetParent(m_newParent.parent);
                    timeAtDisassemble = Time.realtimeSinceStartup;
                }
            }
        }
    }
}


````


