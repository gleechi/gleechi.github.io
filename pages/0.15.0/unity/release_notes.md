---
title: Release Notes
#tags: [getting_started]
keywords: release notes #, announcements, what's new, new features
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_15_0
permalink: release_notes.0.15.0.html
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

##### Update to VG Core library 0.11.0:
* 

##### Known Issues:
*
-->


## V0.15.0-rc1 (state of 2022-07-19; not released)

##### Major Functionality Changes:
* **Breaking change:** The sensor configuration in MyVirtualGrasp has been refactored:
  * Each controller profile (earlier VG_AutoSetup) has been ported into a ScriptableObject of type [VG_ControllerProfile](unity_component_myvirtualgrasp.0.15.0.html#controller-profile) (in Resources/ExternalControllers), uncluttering the [MyVirtualGrasp](unity_component_myvirtualgrasp.0.15.0.html#sensors--controllers) interface.
  * To resolve update issues: for a sensor in avatar in [MyVirtualGrasp](unity_component_myvirtualgrasp.0.15.0.html#sensors--controllers), just drag and drop the controller profile .asset you want to use into the "Profile" slot.
  * You can customize the profiles fully now.
  * VG_AutoSetup has been removed from the API and GUI.

* **Breaking change:** VG_SynthesisMethod has been removed.
  * [VG_SynthesisMethod](grasp_interaction.0.15.0.html#grasp-synthesis-method) has been closely coupled to the [VG_InteractionType](grasp_interaction.0.15.0.html#grasp-interaction-type) that could be set globally (in [MyVirtualGrasp->Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.15.0.html#global-grasp-interaction-settings)) or object-specific (in [VG_Interactable](unity_component_vginteractable.0.15.0.html)).
  * Some combinations had limited usecases, thus now the [VG_SynthesisMethod](grasp_interaction.0.15.0.html#grasp-synthesis-method) is implicitely set automatically based on the [VG_InteractionType](grasp_interaction.0.15.0.html#grasp-interaction-type). Only JUMP_PRIMARY_GRASP will result in a STATIC GRASP; all other [VG_InteractionTypes](grasp_interaction.0.15.0.html#grasp-interaction-type) will result in a DYNAMIC_GRASP.

* **Breaking change:** [VG_GraspStudio](unity_component_vggraspstudio.0.14.0.html) has been removed, and is replaced with [VG_GraspEditor](unity_component_vggraspeditor.0.15.0.html) which is a much simpler interface that can be used in runtime in any client’s unity project. 

##### GUI / Component Changes:
* Avatar Model Field removed to unclutter the interface. We always assume humanoid hand models for now.
* If your version supports networking (Pro feature), you can now toggle DebugSettings->UseNetworkIDs and avatars (in MyVirtualGrasp) and objects (in VG_Articulation) will allow you to set a network ID for them.
* [VG_Articulations](unity_component_vgarticulation.0.15.0.html) / [VG_Interactables](unity_component_vginteractable.0.15.0.html) will be grayed out during runtime to make clear that changing them has no effect. To change them, use the adequate API functions.
* All changes triggered by API functions that change [VG_Articulations](unity_component_vgarticulation.0.15.0.html) or [VG_Interactable](unity_component_vginteractable.0.15.0.html) (except [RecoverObjectJoint](virtualgrasp_unityapi.0.15.0.html#vg_controllerrecoverobjectjoint)) are now reflected in the Inspector components.
* The control flags (that were a list of checkboxes in each Sensor before) have been replaced with a nicer VG_SensorControlFlags [Flags] enum. Due to the change above related to VG_ControllerProfile, they were also moved into VG_ControllerProfile assets.
* Slightly re-ordered some global interaction settings in MyVirtualGrasp.
* VG_ExternalController cleared up and simplified.
* VG_ControllerProfile supports list of controller names, separated by ';', in order of priorization. For example "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.
* GetSynthesisMethodForObject(), SetGlobalSynthesisMethod(), SetSynthesisMethodForSelectedObject(), SetSynthesisMethodForObject() removed (see breaking change on [VG_SynthesisMethod](grasp_interaction.0.15.0.html#grasp-synthesis-method) above).
* VG_GraspStudio.cs and related Prefab and Resources removed. VG_GraspStudio replaced by VG_GraspAnnotator.

##### API Changes:
* Uncluttered API from a number of classes and enums that did not need to be public.
* TOGGLE_SYNTHESIS and TOGGLE_INTERACTION removed from VG_EditorAction.
* GetBroadcastSignal() (used if your version supports networking (Pro feature)) was extended with a flag argument to be able to pick out specific parts of the network signal.
* SetAvatarSpecificObjectSelectionWeight() and ClearAvatarSpecificObjectSelectionWeights() added, allowing to specify relative selection preferences for cluttered objects.
* ResetObject() and ResetAllObjects() marked as deprecated. They will be removed in a future version.
* SetObjectJointState() added to set an articulated object's state in runtime.
* Formerly deprecated SetGestureDuration() and SetPushAngleThreshold() removed.

##### Other / Internal Changes:
* The .NET TargetFrameworkVersion has been downgraded from 4.8 to 4.7.2 since it caused some issues for Unity+VSCode users.
* Debug messages that come from the native VG library to the console have been equipped with "context" as well (if applicable), meaning that selecting the message will highlight the GameObject the message relates to.
* New external controller "UnityInteractionHand" added that supports controller supported by Unity's action-based [Unity Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/index.html) (together with "XRI Default Input Actions.inputactions" in Resources).

##### Update to VG Core library 0.12.0:
* Improved pinch dynamic grasp on small objects. **(fixed known issue from 0.13.0)**
* Always make [SwitchGraspObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerjumpgraspobject) succeed to grasp the target object. **(fixed known issue from 0.13.0)**
* Fixed a crashing bug: when an object and all its upstream objects have FIXED VG_Articulation joint, when grasped by two hands, when one hand releases crash happens. **(fixed known issue from 0.13.0)**

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) as yet. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.0.15.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.0.15.0.html#vg_grasptype). 

* [ResetAllObjects](virtualgrasp_unityapi.0.15.0.html#vg_controllerresetallobjects) and [ResetObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerresetobject) are not working properly. 


## V0.14.0(2022-06-17)

##### Major Functionality Changes:
* **Breaking change:** [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#vg_controllerchangeobjectjoint) is extended with one additional input parameter "new_anchor_transform". 
* {% include tooltip.html tooltip="PhysicalObject" text="Physical objects" %} are allowed to have disabled VG_Articulation components with any constrained joint types. Note the enabled VG_Articulation can only have Floating joint type.
* Customized {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %} (different from default value 1.0f) will be recovered when object is switched from hidden to selectable again to enable interaction.

##### GUI / Component Changes:
* SteamHand.cs added as new external controller to support any controllers supported through SteamVR (for example Knuckles).
* When using finger tracking devices, {% include tooltip.html tooltip="FingerControlType" text="Finger Control Type" %} option -- "BY_ANIMATION" is disabled, so only recommended BY_SENSOR_FULL_DOFS is used.
* GUI issues of some Unity versions resolved by making lists [NonReorderable].
* Pause / Resume replay of recorded sensor data control is added to [VG_Recorder](unity_component_vgrecorder.0.15.0.html) component: Shift + Replay Sequence Key is used to pause or resume replay.
* [MyVirtualGrasp](unity_component_myvirtualgrasp.0.15.0.html)'s elements have been re-ordered. For example: controllers at top to be closer to AutoSetup, GraspButton section removed and merged into Interaction settings.
* All AutoSetup options have been renamed to better reflect the names of the [external controllers](unity_component_vgexternalcontrollermanager.0.15.0.html#vg_externalcontroller-class).

##### API Changes:
* Added [OnObjectPushed](virtualgrasp_unityapi.0.15.0.html#vg_controlleronobjectpushed) event.
* Added [OnGraspTriggered](virtualgrasp_unityapi.0.15.0.html#vg_controllerongrasptriggered) event.
* Added [SwitchGraspObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerswitchgraspobject) API function to allow directly switch grasped object. 
* Removed [SelectObject](virtualgrasp_unityapi.0.13.0.html#vg_controllerselectobject) API function since if VR developers choose to select object differently from [the object selection mechanism in VG](grasp_interaction.0.15.0.html#from-object-selection-to-grasp-synthesis) the result will not integrate well with the subsequent {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} process provided by VirtualGrasp. 
* [GetTriggerButton](virtualgrasp_unityapi.0.13.0.html#vg_controllergettriggerbutton) has been renamed to [GetGraspButton](virtualgrasp_unityapi.0.15.0.html#vg_controllergetgraspbutton) to make naming consistent with "Grasp Button" option in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.15.0.html#global-grasp-interaction-settings) interface.

##### Other / Internal Changes:
* Onboarding scene object models are improved and sound effect added.
* Guard mesh and rig are compatible when registering avatars. 
* Using special characters for object name in Unity is allowed and won't affect VG functionality anymore. 
* A couple of text optimizations to the VirtualGrasp Tutorials to improve understanding.
* Bugfix to avoid NullReference if a ForceReleasedObject is deleted in the same frame.

##### Update to VG Core library 0.11.0:
* Fixed bug that is examplified in [onboarding Task 3](#unity_vgonboarding_task5.0.15.0.html): after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. **(fixed known issue from 0.13.0)**
* Fixed bug on if game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.0.15.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. **(fixed known issue from 0.13.0)**
* Fixed bug on if an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. **(fixed known issue from 0.13.0)**
* Two hands grasp interaction with an object is improved. Both hands now contribute to the position and rotation changes of the grasped object.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.0.15.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.0.15.0.html#vg_grasptype). 

* [ResetAllObjects](virtualgrasp_unityapi.0.15.0.html#vg_controllerresetallobjects) and [ResetObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerresetobject) are not working properly. 

* [SwitchGraspObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.0.15.0.html#vg_controllerjumpgraspobject) may fail due to bad position of the target object with respect to the hand. 

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

* Fixed bug on new recording sensor recording using [VG_Recorder](unity_component_vgrecorder.0.15.0.html) is pending the data to earlier recordings. (**fixed known issue from 0.12.0**)
* Fixed bug on successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.0.15.0.html) can lead to crashing. (**fixed known issue from 0.12.0**)
* Fixed bug on the 2nd method -- pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.0.15.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". (**fixed known issue from 0.12.0**)
* Fixed bug on runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. (**fixed known issue from 0.12.0**)

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.0.15.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* There is an Inspector GUI artifact in VG_MainScript/Sensors, but it is a known [Unity issue](https://issuetracker.unity3d.com/issues/first-array-element-expansion-is-broken-for-arrays-that-use-custom-property-drawers).

* In [onboarding Task 3](#unity_vgonboarding_task5.0.15.0.html), there is a bug after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. This will not happen however if you first grasp bottle then later another hand grasp the cap. We have identified cause and the problem will be fixed in V0.15.0.

## V0.12.0(2022-04-14)

##### Major Functionality Changes:

*  [VG_BakingClient](unity_component_vgbakingclient.0.15.0.html) has been overhauled with support of _Prepare project_ in the same GUI without the need to move to [Debug Settings](debug_files.0.15.0.html) if there are no runtime spawned {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects. 

##### GUI / Component Changes:

* AutoSetup enum name for Oculus finger tracking was changed from "Quest_FT" to "Oculus_FT" to conform with the file names and avoid confusion.
* Fixed confusion of disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description) component. Now, if the component is added but disabled (unchecked) the object will not be {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. Runtime enabling or disabling this component will make the object interactable or uninteractable respectively. However note that it is more efficient to change object's interactable status by [SetObjectSelectionWeight](virtualgrasp_unityapi.0.15.0.html#setobjectselectionweight).  (**fixed known issue from 0.11.1**)

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

* New recording sensor recording using [VG_Recorder](unity_component_vgrecorder.0.15.0.html) is pending the data to earlier recordings.

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.0.15.0.html) can lead to crashing.

* The 2nd method -- pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.0.15.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". 

* Runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. 

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* [GetReplayStartWristPose](virtualgrasp_unityapi.0.15.0.html#getreplaystartwristpose) does not give accurate wrist pose. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.0.15.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

## V0.11.1 (2022-04-11)

##### Major Functionality Changes:

* **Breaking change**: Avatar IDs that were before the array index have been replaced by the Unity instance ID of the SkinnedMeshRenderer that relates to the avatar. The VG API is providing helper functions and the SDK scripts have been adjusted accordingly. Check out [GetSensorControlledAvatarID](virtualgrasp_unityapi.0.15.0.html#getsensorcontrolledavatarid), [GetReplayAvatarID](virtualgrasp_unityapi.0.15.0.html#getreplayavatarid), and [GetAvatarID](virtualgrasp_unityapi.0.15.0.html#getavatarid). 
* Released Gleechi's first original avatar in VirtualGrasp/Resources/GleechiHands. This replaces earlier released OcculusHands, so in the VG SDK that support only one avatar, only GleechiHands are supported.
* Added {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %} support on [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description). See VG Onboarding [Task6](unity_vgonboarding_task6.0.15.0.html) to show the example use. 

##### GUI / Component Changes:

* AutoSetup "External" string for Oculus finger tracking was changed from "QuestHand" to "OculusHand" to conform with the file names and avoid confusion.
* Bugfix on AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.0.15.0.html#vg_externalcontroller-class) you like to use. (**fixed known issue from 0.10.1**)
* [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description) has been overhauled as a dynamic component to improve user experience. 
* Replay and Remote checkboxes for avatar are only shown if the VG version supports this feature.
* [VG_Interactable](unity_component_vginteractable.0.15.0.html) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to allow specifying object-specific throwing power that overwrite those set in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.15.0.html#global-grasp-interaction-settings).
* [VG_Recorder](unity_component_vgrecorder.0.15.0.html) has improved file management so that users can optionally provide in _Recording Filename_ with either a single file name like "MyRecordingFile", or a folder and a file name like "MyRecordingFolder/MyRecordingFile". Also adding the file extension ".sdb" is only optional.

##### API Changes:

* **Breaking change**: [GetObjectJointState](virtualgrasp_unityapi.0.15.0.html#getobjectjointstate) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointState will be invalid.
* **Breaking change**: [GetObjectJointType](virtualgrasp_unityapi.0.15.0.html#getobjectjointtype) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointType will be invalid.
* [SetAvatarActive](virtualgrasp_unityapi.0.15.0.html#setavataractive) added an optional argument: resetPos.
* Added [GetObjectSecondaryJointState](virtualgrasp_unityapi.0.15.0.html#getobjectsecondaryjointstate) which provide {% include tooltip.html tooltip="JointState" text="joint state" %} along yaxis of joint anchor for {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %}. 
* Added api functions to set velocity scales for throwing: [SetGlobalThrowVelocityScale](virtualgrasp_unityapi.0.15.0.html#setglobalthrowvelocityscale), [SetThrowVelocityScaleForSelectedObject](virtualgrasp_unityapi.0.15.0.html#setthrowvelocityscaleforselectedobject), [SetThrowVelocityScaleForObject](virtualgrasp_unityapi.0.15.0.html#setthrowvelocityscaleforobject), [SetGlobalThrowAngularVelocityScale](virtualgrasp_unityapi.0.15.0.html#setglobalthrowangularvelocityscale), [SetThrowAngularVelocityScaleForSelectedObject](virtualgrasp_unityapi.0.15.0.html#setthrowangularvelocityscaleforselectedobject), [SetThrowAngularVelocityScaleForObject](virtualgrasp_unityapi.0.15.0.html#setthrowangularvelocityscaleforobject). 
* Added [GetAvatarID](virtualgrasp_unityapi.0.15.0.html#getavatarid) to receive the ID of an avatar.
* Added [GetSensorControlledAvatarID](virtualgrasp_unityapi.0.15.0.html#getsensorcontrolledavatarid) to receive the ID of the sensor-controlled avatar.
* Added [GetReplayAvatarID](virtualgrasp_unityapi.0.15.0.html#getreplayavatarid) to receive the ID of the replay avatar (if replaying is supported by the VG version).
* Added [UnregisterAvatarAtRuntime](virtualgrasp_unityapi.0.15.0.html#unregisteravataratruntime) to allow deleting avatars. (This is most relevant for multiplayer use case.)

##### Other / Internal Changes:

* Bugfix on [OnObjectSelected](virtualgrasp_unityapi.0.15.0.html#onobjectselected) event is not invoked for object with Index Pushable {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}.
* Bugfix on [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.0.15.0.html#jumpgraspobject) call. (**fixed known issue from 0.10.1**)
* Bugfix on after an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose. (**fixed known issue from 0.10.1**)
* Bugfix on physical avatar when grasping {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with {% include tooltip.html tooltip="StickyHand" text="sticky hand" %} interaction type object and hand is grandually moving away.
* Further performance optimization of selecting which objects need to be synced between Unity and VG.
* Improved grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider. Note however still Unity physical material with smaller friction should be used for desired sliding behaviors. (**fixed known issue from 0.10.1**)

* Provide error message when trying to use an controller but not enabling its #define (e.g., VG_USE_LEAP_CONTROLLER).
* Provide error signal if {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object is labeled as Static.
* Provide error signal if start a scene without providing SkeletalMesh for avatar setup. 
* Provide error message if you are on Mac that Mac is not supported.

* All #defines that enable controllers with dependencies on third party plugins have been prefixed with VG_ (e.g., USE_LEAP_CONTROLLER is now VG_USE_LEAP_CONTROLLER) to avoid conflicts with non-VG defines.
* Onboarding scene added [Task6](unity_vgonboarding_task6.0.15.0.html) to showcase VirtualGrasp's newly added support of {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joints" %}. 
* Added first Unity tutorials.

##### Update to VG Core library 0.8.0:

* Bugfix for physical avatar index finger push gesture formation is not smooth. (**fixed known issue from 0.10.1**)
* Improved pinch grasp on small objects. (**fixed known issue from 0.10.1**)
* Bugfix for when hand form index finger push gesture grasp synthesis adopted push gesture problem.
* Bugfix for [JumpGraspObject](virtualgrasp_unityapi.0.15.0.html#jumpgraspobject) crash on unbaked object problem. 

##### Known Issues:

* There is a problem of unreliable grasp and release triggering for finger tracking solutions OCULUS_FT. 

* If two hands grasp on a non-physical FLOATING object, when one hand releases, the other hand could have a big offset from sensor position.

* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.

* If two hands trigger grasp on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} at the exact same moment, the hands will form grasps, but the object freeze and can not be moved by hands. This is difficult to reproduce but still could happen.

* The newly released GleechiHands does not have perfect mapping of real finger poses when using finger tracking solutions like OCULUS_EXT and LEAP_EXT. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, then there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.0.15.0.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) as yet. 

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.0.15.0.html) can lead to crashing.

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

## V0.10.1 (2022-03-01)

##### Major Functionality Changes:

* **Breaking change**: Removed support of using VG_Articulation component with constrained {% include tooltip.html tooltip="Joint" text="joints" %} (non-FLOATING joint) on objects with Rigidbody. Developers are encouraged to use [Unity Joints](https://docs.unity3d.com/Manual/Joints.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html) for physical joints.
* **Breaking change**: in [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description), "Pivot" changed name to "Anchor" to be more consistent with the terminology used by [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html). And "Push Pivot" changed name to "Push Direction" to be more descriptive. Due to the name change, the reference can be lost and need to be reassigned.
* More stable grasp interaction with {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} and better throwing experiences. 

##### GUI / Component Changes:

* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.15.0.html#grasp-interaction-settings) changed variable name "Grasp Speed" to "Grasp Animation Speed" and "Release Speed" to "Release Animation Speed". The default values for them are reduced to 0.05 (from 0.1) and 0.1 (from 0.2) second respectively to make grasp and release more snappy. The minimum values for both are reduced to 0.01 second (from 0.1 second).
* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.15.0.html#grasp-interaction-settings) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to control power of throw on grasped objects. 
* [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description) editing is disabled when object has Rigidbody component. (Was disabled when object has ArticulationBody component in version 0.9.6)
* Made VG_MainScript abstract since one should only use a child class (such as MyVirtualGrasp).
* Improved handling of AutoSetup when a VG_MainScript is created (such as adding a sensor instead of complaining it has not been added). 
* [MyVirtualGrasp/Avatars](unity_component_myvirtualgrasp.0.15.0.html#avatars) added "Replay" check to indicate if this avatar is to be used for sensor replay. If not checked, it will be controlled by sensor / controller. 

##### API Changes:

* **Breaking change**: VG_Controller.SetProcessedByFrame() function is removed. If you want to set an avatar for sensor replay, you can specify the avatar for replay by checking _Replay_ in [MyVirtualGrasp](unity_component_myvirtualgrasp.0.15.0.html#autosetup--sensors) component. 

##### Other / Internal Changes:

* Event handling bugfix: OnObjectFullyReleased do not trigger on objects that are not grasped. 
* Onboarding scene [Task3](unity_vgonboarding_task3.0.15.0.html) improved ManageContainerObject.cs script.
* Onboarding scene added [Task4](unity_vgonboarding_task4.0.15.0.html) showcase VirtualGrasp's support of interaction with ArticulationBodys. 
* Onboarding scene added [Task5](unity_vgonboarding_task5.0.15.0.html) showcase VirtualGrasp's support of object assembly with VG_Articulation without rely on physics. 
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
* [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.0.15.0.html#jumpgraspobject) call.
* After an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose.
* Grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider shows obvious non-smooth behavior due to some artificial manipulation of object velocities. 
* AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.0.15.0.html#vg_externalcontroller-class) you like to use.

##### Known Issues:

* Since Unity 2019 or earlier versions do not have [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html), these earlier versions of Unity is not supported.
* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.0.15.0.html#onobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.0.15.0.html#onobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small objects may have unatural finger placement.
* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.0.15.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.


## V0.9.6 (2022-02-15)

##### Major Functionality Changes:

* **Breaking change**: Prefabs GleechiLib and GleechiLibBurst removed. You are expected to just insert a VG_MainScript component (such as MyVirtualGrasp) on a GameObject of your choice.
* Grasp .db will be handled automatically, no manual deployment needed anymore (UploadGraspDB menu entry removed).
* Removed ObjectIdentifiers. The single and only component to mark objects as interactable is VG_Articulation. This should not break earlier use of VG_Interactable as Unity will create missing VG_Articulation component through RequireComponent requirement.
* Performance speed up by handling only subset of close-by objects.
* Added 

##### GUI / Component Changes:

* GraspStudio optimized and extended (see [VG_GraspStudio](unity_component_vggraspstudio.0.15.0.html)).
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

## V0.9.3 (2021-12-14)

##### GUI / Component Changes:

* New VG_BakingClient to support CABVG2 cloud baking service (stay tuned for update of [VG_BakingClient](unity_component_vgbakingclient.0.15.0.html))
* VG_Articulation GUI behavior adjusted: grasp/push affordance also selected for floating objects; push pivot only for pushable objects.

##### Other / Internal Changes:

* Null meshes will be detected and reported as error in Console.
* VG_MainScript Start() functionality moved to Awake().
* Fixed screw rate setting for ChangeObjectJoint() function.
* Code documentation for external controllers improved.

##### API Changes:

* [ChangeObjectJoint](virtualgrasp_unityapi.0.15.0.html#changeobjectjoint) fixed the bug that made new_screwRate input with no effect. 

##### Update to VG Core library 0.6.3: 

* Fixed the object selection weight bug so re-enabled object will respect previous set selection weight, or default 1.0 if not specifically set.
* Object selection in cluttered situation improved. 
* Hand positioning in Dynamic Grasp improved. 
* Dynamic Grasp performance improvement.
* Interaction with object with rotating joint improved. 
* Some spamming of debug error output suppressed. 

##### Known Issues:

* If an object has rigidbody, changing object physical properties such as drag or mass won't affect VG interaction.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 

## V0.9.2 (2021-12-06)

##### Major Functionality Changes:

* VG_Articulation will take care of object de/registration to VG. Runtime functions RegisterObjectAtRuntime(), RegisterObjectsAtRuntime(), DeleteDistalObjectAtRuntime() removed.

##### GUI / Component Changes:

* VG_DebugSettings modified. EditMode Save Debug Files for Current Editor Scene ⚠️. Read more on [Debug Files](debug_files.0.15.0.html).
* VG_Articulation.Lock() and VG_Articulation.Unlock() shortcuts removed. Using them in Events was unsafe. In code, use VG_Controller.ChangeObjectJoint(transform, VG_JointType.FIXED) instead of VG_Articulation.Lock(), and VG_Controller.RecoverObjectJoint(transform) instead of VG_Articulation.Unlock().
* Fixed problem in GraspEditor scene creation when UnityEngine.SpatialTracking.TrackedPoseDriver is not available, but only UnityEngine.InputSystem.XR.TrackedPoseDriver.
* VG_EC_GenericHand added and used as fallback for VG_ExternalControllerManager.
* VG_GraspStudio allows deleting grasps. To delete a grasp, you have to "double-disable" it. Read more on [VG_GraspStudio](unity_component_vggraspstudio.0.15.0.html).
* VG_Recorder extended with example to call new VG_Controller.GetReplayStartWristPose().

##### API Changes:

* [SetAvatarActive](virtualgrasp_unityapi.0.15.0.html#setavataractive) added to set avatar in/active (i.e. sensor control and mesh visualization).
* [GetReplayStartWristPose](virtualgrasp_unityapi.0.15.0.html#getreplaystartwristpose) added to return starting wrist poses of a recording, and check [how to query start pose page](unity_component_vgrecorder.0.15.0.html#how-to-query-start-pose-of-hand) to learn to use it.
* RegisterObjectAtRuntime(), RegisterObjectsAtRuntime(), DeleteDistalObjectAtRuntime() removed. VG_Articulation will take care of de/registration.

##### Update to VG Core library 0.6.2: 

* Fixed some big penetration problems in Dynamic Grasp. 
* Added an api function to delete an object in the middle of the object tree and all its downstream objects.
* Fixed a bug that causes crash when useing {% include tooltip.html tooltip="PreviewGrasp" text="preview grasp" %} interaction type.

##### Other / Internal Changes:

* Fallback .db added and implemented to use this one if project .db is not found.
* Grasp Studio Scene will open automatically after creation.
* Fixed a bug in VG_Articulation initialization.
* Fixed kink when using {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} with {% include tooltip.html tooltip="JumpGrasp" text="jump grasp" %} and {% include tooltip.html tooltip="JumpPrimaryGrasp" text="jump primary grasp" %} interaction types.
* Fixed that meshes disappear when prefabs are opened in Editor.
* Fixed screw rate to accept float values.
* Default synthesis method changed from STATIC_GRASP to DYNAMIC_GRASP.

##### Known Issues:

* Rotation interaction on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with revolute joint does not feel so natural.
* Dynamic Grasp sometimes has unaturally large thumb extention. 

## V0.9.1 (2021-11-17)

##### GUI / Component Changes:

* Fixes to VG_ExternalControllerManager to make it work with VG_Controller.RegisterAvatarAtRuntime().

* VG_FingerControlType moved from VG_SensorSettings to VG_SensorSetup, i.e. can be defined by sensor now instead of globally.

* VG_SensorSetup's open and close thresholds removed.

##### API Changes:

* VG_Controller.OnInitialize() event added that can be listened to after VG initialized.

##### Update to VG Core library 0.6.1: 

* Improved pinch grasp on small objects.

* Fixed a bug in dynamic grasp that caused big finger penetrations.

##### Other / Internal Changes:

* Fix that unskinned bones were not registered before, preventing VG to detect certain hand models.

* updateWhenOffscreen will be automatically enabled for all hand models.

##### Known Issues:

* Replay hands spin (invalid data) when using MouseController.

* Replay on controlled avatar only triggers when controllers are active.

* Screw rate on revolute joint is by mistake clamped to integer.

## V0.9.0 (2021-11-12)

##### Major Functionality Changes:

* ⚠️ IMPORTANT SDK and Bake have been separated:

    * The SDK / .unitypackage will from now on be a "vanilla" version fixed to a specific SDK and Core library version, but not to a project / bake anymore.

    * A bake will no longer be a .unitypackage of the whole SDK, but a single .db file that you have to add into your project root folder.

    * The .lab file is obsolete now (because it is incorporated in the single .db file).

    * Read more on [VG_BakingClient](unity_component_vgbakingclient.0.15.0.html) (when updated).


##### GUI / Component Changes:

* VG_GhostHands removed.

* VG_StateVisualizer renamed to VG_HandStatusDebugger and is now a component instead of an Editor Window.

* Assembling.cs added in Onboarding.

* VG_HandVisualizer fixed to show unmapped bones from an external controller and for all hands.

* VG_Highlighter label text corrected.

* VG_HintVisualizer simplified and code optimized.

* Moved the check on current VG_TriggerButton (to use the other button not used for grasping) from UnityXRHand to VG_PostAnimator where it belongs.

* VG_PostAnimator code documentation improved.

* Menu entry "VirtualGrasp→ Utilities→ Upload Grasp .db to Android Device" added. This will copy the .db from your project folder into your application folder on the device (assuming that application name and version number of your application are correct and the application exists).

##### API Changes:

* VirtualGrasp will now present proper version numbers for both SDK and VG Core library in the Console when initialized.

* VG_InteractionMode enum and VG_Controller.GetInteractionMode() removed.

* Lots of API documentation corrected and added, to improve documentation in code as well as on VirtualGrasp Documentations.

##### Update to VG Core library 0.6.0: 

* Baking is producing a separate encrypted grasp db instead of a new dll with grasp db encoded.

* Baking produced grasp db also incorporate all the labels from Grasp Studio.

* Dynamic Grasp single finger pose is more natural.

* Dynamic Grasp works better on objects consisting of some thin parallel elements.

* Hybrid grasp synthesis method added (the one combines Dynamic Grasp and Static Grasp).

##### Other / Internal Changes:

* PostUpdate() called after hand update (to make post-animation) possible again.

* Internal cleanup on some internal variables and VG_Debug calls.

* ChangeObjectJoint() functions refactored, and can have target joint with same type as original joint.

* SetObjectSelectionWeight () fixed bug of set weight to 0 not taking effect.

* Timestamps from VG_Debug removed so Console messages can collapse.

##### Known Issues:

* Replay hands spin (invalid data) when using MouseController.

* Replay on controlled avatar only triggers when controllers are active.


## V0.8.0 (2021-10-28)

##### Major Functionality Changes:

* Plugins folder has been moved to ThirdParty/VirtualGrasp/Plugins. ⚠️ IMPORTANT: Please move your old VirtualGrasp-related Plugins folder into ThirdParty/VirtualGrasp content before updating with the new unitypackage.

* VG_Articulation 's inspector view got a major overhaul in terms of dynamic settings, e.g. the presented visual elements in the view are changing dependent on joint type and other settings.

* Object tags are deprecated and not considered any longer. 

* The object identifier strings (moved to VG_MainScript inspector view) can still be used to define layers. 

* The object identifier strings are now also used to define component names to mark interactable objects, by default VG_Articulation and VG_Interactable.

* ⚠️ IMPORTANT: In order to simplify transition from object tags, select "VirtualGrasp→ Utilities→ Convert Object Tags to VG_Articulations." This will automatically search for GameObjects with "Object" tag, remove the tag, and - if there is none yet - put a VG_Articulation (with FLOATING joint type) in its place. You need to save the scene manually.

##### GUI / Component Changes:

* All VG components have been linked with their OpenReferenceURLs to their respective docs.gleechi.com pages.

* VG_StateVisualizer and VG_BakingClient also received context menus to open documentation links.

* A number of development components were removed: VG_ObjectModifier, VG_GraspVisualizer, VG_HeightController, VG_ObjectWheel, VG_RuntimeRegister, VG_ButtonTester, VG_JointChanger, VG_TriggerEvent , VG_Gestures.

* MyVirtualGraspBurst (inheriting VG_MainScript) fixed and optimized.

* VG_Recorder improved and optimized in terms of terminology.

* VG_Highlighter consistency statuses updated. Now they differentiate between unbaked, baked, and edited (through VG_GraspEditor) objects.

* VG_GraspStudio always hides inactive objects.

* VG_GraspStudio always adds hands for grasp adding when in VR mode.

* VG_GraspStudio label icon update bug fixed.

* VG_MainScript.DebugSettings.ObjectIK disabled by default.

* VG_SelectionSettings.ObjectIdentifiers moved to VG_Mainscript main GUI.

* VG_Avatar.IsReplay removed (should be set manually through VG_Controller.SetProcessedByFrame(), as in VG_Recorder).

* VG_Articulation default VG_JointType changed to FLOATING.

* VG_HandStatus.Distance removed.

* VG_MainScript.GlobalSensorSettings renamed to VG_MainScript.SensorSettings.

* Menu "VirtualGrasp" organized and sorted into three subfolders "Components", "Asset Functions" and "Utilities."

* VG_InteractionMode.PHYSICAL_PUSHING renamed to VG_InteractionMode.PUSHING

##### API Changes:

* GetObjectState() renamed to GetObjectJointState().

* RegisterAvatarOnline() renamed to RegisterAvatarAtRuntime().

* SynthesisMethod.DYNAMIC renamed to VG_SynthesisMethod.DYNAMIC_GRASP.

* SynthesisMethod.STATIC renamed to VG_SynthesisMethod.STATIC_GRASP.

* StartReplay() now takes avatar ID and selected object as input. See Recorder documentation for way of use.

* StopReplay() added.

* Functions that were marked as obsolete and non-functional before were now removed: SetPhysicalObject(), GetNonSelectableObjects(), SetGestureDuration(), SetPushAngleThreshold()

##### Package Changes:

* All Core Scripts / how-tos that are in use have been moved from Scripts/Core to Scripts.

* Scripts/Dev and Scripts/Tests have been removed.

##### Update to VG Core library 0.5.0:

* Improved DG look in terms of naturalism.

* Sensor replay on full sequence can be played on a specified object. 

##### Other / Internal Changes:

* All external controllers (UnityXR, Oculus Finger Tracking, LeapMotion, Mouse) have been updated and tested.

* External controller DebugDraw() also includes unmapped bones.

* Small bugs in Move script and ChangeSelectionWeight script fixed (onboarding).

* Bugfix to not control hands by controllers if they are in replay mode.

* Isolated (burst) and internal VG update loops synced.

* Bugfix that edited grasps and labels were not available in runtime.

##### Known Issues:

* Replay hands spin (invalid data) when using MouseController.

* Replay on controlled avatar only triggers when controllers are active.

## V0.7.1 (2021-10-04)

##### Major Functionality Changes:
* Update to core library 0.4.1, including
* 32 bit libraries for Android replaced by 64 bit Android versions

##### GUI / Component Changes:
* Some elements of VG_SensorSettings moved out into VG_GraspInteractionSettings
* Elements m_graspDelay and m_releaseDelay unexposed.
* Custom inspector view for VG_Articulation
* Some GraspStudio bugs resolved and optimized.
* Bug on nested hierarchy in GraspStudio resolved
* Bug on restart (related to VG_ExternalController initialization) resolved.

##### API Changes:
* ProcessExternalControllers renamed as RegisterExternalControllers
* VG_GraspTypes removed (from VG_Interactable and in general)
* GetObjectJoint renamed GetObjectJointType

##### Package Changes:
* Onboarding folder (for V2.0; including scene, models, solutions) added.

##### VG Core SDK - Changes from V0.4.0 (2021-09-17) to V0.4.1 (2021-09-28)
* Android support switched from 32 bit to 64 bit libraries

## V0.7.0 (2021-09-17)

##### Major Functionality Changes:
* VG_MainScript turned into a proper base class, so various child classes (such as MyVirtualGrasp or MyVirtualGraspBurst) properly inherit main functionality.
* Dependency on TrackedPoseDriver in Editor scripts removed, together with it the need of checking for the availability of the necessary package.
* Create Grasp Editor Scene functionality overhauled to use some components from original scene (cam, VG), others from debug folder (objects, setup)db/lab files created by the grasp editor will not be written as vg_external.db/lab anymore, but [APPLICATION]-[VERSION].db/lab. Note that the wrapper now reads all .db/.lab files in the directory. It is still recommended though to rename the old ones.
* Continuous check on physicality of bodies through observation of RigidBody removal/addition.

##### GUI / Component Changes:
* Enabled experimental “Physical” Mode for avatars to create hand colliders from within VG. Note this will also enable the untested experimental physical interaction with objects. By default it is disabled.
* DebugSettings.m_objectUpdatingMethod removed.
* DebugSettings.m_physicsDefaultContactOffset (experimental) to modify contact offset which may by default be too big for fine hand collisions.
* Default value for grasp speed changed from 0.2 to 0.1
* Made VG_Avatar to distinguish between VR avatars (skinned mesh) and Robot hands (transforms)
* VG_Articulation.m_SetFixFloatingObject removed (obsolete)
* VG_Interactable.m_isKinematic removed. Kinematic properties are now directly linked to the existence of a Rigidbody on an object.
* VG_TriggerEvent extracted from wrapper DLL and made it a public tutorial script (under Core scripts)
* Custom GUI for VG_Avatar in Inspector to optimize interface.
* Custom GUI for VG_Affordances in Inspector to optimize interface.
* Fixed an issue in VG_Articulation GUI / Gizmo that would cause NullReference.
* VG_AutoSetup extended by LEAP_EXT (external controller for Leap), and renamed internal controller LEAP to LEAP_VG

##### API Changes:
* VG_HandSide.UNKNOWN renamed to VG_HandSide.UNKNOWN_HANDSIDE for consistency reasons.
* ChangeObjectJoint(VG_Articulation) completed so all elements of an articulation are considered and updated.
* GraspEditor bug when using VG_EditorAction.ADD_CURRENT fixed.
* GetHands() extended by a boolean argument if you only want valid hands or all.
* GetSelectedObject() removed. You should directly use the VG_HandStatus.m_selectedObject.
* SetExternalObjectPose() removed (obsolete)
* SetExternalSensorPose() removed (obsolete)
* GetSensorVelocities() removed.
* SetGestureDuration() marked deprecated and non-functional.
* SetPushAngleThreshold() marked deprecated and non-functional.
* SetPhysicalObject() marked deprecated and non-functional. Physicality of bodies is now continuously checked through observation of RigidBody removal/addition.

##### Package Changes:
* ExternalController scripts updated to support new external controller handling.
* Some outdated / unmaintained Dev scripts removed: Snapper, FollowSensor
* All scripts updated according to API changes.

##### Other / Internal Changes (“under the hood”):
* Refactoring of avatar bone control classes to improve readability and efficiency.
* Refactoring of object classes to improve readability and efficiency.
* Refactoring of native library integration to improve readability and efficiency.
* Refactoring of external controller classes to not touch Unity transforms of bones, but directly work on their matrices.
* Collider classes added to support physical hands.
* Helper renamed VG_Helper to avoid naming conflicts.
* Python script to generate Unity enums automatically from core.
* VG_ExternalController base class optimized and proper debug visualization added.
* log/lab/db files made part of the debug package / zip
* Separated things into Update() and FixedUpdate() loops for proper physical object behavior.
* CheckTransformDataConsistency() functionality removed.
* PDcontroller changes and force application implemented to improve physical object behaviors.
* Skin extraction for avatars added to improve hand collider estimation.
* HandStatusEvent renamed VG_HandStatusEvent to avoid naming conflicts.
* BugFix on missing sensor data when no sensors are used at all.

##### VG Core SDK - Changes from V0.3.0 (2021-06-17) to V0.4.0 (2021-09-17)
* Requested baking only bake the object shape, no static grasps anymore.
* Primary grasp label is reusable on same object - hand pair, independent of new baking
* Dynamic Grasp reached to the first stable version.
* Improved object shape analysis.
* Improved hand model analysis.
* Object hierarchy is synchronized in runtime in VG when reparenting is done in Unity side.

## V0.6.0 (2021-06-17)

##### Components:
* MyVirtualGrasp / Advanced Settings / Use Object IK added to enable / disable object IK on demand (note: not in runtime)

##### API:
* RegisterRemoteAvatarOnline renamed to RegisterAvatarOnline while adding a parameter of what kind of avatar should be registered
* VG_AvatarType introduced to specify type of avatar (default, remote, replay)
* ENABLE_RECORDING_API api group introduced (feature dependent)
* ENABLE_ROBOTICS_API api group introduced (feature dependent)
* OnObjectFullyReleased event added that is sent when you fully release an object
* Default behavior of releasing improved (VG_GrabAndThrow.cs obsoleted):
* Objects without rigidbody are non-physical from a VG point of view (i.e. not controlled by forces, thus can penetrate others without rigidbodies). 
* Objects with rigidbody and gravity enabled are physical from a VG point of view  (i.e. controlled by forces, do not penetrate other objects, and can be thrown)
* Objects with rigidbody and gravity disabled are physical from a VG point of view  (i.e. controlled by forces, do not penetrate other objects, but cannot be thrown)

##### Scripts/Tutorials:
* All ExternalControllers scripts moved to subfolder ExternalControllers
* All ExternalControllers fixed to cope better with missing data (get rid of spinning hands)
* Base class DebugDraw for all ExternalControllers
* VGA_CoreScripts assembly definition added to address XR Management dependency
* VG_GhostHands.cs tutorial script added.
* VG_GrabAndThrow.cs tutorial script obsoleted and removed
* Multiple improvements and fixes in VG_GraspStudio.cs, among others numbering of grasps

##### Other
* Logger renamed VG_LoggerBase to avoid naming conflicts
* Fixed radians/angle conversion bug in "Create VG Scene" (scene from debug package) generation 
* Non-alphanumeric names for game objects are supported, but VG files using names will save them as “unknown” (they will still be identifiable through hash)
* Various runtime optimizations getting rid of GetComponent<> calls
* Warning message for multiple rigidbodies in a single chain introduced. Can produce unexpected results in Unity in general, and also in VG.

## V0.5.1 (2021-03-25)

##### Bug
* Check runtime activation of touch elements

##### Task
* Investigate alphanumeric check when using Swedish characters
* Make save debug zip overwrite the old one
* Expose grasp button choice
* Check if alphanumeric check for object names can be deactivated
* Make create scene tool create all scenes from vg_tmp

## V0.5.0 (2021-03-24)

##### Scripts/Tutorials
* PicoHand ExternalController added to support PicoSDK controllers
* VG_ChangeObjectJoint renamed to VG_JointChanger
* Improvements on VG_GraspHypothesizer, VG_Recorder, VG_JointChanger scripts
* Some small fixes and optimizations in VG_PostAnimator, VG_ButtonTester, VG_Snapper scripts

##### Components
* VG AutoSetup also includes hand offset
* VG_Articulation API Un/Lock() functions added (to un/lock the articulation)
* Another ChangeObjectJoint() API function added that takes a VG_Articulation as input. This allows re-assigning VG_Articulations during runtime.

##### Other
* Update to most recent VirtualGrasp library (0.2.9-cabvg)
* Update to CABVG 1.1.3 BakingClient
* Assured to work up to Unity version 2020.3.1f
* Objects registered with VG_Controller.RegisterObjectAtRuntime() will now also get fallback grasps if not baked
* New menu entry “Create VG Scene” to recreate a scene from exported data (in vg_tmp)
* New menu entry “Make Interactables Readable” to make all sources of objects in the scene readable
* Internal access to an articulation will relate to the first active VG_Articulation. This allows re-assigning VG_Articulations during runtime.
* .scn file will only be saved when save debug file option is enabled

