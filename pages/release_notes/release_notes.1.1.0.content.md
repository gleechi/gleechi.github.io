## V1.1.0  (2023-03-07)

##### Major Functionality Changes:
* **Breaking change:** How grasp db (.db file) is loaded into the project has been refactored:
  * In previous versions grasp db is unrecognized file for Unity, and now it is recognized as an asset if it is put into Assets folder. And any .db files inside Assets folder will be recognized as grasp db files. 
  * In previous versions once baking is finished the output grasps.db file will be put into StreamingAssets folder and will be automatically loaded into the project when playing. Now each time grasp baking is finished the output will be a new file "Assets/VG_Grasps/grasp-[hash].db" with random hash. 
  * And if you want to use the new baking result, developers need to set it into [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.4.0.html#grasp-db). 
  * If you want to use previously baked grasp db inside the StreamingAssets folder in previous VG versions, you need to move it into Assets folder, and drag this grasp db into [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.4.0.html#grasp-db). 

* **Breaking change for Pro version:** How sensor db (.sdb file) is loaded into the project has been refactored:
  * In previous versions sensor db is unrecognized file for Unity, and now it is recognized as an asset if it is put into Assets folder. And any .sdb files inside Assets folder will be recognized as sensor db assets. 
  * In previous versions [VG_Recorder in VG1.0.0](unity_component_vgrecorder.1.0.0.html) output recorded .sdb file into StreamingAssets folder. Now [VG_Recorder](unity_component_vgrecorder.1.4.0.html) needs to enter complete _New Recording Path_ end with .sdb file to save recorded data. 
  * When replaying recorded .sdb file, this file should be dragged into [VG_Recorder](unity_component_vgrecorder.1.4.0.html)  _Replay Recording_ entry. 

* For Pro version: [VG_Recorder](unity_component_vgrecorder.1.4.0.html) allows to assign multiple _Replay Avatars_. This allows you to replay data on a pair of hands that are represented by [separate hand models](avatars.1.4.0.html#separate-hand-models). **(fixed known issue from 1.0.0)**

* For tiny objects that need precision grasps, the grasp quality now varies depending on which {% include tooltip.html tooltip="InteractionType" text="interaction type" %} is chosen for the object. When {% include tooltip.html tooltip="JumpGrasp" text="jump grasp" %} is used on an object, the grasp will have more accurate finger placement on the object but the object will have larger rotation when "jumping" into the hand. When {% include tooltip.html tooltip="TriggerGrasp" text="trigger grasp" %} is used, the grasp will have less accurate finger placement with the benefit of less hand offset when moved towards the grasping pose. (See [Grasp Interaction Type](grasp_interaction.1.4.0.html#grasp-interaction-type) section.)

* Fixed a bug: "VirtualGrasp -> Make Interactables Readable" helper function now works, and you will see in console output which object(s) has been processed. **(fixed known issue from 1.0.0)**

##### GUI / Component Changes:

* [VG_FingerAnimator](unity_component_vgfingeranimator.1.4.0.html), [VG_ObjectAnimator](unity_component_vgobjectanimator.1.4.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.4.0.html) are added to support easy creation of animation of in-hand manipulation of articulated objects. See [VG onboarding task 9](unity_vgonboarding_task9.1.4.0.html) to learn an example use case.

* Fixed a bug: [SetSensorActive](virtualgrasp_unityapi.1.4.0.html#vg_controllersetsensoractive) now works properly. **(fixed known issue from 1.0.0)**

* Fixed a bug: In previous version, if an object has constrained {% include tooltip.html tooltip="Joint" text="joint" %}, pushing **Step grasp** button on [VG_GraspEditor](unity_component_vggraspeditor.1.4.0.html) to review primary grasps on this object did not work. Now it works. **(fixed known issue from 1.0.0)**

##### API Changes:

* Added two overloaded functions, [GetReplayAvatarID](virtualgrasp_unityapi.1.4.0.html#vg_controllergetreplayavatarid-1) and [GetSensorControlledAvatarID](virtualgrasp_unityapi.1.4.0.html#vg_controllergetsensorcontrolledavatarid-1), to provide two avatar ids when two avatars are used to represent left and right hands respectively. 

* Added [GetCurrentGesture](virtualgrasp_unityapi.1.4.0.html#vg_controllergetcurrentgesture) api function. 

* Previously [SwitchGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerswitchgraspobject) and [JumpGraspObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerjumpgraspobject) only work on objects with {% include tooltip.html tooltip="Floating" text="floating" %} joint, now it works on all objects including those with constrained (non-{% include tooltip.html tooltip="Floating" text="floating" %}) joint types. 

##### Other / Internal Changes:
* Fixed a bug: When an object is held in hand(s), runtime changes of physical properties of Rigidbody or ArticulationBody will be kept after this object is fully released. **(fixed known issue from 1.0.0)**
* [Task2 radio disassemble](unity_vgonboarding_task2.1.4.0.html) and [task7 chain assemble](unity_vgonboarding_task7.1.4.0.html) switched to use the new [VG_Assemble](unity_component_vgassemble.1.4.0.html) component. The old scripts DisassembleWithDistanc.cs and ChainAssembleVGArticulation.cs are removed. 
* [Task7 chain assemble](unity_vgonboarding_task7.1.4.0.html) switched to use the chain loop instead of previous the wrench. 
* [VG onboarding task 8](unity_vgonboarding_task8.1.4.0.html) was added to show case how [VG_Assemble](unity_component_vgassemble.1.4.0.html) is used to assemble or disassemble screw with a screw driver to a box.  
* [VG onboarding task 9](unity_vgonboarding_task9.1.4.0.html) was added to show case how to use the newly added three components, [VG_FingerAnimator](unity_component_vgfingeranimator.1.4.0.html), [VG_ObjectAnimator](unity_component_vgobjectanimator.1.4.0.html) and [VG_AnimationDriver](unity_component_vganimationdriver.1.4.0.html) to create animation of in-hand manipulation of articulated objects.
* VG onboarding scene now switches to use GRIP button as the **Grasp Button** in [MyVirtualGrasp -> Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.4.0.html#global-grasp-interaction-settings). This is to support [VG onboarding task 9](unity_vgonboarding_task9.1.4.0.html) to use TRIGGER button for animating the manipulation of the plier part.
* Fixed a bug: While a hand grasps a physical object to collide with another physical object, if any colliding object's collider is disabled, the controller grasping the object will continue to have vibrating haptic feedback until hand releases the object. Now it is fixed so that when the collider is disabled, the vibration will stop. **(fixed known issue from 1.0.0)**


##### Update to VG Core library:
* When a chain of objects are connected through VG constrained joints, in the previous version, if one hand grasps an upstream object, and the other grasps a distal object, only the distal object (with constrained but movable joint, i.e. non-Fixed) is movable by the hand. In this version (1.4.0) grasping the distal joint will move its upstream movable joint. This change allows (for example in [VG onboarding task 8](unity_vgonboarding_task8.1.4.0.html)) on a chain like box (floating) -> screw (revolute) -> screw driver (fixed), users could grasp box with one hand, and grasp and rotate the distal object, screw driver, with another hand in order to rotate screw into the box.

##### Known Issues:

* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* When index finger tip moves in a different direction from wrist, pushing can get double triggered.

* Multiplayer (_not available in free or pro versions_) with VG network message still can not solve complete object sync for new player registration.

* A few events such as [OnObjectDeselected](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectdeselected) do not function correctly for proxy avatars in multiplayer 
(_not available in free or pro versions_) scenes.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* You can not use _OVR Hand_ (which can be found in the Oculus Integration under Oculus\VR\Scripts\Util\OVRHand.cs) together with VG controllers at the moment, as they both are independently affecting the hand model. 

* The [VG_AnimationDriver](https://docs.virtualgrasp.com/unity_component_vganimationdriver.1.4.0.html) is currently relying on the Unity "XR Interaction Toolkit" package. We thus have a dependency of this system in the current 1.4.0, but will resolve this in the next so it can also be used with legacy input.

* When a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody is released from grasping, the RigidBody.iskinematic always switch to false even if the developer has changed iskinematic to true when object is grasped.

* The first overloaded function [ChangeObjectJoint](virtualgrasp_unityapi.1.4.0.html#vg_controllerchangeobjectjoint) has a bug on joint limit setting of Revolute and Cone joint types because the limit angle in degree missed to be converted to radian before passing to the VirtualGrasp library.

* When handover a {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} from one hand to another, sometimes the receiving hands may drop together with the object. 

* Repeated runtime calling of register and unregister of avtars will cause Unity crash due to memory leaks.  

* When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraint of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. 

{% include_relative release_notes.1.0.0.md %}