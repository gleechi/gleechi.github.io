---
title: Release Notes
#tags: [getting_started]
keywords: release notes #, announcements, what's new, new features
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_2_0
permalink: release_notes.1.2.0.html
redirect_from: release_notes.html
folder: mydoc
---

<!-- (Template)
## Vxx.xx.xx-rcx (xxxx-xx-xx)

##### Major Functionality Changes:
* 

##### GUI / Component Changes:
* 

##### API Changes:
* 

##### Other / Internal Changes:
*

##### Update to VG Core library:
* 

##### Known Issues:
*
-->

## V1.2.0 (2023-04-05)

##### Major Functionality Changes:

* [Hand Profiles](avatars.1.2.0.html#hand-profiles) add a new functionality to allow developers to manually map customized hand bones (wrist and finger bones) to [Gleechi hand model](avatars.1.2.0.html#hand-model-standard). 

* Mirror hand control feature is added. Developers can set a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} to have mirror hand control either at initial [Avatars and Sensors](unity_component_myvirtualgrasp.1.2.0.html#avatars-and-sensors) setting, or in runtime through [SetAvatarMirrorHandControl](virtualgrasp_unityapi.1.2.0.html#vg_controllersetavatarmirrorhandcontrol) api function. 

* [VG_AnimationDriver](https://docs.virtualgrasp.com/unity_component_vganimationdriver.1.2.0.html) now can also be used with legacy input. **(fixed known issue from 1.1.0)**

* VirtualGrasp SDK moved over to [Custom Package](https://docs.unity3d.com/Manual/CustomPackages.html) structure, with SDK being a proper package and the Onboarding being an optionally installable "Sample." We are still unsure how this affects the Asset Store deployment through the Unity verification system, but will update as soon as we have a validated version. We will update potentially incorrect paths in this documentation then.

* [Prefabs "SensorAvatar" and "SensorAndReplayAvatars"](unity_component_myvirtualgrasp.1.2.0.html#sensoravatar-and-sensorandreplayavatars-prefabs) are added in Runtime\Resources\Prefabs\ to provide easy setup of [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html) with GleechiRig. 

##### GUI / Component Changes:

* [My VirtualGrasp -> Avatars and Sensors](unity_component_myvirtualgrasp.1.2.0.html#avatars-and-sensors) shows clearer separation of multiple avatars, and also shows avtar's ID. 

* The [Baking Client](unity_component_vgbakingclient.1.2.0.html) has been visually optimized to make it easier to handle login and baking. 

* The [VG_EC_MouseHand](unity_vg_ec_mousehand.1.2.0.html) controller has been adjusted so it can be used with both Legacy and new Input System.

* When using "NULL" as the origin name in any [VG_ControllerProfile](controllers.1.2.0.html#controller-profile) the origin will be hard reset to zero-origin even if an origin transform is provided in the MyVirtualGrasp component. This to assure that some controllers (such as the [VG_EC_MouseHand](unity_vg_ec_mousehand.1.2.0.html)) do not use any origin offset.

##### API Changes:

* To support runtime register custom avatars, [RegisterReplayAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerregisterreplayavatar), [RegisterRemoteAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerregisterremoteavatar), and all overloaded RegisterSensorAvatar functions has a new optional "handProfile" input.

* [SetAvatarMirrorHandControl](virtualgrasp_unityapi.1.2.0.html#vg_controllersetavatarmirrorhandcontrol) api function is added to allow runtime specify a {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %} to have or not have mirror hand control.

##### Other / Internal Changes:

* VG_OculusHands_Profile is added in Resources/VG_HandProfiles/ to support OVR hand models which do not follow [the Gleechi hand model standard](avatars.1.2.0.html#hand-model-standard). Note developers do not need VirtualGrasp SDK to release a new hand profile to support any custom hand models, and please see [Hand Profiles](avatars.1.2.0.html#hand-profiles) to learn how to create your own hand profile with hand bone maps.

* OculusIntegration sample scene is added (in Samples/OculusIntegration) to compare OVR hand controller with VG's Oculus integration. See [FAQ regarding OVR hand](faqs.1.2.0.html#i-want-to-use-use-ovr-hand-with-virtualgrasp-but-my-hands-can-not-grasp-any-object-why) for more explanation.

* VG Onboarding sample scene include a tool tip box instructing users on how to navigate in the scene. 

* [VG_EC_OVRHand controller](unity_vg_ec_ovrhand.1.2.0.html) is added only for the OculusIntegration sample scene mentioned above.

* Fixed a bug: Solved memory leak and Unity crashing bug when repeatedly calling register and unregister avatars. **(fixed known issue from 1.1.0)**

* Fixed a bug: Solved RigidBody.iskinematic true runtime setting is lost problem when a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody is released from grasping. **(fixed known issue from 1.1.0)**

* Fixed a bug: The first overloaded function [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerchangeobjectjoint) when target is Revolute or Cone joint types limit angle is not converted to radian before passing to the VirtualGrasp library, causing limits appear to be much bigger than the set values. **(fixed known issue from 1.1.0)**

* Fixed a bug: When handover a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} from one hand to another, sometimes the receiving hands may drop together with the object. **(fixed known issue from 1.1.0)**

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* VG main loop runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraint of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. 

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* VG_Articulation on joint gizmo has a bug for Revolute joint, the gizmo shown joint range with left-handed system that is opposite to the direction of object rotation. Also for both Revolute and Prismatic joint, the gizmo is moving together with object, not respecting the initial zero pose. 

* When mirror hand control is enabled, the disabling of hand still are controlled by missing sensor signal from same side. 

## V1.1.0  (2023-03-07)

##### Major Functionality Changes:
* **Breaking change:** How grasp db (.db file) is loaded into the project has been refactored:
  * In previous versions grasp db is unrecognized file for Unity, and now it is recognized as an asset if it is put into Assets folder. And any .db files inside Assets folder will be recognized as grasp db files. 
  * In previous versions once baking is finished the output grasps.db file will be put into StreamingAssets folder and will be automatically loaded into the project when playing. Now each time grasp baking is finished the output will be a new file "Assets/VG_Grasps/grasp-[hash].db" with random hash. 
  * And if you want to use the new baking result, developers need to set it into [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.2.0.html#grasp-db). 
  * If you want to use previously baked grasp db inside the StreamingAssets folder in previous VG versions, you need to move it into Assets folder, and drag this grasp db into [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.2.0.html#grasp-db). 

* **Breaking change for Pro version:** How sensor db (.sdb file) is loaded into the project has been refactored:
  * In previous versions sensor db is unrecognized file for Unity, and now it is recognized as an asset if it is put into Assets folder. And any .sdb files inside Assets folder will be recognized as sensor db assets. 
  * In previous versions [VG_Recorder in VG1.0.0](unity_component_vgrecorder.1.0.0.html) output recorded .sdb file into StreamingAssets folder. Now [VG_Recorder](unity_component_vgrecorder.1.2.0.html) needs to enter complete _New Recording Path_ end with .sdb file to save recorded data. 
  * When replaying recorded .sdb file, this file should be dragged into [VG_Recorder](unity_component_vgrecorder.1.2.0.html)  _Replay Recording_ entry. 

* For Pro version: [VG_Recorder](unity_component_vgrecorder.1.2.0.html) allows to assign multiple _Replay Avatars_. This allows you to replay data on a pair of hands that are represented by [separate hand models](avatars.1.2.0.html#separate-hand-models). **(fixed known issue from 1.0.0)**

* For tiny objects that need precision grasps, the grasp quality now varies depending on which {% include tooltip.html tooltip="InteractionType" text="interaction type" %} is chosen for the object. When {% include tooltip.html tooltip="JumpGrasp" text="jump grasp" %} is used on an object, the grasp will have more accurate finger placement on the object but the object will have larger rotation when "jumping" into the hand. When {% include tooltip.html tooltip="TriggerGrasp" text="trigger grasp" %} is used, the grasp will have less accurate finger placement with the benefit of less hand offset when moved towards the grasping pose. (See [Grasp Interaction Type](grasp_interaction.1.2.0.html#grasp-interaction-type) section.)

* Fixed a bug: "VirtualGrasp --> Make Interactables Readable" helper function mentioned in [Object Setup](unity_get_started_objects.1.2.0.html) now works, and you will see in console output which object(s) has been processed. **(fixed known issue from 1.0.0)**

##### GUI / Component Changes:

* [VG_FingerAnimator](unity_component_vgfingeranimator.1.2.0.html), [VG_ObjectAnimator](unity_component_vgobjectanimator.1.2.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.2.0.html) are added to support easy creation of animation of in-hand manipulation of articulated objects. See [VG onboarding task 9](unity_vgonboarding_task9.1.2.0.html) to learn an example use case.

* Fixed a bug: [SetSensorActive](virtualgrasp_unityapi.1.2.0.html#vg_controllersetsensoractive) now works properly. **(fixed known issue from 1.0.0)**

* Fixed a bug: In previous version, if an object has constrained {% include tooltip.html tooltip="Joint" text="joint" %}, pushing **Step grasp** button on [VG_GraspEditor](unity_component_vggraspeditor.1.2.0.html) to review primary grasps on this object did not work. Now it works. **(fixed known issue from 1.0.0)**

##### API Changes:

* Added two overloaded functions, [GetReplayAvatarID](virtualgrasp_unityapi.1.2.0.html#vg_controllergetreplayavatarid-1) and [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.2.0.html#vg_controllergetsensorcontrolledavatarid-1), to provide two avatar ids when two avatars are used to represent left and right hands respectively. 

* Added [GetCurrentGesture](virtualgrasp_unityapi.1.2.0.html#vg_controllergetcurrentgesture) api function. 

* Previously [SwitchGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerjumpgraspobject) only work on objects with {% include tooltip.html tooltip="Floating" text="floating" %} joint, now it works on all objects including those with constrained (non-{% include tooltip.html tooltip="Floating" text="floating" %}) joint types. 

##### Other / Internal Changes:
* Fixed a bug: When an object is held in hand(s), runtime changes of physical properties of Rigidbody or ArticulationBody will be kept after this object is fully released. **(fixed known issue from 1.0.0)**
* [Task2 radio disassemble](unity_vgonboarding_task2.1.2.0.html) and [task7 chain assemble](unity_vgonboarding_task7.1.2.0.html) switched to use the new [VG_Assemble](unity_component_vgassemble.1.2.0.html) component. The old scripts DisassembleWithDistanc.cs and ChainAssembleVGArticulation.cs are removed. 
* [Task7 chain assemble](unity_vgonboarding_task7.1.2.0.html) switched to use the chain loop instead of previous the wrench. 
* [VG onboarding task 8](unity_vgonboarding_task8.1.2.0.html) was added to show case how [VG_Assemble](unity_component_vgassemble.1.2.0.html) is used to assemble or disassemble screw with a screw driver to a box.  
* [VG onboarding task 9](unity_vgonboarding_task9.1.2.0.html) was added to show case how to use the newly added three components, [VG_FingerAnimator](unity_component_vgfingeranimator.1.2.0.html), [VG_ObjectAnimator](unity_component_vgobjectanimator.1.2.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.2.0.html) to create animation of in-hand manipulation of articulated objects.
* VG onboarding scene now switches to use GRIP button as the **Grasp Button** in [MyVirtualGrasp -> Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#global-grasp-interaction-settings). This is to support [VG onboarding task 9](unity_vgonboarding_task9.1.2.0.html) to use TRIGGER button for animating the manipulation of the plier part.
* Fixed a bug: While a hand grasps a physical object to collide with another physical object, if any colliding object's collider is disabled, the controller grasping the object will continue to have vibrating haptic feedback until hand releases the object. Now it is fixed so that when the collider is disabled, the vibration will stop. **(fixed known issue from 1.0.0)**

* When a chain of objects are connected through VG constrained joints, in the previous version, if one hand grasps an upstream object, and the other grasps a distal object, only the distal object (with constrained but movable joint, i.e. non-Fixed) is movable by the hand. In this version (1.2.0) grasping the distal joint will move its upstream movable joint. This change allows (for example in [VG onboarding task 8](unity_vgonboarding_task8.1.2.0.html)) on a chain like box (floating) --> screw (revolute) --> screw driver (fixed), users could grasp box with one hand, and grasp and rotate the distal object, screw driver, with another hand in order to rotate screw into the box.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* Multiplayer (_not available in free or pro versions_) with VG network message still can not solve complete object sync for new player registration.

* A few events such as [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer 
(_not available in free or pro versions_) scenes.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* You can not use _OVR Hand_ (which can be found in the Oculus Integration under Oculus\VR\Scripts\Util\OVRHand.cs) together with VG controllers at the moment, as they both are independently affecting the hand model. 

* The [VG_AnimationDriver](https://docs.virtualgrasp.com/unity_component_vganimationdriver.1.2.0.html) is currently relying on the Unity "XR Interaction Toolkit" package. We thus have a dependency of this system in the current 1.2.0, but will resolve this in the next so it can also be used with legacy input.

* When a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody is released from grasping, the RigidBody.iskinematic always switch to false even if the developer has changed iskinematic to true when object is grasped.

* The first overloaded function [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerchangeobjectjoint) has a bug on joint limit setting of Revolute and Cone joint types because the limit angle in degree missed to be converted to radian before passing to the VirtualGrasp library.

* When handover a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} from one hand to another, sometimes the receiving hands may drop together with the object. 

* Repeated runtime calling of register and unregister of avtars will cause Unity crash due to memory leaks.  

* When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraint of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. 

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

## V1.0.0(2022-12-07)

##### Major Functionality Changes:
* **Breaking change:** The Sensor/Avatar configuration in the MyVirtualGrasp component has been refactored:
  * While before, a list of Avatars could be assigned to each element of a list of Sensors (see [MyVirtualGrasp 0.15.0](unity_component_myvirtualgrasp.0.15.0.html#sensors--controllers)), 
  * now maximally 2 Sensor setups can be assigned to each element of a a list of Avatars (see [MyVirtualGrasp 1.2.0](unity_component_myvirtualgrasp.1.2.0.html#avatars-and-sensors)).
  * If you are updating to this version from an older version, **you need to re-configure your MyVirtualGrasp component**.

* **Breaking change:** The old [GetNumGrasps](virtualgrasp_unityapi.0.15.0.html#vg_controllergetnumgrasps) api function changed name to [GetNumGraspsInDB](virtualgrasp_unityapi.1.2.0.html#vg_controllergetnumgraspsindb) to avoid potentially confusing user to think GetNumGrasps is to obtain currently executed grasps on an object. 
  * Together with this change, a new api function [GetNumPrimaryGraspsInDB](virtualgrasp_unityapi.1.2.0.html#vg_controllergetnumprimarygraspsindb) is added to give number of enabled {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} in the grasp DB. 

* **Breaking change:** Enum [VG_AvatarType](virtualgrasp_unityapi.0.15.0.html#vg_avatartype) has been removed. The old [RegisterAvatar](virtualgrasp_unityapi.0.15.0.html#vg_controllerregisteravatar) api functions have been split upto 3 functions depending on avatar type:
  * [RegisterSensorAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerregistersensoravatar) for sensor controlled avatars, where several overloads exist. The most common is to register an avatar with a single sensor setup without any network output. A secondary sensor setup and network output can be added. 
  * [RegisterRemoteAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerregisterremoteavatar) for remote controlled avatars in multiplayer applications, and
  * [RegisterReplayAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerregisterreplayavatar) for replay controlled avatars.

* [VG_HandProfiles](avatars.1.2.0.html#hand-profiles) were introduced to simplify the external controller mapping for custom hand models.

* [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerchangeobjectjoint) (two overloaded functions) and [RecoverObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerrecoverobjectjoint) do not have any function signature change. However from this version, VG will internally remove Rigidbody or ArticulationBody on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} if the function call intends to change object joint to a constrained joint type (non-{% include tooltip.html tooltip="Floating" text="floating" %}), and recover just removed Rigidbody or ArticulationBody when it changes back to  {% include tooltip.html tooltip="Floating" text="floating" %} joint type. This change makes it convenient for Unity developers to benefit from VG's [object articulation](object_articulation.1.2.0.html) system on both physical and non-physical environments.

* Added "ensemble physical object" support. That is when assembling two {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} through [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerchangeobjectjoint), as an example shown in [VG Onboarding Task7](unity_vgonboarding_task7.1.2.0.html), grasping the child objects (when child became non-physical due to object change to constrained joint type), the parent which is still a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} will follow as if the parent-child has become an ensemble physical object.

* When an object's Rigidbody component has Rigidbody.isKinematic true, VG will consider this object as a non-{% include tooltip.html tooltip="PhysicalObject" text="physical object" %}. (In previous versions whenever an object has Rigidbody component, even when it is kinematic, VG considers the object physical resulting in some unwanted interaction behaviors.)

##### GUI / Component Changes:
* Only one enabled [VG_Articulation](unity_component_vgarticulation.1.2.0.html) component is allowed now, and the enabled component reflects the current [object articulation](object_articulation.1.2.0.html) status.
* [VG_Articulation](unity_component_vgarticulation.1.2.0.html) for constrained joint types now allows selection of "Motion Type" to be Limited or Free, where Free means there is no limitation along the constrained dof(s) of this joint. 
* [VG_GraspEditor](unity_component_vggraspeditor.1.2.0.html) 
  * The prefab has improved 3D shape and texture, and
  * has been moved to ThirdParty/VirtualGrasp/Resources/GraspEditor/ to separate it from the Onboarding demo scene.
  * VG_GraspEditor script exposed an option _Editing Interaction Type_ to allow developers to choose the main {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to use when adding primary grasps. 
* "VirtualGrasp" Menu cleanup. Some obsolete entries were removed.
* [VG_Articulation](unity_component_vgarticulation.1.2.0.html), [VG_Interactable](unity_component_vginteractable.1.2.0.html) and [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html) scripts are deactivated during runtime to better reflect that changes to them are only valid in editor mode.
* Grasp and Release animation speeds in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html) GUI integer fields were replaced by range sliders.

##### API Changes:

* Fixed a bug:: if runtime [UnRegisterAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllerunregisteravatar) and then reregister again, the reregistered avatar will lose sensor control. 
* Added [VG_GestureType](virtualgrasp_unityapi.1.2.0.html#vg_gesturetype) enum and [MakeGesture](virtualgrasp_unityapi.1.2.0.html#vg_controllermakegesture) api switched to use this enum instead of previously using [VG_GraspType](virtualgrasp_unityapi.1.2.0.html#vg_grasptype). **(fixed known issue from 0.15.0)**
* All API functions properly guarded if VG is actually active.
* Removed SetPhysicalObject, OnAfterReset, OnBeforeReset and ResetObject and ResetAllObjects API functions.
* Added [GetObjectSelectionWeight](virtualgrasp_unityapi.1.2.0.html#vg_controllergetobjectselectionweight) and [GetAvatarSpecificObjectSelectionWeight](virtualgrasp_unityapi.1.2.0.html#vg_controllergetavatarspecificobjectselectionweight) API functions.
* Added [SetRecordingStatesOnAvatar](virtualgrasp_unityapi.1.2.0.html#vg_controllersetrecordingstatesonavatar) API function.
* Some minor tweaks to VG_GraspEditor, VG_Highlighter, and VG_Recorder.

##### Other / Internal Changes:
* Fixed a bug: when [OnGraspTriggered](virtualgrasp_unityapi.1.2.0.html#vg_controllerongrasptriggered) event invoked, sometimes m_selectedObject is null.
* Fixed a bug: sometimes an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object's {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %} becomes negative causing this object not interactable. 
* If an object is set to afford INDEX_PUSHABLE interaction, VG library will switch its {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to {% include tooltip.html tooltip="StickyHand" text="STICKY HAND" %} to avoid some unneccssary debug outputs.
* [VG onboarding task 5](unity_vgonboarding_task5.1.2.0.html) added an additional prefab, "Task5_bottle_with_rigidbody", in the onboarding scene to show the same AssembleVGArticulation.cs also works on the bottle and cap when they are physical objects. 
* Added [VG onboarding task 7](unity_vgonboarding_task7.1.2.0.html) showing off using VG Articulation to assemble a chain with physical objects.  
* For [VG onboarding task4](unity_vgonboarding_task4.1.2.0.html) and [task5](unity_vgonboarding_task5.1.2.0.html), the function for assembling has improved computation of desired object rotation; the assembling and dissasembling code are called in LateUpdate instead of Update to sync with player input. 
* Multiplayer (_not available in free or pro versions_) VG support now allows multiple players grasping on the same object at the same time, and also works with complex object settings.
* Explicit asset database refresh added when VG creates files (such as files for mesh baking input and output).
* Adjusted In-Editor tutorials to follow the new changes in the VG API and GUI.
* Improved the project file structure. Among others made it possible to delete the example onboarding folder and resources to make the plugin lighter without affecting VG functionality.
* Fixed a bug: {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered. **(fixed known issue from 0.15.0)**
* Fixed a bug: If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. **(fixed known issue from 0.15.0)**
* The .NET TargetFrameworkVersion has been downgraded from 4.7.2 to 4.7.1 since it caused some issues for Unity+VSCode users.
* Fixed a bug: when pause a VR app with Occulus button or remove headset, the grasp pose is lost. 
* Improved the status sync of [VG_Articulation](unity_component_vgarticulation.1.2.0.html) on a Game Object with the interactability of that objects.
* Fixed a bug: the second avatar registered has twisted finger bones. 
* Improved the VG_MainScript inspector DebugSettings to become a proper foldout menu. 
* Fixed a bug: crashing when [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerjumpgraspobject), [SwitchGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerswitchgraspobject), or [TogglePrimaryGraspOnObject](virtualgrasp_unityapi.1.2.0.html#vg_controllertoggleprimarygrasponobject) is called on an object without mesh assigned to it.


* Improved the grasp interaction on object that has rotating {% include tooltip.html tooltip="JointType" text="joint types" %}. 
* Improved the grasp interaction on floating objects with multiple hands. 
* Completed {% include tooltip.html tooltip="Planar" text="planar" %} joint features by adding {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) support. **(fixed known issue from 0.15.0)**
* Reduced dynamic grasp finger-object penetration when pinch grasp small elongated objects.
* Fixed a bug: hand twisting when registering multiple avatars of same structure was fixed.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* Multiplayer (_not available in free or pro versions_) with VG network message still can not solve complete object sync for new player registration.

* A few events such as [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer 
(_not available in free or pro versions_) scenes.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* [VG_Recorder](unity_component_vgrecorder.1.2.0.html) only allows to assign one _Replay Avatar_, which makes it not work if you have [separate hand models](avatars.1.2.0.html#separate-hand-models) when using custom avatar supported by VG **Pro version**.  

* [SetSensorActive](virtualgrasp_unityapi.1.2.0.html#vg_controllersetsensoractive) does not have effect. If you set it inactive, the avatar's hands are still controlled and moved by the sensor / controller. 

* "VirtualGrasp --> Make Interactables Readable" helper function mentioned in [Object Setup](unity_get_started_objects.1.2.0.html) is not working. For now you have to manually check “Read/Write enabled” checkbox in the model inspector of your object in order to interact with the object or bake grasp.

* When an object is held in hand(s), runtime changes of physical properties of Rigidbody or ArticulationBody get lost once this object is fully released.

* If an object has constrained {% include tooltip.html tooltip="Joint" text="joint" %}, pushing **Step grasp** button on [VG_GraspEditor](unity_component_vggraspeditor.1.2.0.html) to review primary grasps on this object does not work.

* While a hand grasps a physical object to collide with another physical object, if any colliding object's collider is disabled, the controller grasping the object will continue to have vibrating haptic feedback until hand releases the object.

* You can not use _OVR Hand_ (which can be found in the Oculus Integration under Oculus\VR\Scripts\Util\OVRHand.cs) together with VG controllers at the moment, as they both are independently affecting the hand model. 

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

## V0.15.0(2022-07-27)

##### Major Functionality Changes:
* **Breaking change:** The sensor configuration in MyVirtualGrasp has been refactored:
  * Each controller profile (earlier VG_AutoSetup) has been ported into a ScriptableObject of type [VG_ControllerProfile](unity_component_myvirtualgrasp.1.2.0.html#controller-profile) (in Resources/ExternalControllers), uncluttering the [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html#sensors--controllers) interface.
  * To resolve update issues: for a sensor in avatar in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html#sensors--controllers), just drag and drop the controller profile .asset you want to use into the "Profile" slot.
  * You can customize the profiles fully now.
  * The profile supports list of controller names, separated by ';', in order of priorization. For example "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.
  * VG_AutoSetup has been removed from the API and GUI.
  * Origin transform has been kept in MyVirtualGrasp to allow overwrite of the name-based origin in the [VG_ControllerProfile](unity_component_myvirtualgrasp.1.2.0.html#controller-profile).

* **Breaking change:** VG_SynthesisMethod has been removed.
  * [VG_SynthesisMethod](grasp_interaction.1.2.0.html#grasp-synthesis-method) has been closely coupled to the [VG_InteractionType](grasp_interaction.1.2.0.html#grasp-interaction-type) that could be set globally (in [MyVirtualGrasp->Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#global-grasp-interaction-settings)) or object-specific (in [VG_Interactable](unity_component_vginteractable.1.2.0.html)).
  * Some combinations had limited usecases, thus now the [VG_SynthesisMethod](grasp_interaction.1.2.0.html#grasp-synthesis-method) is implicitely set automatically based on the [VG_InteractionType](grasp_interaction.1.2.0.html#grasp-interaction-type). Only JUMP_PRIMARY_GRASP will result in a STATIC GRASP; all other [VG_InteractionTypes](grasp_interaction.1.2.0.html#grasp-interaction-type) will result in a DYNAMIC_GRASP.
  * GetSynthesisMethodForObject, SetGlobalSynthesisMethod, SetSynthesisMethodForSelectedObject, and SetSynthesisMethodForObject removed.

* **Breaking change:** [VG_GraspStudio](unity_component_vggraspstudio.0.14.0.html) related script, resources and prefab have been removed, and is replaced with [VG_GraspEditor](unity_component_vggraspeditor.1.2.0.html) which is a much simpler interface that can be used in runtime in any client’s unity project. 

##### GUI / Component Changes:
* [Avatar Model Field](unity_component_myvirtualgrasp.1.2.0.html#sensors--controllers) removed to unclutter the interface. We always assume humanoid hand models for now.
* If your version supports networking (Pro feature), you can now enable [DebugSettings->UseNetworkIDs](unity_component_myvirtualgrasp.1.2.0.html#debug-settings) to set network ID for avatar's left/right hand (through [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.2.0.html#sensors--controllers)), and set network ID for object (through [VG_Articulation](unity_component_vgarticulation.1.2.0.html)).
* [VG_Articulations](unity_component_vgarticulation.1.2.0.html) / [VG_Interactables](unity_component_vginteractable.1.2.0.html) will be grayed out during runtime to make clear that changing them has no effect. To change them, use the adequate API functions.
* All changes triggered by API functions that change [VG_Articulations](unity_component_vgarticulation.1.2.0.html) or [VG_Interactable](unity_component_vginteractable.1.2.0.html) (except [RecoverObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerrecoverobjectjoint)) are now reflected in the Inspector components.
* The control flags (that were a list of checkboxes in each Sensor before) have been replaced with a nicer VG_SensorControlFlags [Flags] enum. Due to the change above related to [VG_ControllerProfile](unity_component_myvirtualgrasp.1.2.0.html#controller-profile), they were also moved into VG_ControllerProfile assets.
* Slightly re-ordered some [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#global-grasp-interaction-settings) in MyVirtualGrasp.
* VG_ExternalController cleared up and simplified.
* Bugfix: when anchor of VG_Articulation is not set, no change needs to be reflected on anchor when calling API functions such as ChangeObjectJoint.

##### API Changes:
* Uncluttered API from a number of classes and enums that did not need to be public.
* TOGGLE_SYNTHESIS and TOGGLE_INTERACTION removed from [VG_EditorAction](virtualgrasp_unityapi.1.2.0.html#vg_editoraction).
* [GetBroadcastSignal](virtualgrasp_unityapi.1.2.0.html#vg_controllergetbroadcastsignal) -- if your version supports networking (Pro feature) -- was extended with a flag argument to be able to pick out specific parts of the network signal.
* [SetAvatarSpecificObjectSelectionWeight](virtualgrasp_unityapi.1.2.0.html#vg_controllersetavatarspecificobjectselectionweight) and [ClearAvatarSpecificObjectSelectionWeights](virtualgrasp_unityapi.1.2.0.html#vg_controllerclearavatarspecificobjectselectionweights) added, allowing to specify different selection preferences on an object for different avatars.
* [SetObjectJointState](virtualgrasp_unityapi.1.2.0.html#vg_controllersetobjectjointstate) added to set an articulated object's state in runtime.
* Formerly deprecated SetGestureDuration and SetPushAngleThreshold are removed.
* Formerly deprecated ResetObject and ResetAllObjects are removed.

##### Other / Internal Changes:
* The .NET TargetFrameworkVersion has been downgraded from 4.8 to 4.7.2 since it caused some issues for Unity+VSCode users.
* Debug messages that come from the native VG library to the console have been equipped with "context" as well (if applicable), meaning that selecting the message will highlight the GameObject the message relates to.
* New external controller "UnityInteractionHand" added that supports controller supported by Unity's action-based [Unity Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/index.html) (together with "XRI Default Input Actions.inputactions" in Resources).
* [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.2.0.html) runtime optimizations.
* Bugfix: rig registration now also considers hidden bones.

##### Update to VG Core library:

* Dramatic runtime performance optimization for dynamic grasping
* Improved pinch dynamic grasp on small objects. **(fixed known issue from 0.14.0)**
* Always make [SwitchGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerjumpgraspobject) succeed to grasp the target object. **(fixed known issue from 0.14.0)**
* Fixed a crashing bug: when an object and all its upstream objects have FIXED VG_Articulation joint, when grasped by two hands, when one hand releases crash happens. **(fixed known issue from 0.14.0)**
* Fixed a crashing bug: networking objectSignal will not crash anymore when invalid key is provided.

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) as yet. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.1.2.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.1.2.0.html#vg_grasptype). 

* When using the [VG_GraspEditor](unity_component_vggraspeditor.1.2.0.html) on Android, the grasp database is not modified. We recommend for now to do all grasp editing in the Unity Editor.

## V0.14.0 (2022-06-17)

##### Major Functionality Changes:
* **Breaking change:** [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#vg_controllerchangeobjectjoint) is extended with one additional input parameter "new_anchor_transform". 
* {% include tooltip.html tooltip="PhysicalObject" text="Physical objects" %} are allowed to have disabled VG_Articulation components with any constrained joint types. Note the enabled VG_Articulation can only have Floating joint type.
* Customized {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %} (different from default value 1.0f) will be recovered when object is switched from hidden to selectable again to enable interaction.

##### GUI / Component Changes:
* SteamHand.cs added as new external controller to support any controllers supported through SteamVR (for example Knuckles).
* When using finger tracking devices, {% include tooltip.html tooltip="FingerControlType" text="Finger Control Type" %} option -- "BY_ANIMATION" is disabled, so only recommended BY_SENSOR_FULL_DOFS is used.
* GUI issues of some Unity versions resolved by making lists [NonReorderable].
* Pause / Resume replay of recorded sensor data control is added to [VG_Recorder](unity_component_vgrecorder.1.2.0.html) component: Shift + Replay Sequence Key is used to pause or resume replay.
* [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html)'s elements have been re-ordered. For example: controllers at top to be closer to AutoSetup, GraspButton section removed and merged into Interaction settings.
* All AutoSetup options have been renamed to better reflect the names of the [external controllers](unity_component_vgexternalcontrollermanager.1.2.0.html#vg_externalcontroller-class).

##### API Changes:
* Added [OnObjectPushed](virtualgrasp_unityapi.1.2.0.html#vg_controlleronobjectpushed) event.
* Added [OnGraspTriggered](virtualgrasp_unityapi.1.2.0.html#vg_controllerongrasptriggered) event.
* Added [SwitchGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerswitchgraspobject) API function to allow directly switch grasped object. 
* Removed [SelectObject](virtualgrasp_unityapi.0.13.0.html#vg_controllerselectobject) API function since if VR developers choose to select object differently from [the object selection mechanism in VG](grasp_interaction.1.2.0.html#from-object-selection-to-grasp-synthesis) the result will not integrate well with the subsequent {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} process provided by VirtualGrasp. 
* [GetTriggerButton](virtualgrasp_unityapi.0.13.0.html#vg_controllergettriggerbutton) has been renamed to [GetGraspButton](virtualgrasp_unityapi.1.2.0.html#vg_controllergetgraspbutton) to make naming consistent with "Grasp Button" option in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#global-grasp-interaction-settings) interface.

##### Other / Internal Changes:
* Onboarding scene object models are improved and sound effect added.
* Guard mesh and rig are compatible when registering avatars. 
* Using special characters for object name in Unity is allowed and won't affect VG functionality anymore. 
* A couple of text optimizations to the VirtualGrasp Tutorials to improve understanding.
* Bugfix to avoid NullReference if a ForceReleasedObject is deleted in the same frame.

##### Update to VG Core library 0.11.0:
* Fixed bug that is examplified in [onboarding Task 3](#unity_vgonboarding_task5.1.2.0.html): after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. **(fixed known issue from 0.13.0)**
* Fixed bug on if game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.2.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. **(fixed known issue from 0.13.0)**
* Fixed bug on if an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. **(fixed known issue from 0.13.0)**
* Two hands grasp interaction with an object is improved. Both hands now contribute to the position and rotation changes of the grasped object.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.1.2.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.1.2.0.html#vg_grasptype). 

* [ResetAllObjects](virtualgrasp_unityapi.1.2.0.html#vg_controllerresetallobjects) and [ResetObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerresetobject) are not working properly. 

* [SwitchGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#vg_controllerjumpgraspobject) may fail due to bad position of the target object with respect to the hand. 

* Crashing bug: when an object and all its upstream objects have FIXED VG_Articulation joint, when grasped by two hands, when one hand releases crash happens.

## V0.13.0 (2022-05-23)

##### Major Functionality Changes:

* The AutoSetup function was optimized by adding it to each single sensor. No need for indexing sensors anymore.

##### GUI / Component Changes:

* VirtualGrasp menu re-organized for better usability.
* Some VirtualGrasp menu functions were made obsolete/removed: "Create VG Scene," "Convert object tags to VG_Articulations,"
* The "About" (VirtualGrasp) window was made fixed size.
* A "Welcome" window was added that can be access from the VirtualGrasp menu. It will automatically open if it is detected that XR Plugin Management is not installed, but used in the scene. The choice to install the UnityXR package and the Unity Tutorial package is provided to the user.
* MyVirtualGraspBurst was removed.
* In VG_Highlighter, if no shader is assigned, the included "RimLight" shader will be used.

##### API Changes:

* All functions that were "XYZAtRuntime()" functions (such as RegisterAvatarAtRuntime()) have been renamed by removing that suffix (such as to RegisterAvatar()).

##### Other / Internal Changes:

* A more appealing environment was added to the VG_Onboarding scene.
* A version check was added to the BakingClient to inform you if a newer version of VG is available for download.
* SDK was successfully tested with Unity 2022.1.0b16.
* Some 3D models in the VG_Onboarding scene were simplied and optimized.
* Additional .xml files have been packaged along the .dll libraries to expose the comments / summaries for the API into the coding environment.
* Creating a VG_Editor scene can only be done when XR Management is installed and a vg_tmp directory exists.
* Unity Tutorial Framework dependency handled. Version >=2.0 needs to be installed to run VG Unity tutorials.
* physicsDefaultContactOffset removed from DebugSettings. We won't fiddle with your project settings anymore.
* Some graphical adjustments to the onboarding scene.
* Allowed to get rid of the VG welcome window if you want to.
* A number of warnings that were not really warnings were removed.

##### Update to VG Core library 0.10.0:

* Fixed bug on new recording sensor recording using [VG_Recorder](unity_component_vgrecorder.1.2.0.html) is pending the data to earlier recordings. (**fixed known issue from 0.12.0**)
* Fixed bug on successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.2.0.html) can lead to crashing. (**fixed known issue from 0.12.0**)
* Fixed bug on the 2nd method -- pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.1.2.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". (**fixed known issue from 0.12.0**)
* Fixed bug on runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. (**fixed known issue from 0.12.0**)

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.2.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* There is an Inspector GUI artifact in VG_MainScript/Sensors, but it is a known [Unity issue](https://issuetracker.unity3d.com/issues/first-array-element-expansion-is-broken-for-arrays-that-use-custom-property-drawers).

* In [onboarding Task 3](#unity_vgonboarding_task5.1.2.0.html), there is a bug after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. This will not happen however if you first grasp bottle then later another hand grasp the cap. We have identified cause and the problem will be fixed in V1.2.0.

## V0.12.0(2022-04-14)

##### Major Functionality Changes:

*  [VG_BakingClient](unity_component_vgbakingclient.1.2.0.html) has been overhauled with support of _Prepare project_ in the same GUI without the need to move to [Debug Settings](debug_files.1.2.0.html) if there are no runtime spawned {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects. 

##### GUI / Component Changes:

* AutoSetup enum name for Oculus finger tracking was changed from "Quest_FT" to "Oculus_FT" to conform with the file names and avoid confusion.
* Fixed confusion of disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description) component. Now, if the component is added but disabled (unchecked) the object will not be {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. Runtime enabling or disabling this component will make the object interactable or uninteractable respectively. However note that it is more efficient to change object's interactable status by [SetObjectSelectionWeight](virtualgrasp_unityapi.1.2.0.html#setobjectselectionweight).  (**fixed known issue from 0.11.1**)

##### API Changes:

* There are no API changes. 

##### Other / Internal Changes:

* Updated GleechiHands with better shader and material, as well as bone structure for finger pose mapping and grasp interaction (**fixed known issue from 0.11.1**).
* Updated Unity tutorials for VG baking client. 
* Bugfix on if two hands trigger grasp on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} at the exact same moment, the hands will form grasps, but the object freeze and can not be moved by hands. (**fixed known issue from 0.11.1**)

##### Update to VG Core library 0.9.0:

* Bugfix on unreliable grasp and release triggering for finger tracking solutions OCULUS_FT. (**fixed known issue from 0.11.1**)
* Bugfix on if two hands grasp on a non-physical FLOATING object, when one hand releases, the other hand could have a big offset from sensor position. (**fixed known issue from 0.11.1**)

##### Known Issues:

* New recording sensor recording using [VG_Recorder](unity_component_vgrecorder.1.2.0.html) is pending the data to earlier recordings.

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.2.0.html) can lead to crashing.

* The 2nd method -- pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.1.2.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". 

* Runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. 

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* [GetReplayStartWristPose](virtualgrasp_unityapi.1.2.0.html#getreplaystartwristpose) does not give accurate wrist pose. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.2.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

## V0.11.1 (2022-04-11)

##### Major Functionality Changes:

* **Breaking change**: Avatar IDs that were before the array index have been replaced by the Unity instance ID of the SkinnedMeshRenderer that relates to the avatar. The VG API is providing helper functions and the SDK scripts have been adjusted accordingly. Check out [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.2.0.html#getsensorcontrolledavatarid), [GetReplayAvatarID](virtualgrasp_unityapi.1.2.0.html#getreplayavatarid), and [GetAvatarID](virtualgrasp_unityapi.1.2.0.html#getavatarid). 
* Released Gleechi's first original avatar in VirtualGrasp/Resources/GleechiHands. This replaces earlier released OcculusHands, so in the VG SDK that support only one avatar, only GleechiHands are supported.
* Added {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %} support on [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description). See VG Onboarding [Task6](unity_vgonboarding_task6.1.2.0.html) to show the example use. 

##### GUI / Component Changes:

* AutoSetup "External" string for Oculus finger tracking was changed from "QuestHand" to "OculusHand" to conform with the file names and avoid confusion.
* Bugfix on AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.1.2.0.html#vg_externalcontroller-class) you like to use. (**fixed known issue from 0.10.1**)
* [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description) has been overhauled as a dynamic component to improve user experience. 
* Replay and Remote checkboxes for avatar are only shown if the VG version supports this feature.
* [VG_Interactable](unity_component_vginteractable.1.2.0.html) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to allow specifying object-specific throwing power that overwrite those set in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#global-grasp-interaction-settings).
* [VG_Recorder](unity_component_vgrecorder.1.2.0.html) has improved file management so that users can optionally provide in _Recording Filename_ with either a single file name like "MyRecordingFile", or a folder and a file name like "MyRecordingFolder/MyRecordingFile". Also adding the file extension ".sdb" is only optional.

##### API Changes:

* **Breaking change**: [GetObjectJointState](virtualgrasp_unityapi.1.2.0.html#getobjectjointstate) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointState will be invalid.
* **Breaking change**: [GetObjectJointType](virtualgrasp_unityapi.1.2.0.html#getobjectjointtype) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointType will be invalid.
* [SetAvatarActive](virtualgrasp_unityapi.1.2.0.html#setavataractive) added an optional argument: resetPos.
* Added [GetObjectSecondaryJointState](virtualgrasp_unityapi.1.2.0.html#getobjectsecondaryjointstate) which provide {% include tooltip.html tooltip="JointState" text="joint state" %} along yaxis of joint anchor for {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %}. 
* Added api functions to set velocity scales for throwing: [SetGlobalThrowVelocityScale](virtualgrasp_unityapi.1.2.0.html#setglobalthrowvelocityscale), [SetThrowVelocityScaleForSelectedObject](virtualgrasp_unityapi.1.2.0.html#setthrowvelocityscaleforselectedobject), [SetThrowVelocityScaleForObject](virtualgrasp_unityapi.1.2.0.html#setthrowvelocityscaleforobject), [SetGlobalThrowAngularVelocityScale](virtualgrasp_unityapi.1.2.0.html#setglobalthrowangularvelocityscale), [SetThrowAngularVelocityScaleForSelectedObject](virtualgrasp_unityapi.1.2.0.html#setthrowangularvelocityscaleforselectedobject), [SetThrowAngularVelocityScaleForObject](virtualgrasp_unityapi.1.2.0.html#setthrowangularvelocityscaleforobject). 
* Added [GetAvatarID](virtualgrasp_unityapi.1.2.0.html#getavatarid) to receive the ID of an avatar.
* Added [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.2.0.html#getsensorcontrolledavatarid) to receive the ID of the sensor-controlled avatar.
* Added [GetReplayAvatarID](virtualgrasp_unityapi.1.2.0.html#getreplayavatarid) to receive the ID of the replay avatar (if replaying is supported by the VG version).
* Added [UnregisterAvatarAtRuntime](virtualgrasp_unityapi.1.2.0.html#unregisteravataratruntime) to allow deleting avatars. (This is most relevant for multiplayer use case.)

##### Other / Internal Changes:

* Bugfix on [OnObjectSelected](virtualgrasp_unityapi.1.2.0.html#onobjectselected) event is not invoked for object with Index Pushable {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}.
* Bugfix on [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#jumpgraspobject) call. (**fixed known issue from 0.10.1**)
* Bugfix on after an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose. (**fixed known issue from 0.10.1**)
* Bugfix on physical avatar when grasping {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with {% include tooltip.html tooltip="StickyHand" text="sticky hand" %} interaction type object and hand is grandually moving away.
* Further performance optimization of selecting which objects need to be synced between Unity and VG.
* Improved grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider. Note however still Unity physical material with smaller friction should be used for desired sliding behaviors. (**fixed known issue from 0.10.1**)

* Provide error message when trying to use an controller but not enabling its #define (e.g., VG_USE_LEAP_CONTROLLER).
* Provide error signal if {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object is labeled as Static.
* Provide error signal if start a scene without providing SkeletalMesh for avatar setup. 
* Provide error message if you are on Mac that Mac is not supported.

* All #defines that enable controllers with dependencies on third party plugins have been prefixed with VG_ (e.g., USE_LEAP_CONTROLLER is now VG_USE_LEAP_CONTROLLER) to avoid conflicts with non-VG defines.
* Onboarding scene added [Task6](unity_vgonboarding_task6.1.2.0.html) to showcase VirtualGrasp's newly added support of {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joints" %}. 
* Added first Unity tutorials.

##### Update to VG Core library 0.8.0:

* Bugfix for physical avatar index finger push gesture formation is not smooth. (**fixed known issue from 0.10.1**)
* Improved pinch grasp on small objects. (**fixed known issue from 0.10.1**)
* Bugfix for when hand form index finger push gesture grasp synthesis adopted push gesture problem.
* Bugfix for [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#jumpgraspobject) crash on unbaked object problem. 

##### Known Issues:

* There is a problem of unreliable grasp and release triggering for finger tracking solutions OCULUS_FT. 

* If two hands grasp on a non-physical FLOATING object, when one hand releases, the other hand could have a big offset from sensor position.

* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.

* If two hands trigger grasp on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} at the exact same moment, the hands will form grasps, but the object freeze and can not be moved by hands. This is difficult to reproduce but still could happen.

* The newly released GleechiHands does not have perfect mapping of real finger poses when using finger tracking solutions like OCULUS_EXT and LEAP_EXT. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, then there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.2.0.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.2.0.html#changeobjectjoint) as yet. 

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.2.0.html) can lead to crashing.

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

## V0.10.1 (2022-03-01)

##### Major Functionality Changes:

* **Breaking change**: Removed support of using VG_Articulation component with constrained {% include tooltip.html tooltip="Joint" text="joints" %} (non-FLOATING joint) on objects with Rigidbody. Developers are encouraged to use [Unity Joints](https://docs.unity3d.com/Manual/Joints.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html) for physical joints.
* **Breaking change**: in [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description), "Pivot" changed name to "Anchor" to be more consistent with the terminology used by [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html). And "Push Pivot" changed name to "Push Direction" to be more descriptive. Due to the name change, the reference can be lost and need to be reassigned.
* More stable grasp interaction with {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} and better throwing experiences. 

##### GUI / Component Changes:

* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#grasp-interaction-settings) changed variable name "Grasp Speed" to "Grasp Animation Speed" and "Release Speed" to "Release Animation Speed". The default values for them are reduced to 0.05 (from 0.1) and 0.1 (from 0.2) second respectively to make grasp and release more snappy. The minimum values for both are reduced to 0.01 second (from 0.1 second).
* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.2.0.html#grasp-interaction-settings) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to control power of throw on grasped objects. 
* [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description) editing is disabled when object has Rigidbody component. (Was disabled when object has ArticulationBody component in version 0.9.6)
* Made VG_MainScript abstract since one should only use a child class (such as MyVirtualGrasp).
* Improved handling of AutoSetup when a VG_MainScript is created (such as adding a sensor instead of complaining it has not been added). 
* [MyVirtualGrasp/Avatars](unity_component_myvirtualgrasp.1.2.0.html#avatars) added "Replay" check to indicate if this avatar is to be used for sensor replay. If not checked, it will be controlled by sensor / controller. 

##### API Changes:

* **Breaking change**: VG_Controller.SetProcessedByFrame() function is removed. If you want to set an avatar for sensor replay, you can specify the avatar for replay by checking _Replay_ in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.2.0.html#autosetup--sensors) component. 

##### Other / Internal Changes:

* Event handling bugfix: OnObjectFullyReleased do not trigger on objects that are not grasped. 
* Onboarding scene [Task3](unity_vgonboarding_task3.1.2.0.html) improved ManageContainerObject.cs script.
* Onboarding scene added [Task4](unity_vgonboarding_task4.1.2.0.html) showcase VirtualGrasp's support of interaction with ArticulationBodys. 
* Onboarding scene added [Task5](unity_vgonboarding_task5.1.2.0.html) showcase VirtualGrasp's support of object assembly with VG_Articulation without rely on physics. 
* Endpoints for CABVG cloud baking updated to new server.
* Hidden affordances (such as after switching a VG_Articulation from revolute joint to fixed joint) are ignored as they should be.
* Recording files added to StreamingAssets.
* Bugfix when objects are moved to a different parent which has not been registered.

##### Update to VG Core library 0.7.0:

* Default hand pose animation is improved.
* Dyamic Grasp rejection rate is improved.
* Improved hand palm colliders for physical avatar.
* Removed the controller hand offset when runtime change a grasped object's VG Articulation to FLOATING joint type.

##### Known Issues (To Be Fixed In Next Release)

* Index finger push gesture formation is not smooth when avatar is set to be physical.
* [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.1.2.0.html#jumpgraspobject) call.
* After an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose.
* Grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider shows obvious non-smooth behavior due to some artificial manipulation of object velocities. 
* AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.1.2.0.html#vg_externalcontroller-class) you like to use.

##### Known Issues:

* Since Unity 2019 or earlier versions do not have [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html), these earlier versions of Unity is not supported.
* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.2.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.2.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small objects may have unatural finger placement.
* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.2.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.


## V0.9.6 (2022-02-15)

##### Major Functionality Changes:

* **Breaking change**: Prefabs GleechiLib and GleechiLibBurst removed. You are expected to just insert a VG_MainScript component (such as MyVirtualGrasp) on a GameObject of your choice.
* Grasp .db will be handled automatically, no manual deployment needed anymore (UploadGraspDB menu entry removed).
* Removed ObjectIdentifiers. The single and only component to mark objects as interactable is VG_Articulation. This should not break earlier use of VG_Interactable as Unity will create missing VG_Articulation component through RequireComponent requirement.
* Performance speed up by handling only subset of close-by objects.
* Added 

##### GUI / Component Changes:

* GraspStudio optimized and extended (see [VG_GraspStudio](unity_component_vggraspstudio.1.2.0.html)).
* Helper tooltips adjusted after documentation being transferred to docs.virtualgrasp.com.
* Disabling VG_Articulation editing when ArticulationBody is on object.
* Adjusted auto-setup offsets for provided hand model when using UnityXR.

##### API Changes:

* OnObjectFullyReleased event carries VG_HandStatus instead of Transform, aligning with all other VG events.
* VG_AutoSetup.QUEST renamed to VG_AutoSetup.UNITYXR
* VG_VrButton extended with GRIP_OR_TRIGGER to enable both buttons for grabbing.
* VG_Controller.SetObjectAffordances() added to change object affordances in runtime.

##### Other / Internal Changes:

* Event handling order bugfix: OnObjectReleased() called before OnObjectFullyReleased()
* All assets (onboarding scene) provided as Prefabs.
* .scn files also saved when using Save Debug Edit.
* Avatar Bone management optimized.
* Removed Unity Garbage Collection during Editor time.
* Initial support for Unity ArticulationBodies.
* Improved upon {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} handling.
* Improved upon physical hand handling.

##### Update to VG Core library 0.6.6:

* Added support to interact with objects with [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html) components. 
* For non-physical objects (objects without RigidBody or ArticulationBody), grasping a child object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} will also move the parent non-physical object, and the movement will propagate back to upstream non-physical objects as long as they are connected through constrained {% include tooltip.html tooltip="Joint" text="joints" %}. 
* DG can grasp on the inner structure of a complex object, for example a driving wheel. 
* Improved fitting of physical avatar finger colliders.

##### Known Issues:

* When grasping freely movable {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %}, movement with the object is suboptimal with observable wobbling effects. This is to be fixed in next release. 
* When throwing a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %}, the object velocity is suboptimal. This is to be fixed in next release.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small object may have unatural finger placement.

## V0.9.5 (2022-01-14)

##### GUI / Component Changes:

* Grasp DB file for baking can now be adjusted in scriptable object VG_VirtualGraspDbFile.
* All objects and hand included as Prefabs and used as Prefabs in VG_Onboarding scene.

##### Other / Internal Changes:

* Bugfix that if loading .db at start fails, it will not overwrite at end.
* Proper reading of VG_Onboarding's fallback .db when no .db is found.
* PDFs added in Doc/ for offline tutorial and offline API documentations.

##### Update to VG Core library 0.6.5:

* Bugfix that intermediate empty object can cause crash.
* Won't save empty object db entries into grasp db file.

##### Known Issues:

* If an object has rigidbody, changing object physical properties such as drag or mass won't affect VG interaction.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small object may have unatural finger placement.

## V0.9.4 (2021-12-16)

##### Other / Internal Changes:

* VG_BakingClient updated to support larger files.
* Warning added if you have an index-pushable, physical (i.e. Rigidbody) object but no physical hand that would be needed to interact with a physical button.

##### Update to VG Core library 0.6.4: 

* Default hand pose becomes more natural.
* Pinch grasp object is chosen more strictly. 

##### Known Issues:

* If an object has rigidbody, changing object physical properties such as drag or mass won't affect VG interaction.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small object may have unatural finger placement.

