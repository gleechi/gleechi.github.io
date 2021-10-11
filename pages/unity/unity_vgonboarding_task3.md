---
title: VirtualGrasp Onboarding Task3 - Container
#tags: [getting_started]
keywords: casestudy, task2, vgonboarding, dissemble
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_vgonboarding_task3.html
folder: mydoc
---

We have a series of VG onboarding tasks to show how to tackle different practical use cases in a VR application.

### Task Description
<iframe width="560" height="315" src="https://www.youtube.com/embed/97Bj8AgV8SY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Interaction behaviors wanted

* Initially the plate and all other floating objects are physical object, i.e. react to physics in the environment.
* After the user places the apple or other objects on the plate, we expect when the plate is moved, either by hand or through teleportation, the objects in the plate should follow stably along. 

#### Tips for VR developers

* How to let objects placed on plate to follow the plate stably without easily rolling and falling down due to physical reactions. Can we use **ChangeObjectJoint**?

#### Solution

In VirtualGrasp SDK, we packed the solution of this task in **VirtualGrasp\Scenes\onboarding**.

```js
VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity
````
is the unity scene showing how plate and apple are setup with physical properties using Unity's rigid body and collider components;
and ManageContainerObject.cs script is attached to plate as the container object.

```js
//VirtualGrasp\Scenes\onboarding\Scripts\ManageContainerObject.cs:

using System.Collections.Generic;
using VirtualGrasp;
using UnityEngine;

public class ManageContainerObject : MonoBehaviour
{
    /// A set off objects that are actively colliding with this one.
    private HashSet<Transform> m_collisions = new HashSet<Transform>();
    /// A map of objects that are attached to this one to their original parents.
    private Dictionary<Transform, Transform> m_parentCache = new Dictionary<Transform, Transform>();
    /// If dot product between velocity and down is large enough (ie. vectors are aligned).
    public float m_dropAlignment = 0.8f;

    private void Start()
    {
        // Register the some grasp event listeners
        VG_Controller.OnObjectFullyReleased.AddListener(OnObjectFullyReleased);
        VG_Controller.OnObjectGrasped.AddListener(OnObjectGrasped);
    }

    private void OnCollisionEnter(Collision collision)
    {
        // See if the object in collision is actually held by a hand (and is not a hand itself).
        bool valid_object = true;
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            if (hand.m_hand == collision.transform)
                valid_object &= false;
            if (hand.m_selectedObject == collision.transform && hand.IsHolding())
                valid_object &= false;
        }

        if (valid_object && // If it's valid ...
            collision.rigidbody != null && // and has a rigid body ...
            Vector3.Dot(collision.relativeVelocity.normalized, Vector3.down) > m_dropAlignment) // .. and if the object is dropped from somewhat above.
        {
            Attach(collision.transform);
            m_collisions.Add(collision.transform);
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        m_collisions.Remove(collision.transform);
    }

    private void OnObjectFullyReleased(Transform t)
    {
        if (m_collisions.Contains(t)) Attach(t);
    }

    private void OnObjectGrasped(VG_HandStatus hand)
    {
        if (hand.m_selectedObject.parent == transform && VG_Controller.GetObjectJointType(hand.m_selectedObject) != VG_JointType.FLOATING)
            Unattach(hand.m_selectedObject);
    }

    void Attach(Transform attachedObject)
    {
        Rigidbody rigidBody = attachedObject.GetComponent<Rigidbody>();
        Destroy(rigidBody);
        VG_Controller.ChangeObjectJoint(attachedObject, VG_JointType.FIXED);
        m_parentCache[attachedObject] = attachedObject.parent;
        attachedObject.SetParent(transform);
    }

    void Unattach(Transform attachedObject)
    {
        // If the object was floating before attaching it, recover this.
        if (VG_Controller.GetObjectJointType(attachedObject, true) == VG_JointType.FLOATING)
            VG_Controller.RecoverObjectJoint(attachedObject);
        else // Otherwise, we don't want the original state back.
            VG_Controller.ChangeObjectJoint(attachedObject, VG_JointType.FLOATING);
        
        Rigidbody rigidbody = attachedObject.gameObject.AddComponent<Rigidbody>();
        rigidbody.useGravity = true;
        attachedObject.SetParent(m_parentCache[attachedObject]);
    }
}


````
is the script showing how to use API function **ChangeObjectJoint** and **RecoverObjectJoint** 
to attach and unattach the object to the plate. 
Note that when an object is attached to the plate, its rigid body should be removed to avoid
object being moved by physical forces. 

