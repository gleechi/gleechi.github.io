---
title: VirtualGrasp Onboarding Task2 - Dissemble
#tags: [getting_started]
keywords: casestudy, task2, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_vgonboarding_task2.html
folder: mydoc
---

We have a series of VG onboarding tasks to show how to tackle different practical use cases in a VR application.

### Task Description
<iframe width="560" height="315" src="https://www.youtube.com/embed/x9emKcJleCk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Interaction behaviors wanted

* Radio's body is physically reacting to the environment and gravity
* Radio's antenna should rotate in a cone-shaped joint range. (using Cone <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">Joint Type</a>)
* Radio's two knobs are to be rotated like as a revolute joint with certain angular range.
* When one hand grasp the radio body, the other hand should be able to easily grasp knobs (NOTE this is a challenging object selection problem when a smaller object like knobs are close with a bigger radio object).  
* Can dissembling the antenna and two knobs from the radio body when hand grasping on them and pulling farther away. 
* After the antenna or two knobs are dissembled, they should also physically react to the environment and gravity.

#### Tips for VR developers

* Which <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">Joint Type</a> should be assigned to the antenna and two knobs?
* How to use <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SelectionWeight}}">Selection Weight</a> to make small object like knobs that are near the big radio body easily selected and grasped?
* How to dissembling radio's parts using runtime change object joint types. 
* How to make the dissembled parts decoupled from radio and freely move and physically react to environment and gravity.

#### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp\Scenes\onboarding**.

```js
VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity
````
is the unity scene showing how [VG_Articulation](unity_component_vgarticulation.html) component is used to setup antenna and knobs' articulation settings.


```js
//VirtualGrasp\Scenes\onboarding\Scripts\ChangeSelectionWeight.cs:

using UnityEngine;
using VirtualGrasp;

public class ChangeSelectionWeight : MonoBehaviour
{
    public Transform m_dependent_object;
    public float m_releasedWeight = 1.0f;
    public float m_graspedWeight = 20.0f;

    void Start()
    {
        VG_Controller.OnObjectFullyReleased.AddListener(ObjectReleased);
        VG_Controller.OnObjectGrasped.AddListener(ObjectGrasped);
    }

    void ObjectReleased(Transform obj)
    {
        if(obj == m_dependent_object)
            VG_Controller.SetObjectSelectionWeight(transform, m_releasedWeight);
    }

    void ObjectGrasped(VG_HandStatus handStatus)
    {
        if(handStatus.m_selectedObject == m_dependent_object)
            VG_Controller.SetObjectSelectionWeight(transform, m_graspedWeight);
    }
}

````
is the script showing how to use API function **SetObjectSelectionWeight** to tune up and down the selection weight in runtime.
This script is attached to the two knobs, and the main radio body would be **m_dependent_object**; 
as a result, once the radio is grasped by one hand, the selection weight of the two knobs will be tuned up to **m_graspedWeight**
so that the knobs can be easily selected for grasping by the other hand. 
The logic may not be perfect, however the main goal in this script is to show 
the use cases of <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SelectionWeight}}">Selection Weight</a>.

```js
//VirtualGrasp\Scenes\onboarding\Scripts\DissembleWithDistance.cs:

using UnityEngine;
using VirtualGrasp;

public class DissembleWithDistance : MonoBehaviour
{
    public Transform new_parent;

    public float m_disassembleDistance = 0.2f;

    void Update()
    {        
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            if(hand.m_selectedObject == transform && hand.IsHolding()
                && VG_Controller.GetObjectJointType(transform) != VG_JointType.FLOATING)
            {
                VG_Controller.GetSensorPose(hand.m_avatarID, hand.m_side, out Vector3 sensor_pos, out Quaternion sensor_rot);
                if((sensor_pos - hand.m_hand.position).magnitude > m_disassembleDistance)
                {
                    VG_Controller.ChangeObjectJoint(transform, VG_JointType.FLOATING);
                    transform.SetParent(new_parent);

                    // Set this object as physical object
                    Rigidbody rigidbody = transform.gameObject.AddComponent<Rigidbody>();
                    rigidbody.useGravity = true;
                    if (transform.GetComponent<Collider>() == null)
                        transform.gameObject.AddComponent<BoxCollider>();
                }
            }
        }
    }
}

````
is the script to use API function **GetSensorPose** to check when sensor controlled wrist position (**sensor_pos**) is 
too far from the avatar hand's wrist position (**hand.m_hand.position**) by a certain threshold (**m_disassembleDistance**),
then API function **ChangeObjectJoint** is used to change object 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">Joint Type</a> to freely floating.



