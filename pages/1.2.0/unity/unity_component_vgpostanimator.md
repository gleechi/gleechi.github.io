---
title: VG_PostAnimator Component
keywords: component, animator, grasp, postanimator
sidebar: main_sidebar_1_2_0
permalink: unity_component_vgpostanimator.1.2.0.html
folder: mydoc
---

{% include important.html content="VG_PostAnimator will be obsolete and removed in next VG release. The functionality is now provided with the new components [VG_FingerAnimator](unity_component_vgfingeranimator.1.2.0.html), [VG_ObjectAnimator](unity_component_vgobjectanimator.1.2.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.2.0.html). See [Onboarding Task9](unity_vgonboarding_task9.1.2.0.html) to see an example of their uses." %}
 
## Description

VG_PostAnimator is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that exemplifies how you could overwrite ("post-animate") grasp animations that are generated by VirtualGrasp.

The emphasis here that this is merely an example, and that the important thing is that it is possible to overwrite grasp animations with your own animations 
during grasping by adding a listener to the [VG_Controller.OnPostUpdate](virtualgrasp_unityapi.1.2.0.html#onpostupdate) event.

{% include multiple_script.html %}

## Simple Use Case

In this simple example script, the VR trigger button (value between 0 and 1) is used to slerp the rotation of the index finger between the current bone rotation 
(generated by VirtualGrasp) and a manually defined target rotation. 

This is a use case that you may want to follow if you want to animate a finger push while you have an object in your hand (such as when using an electric tool). 

The video shows the behavior you would get when attaching a VG_PostAnimator to the Antenna object in the onboarding scene (VirtualGrasp\Scenes\onboarding\VG_Onboarding.unity).

<!--{% include image.html file="gifs/post_animator.gif" width="100%" alt="VG_PostAnimator" caption="Default VG_PostAnimator will modify the index finger bending." %}-->
 
{% include youtube.html id="khZ_An5_eDg" caption="Default VG_PostAnimator will modify the index finger bending." %}

```js

// VirtualGrasp/Scripts/VG_PostAnimator.cs

using UnityEngine;
using UnityEngine.XR;
using VirtualGrasp;

/** 
 * VG_PostAnimator exemplifies how you could overwrite (post-animate) grasp animations that are handled by VirtualGrasp.
 */
[LIBVIRTUALGRASP_UNITY_SCRIPT]
[HelpURL("https://docs.gleechi.com/unity_component_vgpostanimator.html")]
public class VG_PostAnimator : MonoBehaviour
{
    private Quaternion m_leftHandTargetRotation = Quaternion.Euler(14.47f, -274.42f, -348.29f);
    private Quaternion m_rightHandTargetRotation = Quaternion.Euler(14.47f, 274.42f, 348.29f);

    void Start()
    {
        VG_Controller.OnPostUpdate.AddListener(Animate);
    }

    private bool GetOtherButtonTrigger(VG_HandSide handSide, out float trigger)
    {
        // Receive the device used for this hand side, and receive the trigger value of ...
        InputDevice device = UnityEngine.XR.InputDevices.GetDeviceAtXRNode(handSide == VG_HandSide.LEFT ? XRNode.LeftHand : XRNode.RightHand);
        // ... the grip button if VG is using the trigger for grasping (or the other way around)
        return device.TryGetFeatureValue(VG_Controller.GetTriggerButton() == VG_VrButton.GRIP ? CommonUsages.trigger : CommonUsages.grip, out trigger);
    }

    public void Animate()
    {
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            // Check if it is this object that is held in the hand.
            if (hand.m_selectedObject != transform || !hand.IsHolding())
                continue;

            // Receive the trigger signal of the controller and the transform of the first (0) bone of the index finger (1).
            if (GetOtherButtonTrigger(hand.m_side, out float trigger) &&
                VG_Controller.GetFingerBone(hand.m_avatarID, hand.m_side, 1, 0, out Transform currentTransform) == VG_ReturnCode.SUCCESS)
            {
                // Modify the local transform by interpolating it between the current and the target rotation.
                currentTransform.localRotation = Quaternion.Slerp(hand.m_side == VG_HandSide.LEFT ?
                    m_leftHandTargetRotation : m_rightHandTargetRotation,
                    currentTransform.localRotation,
                    trigger);
            }
        }
    }
}

````

## Complex Use Case

Manually programming your animations will allow you to implement more complex use cases, such as creating finger animations on an articulated object, for example scissors.

{% include youtube.html id="SWekpa7OxHI" caption="You can customize VG_PostAnimator to more complex use cases." %}