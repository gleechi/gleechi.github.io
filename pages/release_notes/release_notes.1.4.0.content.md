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

## V1.4.0 (2023-07-24)

##### Major Functionality Changes:

* Prior to this version, if an object's initial pose (which is the zero pose) is violating the joint limit setting (for example when joint limit exclude zero pose), after game start, only when hand is interacting with this object (pushing or grasping), the object snaps to the valid pose respecting the joint limit. This creates a sense of buggy application. Now, the object is directly set to the joint limit range at the game start. 

* [VG_EC_Mouse](unity_vg_ec_mouse.1.4.0.html) external controller allows separate control of left and right hand movement depending on if left-shift or right-shift key is pressed. This improvement is only when Unity "Input System" is used. 

##### GUI / Component Changes:

* [VG_Articulation](unity_component_vgarticulation.1.4.0.html) now enables [Dual Hands Only](object_articulation.1.4.0.html#dual-hands-only) option for {% include tooltip.html tooltip="PhysicalObject" text="physical object" %}. 
* [VG_BakingClient](unity_component_vgbakingclient.1.4.0.html#step-2-packaging) GUI moved "Clear" button before "Export" button to be more aligned of order of actions.
* [VG_HandStatus](unity_component_vghandstatus.1.4.0.html) exposed more relevant variables: mode, grasp pose, isremote, linkedObjects and joint states. 
* [VG_ManusHand](unity_vg_ec_manus.1.4.0.html) was added as an experimental controller, including controller profile and hand profile.

##### API Changes:

* Add [ForceReleaseObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerforcereleaseobject-2) overloaded function that recieves transform of the object that is to be released by all grasping hands.

* Add [GetHand](virtualgrasp_unityapi.1.4.0.html#vg_controllergethand-1) overloaded function that recieves transform of the wrist.

* Add [GetFingerBone](virtualgrasp_unityapi.1.4.0.html#vg_controllergetfingerbone-3) overloaded function that recieves transform of the wrist.

* The former VG_ExternalControllerManager was integrated into the core functionality of the VG SDK. Controllers are now automatically instantiated through the rig registration and it is not necessary anymore to do this separately. Thus, the VG_ExternalControllerManager page has been removed from the documentation (and a new page for [VG_ControllerProfile](unity_component_vgcontrollerprofile.1.4.0.html) was created instead).

* Due to earlier confusion about the naming convention of controllers, controller profiles, and hand profiles, many assets have been renamed:
  * All controller scripts (child classes of VG_ExternalController, in Runtime/Scripts/VG_ExternalControllers/) as well as the classes inside have been renamed using VG_EC_* prefix and a more descriptive the name of the controller.
  * All [VG_ControllerProfiles](unity_component_vgcontrollerprofile.1.4.0.html) (ScriptableObjects, in Runtime/Resources/VG_ControllerProfiles) have been renamed using VG_CP_* prefix and more descriptive names of the provider and the controller. The member "external type" of each VG_ControllerProfile was renamed to "controller classes" and now expects one or more exact names of the VG_EC_* controller classes (see above).
  * All [VG_HandProfiles](unity_component_vghandprofile.1.4.0.html) (ScriptableObjects, in Runtime/Resources/VG_HandProfiles) have been renamed using VG_HP_* prefix and more descriptive names of the provider.

##### Other / Internal Changes:

* Fixed a bug: When runtime spawn a new avatar, the existing registered avatar's hands will suddenly flip. **(fixed known issue from 1.3.0)**

* Fixed a bug: [Grasp Editor](unity_component_vggraspeditor.1.4.0.html) was not working with runtime spawned {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}, and now it is fixed. **(fixed known issue from 1.3.0)**

* The In-Editor Tutorials folder was moved to the Samples folder. This allows to install the tutorials optionally in an NPM package setup.

* Naming convention for asset files was introduced and implemented, such as T_* for textures, M_* for materials, etc.

<!-- DONT DELETE, FOR INTERNAL NOTES
* [Not Available For Released Versions] VG works with multiplayer non-{% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with singular or combo object settings, and also works with object assembling in collaboration with multiplayer players. 
-->

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* When index finger tip moves in a different direction from wrist, pushing can get double triggered.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.4.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup.

* There is a typo on the controller profile scritable object **VG_CP_Unity.XRInteraction**, "VG_EC_UnityXRInteraction" should be changed to "VG_EC_UnityInteraction", corresponding to the name of [the corresponding external controller class](unity_vg_ec_unityinteraction.1.4.0.html).

* VG_Recorder click on the defined **Replay Sequence Key** or **Replay Segment Key** can not replay just recorded data. 

* [StartReplay](virtualgrasp_unityapi.1.4.0.html#vg_controllerstartreplay) entering selectedObject will not fully support object-centered replay.

* [SetBlockRelease](virtualgrasp_unityapi.1.4.0.html#vg_controllersetblockrelease) with no hand side input has a bug: if input avatarID corresponds to an avatar that has only right hand, then this function will not set block release on the right hand because an early return happens when left hand is not found. Before this is fixed, to safely set block release on right hand, use the overloaded function [SetBlockRelease](virtualgrasp_unityapi.1.4.0.html#vg_controllersetblockrelease-1) with hand side input  instead.

* [ForceReleaseObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerforcereleaseobject) with no hand side input has a bug: if input avatarID corresponds to an avatar that has only right hand, then this function will not force release the right hand because an early return happens when left hand is not found. Before this is fixed, to safely release right hand, use the overloaded function [ForceReleaseObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerforcereleaseobject-1) with hand side input instead.

* [VG_FingerAnimator](unity_component_vgfingeranimator.1.4.0.html) has a fundamental algorithm error that leads to the absolute target rotation keep changing, resulting in flickering finger animation.

{% include_relative release_notes.1.3.0.content.md %}

<!--

## V0.15.0(2022-07-27)

##### Major Functionality Changes:
* **Breaking change:** The sensor configuration in MyVirtualGrasp has been refactored:
  * Each controller profile (earlier VG_AutoSetup) has been ported into a ScriptableObject of type [VG_ControllerProfile](unity_component_myvirtualgrasp.1.4.0.html#controller-profile) (in Resources/ExternalControllers), uncluttering the [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html) interface.
  * To resolve update issues: for a sensor in avatar in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html), just drag and drop the controller profile .asset you want to use into the "Profile" slot.
  * You can customize the profiles fully now.
  * The profile supports list of controller names, separated by ';', in order of priorization. For example "OculusHand;UnityXR" (assuming that you have enabled both controllers properly) will use Oculus hand tracking as a priority, but if no hands are tracked, it will fallback to UnityXR controllers.
  * VG_AutoSetup has been removed from the API and GUI.
  * Origin transform has been kept in MyVirtualGrasp to allow overwrite of the name-based origin in the [VG_ControllerProfile](unity_component_myvirtualgrasp.1.4.0.html#controller-profile).

* **Breaking change:** VG_SynthesisMethod has been removed.
  * [VG_SynthesisMethod](grasp_interaction.1.4.0.html#grasp-synthesis-method) has been closely coupled to the [VG_InteractionType](grasp_interaction.1.4.0.html#grasp-interaction-type) that could be set globally (in [MyVirtualGrasp->Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings)) or object-specific (in [VG_Interactable](unity_component_vginteractable.1.4.0.html)).
  * Some combinations had limited usecases, thus now the [VG_SynthesisMethod](grasp_interaction.1.4.0.html#grasp-synthesis-method) is implicitely set automatically based on the [VG_InteractionType](grasp_interaction.1.4.0.html#grasp-interaction-type). Only JUMP_PRIMARY_GRASP will result in a STATIC GRASP; all other [VG_InteractionTypes](grasp_interaction.1.4.0.html#grasp-interaction-type) will result in a DYNAMIC_GRASP.
  * GetSynthesisMethodForObject, SetGlobalSynthesisMethod, SetSynthesisMethodForSelectedObject, and SetSynthesisMethodForObject removed.

* **Breaking change:** [VG_GraspStudio](unity_component_vggraspstudio.0.14.0.html) related script, resources and prefab have been removed, and is replaced with [VG_GraspEditor](unity_component_vggraspeditor.1.4.0.html) which is a much simpler interface that can be used in runtime in any client’s unity project. 

##### GUI / Component Changes:
* [Avatar Model Field](unity_component_myvirtualgrasp.1.4.0.html) removed to unclutter the interface. We always assume humanoid hand models for now.
* If your version supports networking (Pro feature), you can now enable [DebugSettings->UseNetworkIDs](unity_component_myvirtualgrasp.1.4.0.html#debug-settings) to set network ID for avatar's left/right hand (through [MyVirtualGrasp->Avatar](unity_component_myvirtualgrasp.1.4.0.html)), and set network ID for object (through [VG_Articulation](unity_component_vgarticulation.1.4.0.html)).
* [VG_Articulations](unity_component_vgarticulation.1.4.0.html) / [VG_Interactables](unity_component_vginteractable.1.4.0.html) will be grayed out during runtime to make clear that changing them has no effect. To change them, use the adequate API functions.
* All changes triggered by API functions that change [VG_Articulations](unity_component_vgarticulation.1.4.0.html) or [VG_Interactable](unity_component_vginteractable.1.4.0.html) (except [RecoverObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerrecoverobjectjoint)) are now reflected in the Inspector components.
* The control flags (that were a list of checkboxes in each Sensor before) have been replaced with a nicer VG_SensorControlFlags [Flags] enum. Due to the change above related to [VG_ControllerProfile](unity_component_myvirtualgrasp.1.4.0.html#controller-profile), they were also moved into VG_ControllerProfile assets.
* Slightly re-ordered some [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings) in MyVirtualGrasp.
* VG_ExternalController cleared up and simplified.
* Bugfix: when anchor of VG_Articulation is not set, no change needs to be reflected on anchor when calling API functions such as ChangeObjectJoint.

##### API Changes:
* Uncluttered API from a number of classes and enums that did not need to be public.
* TOGGLE_SYNTHESIS and TOGGLE_INTERACTION removed from [VG_EditorAction](virtualgrasp_unityapi.1.4.0.html#vg_editoraction).
* [GetBroadcastSignal](virtualgrasp_unityapi.0.15.0.html#vg_controllergetbroadcastsignal) -- if your version supports networking (Pro feature) -- was extended with a flag argument to be able to pick out specific parts of the network signal.
* [SetAvatarSpecificObjectSelectionWeight](virtualgrasp_unityapi.1.4.0.html#vg_controllersetavatarspecificobjectselectionweight) and [ClearAvatarSpecificObjectSelectionWeights](virtualgrasp_unityapi.1.4.0.html#vg_controllerclearavatarspecificobjectselectionweights) added, allowing to specify different selection preferences on an object for different avatars.
* [SetObjectJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllersetobjectjointstate) added to set an articulated object's state in runtime.
* Formerly deprecated SetGestureDuration and SetPushAngleThreshold are removed.
* Formerly deprecated ResetObject and ResetAllObjects are removed.

##### Other / Internal Changes:
* The .NET TargetFrameworkVersion has been downgraded from 4.8 to 4.7.2 since it caused some issues for Unity+VSCode users.
* Debug messages that come from the native VG library to the console have been equipped with "context" as well (if applicable), meaning that selecting the message will highlight the GameObject the message relates to.
* New external controller "UnityInteractionHand" added that supports controller supported by Unity's action-based [Unity Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/index.html) (together with "XRI Default Input Actions.inputactions" in Resources).
* [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.4.0.html) runtime optimizations.
* Bugfix: rig registration now also considers hidden bones.

##### Update to VG Core library:

* Dramatic runtime performance optimization for dynamic grasping
* Improved pinch dynamic grasp on small objects. **(fixed known issue from 0.14.0)**
* Always make [SwitchGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) succeed to grasp the target object. **(fixed known issue from 0.14.0)**
* Fixed a crashing bug: when an object and all its upstream objects have FIXED VG_Articulation joint, when grasped by two hands, when one hand releases crash happens. **(fixed known issue from 0.14.0)**
* Fixed a crashing bug: networking objectSignal will not crash anymore when invalid key is provided.

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) as yet. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.1.4.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.1.4.0.html#vg_grasptype). 

* When using the [VG_GraspEditor](unity_component_vggraspeditor.1.4.0.html) on Android, the grasp database is not modified. We recommend for now to do all grasp editing in the Unity Editor.

## V0.14.0 (2022-06-17)

##### Major Functionality Changes:
* **Breaking change:** [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) is extended with one additional input parameter "new_anchor_transform". 
* {% include tooltip.html tooltip="PhysicalObject" text="Physical objects" %} are allowed to have disabled VG_Articulation components with any constrained joint types. Note the enabled VG_Articulation can only have Floating joint type.
* Customized {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %} (different from default value 1.0f) will be recovered when object is switched from hidden to selectable again to enable interaction.

##### GUI / Component Changes:
* SteamHand.cs added as new external controller to support any controllers supported through SteamVR (for example Knuckles).
* When using finger tracking devices, {% include tooltip.html tooltip="FingerControlType" text="Finger Control Type" %} option -- "BY_ANIMATION" is disabled, so only recommended BY_SENSOR_FULL_DOFS is used.
* GUI issues of some Unity versions resolved by making lists [NonReorderable].
* Pause / Resume replay of recorded sensor data control is added to [VG_Recorder](unity_component_vgrecorder.1.4.0.html) component: Shift + Replay Sequence Key is used to pause or resume replay.
* [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html)'s elements have been re-ordered. For example: controllers at top to be closer to AutoSetup, GraspButton section removed and merged into Interaction settings.
* All AutoSetup options have been renamed to better reflect the names of the [external controllers](unity_component_vgexternalcontrollermanager.0.14.0.html#vg_externalcontroller-class).

##### API Changes:
* Added [OnObjectPushed](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectpushed) event.
* Added [OnGraspTriggered](virtualgrasp_unityapi.1.4.0.html#vg_controllerongrasptriggered) event.
* Added [SwitchGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerswitchgraspobject) API function to allow directly switch grasped object. 
* Removed [SelectObject](virtualgrasp_unityapi.0.13.0.html#selectobject) API function since if VR developers choose to select object differently from [the object selection mechanism in VG](grasp_interaction.1.4.0.html#from-object-selection-to-grasp-synthesis) the result will not integrate well with the subsequent {% include tooltip.html tooltip="GraspSynthesis" text="grasp synthesis" %} process provided by VirtualGrasp. 
* [GetTriggerButton](virtualgrasp_unityapi.0.13.0.html#gettriggerbutton) has been renamed to [GetGraspButton](virtualgrasp_unityapi.1.4.0.html#vg_controllergetgraspbutton) to make naming consistent with "Grasp Button" option in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings) interface.

##### Other / Internal Changes:
* Onboarding scene object models are improved and sound effect added.
* Guard mesh and rig are compatible when registering avatars. 
* Using special characters for object name in Unity is allowed and won't affect VG functionality anymore. 
* A couple of text optimizations to the VirtualGrasp Tutorials to improve understanding.
* Bugfix to avoid NullReference if a ForceReleasedObject is deleted in the same frame.

##### Update to VG Core library 0.11.0:
* Fixed bug that is examplified in [onboarding Task 3](unity_vgonboarding_task5.1.4.0.html): after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. **(fixed known issue from 0.13.0)**
* Fixed bug on if game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.4.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. **(fixed known issue from 0.13.0)**
* Fixed bug on if an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. **(fixed known issue from 0.13.0)**
* Two hands grasp interaction with an object is improved. Both hands now contribute to the position and rotation changes of the grasped object.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* The {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* [MakeGesture](virtualgrasp_unityapi.1.4.0.html#vg_controllermakegesture) have a bug when choose gesture from [VG_GraspType.FLAT](virtualgrasp_unityapi.1.4.0.html#vg_grasptype). 

* [ResetAllObjects](virtualgrasp_unityapi.1.4.0.html#vg_controllerresetallobjects) and [ResetObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerresetobject) are not working properly. 

* [SwitchGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) may fail due to bad position of the target object with respect to the hand. 

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

* Fixed bug on new recording sensor recording using [VG_Recorder](unity_component_vgrecorder.1.4.0.html) is pending the data to earlier recordings. (**fixed known issue from 0.12.0**)
* Fixed bug on successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.4.0.html) can lead to crashing. (**fixed known issue from 0.12.0**)
* Fixed bug on the 2nd method - pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.1.4.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". (**fixed known issue from 0.12.0**)
* Fixed bug on runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. (**fixed known issue from 0.12.0**)

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.4.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* There is an Inspector GUI artifact in VG_MainScript/Sensors, but it is a known [Unity issue](https://issuetracker.unity3d.com/issues/first-array-element-expansion-is-broken-for-arrays-that-use-custom-property-drawers).

* In [onboarding Task 3](#unity_vgonboarding_task5.1.4.0.html), there is a bug after assembling cap to the bottle where cap becomes bottle's child, then grasp bottle and cap together could make cap move off the initial position relative to the parent bottle. This will not happen however if you first grasp bottle then later another hand grasp the cap. We have identified cause and the problem will be fixed in V1.4.0.

## V0.12.0(2022-04-14)

##### Major Functionality Changes:

*  [VG_BakingClient](unity_component_vgbakingclient.1.4.0.html) has been overhauled with support of _Prepare project_ in the same GUI without the need to move to [Debug Settings](debug_files.1.4.0.html) if there are no runtime spawned {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects. 

##### GUI / Component Changes:

* AutoSetup enum name for Oculus finger tracking was changed from "Quest_FT" to "Oculus_FT" to conform with the file names and avoid confusion.
* Fixed confusion of disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description) component. Now, if the component is added but disabled (unchecked) the object will not be {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. Runtime enabling or disabling this component will make the object interactable or uninteractable respectively. However note that it is more efficient to change object's interactable status by [SetObjectSelectionWeight](virtualgrasp_unityapi.1.4.0.html#setobjectselectionweight).  (**fixed known issue from 0.11.1**)

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

* New recording sensor recording using [VG_Recorder](unity_component_vgrecorder.1.4.0.html) is pending the data to earlier recordings.

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.4.0.html) can lead to crashing.

* The 2nd method - pressing button "Export Scene in Edit" to [Create Debug Files](debug_files.1.4.0.html#creating-debug-files) has a bug: instead of create debug files in vg_tmp folder, it enabled "Export Scene in Runtime". 

* Runtime change parent of an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained joint type may result in unexpected {% include tooltip.html tooltip="JointAxis" text="joint axis" %}  different from its initial setting. 

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* [GetReplayStartWristPose](virtualgrasp_unityapi.1.4.0.html#getreplaystartwristpose) does not give accurate wrist pose. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.4.0.html) or [ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) as yet. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

## V0.11.1 (2022-04-11)

##### Major Functionality Changes:

* **Breaking change**: Avatar IDs that were before the array index have been replaced by the Unity instance ID of the SkinnedMeshRenderer that relates to the avatar. The VG API is providing helper functions and the SDK scripts have been adjusted accordingly. Check out [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.4.0.html#getsensorcontrolledavatarid), [GetReplayAvatarID](virtualgrasp_unityapi.1.4.0.html#getreplayavatarid), and [GetAvatarID](virtualgrasp_unityapi.1.4.0.html#getavatarid). 
* Released Gleechi's first original avatar in VirtualGrasp/Resources/GleechiHands. This replaces earlier released OcculusHands, so in the VG SDK that support only one avatar, only GleechiHands are supported.
* Added {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %} support on [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description). See VG Onboarding [Task6](unity_vgonboarding_task6.1.4.0.html) to show the example use. 

##### GUI / Component Changes:

* AutoSetup "External" string for Oculus finger tracking was changed from "QuestHand" to "OculusHand" to conform with the file names and avoid confusion.
* Bugfix on AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.1.4.0.html#vg_externalcontroller-class) you like to use. (**fixed known issue from 0.10.1**)
* [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description) has been overhauled as a dynamic component to improve user experience. 
* Replay and Remote checkboxes for avatar are only shown if the VG version supports this feature.
* [VG_Interactable](unity_component_vginteractable.1.4.0.html) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to allow specifying object-specific throwing power that overwrite those set in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings).
* [VG_Recorder](unity_component_vgrecorder.1.4.0.html) has improved file management so that users can optionally provide in _Recording Filename_ with either a single file name like "MyRecordingFile", or a folder and a file name like "MyRecordingFolder/MyRecordingFile". Also adding the file extension ".sdb" is only optional.

##### API Changes:

* **Breaking change**: [GetObjectJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectjointstate) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointState will be invalid.
* **Breaking change**: [GetObjectJointType](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectjointtype) changed function signature, so it checks if input selectedObject is null, will return error code, and output JointType will be invalid.
* [SetAvatarActive](virtualgrasp_unityapi.1.4.0.html#vg_controllersetavataractive) added an optional argument: resetPos.
* Added [GetObjectSecondaryJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectsecondaryjointstate) which provide {% include tooltip.html tooltip="JointState" text="joint state" %} along yaxis of joint anchor for {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joint" %}. 
* Added api functions to set velocity scales for throwing: [SetGlobalThrowVelocityScale](virtualgrasp_unityapi.1.4.0.html#vg_controllersetglobalthrowvelocityscale), [SetThrowVelocityScaleForSelectedObject](virtualgrasp_unityapi.1.4.0.html#vg_controllersetthrowvelocityscaleforselectedobject), [SetThrowVelocityScaleForObject](virtualgrasp_unityapi.1.4.0.html#vg_controllersetthrowvelocityscaleforobject), [SetGlobalThrowAngularVelocityScale](virtualgrasp_unityapi.1.4.0.html#setglobalthrowangularvelocityscale), [SetThrowAngularVelocityScaleForSelectedObject](virtualgrasp_unityapi.1.4.0.html#setthrowangularvelocityscaleforselectedobject), [SetThrowAngularVelocityScaleForObject](virtualgrasp_unityapi.1.4.0.html#setthrowangularvelocityscaleforobject). 
* Added [GetAvatarID](virtualgrasp_unityapi.1.4.0.html#vg_controllergetavatarid) to receive the ID of an avatar.
* Added [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.4.0.html#vg_controllergetsensorcontrolledavatarid) to receive the ID of the sensor-controlled avatar.
* Added [GetReplayAvatarID](virtualgrasp_unityapi.1.4.0.html#vg_controllergetreplayavatarid) to receive the ID of the replay avatar (if replaying is supported by the VG version).
* Added [UnregisterAvatarAtRuntime](virtualgrasp_unityapi.1.4.0.html#vg_controllerunregisteravataratruntime) to allow deleting avatars. (This is most relevant for multiplayer use case.)

##### Other / Internal Changes:

* Bugfix on [OnObjectSelected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectselected) event is not invoked for object with Index Pushable {% include tooltip.html tooltip="InteractionAffordance" text="interaction affordance" %}.
* Bugfix on [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) call. (**fixed known issue from 0.10.1**)
* Bugfix on after an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose. (**fixed known issue from 0.10.1**)
* Bugfix on physical avatar when grasping {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with {% include tooltip.html tooltip="StickyHand" text="sticky hand" %} interaction type object and hand is grandually moving away.
* Further performance optimization of selecting which objects need to be synced between Unity and VG.
* Improved grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider. Note however still Unity physical material with smaller friction should be used for desired sliding behaviors. (**fixed known issue from 0.10.1**)

* Provide error message when trying to use an controller but not enabling its #define (e.g., VG_USE_LEAP_CONTROLLER).
* Provide error signal if {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object is labeled as Static.
* Provide error signal if start a scene without providing SkeletalMesh for avatar setup. 
* Provide error message if you are on Mac that Mac is not supported.

* All #defines that enable controllers with dependencies on third party plugins have been prefixed with VG_ (e.g., USE_LEAP_CONTROLLER is now VG_USE_LEAP_CONTROLLER) to avoid conflicts with non-VG defines.
* Onboarding scene added [Task6](unity_vgonboarding_task6.1.4.0.html) to showcase VirtualGrasp's newly added support of {% include tooltip.html tooltip="Planar" text="planar" %} {% include tooltip.html tooltip="Joint" text="joints" %}. 
* Added first Unity tutorials.

##### Update to VG Core library 0.8.0:

* Bugfix for physical avatar index finger push gesture formation is not smooth. (**fixed known issue from 0.10.1**)
* Improved pinch grasp on small objects. (**fixed known issue from 0.10.1**)
* Bugfix for when hand form index finger push gesture grasp synthesis adopted push gesture problem.
* Bugfix for [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) crash on unbaked object problem. 

##### Known Issues:

* There is a problem of unreliable grasp and release triggering for finger tracking solutions OCULUS_FT. 

* If two hands grasp on a non-physical FLOATING object, when one hand releases, the other hand could have a big offset from sensor position.

* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.

* If two hands trigger grasp on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} at the exact same moment, the hands will form grasps, but the object freeze and can not be moved by hands. This is difficult to reproduce but still could happen.

* The newly released GleechiHands does not have perfect mapping of real finger poses when using finger tracking solutions like OCULUS_EXT and LEAP_EXT. 

* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.

* If game object's pivot is relatively far away from mesh center, then there is strange interactive behavior on PRISMATIC joint (both through [VG_Articulation](unity_component_vgarticulation.1.4.0.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html)): the rotating movement of controller can result in unexpected translation of object along the joint axis. Other constrained joint types are also affected. 

* If an object has rotational VG articulation joints, when switch from two hands grasping to one hand, or when one hand grasps an object at the moment of another hand releasing it, the remaining grasping hand have trouble to control the constrained object movement. 

* The newly added {% include tooltip.html tooltip="Planar" text="planar" %} joint does not support {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) as yet. 

* Successively recording sensor data using [VG_Recorder](unity_component_vgrecorder.1.4.0.html) can lead to crashing.

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered due to event handling is not taking care of this interaction type yet.

* If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. 

* Dynamic Grasp on small or thin objects sometimes thumb has no contact on the object.

## V0.10.1 (2022-03-01)

##### Major Functionality Changes:

* **Breaking change**: Removed support of using VG_Articulation component with constrained {% include tooltip.html tooltip="Joint" text="joints" %} (non-FLOATING joint) on objects with Rigidbody. Developers are encouraged to use [Unity Joints](https://docs.unity3d.com/Manual/Joints.html) or [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html) for physical joints.
* **Breaking change**: in [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description), "Pivot" changed name to "Anchor" to be more consistent with the terminology used by [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html). And "Push Pivot" changed name to "Push Direction" to be more descriptive. Due to the name change, the reference can be lost and need to be reassigned.
* More stable grasp interaction with {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} and better throwing experiences. 

##### GUI / Component Changes:

* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings) changed variable name "Grasp Speed" to "Grasp Animation Speed" and "Release Speed" to "Release Animation Speed". The default values for them are reduced to 0.05 (from 0.1) and 0.1 (from 0.2) second respectively to make grasp and release more snappy. The minimum values for both are reduced to 0.01 second (from 0.1 second).
* In [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings) added "Throw Velocity Scale" and "Throw Angular Velocity Scale" to control power of throw on grasped objects. 
* [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description) editing is disabled when object has Rigidbody component. (Was disabled when object has ArticulationBody component in version 0.9.6)
* Made VG_MainScript abstract since one should only use a child class (such as MyVirtualGrasp).
* Improved handling of AutoSetup when a VG_MainScript is created (such as adding a sensor instead of complaining it has not been added). 
* [MyVirtualGrasp/Avatars](unity_component_myvirtualgrasp.1.4.0.html#avatars) added "Replay" check to indicate if this avatar is to be used for sensor replay. If not checked, it will be controlled by sensor / controller. 

##### API Changes:

* **Breaking change**: VG_Controller.SetProcessedByFrame() function is removed. If you want to set an avatar for sensor replay, you can specify the avatar for replay by checking _Replay_ in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html#autosetup-sensors) component. 

##### Other / Internal Changes:

* Event handling bugfix: OnObjectFullyReleased do not trigger on objects that are not grasped. 
* Onboarding scene [Task3](unity_vgonboarding_task3.1.4.0.html) improved ManageContainerObject.cs script.
* Onboarding scene added [Task4](unity_vgonboarding_task4.1.4.0.html) showcase VirtualGrasp's support of interaction with ArticulationBodys. 
* Onboarding scene added [Task5](unity_vgonboarding_task5.1.4.0.html) showcase VirtualGrasp's support of object assembly with VG_Articulation without rely on physics. 
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
* [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) event is not invoked for [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) call.
* After an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object with constrained {% include tooltip.html tooltip="Joint" text="joint" %} follows the move of its non-{% include tooltip.html tooltip="VGInteractable" text="interactable" %} parent (or an ancester), the moment when hand grasp or push this constrained object, it jump back to the original global pose.
* Grasping and sliding a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} on another object with collider shows obvious non-smooth behavior due to some artificial manipulation of object velocities. 
* AutoSetup in MyVirtualGrasp is broken. Please refer to the manual "AutoSetup" sections on the [ExternalController](unity_component_vgexternalcontrollermanager.1.4.0.html#vg_externalcontroller-class) you like to use.

##### Known Issues:

* Since Unity 2019 or earlier versions do not have [Unity ArticulationBody](https://docs.unity3d.com/Manual/class-ArticulationBody.html), these earlier versions of Unity is not supported.
* A few events such as [OnObjectGrasped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectgrasped) and [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer scenes.
* Dynamic Grasp sometimes has unnaturally large thumb extention. 
* Grasps on small objects may have unatural finger placement.
* If a game object only has a disabled (unchecked) [VG_Articulation](unity_component_vgarticulation.1.4.0.html#description) component, this game object is still marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} so that you can grasp it. And even if this disabled VG_Articulation set a {% include tooltip.html tooltip="Joint" text="joint" %} other than Floating, it will behave as Floating {% include tooltip.html tooltip="Joint" text="joint" %}. These are undesired behavior and will be fixed.


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

-->