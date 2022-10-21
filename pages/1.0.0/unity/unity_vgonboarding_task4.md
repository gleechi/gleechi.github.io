---
title: VirtualGrasp Onboarding Task4 - Assemble-Dissemble with Articulation Body
#tags: [getting_started]
keywords: casestudy, task4, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_0_0
permalink: unity_vgonboarding_task4.1.0.0.html
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
 * AssembleVGArticulation shows as a tutorial on how to use the VG_Controller.ChangeObjectJoint function for
 * assemble and dissemble non-physical objects (objects without rigid body or articulation body).
 */
[LIBVIRTUALGRASP_UNITY_SCRIPT]
[HelpURL("https://docs.virtualgrasp.com/unity_vgonboarding_task5." + VG_Version.__VG_VERSION__ + ".html")]
public class AssembleVGArticulation : MonoBehaviour
{
    [Tooltip("When assemble, the new parent to assign to this object.")]
    public Transform m_newParent = null;
    [Tooltip("The target pose of the assembled object.")]
    public Transform m_desiredPose = null;
    [Tooltip("Threshold to assemble when object to Desired Pose is smaller than this value.")]
    public float m_assembleDistance = 0.05f;
    [Tooltip("Threshold to disassemble when sensor hand position to grasped hand position is bigger than this value.")]
    public float m_disassembleDistance = 0.5f;
    [Tooltip("The VG Articulation of constrained (non-FLOATING) joint type to switch to when assemble an object.")]
    public VG_Articulation m_assembleArticulation = null;

    [Tooltip("If provided give disassemble sound effect.")]
    public AudioSource m_disassembleSoundEffect;
    [Tooltip("If provided give assemble sound effect.")]
    public AudioSource m_assembleSoundEffect;

    private float m_timeAtDisassemble = 0.0F;
    private float m_assembleDelay = 1.0F;

    void Start()
    {
        if (m_assembleArticulation == null)
            VG_Debug.LogError("Has to assign an Assemble Articulation on " + this.transform.name);
        if (m_assembleArticulation.m_type == VG_JointType.FLOATING)
            VG_Debug.LogError("Assemble Articulation should be of a constrained joint type, can not be FLOATING on " + this.transform.name);
    }

    void Update()
    {
        assembleByJointChange();
        dessembleByJointChange();
    }

    void assembleByJointChange()
    {
        VG_JointType jointType;
        if ((Time.realtimeSinceStartup - m_timeAtDisassemble) > m_assembleDelay
           && (m_desiredPose.position - this.transform.position).magnitude < m_assembleDistance
           && VG_Controller.GetObjectJointType(this.transform, false, out jointType) == VG_ReturnCode.SUCCESS &&
           jointType == VG_JointType.FLOATING)
        {
            m_desiredPose.gameObject.SetActive(false);

            // Project object rotation axis to align to desired rotation axis.
            Quaternion q_raw = Quaternion.LookRotation(m_desiredPose.up, transform.forward);
            Quaternion q_nat = q_raw * Quaternion.Euler(0, 180, 0) * Quaternion.Euler(-90, 0, 0);
            this.transform.SetPositionAndRotation(m_desiredPose.position, q_nat);

            if (m_newParent != null)
                this.transform.SetParent(m_newParent);

            VG_ReturnCode ret = VG_Controller.ChangeObjectJoint(transform, m_assembleArticulation);
            if(ret != VG_ReturnCode.SUCCESS)
                VG_Debug.LogError("Failed to ChangeObjectJoint() on " + transform.name + " with return code " + ret);

            m_assembleSoundEffect?.Play();
        }
    }

    void dessembleByJointChange()
    {
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            VG_JointType jointType;
            if (hand.m_selectedObject == transform && hand.IsHolding()
                && VG_Controller.GetObjectJointType(transform, false, out jointType) == VG_ReturnCode.SUCCESS
                && jointType != VG_JointType.FLOATING)
            {
                VG_Controller.GetSensorPose(hand.m_avatarID, hand.m_side, out Vector3 sensor_pos, out Quaternion sensor_rot);
                float jointState = 0.0f;
                if (jointType == VG_JointType.REVOLUTE)
                    VG_Controller.GetObjectJointState(transform, out jointState);
                if (jointState == 0.0f && (sensor_pos - hand.m_hand.position).magnitude > m_disassembleDistance)
                {
                    m_desiredPose.gameObject.SetActive(true);
                    transform.SetParent(m_newParent.parent);
                    VG_ReturnCode ret = VG_Controller.RecoverObjectJoint(transform);
                    if (ret != VG_ReturnCode.SUCCESS)
                        VG_Debug.LogError("Failed to RecoverObjectJoint() on " + transform.name + " with return code " + ret);

                    m_timeAtDisassemble = Time.realtimeSinceStartup;
                    m_disassembleSoundEffect?.Play();
                }
            }
        }
    }
}

````


