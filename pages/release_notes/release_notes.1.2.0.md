---
title: Release Notes
keywords: release notes #, announcements, what's new, new features
sidebar: main_sidebar_1_2_0
permalink: release_notes.1.2.0.html
folder: mydoc
---


## V1.2.0 (2023-04-03)

##### Major Functionality Changes:

* [Hand Profiles](unity_component_vghandprofile.1.4.0.html) add a new functionality to allow developers to manually map customized hand bones (wrist and finger bones) to [Gleechi hand model](avatars.1.4.0.html#hand-model-standard). 

* Mirror hand control feature is added. Developers can set a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} to have mirror hand control either at initial [Avatars and Sensors](unity_component_myvirtualgrasp.1.4.0.html) setting, or in runtime through [SetAvatarMirrorHandControl](virtualgrasp_unityapi.1.4.0.html#vg_controllersetavatarmirrorhandcontrol) api function. 

* [VG_AnimationDriver](https://docs.virtualgrasp.com/unity_component_vganimationdriver.1.4.0.html) now can also be used with legacy input. **(fixed known issue from 1.1.0)**

* VirtualGrasp SDK moved over to [Custom Package](https://docs.unity3d.com/Manual/CustomPackages.html) structure, with SDK being a proper package and the Onboarding being an optionally installable "Sample." We are still unsure how this affects the Asset Store deployment through the Unity verification system, but will update as soon as we have a validated version. We will update potentially incorrect paths in this documentation then.

##### GUI / Component Changes:

* [My VirtualGrasp -> Avatars and Sensors](unity_component_myvirtualgrasp.1.4.0.html#avatars-and-sensors) shows clearer separation of multiple avatars, and also shows avtar's ID. 

* The [Baking Client](unity_component_vgbakingclient.1.4.0.html) has been visually optimized to make it easier to handle login and baking. 

* The [VG_EC_MouseHand](unity_vg_ec_mouse.1.4.0.html) controller has been adjusted so it can be used with both Legacy and new Input System.

* When using "NULL" as the origin name in any [VG_ControllerProfile](controllers.1.4.0.html#controller-profile) the origin will be hard reset to zero-origin even if an origin transform is provided in the MyVirtualGrasp component. This to assure that some controllers (such as the [VG_EC_MouseHand](unity_vg_ec_mouse.1.4.0.html)) do not use any origin offset.

##### API Changes:

* To support runtime register custom avatars, [RegisterReplayAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerregisterreplayavatar), [RegisterRemoteAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerregisterremoteavatar), and all overloaded RegisterSensorAvatar functions has a new optional "handProfile" input.

* [SetAvatarMirrorHandControl](virtualgrasp_unityapi.1.4.0.html#vg_controllersetavatarmirrorhandcontrol) api function is added to allow runtime specify a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} to have or not have mirror hand control.

##### Other / Internal Changes:

* VG_OculusHands_Profile is added in Resources/VG_HandProfiles/ to support OVR hand models which do not follow [the Gleechi hand model standard](avatars.1.4.0.html#hand-model-standard). Note developers do not need VirtualGrasp SDK to release a new hand profile to support any custom hand models, and please see [Hand Profiles](unity_component_vghandprofile.1.4.0.html) to learn how to create your own hand profile with hand bone maps.

* OculusIntegration sample scene is added (in Samples/OculusIntegration) to compare OVR hand controller with VG's Oculus integration. See [FAQ regarding OVR hand](faqs.1.4.0.html#i-want-to-use-use-ovr-hand-with-virtualgrasp-but-my-hands-can-not-grasp-any-object-why) for more explanation.

*  [VG_EC_OVRHand controller](unity_vg_ec_ovr.1.4.0.html) is added only for the OculusIntegration sample scene mentioned above.

* Fixed a bug: Solved memory leak and Unity crashing bug when repeatedly calling register and unregister avatars. **(fixed known issue from 1.1.0)**

* Fixed a bug: Solved RigidBody.iskinematic true runtime setting is lost problem when a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody is released from grasping. **(fixed known issue from 1.1.0)**

* Fixed a bug: The first overloaded function [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) when target is Revolute or Cone joint types limit angle is not converted to radian before passing to the VirtualGrasp library, causing limits appear to be much bigger than the set values. **(fixed known issue from 1.1.0)**

* Fixed a bug: When handover a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} from one hand to another, sometimes the receiving hands may drop together with the object. **(fixed known issue from 1.1.0)**

* Fixed a bug: When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraints of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. Now the physical constraints will be respected. **(fixed known issue from 1.1.0)**

##### Update to VG Core library:
* No update.

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraint of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. 

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* VG_Articulation on joint gizmo has a bug for Revolute joint, the gizmo shown joint range with left-handed system that is opposite to the direction of object rotation. Also for both Revolute and Prismatic joint, the gizmo is moving together with object, not respecting the initial zero pose. 

* When mirror hand control is enabled, the disabling of hand still are controlled by missing sensor signal from same side. 

{% include_relative release_notes.1.1.0.md %}