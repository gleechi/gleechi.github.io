---
title: VirtualGrasp Onboarding Task4 - Assemble-Dissemble with Articulation Body
#tags: [getting_started]
keywords: casestudy, task4, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_3
permalink: unity_vgonboarding_task4.1.6.3.html
folder: mydoc
---

{% include onboarding_task.html %}

### Task Description

<!--{% include youtube.html id="85btM4KdeNM" %}-->

{% include youtube.html id="JhqhdDnvMs8" %}


#### Interaction behaviors wanted

* Initially the valve is a free moving physical object with Articulation Body component.
* When user grasp and moves it to a target desired position (indicated by the transparent valve), it will be assembled to this position and becomes a rotatable valve around the center.
* When user grasp the assembled valve and pull out to certain distance, the valve will become dissembled and freely movable again. 

#### Tips for VR developers

* This task is mainly to showcase VirtualGrasp's support on interaction with ArticulationBody. 
* The assembling in this example is not making use of VG's non-physical joint systems, but purely of Unity's physical joint system provided by ArticulationBody component. To see how to use VG's joint system for assembling check out other assembling tasks in this onboarding scene.

### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp/Scenes/onboarding**.

```js
VirtualGrasp/Scenes/onboarding/VG_Onboarding.unity
````

```js
//VirtualGrasp/Scenes/onboarding/Scripts/AssembleArticulationBody.cs:

using UnityEngine;
using VirtualGrasp;

/** 
 * AssembleArticulationBody shows as a tutorial on how to use VG to
 * assemble and dissemble objects through Unity's ArticulationBody.
 */
[LIBVIRTUALGRASP_UNITY_SCRIPT]
[HelpURL("https://docs.virtualgrasp.com/unity_vgonboarding_task4." + VG_Version.__VG_VERSION__ + ".html")]
public class AssembleArticulationBody : MonoBehaviour
{
    public Transform m_newParent = null;
    public Transform m_desiredPose = null;
    public float m_assembleDistance = 0.05f;
    public float m_disassembleDistance = 0.5f;

    public ArticulationJointType m_jointType = ArticulationJointType.FixedJoint;
    public bool m_matchAnchors = true;
    public Vector3 m_anchorPosition = Vector3.zero;
    public Vector3 m_anchorRotation = Vector3.zero;
    public Vector3 m_parentAnchorPosition = Vector3.zero;
    public Vector3 m_parentAnchorRotation = Vector3.zero;

    public AudioSource m_turnWheelEffect;

    private ArticulationBody m_this_ab;
    private ArticulationBody m_parent_ab;

    private float timeAtDisassemble = 0.0F;
    private float assembleDelay = 1.0F;

    private float m_state = 0;

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

        // Uncomment for sound effect
        if(m_turnWheelEffect != null)
            InvokeRepeating("turnWheelEffect", 0.0F, .5F);
    }

    void LateUpdate()
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
            
            // Project object rotation axis to align to desired rotation axis.
            transform.SetPositionAndRotation(m_desiredPose.position, Quaternion.LookRotation(m_desiredPose.forward, transform.up));
            transform.SetParent(m_newParent);
            m_this_ab.jointType = m_jointType;
#if UNITY_2021_2_OR_NEWER
            m_this_ab.matchAnchors = m_matchAnchors;
#elif UNITY_2021_1
            m_this_ab.computeParentAnchor = m_matchAnchors;
#endif
            m_this_ab.anchorPosition = m_anchorPosition;
            m_this_ab.anchorRotation = Quaternion.Euler(m_anchorRotation);
            m_this_ab.parentAnchorPosition = m_parentAnchorPosition;
            m_this_ab.parentAnchorRotation = Quaternion.Euler(m_parentAnchorRotation);
        }
    }

    void turnWheelEffect()
    {
        if (transform.parent == m_newParent)
        {
            float newState = m_this_ab.jointPosition[0];

            if (Mathf.Abs(newState - m_state) > .3 && !m_turnWheelEffect.isPlaying)
            {
                if (!m_turnWheelEffect.isPlaying)
                    m_turnWheelEffect.Play();
            }
            else if (Mathf.Abs(newState - m_state) < .3 && m_turnWheelEffect.isPlaying)
            {
                m_turnWheelEffect.Stop();
            }

            m_state = newState;
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


