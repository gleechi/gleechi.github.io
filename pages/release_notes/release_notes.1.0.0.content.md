## V1.0.0 (2022-12-07)

##### Major Functionality Changes:
* **Breaking change:** The Sensor/Avatar configuration in the MyVirtualGrasp component has been refactored:
  * While before, a list of Avatars could be assigned to each element of a list of Sensors, 
  * now maximally 2 Sensor setups can be assigned to each element of a a list of Avatars (see [MyVirtualGrasp 1.4.0](unity_component_myvirtualgrasp.1.4.0.html#avatars-and-sensors)).
  * If you are updating to this version from an older version, **you need to re-configure your MyVirtualGrasp component**.

* **Breaking change:** The old GetNumGrasps API function changed name to [GetNumGraspsInDB](virtualgrasp_unityapi.1.4.0.html#vg_controllergetnumgraspsindb) to avoid potentially confusing user to think GetNumGrasps is to obtain currently executed grasps on an object. 
  * Together with this change, a new api function [GetNumPrimaryGraspsInDB](virtualgrasp_unityapi.1.4.0.html#vg_controllergetnumprimarygraspsindb) is added to give number of enabled {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasps" %} in the grasp DB. 

* **Breaking change:** Enum VG_AvatarType has been removed. The old RegisterAvatar API functions have been split upto 3 functions depending on avatar type:
  * [RegisterSensorAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerregistersensoravatar) for sensor controlled avatars, where several overloads exist. The most common is to register an avatar with a single sensor setup without any network output. A secondary sensor setup and network output can be added. 
  * [RegisterRemoteAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerregisterremoteavatar) for remote controlled avatars in multiplayer applications, and
  * [RegisterReplayAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerregisterreplayavatar) for replay controlled avatars.

* [VG_HandProfiles](avatars.1.4.0.html) were introduced to simplify the external controller mapping for custom hand models.

* [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) (two overloaded functions) and [RecoverObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerrecoverobjectjoint) do not have any function signature change. However from this version, VG will internally remove Rigidbody or ArticulationBody on a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} if the function call intends to change object joint to a constrained joint type (non-{% include tooltip.html tooltip="Floating" text="floating" %}), and recover just removed Rigidbody or ArticulationBody when it changes back to  {% include tooltip.html tooltip="Floating" text="floating" %} joint type. This change makes it convenient for Unity developers to benefit from VG's [object articulation](object_articulation.1.4.0.html) system on both physical and non-physical environments.

* Added "ensemble physical object" support. That is when assembling two {% include tooltip.html tooltip="PhysicalObject" text="physical objects" %} through [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint), as an example shown in [VG Onboarding Task7](unity_vgonboarding_task7.1.4.0.html), grasping the child objects (when child became non-physical due to object change to constrained joint type), the parent which is still a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} will follow as if the parent-child has become an ensemble physical object.

* When an object's Rigidbody component has Rigidbody.isKinematic true, VG will consider this object as a non-{% include tooltip.html tooltip="PhysicalObject" text="physical object" %}. (In previous versions whenever an object has Rigidbody component, even when it is kinematic, VG considers the object physical resulting in some unwanted interaction behaviors.)

##### GUI / Component Changes:
* Only one enabled [VG_Articulation](unity_component_vgarticulation.1.4.0.html) component is allowed now, and the enabled component reflects the current [object articulation](object_articulation.1.4.0.html) status.
* [VG_Articulation](unity_component_vgarticulation.1.4.0.html) for constrained joint types now allows selection of "Motion Type" to be Limited or Free, where Free means there is no limitation along the constrained dof(s) of this joint. 
* [VG_GraspEditor](unity_component_vggraspeditor.1.4.0.html) 
  * The prefab has improved 3D shape and texture, and
  * has been moved to ThirdParty/VirtualGrasp/Resources/GraspEditor/ to separate it from the Onboarding demo scene.
  * VG_GraspEditor script exposed an option _Editing Interaction Type_ to allow developers to choose the main {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to use when adding primary grasps. 
* "VirtualGrasp" Menu cleanup. Some obsolete entries were removed.
* [VG_Articulation](unity_component_vgarticulation.1.4.0.html), [VG_Interactable](unity_component_vginteractable.1.4.0.html) and [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html) scripts are deactivated during runtime to better reflect that changes to them are only valid in editor mode.
* Grasp and Release animation speeds in [MyVirtualGrasp](unity_component_myvirtualgrasp.1.4.0.html) GUI integer fields were replaced by range sliders.

##### API Changes:

* Fixed a bug:: if runtime [UnRegisterAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllerunregisteravatar) and then reregister again, the reregistered avatar will lose sensor control. 
* Added [VG_GestureType](virtualgrasp_unityapi.1.4.0.html#vg_gesturetype) enum and [MakeGesture](virtualgrasp_unityapi.1.4.0.html#vg_controllermakegesture) api switched to use this enum instead of previously using [VG_GraspType](virtualgrasp_unityapi.1.4.0.html#vg_grasptype). **(fixed known issue from 0.15.0)**
* All API functions properly guarded if VG is actually active.
* Removed SetPhysicalObject, OnAfterReset, OnBeforeReset and ResetObject and ResetAllObjects API functions.
* Added [GetObjectSelectionWeight](virtualgrasp_unityapi.1.4.0.html#vg_controllergetobjectselectionweight) and [GetAvatarSpecificObjectSelectionWeight](virtualgrasp_unityapi.1.4.0.html#vg_controllergetavatarspecificobjectselectionweight) API functions.
* Added [SetRecordingStatesOnAvatar](virtualgrasp_unityapi.1.4.0.html#vg_controllersetrecordingstatesonavatar) API function.
* Some minor tweaks to VG_GraspEditor, VG_Highlighter, and VG_Recorder.

##### Other / Internal Changes:
* Fixed a bug: when [OnGraspTriggered](virtualgrasp_unityapi.1.4.0.html#vg_controllerongrasptriggered) event invoked, sometimes m_selectedObject is null.
* Fixed a bug: sometimes an {% include tooltip.html tooltip="VGInteractable" text="interactable" %} object's {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %} becomes negative causing this object not interactable. 
* If an object is set to afford INDEX_PUSHABLE interaction, VG library will switch its {% include tooltip.html tooltip="InteractionType" text="interaction type" %} to {% include tooltip.html tooltip="StickyHand" text="STICKY HAND" %} to avoid some unneccssary debug outputs.
* [VG onboarding task 5](unity_vgonboarding_task5.1.4.0.html) added an additional prefab, "Task5_bottle_with_rigidbody", in the onboarding scene to show the same AssembleVGArticulation.cs also works on the bottle and cap when they are physical objects. 
* Added [VG onboarding task 7](unity_vgonboarding_task7.1.4.0.html) showing off using VG Articulation to assemble a chain with physical objects.  
* For [VG onboarding task4](unity_vgonboarding_task4.1.4.0.html) and [task5](unity_vgonboarding_task5.1.4.0.html), the function for assembling has improved computation of desired object rotation; the assembling and dissasembling code are called in LateUpdate instead of Update to sync with player input. 
* Multiplayer (_not available in free or pro versions_) VG support now allows multiple players grasping on the same object at the same time, and also works with complex object settings.
* Explicit asset database refresh added when VG creates files (such as files for mesh baking input and output).
* Adjusted In-Editor tutorials to follow the new changes in the VG API and GUI.
* Improved the project file structure. Among others made it possible to delete the example onboarding folder and resources to make the plugin lighter without affecting VG functionality.
* Fixed a bug: {% include tooltip.html tooltip="PreviewGrasp" text="Preview grasp" %} is not able to pick up a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} once grasp is triggered. **(fixed known issue from 0.15.0)**
* Fixed a bug: If _Haptics_ is enabled in [Sensor Control](unity_component_myvirtualgrasp.1.4.0.html) specifications, haptics feedback is not consistently given at the moment of grasp, release or collision on build. **(fixed known issue from 0.15.0)**
* The .NET TargetFrameworkVersion has been downgraded from 4.7.2 to 4.7.1 since it caused some issues for Unity+VSCode users.
* Fixed a bug: when pause a VR app with Occulus button or remove headset, the grasp pose is lost. 
* Improved the status sync of [VG_Articulation](unity_component_vgarticulation.1.4.0.html) on a Game Object with the interactability of that objects.
* Fixed a bug: the second avatar registered has twisted finger bones. 
* Improved the VG_MainScript inspector DebugSettings to become a proper foldout menu. 
* Fixed a bug: crashing when [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject), [SwitchGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerswitchgraspobject), or [TogglePrimaryGraspOnObject](virtualgrasp_unityapi.1.4.0.html#vg_controllertoggleprimarygrasponobject) is called on an object without mesh assigned to it.

##### Update to VG Core library:

* Improved the grasp interaction on object that has rotating {% include tooltip.html tooltip="JointType" text="joint types" %}. 
* Improved the grasp interaction on floating objects with multiple hands. 
* Completed {% include tooltip.html tooltip="Planar" text="planar" %} joint features by adding {% include tooltip.html tooltip="DiscreteStates" text="discrete states" %} and [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) support. **(fixed known issue from 0.15.0)**
* Reduced dynamic grasp finger-object penetration when pinch grasp small elongated objects.
* Fixed a bug: hand twisting when registering multiple avatars of same structure was fixed.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* When index finger tip moves in a different direction from wrist, pushing can get double triggered.

* Multiplayer (_not available in free or pro versions_) with VG network message still can not solve complete object sync for new player registration.

* A few events such as [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer 
(_not available in free or pro versions_) scenes.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* [VG_Recorder](unity_component_vgrecorder.1.4.0.html) only allows to assign one _Replay Avatar_, which makes it not work if you have [separate hand models](avatars.1.4.0.html#separate-hand-models) when using custom avatar supported by VG **Pro version**.  

* [SetSensorActive](virtualgrasp_unityapi.1.4.0.html#vg_controllersetsensoractive) does not have effect. If you set it inactive, the avatar's hands are still controlled and moved by the sensor / controller. 

* "VirtualGrasp -> Make Interactables Readable" helper function is not working. For now you have to manually check “Read/Write enabled” checkbox in the model inspector of your object in order to interact with the object or bake grasp.

* When an object is held in hand(s), runtime changes of physical properties of Rigidbody or ArticulationBody get lost once this object is fully released.

* If an object has constrained {% include tooltip.html tooltip="Joint" text="joint" %}, pushing **Step grasp** button on [VG_GraspEditor](unity_component_vggraspeditor.1.4.0.html) to review primary grasps on this object does not work.

* While a hand grasps a physical object to collide with another physical object, if any colliding object's collider is disabled, the controller grasping the object will continue to have vibrating haptic feedback until hand releases the object.

* You can not use _OVR Hand_ (which can be found in the Oculus Integration under Oculus\VR\Scripts\Util\OVRHand.cs) together with VG controllers at the moment, as they both are independently affecting the hand model. 
