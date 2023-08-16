## V1.3.0 (2023-05-15)

##### Major Functionality Changes:
* [StopSettingObjectJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllerstopsettingobjectjointstate) is added and should be called after [SetObjectJointState](virtualgrasp_unityapi.1.4.0.html#vg_controllersetobjectjointstate) is called on an object. If not this object may not be able to be moved by grasping hands later. 


##### GUI / Component Changes:
* Extend [Hand Profile](unity_component_vghandprofile.1.4.0.html) UI by thumb rotation, and hide the **Hand Bone Indices** that form the map of avatar's bone to gleechi hand model.

##### API Changes:
* Add AVATAR_ALREADY_REGISTERED enum to use when registering avatar is already registered (and return that avatars ID instead of 0). 
* [OnObjectPushStopped](virtualgrasp_unityapi.1.4.0.html#vg_controlleronobjectpushstopped) event is added when hand released push on an object. 
* [GetHand](virtualgrasp_unityapi.1.4.0.html#vg_controllergethand-1) overload function is added. 

##### Other / Internal Changes:
* Fixed a bug: When {% include tooltip.html tooltip="PhysicalObject" text="physical object" %} with RigidBody has constraint of movement, and {% include tooltip.html tooltip="JumpGrasp" text="Jump Grasp" %} interaction type is used, object will jump to hand without respecting this physical constraints. Now it is fixed and hand will interpolate to the object instead. **(fixed known issue from 1.2.0)**
* Fixed a bug: VG_Articulation on joint gizmo has a bug for Revolute joint, the gizmo shown joint range with left-handed system that is opposite to the direction of object rotation. Also for both Revolute and Prismatic joint, the gizmo is moving together with object, not respecting the initial zero pose. Now both problems are fixed. **(fixed known issue from 1.2.0)**
* Fixed a bug: When mirror hand control is enabled, the disabling of hand still are controlled by missing sensor signal from same side. Now it will only disable hand if mirrored sensor signal missing. **(fixed known issue from 1.2.0)**
* Make external controller VG_EC_MouseHand only update pose if Application.isFocused. 

##### Known Issues:
* When graspable object is very close to an index pushable object, after grasp the object, pushing gesture may not form. 

* When index finger tip moves in a different direction from wrist, pushing can get double triggered.

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.4.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup.

* When runtime spawn a new avatar, the existing registered avatar's hands will suddenly flip. 

* [Grasp Editor](unity_component_vggraspeditor.1.4.0.html) is not working with runtime spawned {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}.

{% include_relative release_notes.1.2.0.md %}