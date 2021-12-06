---
title: Release Notes
#tags: [getting_started]
keywords: release notes #, announcements, what's new, new features
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: release_notes.html
folder: mydoc
---

## V0.9.2 (2021-12-06)

##### Major Functionality Changes:

* VG_Articulation will take care of object de/registration to VG. Runtime functions RegisterObjectAtRuntime(), RegisterObjectsAtRuntime(), DeleteDistalObjectAtRuntime() removed.

##### GUI / Component Changes:

* VG_DebugSettings modified. EditMode Save Debug Files for Current Editor Scene ⚠️. Read more on [Debug Files](debug_files.html).
* VG_Articulation.Lock() and VG_Articulation.Unlock() shortcuts removed. Using them in Events was unsafe. In code, use VG_Controller.ChangeObjectJoint(transform, VG_JointType.FIXED) instead of VG_Articulation.Lock(), and VG_Controller.RecoverObjectJoint(transform) instead of VG_Articulation.Unlock().
* Fixed problem in GraspEditor scene creation when UnityEngine.SpatialTracking.TrackedPoseDriver is not available, but only UnityEngine.InputSystem.XR.TrackedPoseDriver.
* VG_EC_GenericHand added and used as fallback for VG_ExternalControllerManager.
* VG_GraspStudio allows deleting grasps. To delete a grasp, you have to "double-disable" it. Read more on [VG_GraspStudio](unity_component_vggraspstudio.html).
* VG_Recorder extended with example to call new VG_Controller.GetReplayStartWristPose().

##### API Changes:
* SetAvatarActive() added to set avatar in/active (i.e. sensor control and mesh visualization).
* GetReplayStartWristPose() added to return starting wrist poses of a recording.
* RegisterObjectAtRuntime(), RegisterObjectsAtRuntime(), DeleteDistalObjectAtRuntime() removed. VG_Articulation will take care of de/registration.

##### Update to VG Core library 0.6.2: 

* Fixed some big penetration problems in Dynamic Grasp. 
* Added an api function to delete an object in the middle of the object tree and all its downstream objects.
* Fixed a bug that causes crash when useing {% include tooltip.html tooltip="PreviewGrasp" text="preview grasp" %} interaction type.

##### Other / Internal Changes:

* Fallback .db added and implemented to use this one if project .db is not found.
* Grasp Studio Scene will open automatically after creation.
* Fixed a bug in VG_Articulation initialization.
* Fixed kink when using physical objects with {% include tooltip.html tooltip="JumpGrasp" text="jump grasp" %} and {% include tooltip.html tooltip="JumpPrimaryGrasp" text="jump primary grasp" %} interaction types.
* Fixed that meshes disappear when prefabs are opened in Editor.
* Fixed screw rate to accept float values.
* Default synthesis method changed from STATIC_GRASP to DYNAMIC_GRASP.

##### Known Issues:

* Rotation interaction on physical object with revolute joint does not feel so natural.

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

    * Read more on [VG_BakingClient](unity_component_vgbakingclient.html) (when updated).


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

