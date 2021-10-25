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


## Changes from V0.7.0 (2021-09-17) to V0.7.1 (2021-10-04)

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

## Changes from V0.6.0 (2021-06-17) to V0.7.0 (2021-09-17)

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

## V0.5 (2021-03-24)

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

