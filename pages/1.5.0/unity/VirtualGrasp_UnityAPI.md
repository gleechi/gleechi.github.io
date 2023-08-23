---
title: Unity API
sidebar: main_sidebar_1_5_0
keywords: grasp, baking, cabvg
permalink: virtualgrasp_unityapi.1.5.0.html
folder: unity
toc: true
---
<hr><b>Tags</b>
<table>
<tr><td><span class="label label-primary">pro</span></td><td>this function is related to a feature that is not part of the free version.
Calling it when not supported should result in a VG_ReturnCode.UNSUPPORTED_FUNCTION.</td></tr>
<tr><td><span class="label label-default">video</span></td><td>this function is related to a tutorial movie.</td></tr>
</table><hr>

## [ENUMS](#enums)

### VG_BoneType

An enum to describe a bone type, used for accessing of bones from outside the library.

|WRIST|The wrist bone of a hand|
|ELBOW|The elbow bone of an arm|
|SHOULDER|The shoulder bone of an arm|
|CLAVICLE|The clavicle bone of an arm|
|APPROACH|The approach handle of a grasp|


### VG_EditorAction

Action towards the grasp editor, see EditGrasp()

|PRIMARY_CURRENT|Label the current grasp as primary, so it will be the only grasp for this object|
|DISABLE_CURRENT|Label the current grasp as disabled, so it will not be accessible for static grasping.|
|DELETE_CURRENT|Currently the same as DISABLE_CURRENT, since we do not really want to remove grasps.|
|DELETE_ALL_HAND_GRASPS|Delete the HandGrasp entry for a given object and hand hash|
|ADD_CURRENT|Add the current grasp as a valid one, so it becomes accessible for static grasping.|
|CLEAR_PRIMARY|Remove the label of the current object's primary grasp, so all grasps will be valid again.|
|CLEAR_DISABLED|Remove the label of the current object's disabled grasps, so all grasps will be valid again.|


### VG_FingerControlType

An enum to describe how fingers are controlled.

|BY_NOTHING|When not grasping, fingers are not controlled at all.|
|BY_SENSOR_FULL_DOFS|When not grasping, fingers are fully controlled by sensor|
|BY_SENSOR_LOW_DOFS|When not grasping, fingers are controlled by sensor, but less DOF.|
|BY_ANIMATION|When not grasping, fingers are controlled by animation.|
|BY_OSCILLATED_ANIMATION|When not grasping, fingers are controlled by oscillating between two state of animations|


### VG_GestureType

A humanoid hand gesture type enum.

|UNKNOWN_GESTURETYPE|Unknown type|
|PUSH_GESTURE|Index finger push gesture|
|FIST_GESTURE|Fist gesture|


### VG_GraspLabel

For labeling grasps (grasp editor functionality).

|DISABLED|Labels a grasp as disabled|
|PRIMARY|Labels a grasp as primary|
|SUCCEEDED|Labels a grasp as succeeded|
|FAILED|Labels a grasp as failed|
|RANK|TBD|


### VG_GraspType

Animation grasp type enum.

|UNKNOWN_GRASPTYPE|Unknown type|
|POWER|Humanoid power grasp|
|PINCH|Humanoid pinch grasp|
|OPENING|Robotic opening grasp|
|CLOSING|Robotic closing grasp|
|SUCTION_PIN|Robotic suction pin grasp|


### VG_HandSide

We support two hands per avatar, left and right in this enum.

|LEFT|Left hand|
|UNKNOWN_HANDSIDE|Unknown hand side|
|RIGHT|Right hand|


### VG_InteractionMode

Enum that defines at what state the hand is in and you can access a specific hand's mode through its VG_HandStatus.

|RELEASE|when wrist and finger toward sensor pose|
|GRASP|when wrist and finger towards target grasp pose|
|HOLD|when hand hold the object, and wrist towards following sensor pose|
|EMPTY|when hand not hold the object, wrist and finger fully follow sensor pose|
|PREVIEW|when grasp is to be previewed before change to HOLD by grasp trigger|
|MANIPULATE|when wrist is controlled by sensor relative pose|
|HOLD_MULTIHAND|when doing multi-hands holding|
|MANIPULATE_MULTIHAND|when doing multi-hands manipulation|
|PREVIEW_RELEASE|when release from PREVIEW mode, wrist and finger interpolate toward sensor pose|
|GRASP_TO_PREVIEW|when wrist and finger interpolate towards target grasp pose synthesized once a new object is selected|
|PUSHING|when index finger tip do push on object|
|PUSHING_MULTIHAND|when both hand's index finger tip do push on same object|


### VG_InteractionType

An enum to describe a hand interaction type (i.e. a mode on grasp visualization).

|TRIGGER_GRASP|Default, hand goes to object at grasp position|
|PREVIEW_GRASP|Grasp is always previewed once object is selected, trigger will pick up the object|
|PREVIEW_ONLY|like PREVIEW_GRASP, but trigger will not allow pick up the object|
|JUMP_GRASP|Object jumps to hand when grasp is triggered|
|STICKY_HAND|Object sticks to hand without forming grasp pose when grasp is triggered|
|JUMP_PRIMARY_GRASP|Using mechanism like JUMP_GRASP, but use a primary grasp in grasp DB|


### VG_JointType

Different articulated joint types supported by VG.

|REVOLUTE|revolute joint with constrained rotational movement around an axis|
|PRISMATIC|prismatic joint with constrained translational movement along an axis|
|FIXED|fixed, non-moveable joint|
|FLOATING|floating, unconstrained joint|
|PLANAR|planar joint with constrained translational movement on a plane|
|CONE|3-DOF ball and socket joint modeled with cone joint limit|


### VG_MotionType

Whether the motion is free or limited

|Limited|If motion is limited by the limits in the joint's degree of freedom(s)|
|Free|If motion is free in the joint's degree of freedom(s)|


### VG_NetworkSignal

Enum bitmask to compose parts of a NetworkSignal

|None|Empty signal|
|ControllerSignal|Flag for the controller part of the network signal.|
|SensorSignal|Flag for the sensor part of the network signal.|
|TriggerSignal|Flag for the trigger part of the network signal.|
|ObjectSignal|Flag for the object part of the network signal.|


### VG_QueryGraspMethod

The query grasp method for GetGrasp() function

|BY_INDEX|get grasp by index|
|BY_ID|get grasp by ID|
|BY_TCP|get grasp by TCP|


### VG_QueryGraspMode

Decide when query grasp if hand moves and how to move hand.

|NO_MOVE|will not move internal object and hand|
|MOVE_HAND_SMOOTHLY|will move object and hand moves smoothly with a transition period|
|MOVE_HAND_DIRECTLY|will move object and hand move directly to target grasp pose|


### VG_ReturnCode

ReturnCode for various VirtualGrasp functions.Most functions in this API provide such a return code.

|SUCCESS|Succeeded in processing function|
|DLL_NOT_INITIALIZED|Failed in processing function because library has not been initialized.|
|DLL_FUNCTION_FAILED|Failed in processing function because library has not been initialized.|
|INVALID_AVATAR|Failed in processing function because the provided avatar is invalid.|
|INVALID_LIMB|Failed in processing function because the provided limb or object is invalid.|
|INVALID_GRASP|Failed in processing function because the provided grasp is invalid.|
|INVALID_TARGET|Failed in processing function because the provided target is invalid.|
|ARGUMENT_ERROR|Failed in processing function because a provided argument is invalid.|
|UNSUPPORTED_FUNCTION|Failed in processing function because it is unsupported.|
|OBJECT_NO_GRASPS|Failed in processing function because there are no static grasps baked.|
|OBJECT_NO_BAKE|Failed in processing function because a baking process failed / there is no bake at all.|
|LOAD_GRASP_DB_FAILED|Failed to pass a grasp db file into the library and process it.|
|SAVE_GRASP_DB_FAILED|Failed to export the internal grasp db to a file.|
|UNKNOWN_AVATAR||
|AVATAR_BLOCKED||
|ARTICULATION_SETUP_FAILED||
|NO_SENSOR_DB||
|ARTICULATION_NO_CHANGE||
|INVALID_OBJECT||
|AVATAR_ALREADY_REGISTERED||
|NO_GRABER_WRIST_FOUND||
|INVALID_FIRST_GRABBER||


### VG_SensorControlFlags

Enum flag to describe what controller signals a sensor should cover.

|POSITION|Enable wrist position signal|
|ROTATION|Enable wrist rotation signal|
|FINGERS|Enable finger configuration signals|
|GRASP|Enable grasp trigger signal|
|HAPTICS|Enable haptics signals|


### VG_SensorType

Different sensor (or controller) types that can be used by VirtualGrasp. Note only External Controller is supported.

|NO_CONTROLLER|no controller|
|LEAP|Internal Controller (not supported), Leap motion 3D camera|
|RAZER_HYDRA|Internal Controller (not supported), Razer Hydra controllers|
|INTEL_REALSENSE|Internal Controller (not supported), Intel Realsense 3D camera|
|MANUS|Internal Controller (not supported), Manus VR gloves|
|KNUCKLES|Internal Controller (not supported), Valve Knuckles controller|
|VIVE|Internal Controller (not supported), HTC Vive controllers, supported through OpenVR|
|OCULUS_TOUCH_OPENVR|Internal Controller (not supported), Oculus Touch controllers, supported through OpenVR|
|VIVE_TRACKER|Internal Controller (not supported), A ViveTracker|
|OCULUS_TOUCH_OVR|Internal Controller (not supported), Oculus Touch controllers, through OculusVR.|
|EXTERNAL_CONTROLLER|External Controller, customized controller|
|BEBOP|Internal Controller (not supported), Bebop VR gloves|


### VG_VrButton

Enum for setting which (VR) controller buttons.

|TRIGGER|Use the trigger button (usually index finger on the controller) to grasp.|
|GRIP|Use the grip button (usually middle finger on the controller) to grasp.|
|GRIP_OR_TRIGGER|Use both the trigger and the grip button (logical OR) to grasp.|



## [EVENTS](#events)

### VG_Controller.OnAvatarSpecificObjectSelectionWeightChanged

This event is invoked when an avatar-specific object selection weight is changed. The event carries the object and avatarID for which the weight has been changed and the new weight.



### VG_Controller.OnGraspTriggered

This event is invoked in the frame when a hand is starting to grasp an object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectCollided

This event is invoked when a grasped object is colliding with another object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectDeselected

This event is invoked in the frame when a hand is starting to deselect an object. The VG_HandStatus it carries includes more information about the interaction.


Used in: [VG_Highlighter](unity_component_vghighlighter.1.5.0.html)


### VG_Controller.OnObjectFullyReleased

This event is invoked in the frame when an object is fully release by all hands. The Transform it carries includes the object that has just been released.



### VG_Controller.OnObjectGrasped

This event is invoked in the frame when a hand has fully grasped an object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectJointChanged

This event is invoked when an object's articulation / joint is changed. The VG_Articulation it carries includes more information about the joint.



### VG_Controller.OnObjectJointChangedOnJointConfig

This event is invoked when an object's articulation / joint is changed. The VG_ObjectJointConfig carries the new joint configuration after joint change.



### VG_Controller.OnObjectPushStopped

This event is invoked in the frame when a hand releases push on an object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectPushed

This event is invoked in the frame when a hand pushing an object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectReleased

This event is invoked in the frame when a hand is starting to release an object. The VG_HandStatus it carries includes more information about the interaction.



### VG_Controller.OnObjectSelected

This event is invoked in the frame when a hand is starting to select an object. The VG_HandStatus it carries includes more information about the interaction.


Used in: [VG_Highlighter](unity_component_vghighlighter.1.5.0.html)


### VG_Controller.OnObjectSelectionWeightChanged

This event is invoked when an object's selection weight is changed. The event carries the object for which the weight has been changed and the new weight.




## [OBJECT_SELECTION_API](#object_selection_api)

### VG_Controller.ChangeObjectJoint

Change a set of parameters of an object's joint in runtime.

| _Transform_ |selectedObject|The object to change the object joint parameters.|
|[*VG_JointType*](#vg_jointtype) | jointType|The new joint type.|
|[*VG_MotionType*](#vg_motiontype) | motionType|The new motion type specifying if motion should be limited or free.|
| _Transform_ |anchorTransform|The new anchor transform.|
| _Vector2_ |limit|The new limit of the new joint type. For planar joint this is the limit along xaxis of the anchor transform. |
| _float_ |screwRate|The new screw rate (\>=0, in cm per degree) for revolute joint.|
| _Vector2_ |limit2|The new limit along y-axis of the anchor transform for planar joint.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 If screwRate is set to 0 then rotating of revolute object will not move object position along the joint axis.


**Remark:**
 Recommend to use this in LateUpdate to guarantee object pose is in sync with VirtualGrasp library.


**Remark:**
 Should not be called on a Game Object that has [RequireComponent(typeof(Rigidbody))] attribute since VG needs to destroy Rigidbody when change to constrained joint type.



### VG_Controller.ChangeObjectJoint

Change an object's joint and all other articulation parameters in runtime.

| _Transform_ |selectedObject|The object to change the joint for.|
| _VG_Articulation_ |articulation|An articulation describing the new articulation parameters.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Recommend to use this in LateUpdate to guarantee object pose is in sync with VirtualGrasp library.


**Remark:**
 Should not be called on a Game Object that has [RequireComponent(typeof(Rigidbody))] attribute since VG needs to destroy Rigidbody when change to constrained joint type.



### VG_Controller.ClearAvatarSpecificObjectSelectionWeights

Clear all avatar specific object selection weights.

| _int_ |avatarID|The avatar id|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.GetAvatarSpecificObjectSelectionWeight

Returns the avatar specific object selection weight of an object for interaction.

| _int_ |avatarID|The avatar id|
| _Transform_ |obj|Which object to specify weight|
| _**out** float_ |weight|The corresponding weight|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Note by default this weight is equal to the object's selection weight for all avatars.


**Remark:**
 Use case is mainly to specify relative selection preferences for cluttered objects.



### VG_Controller.GetGraspButton

Return the currently selected GraspButton.



### VG_Controller.GetGraspingAvatars

Return the avatar/hand pairs that are currently grasping a specified object.

| _Transform_ |objectToCheck|The object to be checked if it is currently grasped.|
| _**out** List\<KeyValuePair\<int, VG_HandSide\>\>_ |hands|An output list of avatar-hand-side-pairs describing which hands are currently grasping that object.|
| **returns** | _int_ | Number of hands grasping the object.|


### VG_Controller.GetObjectJointState

Get the current joint state of a single-dof articulated object. For planar joint, the joint state along x-axis of the joint anchor.

| _Transform_ |selectedObject|The object to get the current joint state value for.|
| _**out** float_ |jointState|The returned joint state. Will be set to 0.0f upon error|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call. when selectedObject is null, or VG_ReturnCode.DLL_FUNCTION_FAILED on an unexpected error.|


### VG_Controller.GetObjectJointType

Get object's original or current joint type.

| _Transform_ |selectedObject|The object to get the current joint state value for.|
| _bool_ |original|If true, get the original joint type, otherwise the current type.|
| _**out** VG_JointType_ |jointType|The returned joint type. Will be set to FLOATING upon error.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call. when selectedObject is null, or VG_ReturnCode.DLL_FUNCTION_FAILED on an unexpected error.|


### VG_Controller.GetObjectSecondaryJointState

Get the current secondary joint state along y-axis of joint anchor for planar articulated object.

| _Transform_ |selectedObject|The object to get the current joint state value for.|
| _**out** float_ |secondaryJointState|The returned secondary joint state. Will be set to 0.0f upon error.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call. when selectedObject is null, or VG_ReturnCode.DLL_FUNCTION_FAILED on an unexpected error.|


### VG_Controller.GetObjectSelectionWeight

Returns the object selection weight for grasping interaction.

| _Transform_ |obj|Which object to specify weight|
| _**out** float_ |weight|The corresponding weight|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Note by default this weight is 1 for all objects.


**Remark:**
 Use case is mainly to specify relative selection preferences for cluttered objects.



### VG_Controller.GetObjectZeroPose

Receive the zero pose of the object or its joint anchor.

| _int_ |objectID|The avatar to get the zero pose.|
| _**out** Vector3_ |p|The returned position.|
| _**out** Quaternion_ |q|The returned rotation.|
| _bool_ |isJointAnchor|Set True (default) to get zero pose of object's joint center (anchor)s, and False to return the zero pose of object.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.GetSelectableObjects

Return all interactable objects.

| _bool_ |excludeHidden|If to exclude objects that have been hidden in the scene.|
| _bool_ |excludeUntagged|If to exclude objects that have been untagged in the scene.|
| **returns** | _IEnumerable\<Transform\>_ | All interactable objects in the scene.|


### VG_Controller.GetSelectableObjectsFromScene

Return all interactable objects from the editor scene.

| _bool_ |excludeHidden|If to exclude objects that have been hidden in the scene.|
| _bool_ |excludeUntagged|If to exclude objects that have been untagged in the scene.|
| **returns** | _List\<Transform\>_ | All interactable objects in the editor scene.|


### VG_Controller.GetSensorPose

Receive the sensor pose of a given avatar and hand.

| _int_ |avatarID|The avatar to get the pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the pose from.|
| _**out** Vector3_ |p|The returned position.|
| _**out** Quaternion_ |q|The returned rotation.|
| _bool_ |absolute|Set True (default) to return the absolute pose, and False to return the relative pose.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.GetUnbakedObjects

Return all unbaked objects.

| **returns** | _List\<Transform\>_ | A list of all unbaked objects in the scene as Unity Transforms.|


### VG_Controller.JumpGraspObject

Specify an object to be grasped by a hand no matter how far the object is.

| _int_ |avatarID|The avatar id|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand|
| _Transform_ |obj|The transform of the object that will be grasped by this hand|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Recommend to use "Jump Primary Grasp" interaction type on the object since otherwise dynamically generated grasp can be unnatural due to suboptimal hand placement.



### VG_Controller.RecoverObjectJoint

Recover an object's original joint, after it has been changed by ChangeObjectJoint().

| _Transform_ |selectedObject|The object to recover the joint for.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Recommend to use this in LateUpdate to guarantee object pose is in sync with VirtualGrasp library.



### VG_Controller.SetAvatarSpecificObjectSelectionWeight

Specify the avatar specific object selection weight of an object for interaction.

| _int_ |avatarID|The avatar id|
| _Transform_ |obj|Which object to specify weight|
| _float_ |weight|Should be \>=0 value to specify the preferences to select this object. If 0 exclude this object in selection process|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Note by default this weight is equal to the object's selection weight for all avatars.


**Remark:**
 Use case is mainly to specify different grasp preferences for avatars e.g. master vs. student grasp abilities.



### VG_Controller.SetDualHandsOnly

Set if an object can only be manipulated by two or more hands from same or different avatars.

| _Transform_ |selectedObject|The object to change the dual hand type for.|
| _bool_ |dualHandsOnly|If dual hand only.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetObjectJointState

Set the current joint to desired state for a single-dof articulated object or planar joint object.

| _Transform_ |selectedObject|The object to set the joint state value for.|
| _float_ |jointState|The target joint state. If exceed joint limit will be constrained within limit.|
| _float_ |jointState2|The target secondary joint state for Planar joint. If exceed joint limit will be constrained within limit.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call. \<remarks\> After once this is called on object that are grasped by a hand, this will turn off hand control on the object pose. The hand control on this object will be allowed again when either release grasp on this object or call StopSettingObjectJointState()\</remarks\>|


### VG_Controller.SetObjectSelectionWeight

Specify the object selection weights for grasping interaction.

| _Transform_ |obj|Which object to specify weight|
| _float_ |weight|Should be \>=0 value to specify the preferences to select this object. If 0 exclude this object in selection process|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Note by default this weight is 1 for all objects.


**Remark:**
 Use case is mainly to specify different grasp preferences for avatars e.g. master vs. student grasp abilities.



### VG_Controller.StopSettingObjectJointState

Stop setting the current joint to desired state for a single-dof articulated object or planar joint object.

| _Transform_ |selectedObject|The object to set the joint state value for.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call. \<remarks\> Should call this function to enable hand control on object pose after SetObjectJointState is finished. \</remarks\>|


### VG_Controller.SwitchGraspObject

Instantaneously switch the grasped object to specified object in the function.

| _int_ |avatarID|The avatar id|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand|
| _Transform_ |obj|The transform of the object to switch to grasp|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 Recommend to use "Jump Primary Grasp" interaction type on the object since otherwise dynamically generated grasp can be unnatural due to suboptimal hand placement.



### VG_Controller.TogglePrimaryGraspOnObject

Instantaneously switch the grasped object, and continuously calling also toggle through primary grasps on this object.

| _int_ |avatarID|The avatar id|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand|
| _Transform_ |obj|The transform of the object to switch to grasp and toggle primary grasps.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 The specified object should have JUMP_PRIMARY_GRASP interaction type and has added primary grasps in the grasp db.




## [VIRTUALGRASP_CONTROLLER_FUNCTIONS](#virtualgrasp_controller_functions)

### VG_Controller.Clear

Reset the plugin.



### VG_Controller.GetAvatarID

Get the AvatarID of the given skinned mesh renderer

| _**out** int_ |avatarID|The returned AvatarID.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode.SUCCESS on successful avatar id fetch, or VG_ReturnCode.INVALID_AVATAR if avatar is null.|


### VG_Controller.GetHand

Receive a specific hand and its status.

| _int_ |avatarID|The avatar to get the hand status for.|
|[*VG_HandSide*](#vg_handside) | side|The hand side to get the avatar from.|
| **returns** | _VG_HandStatus_ | A VG_HandStatus.|


### VG_Controller.GetHand

Receive a specific hand and its status.

| _Transform_ |wrist|The wrist transform corresponding to the queried hand status.|
| **returns** | _VG_HandStatus_ | A VG_HandStatus.|


### VG_Controller.GetHands

Receive an enumerator of all registered hands and their status.

| **returns** | _List\<VG_HandStatus\>_ | Enumerator over VG_HandStatus.|


### VG_Controller.GetSensorControlledAvatarID

Get the AvatarID of the sensor controlled avatar when the avatar represents both left and right hands.

| _**out** int_ |avatarID|The returned AvatarID. Will be set to -1 upon error.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode.SUCCESS on successful avatar id fetch, or VG_ReturnCode.DLL_FUNCTION_FAILED on an unexpected error.|

**Remark:**
 No guarantee on returning the one that was first sensor controlled avatar



### VG_Controller.GetSensorControlledAvatarID

Get the AvatarID(s) of the sensor controlled avatar(s) when each avatar represents both hand sides or just one hand side. If the avatar represents both hand sides then avatarIDLeft and avatarIDRight are identical.

| _**out** int_ |avatarIDLeft|The ID of sensor avatar that include left hand. Will be set to -1 upon error or if there is no sensor avatar representing left hand.|
| _**out** int_ |avatarIDRight|The ID of sensor avatar that include right hand. Will be set to -1 upon error or if there is no sensor avatar representing right hand.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.Initialize

Initialize the plugin.



### VG_Controller.IsEnabled

Check if the plugin has been initialized and is ready to use.



### VG_Controller.IsolatedUpdate

The Update() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdate() runs the main update loop in VG.



### VG_Controller.IsolatedUpdateDataIn

The FixedUpdate() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdateDataIn() isolates data communication from Unity to VG.



### VG_Controller.IsolatedUpdateDataOut

The Update() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdateDataOut() isolates data communication from VG to Unity.



### VG_Controller.RegisterRemoteAvatar

Register a new remote avatar during runtime.

| _SkinnedMeshRenderer_ |avatar|The skinned mesh renderer of the model that should be registered to VG.|
| _**out** int_ |id|The new avatar ID will be assigned to this value after registration; -1 if it failed.|
| _VG_HandProfile_ |handProfile|Optional, provide the hand profile for this avatar registration.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.RegisterReplayAvatar

Register a new avatar during runtime.

| _SkinnedMeshRenderer_ |avatar|The skinned mesh renderer of the model that should be registered to VG.|
| _**out** int_ |id|The new avatar ID will be assigned to this value after registration; -1 if it failed.|
| _VG_HandProfile_ |handProfile|Optional, provide the hand profile for this avatar registration.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.RegisterSensorAvatar

Register a new avatar during runtime. Single sensor controlling each hand.

| _SkinnedMeshRenderer_ |avatar|The skinned mesh renderer of the model that should be registered to VG.|
| _**out** int_ |id|The new avatar ID will be assigned to this value after registration; -1 if it failed.|
| _VG_SensorSetup_ |primarySetup|The primary sensor setup used to control the avatar.|
| _VG_HandProfile_ |handProfile|Optional, provide the hand profile for this avatar registration.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.RegisterSensorAvatar

Register a new avatar during runtime. Double sensor for each hand.

| _SkinnedMeshRenderer_ |avatar|The skinned mesh renderer of the model that should be registered to VG.|
| _**out** int_ |id|The new avatar ID will be assigned to this value after registration; -1 if it failed.|
| _VG_SensorSetup_ |primarySetup|The primary sensor setup used to control the avatar.|
| _VG_SensorSetup_ |secondarySetup|The secondary sensor setup used to control the avatar.|
| _VG_HandProfile_ |handProfile|Optional, provide the hand profile for this avatar registration.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.Release

Release the plugin.



### VG_Controller.SaveState

Save the object hierarchy debug state. This is done automatically when closing VirtualGrasp.



### VG_Controller.SetAvatarMirrorHandControl

Set for a sensor avatar if has mirror hand control

| _int_ |avatarID|The id of the avatar to be unregistered.|
| _bool_ |mirrorHand|Specify if sensor will control avatar hand of the opposite side.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetRecordingStatesOnAvatar

Set if use the avatar for recording response states during sensor recording or replay.

| _int_ |avatarID|The avatar id.|
| _bool_ |recordingStates|If use this avatar to record response states in sensor db.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 When recordingStates is true, if avatar is used for sensor recording, then recording will also include response states, while if avatar is used for replay sensor db, then replay will update response states in the sensor db.



### VG_Controller.UnRegisterAvatar

Unregister avatar during runtime

| _int_ |avatarID|The id of the avatar to be unregistered.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.new

The event to call when we have successfully initialized the library.



### VG_Controller.new

This event is invoked in the update loop before VG runs its update. Thus, all other scripts that should update before the VG cycle should listen to this event.



### VG_Controller.new

This event is invoked in the update loop after VG runs its update. Thus, all other scripts that should update after the VG cycle should listen to this event.




## [RECORDING_INTERFACE_API **[pro]**](#recording_interface_api-pro)

### VG_Controller.CollectRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Collect recording sensor data.

| _**out** VG_Recording_ |recording|[output] vg sensor recording.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.CollectRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Collect recording sensor data.

| _**out** byte[]_ |recording|[output] byte array containing the sensor recording.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.GetReplayAvatarID
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Get the AvatarID of the replay avatar when the avatar represents both left and right hands.

| _**out** int_ |avatarID|The returned AvatarID. Will be set to -1 upon error.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 No guarantee on returning the one that was first registered as replay avatar



### VG_Controller.GetReplayAvatarID
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Get the AvatarID(s) of the replay avatar(s) when each avatar represents both hand sides or just one hand side. If the avatar represents both hand sides then avatarIDLeft and avatarIDRight are identical.

| _**out** int_ |avatarIDLeft|The ID of replay avatar that include left hand. Will be set to -1 upon error or if there is no replay avatar representing left hand.|
| _**out** int_ |avatarIDRight|The ID of replay avatar that include right hand. Will be set to -1 upon error or if there is no replay avatar representing right hand.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.GetReplayStartWristPose
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Get the starting wrist poses for full replay of the whole interaction sequence.

| _int_ |avatarID|The ID of the avatar to play the recording on (note: it has to be an avatar enabled for replay).|
| _Transform_ |selectedObject|If provided, the entire sensor recording will transformed in to object's frame. If not, in global frame.|
| _**out** Vector3_ |p_left|The position of the left wrist.|
| _**out** Quaternion_ |q_left|The orientation of the left wrist.|
| _**out** Vector3_ |p_right|The position of the right wrist.|
| _**out** Quaternion_ |q_right|The orientation of the right wrist.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

**Remark:**
 LoadRecording need to be called before this to load recorded sensor data.


**Remark:**
 SetProcessByRecordedFrame need to be called before this to set this avatar to be enabled for replay.


Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.IsReplaySuccess
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Check if finished replay had identical response as recorded

| **returns** | _bool_ | True if replay was identical, False otherwise.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.IsReplaying
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Check if a hand is currently replaying a recorded sensor data.

| _int_ |avatarID|The avatar to check.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand to check.|
| **returns** | _bool_ | True if replaying, False otherwise.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.IsReplaying
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Check if avatar is currently replaying a recorded sensor data.

| _int_ |avatarID|The avatar to check.|
| **returns** | _bool_ | True if replaying, False otherwise.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.LoadRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Load recorded sensor data from a file, but do not start replay

| _string_ |fullPath|The full path to load the recording from.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.LoadRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Load recorded sensor data from a byte array.

| _VG_Recording_ |recording|The byte array to load the recording from.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.ResumeReplay
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Resume replaying of an avatar.

| _int_ |avatarID|The ID of the avatar to resume replaying the recording on (note: it has to be an avatar enabled for replay).|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.SaveRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Save recording sensor data and store the whole sequence to a file

| _string_ |fullPath|The full path of the filename to save the recording to.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.StartRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Start recording sensor data.

| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.StartReplay
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Start full replay of the whole interaction sequence on an avatar.

| _int_ |avatarID|The ID of the avatar to play the recording on (note: it has to be an avatar enabled for replay).|
| _Transform_ |selectedObject|If provided, the entire sensor recording will be replayed in this object's frame. If not, in global frame.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.StartReplayOnObject
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Start replaying a specific interaction segment on one object.

| _Transform_ |obj|The object to play the interaction on.|
| _int_ |avatarID|The avatar to play the interaction with.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand to play the interaction with.|
| _int_ |interactionId|The ID of the interaction segment to be played on this object.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.StopRecording
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Stop recording sensor data.

| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)


### VG_Controller.StopReplay
<span class="label label-primary">pro</span> (= will return VG_ReturnCode::UNSUPPORTED_FUNCTION in free version)

Stop replay of the recorded interaction sequence on an avatar.

| _int_ |avatarID|The ID of the avatar to play the recording on (note: it has to be an avatar enabled for replay).|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_Recorder](unity_component_vgrecorder.1.5.0.html)



## [GRASP_EDITOR_API](#grasp_editor_api)

### VG_Controller.EditGrasp
<a href="https://youtu.be/40kYLBKhmqk?list=TLGGpdQGi0diO7gxNjExMjAyMg"><span class="label label-default">video</span></a>


Call grasp editor functionality on a currently selected object and grasp.

| _int_ |avatarID|The avatar to call grasp editor functionality on.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to call grasp editor functionality on.|
|[*VG_EditorAction*](#vg_editoraction) | action|The grasp editor function / action to call.|
| _Transform_ |obj|The object to call the action on (if not provided, the object in the hand).|
| _int_ |grasp|The grasp ID to call the action on (if not provided, the current grasp of the hand).|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_GraspStudio](unity_component_vggraspstudio.1.5.0.html)


### VG_Controller.GetGrasp

Receive a grasp in the grasp DB by index.

| _Transform_ |selectedObject|The object to receive a grasp for.|
| _int_ |avatarID|The avatar to receive a grasp for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive a grasp for.|
| _int_ |graspIndex|The index of grasp to receive.|
| _**out** Vector3_ |p|The received wrist position of the grasp.|
| _**out** Quaternion_ |q|The received wrist orientation of the grasp.|
| _**out** VG_GraspType_ |type|The received VG_GraspType of the grasp.|
| _**out** VG_GraspLabel_ |label|The received VG_GraspLabel of the grasp.|
|[*VG_QueryGraspMode*](#vg_querygraspmode) | queryGraspMode|Can be used to define if and how the grasp should be applied also.|
|[*VG_QueryGraspMethod*](#vg_querygraspmethod) | queryGraspMethod|Can be used to define how the graspIndex should be interpreted.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_GraspStudio](unity_component_vggraspstudio.1.5.0.html)


### VG_Controller.GetInteractionTypeForObject

Get the current interaction type assigned to an object.

| _Transform_ |selectedObject|The object to receive the interaction type for.|
| **returns** |[VG_InteractionType](#vg_interactiontype) | VG_InteractionType describing the current interaction type of the object.|


### VG_Controller.GetNumGraspsInDB

Receive the number of saved grasps in the grasp db for a specific object, and optionally a specified hand.

| _Transform_ |selectedObject|The object to get the number of available grasps for.|
| _int_ |avatarID|If a valid avatarID together with handSide, receive only the available grasps for this hand (otherwise all available grasps).|
|[*VG_HandSide*](#vg_handside) | handSide|If a valid handSide together with avatarID, receive only the available grasps for this hand (otherwise all available grasps).|
| **returns** | _int_ | The number of saved grasps in the grasp db for the selected object (either all or for the specified hand).|

Used in: [VG_HintVisualizer](unity_component_vghintvisualizer.1.5.0.html)


### VG_Controller.GetNumPrimaryGraspsInDB

Receive the number of primary grasps in the grasp db for a specific object, and optionally a specified hand.

| _Transform_ |selectedObject|The object to get the number of available grasps for.|
| _int_ |avatarID|If a valid avatarID together with handSide, receive only the primary grasps for this hand (otherwise all available grasps).|
|[*VG_HandSide*](#vg_handside) | handSide|If a valid handSide together with avatarID, receive only the primary grasps for this hand (otherwise all available grasps).|
| **returns** | _int_ | The number of primary grasps in the grasp db for the selected object (either all or for the specified hand).|

Used in: [VG_HintVisualizer](unity_component_vghintvisualizer.1.5.0.html)



## [GRASP_SELECTION_API](#grasp_selection_api)

### VG_Controller.ForceReleaseObject

Force the release of a grasp.

| _int_ |avatarID|The avatar to release grasps on all its hands.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.ForceReleaseObject

Force the release of a grasp.

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.ForceReleaseObject

Force the release of the selected object by all grasping hands.

| _Transform_ |selectedObject|The object to be released.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.GetBone

Return the pose (i.e. position and orientation) of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _**out** Transform_ |t|The returned pose of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetBone

Return the Transform that corresponds to a provided instance ID.

| _int_ |transformID|The instance ID.|
| **returns** | _Transform_ | The Transform that corresponds to the transformID.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetBone

Return the pose (i.e. position and orientation) of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Vector3_ |p|The returned position of the bone.|
| _**out** Quaternion_ |q|The returned rotation of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetBone

Return the pose matrix of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Matrix4x4_ |m|The returned pose matrix of the bone.|
| **returns** | _Transform_ | The Unity Transform that corresponds to the requested bone.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetCurrentGesture

Query what is the gesture a hand is forming, holding or releasing at the moment.

| _int_ |avatarID|The avatar to query gesture status for.|
|[*VG_HandSide*](#vg_handside) | side|The hand on which to query gesture status.|
| _**out** VG_GestureType_ |gesture|Output, the current gesture type the hand is in.|

**Remark:**
 If gesture output is UNKNOWN_GESTURETYPE, that means the hand is not forming, holding or releasing any gesture, but at a complete gesture-empty state.



### VG_Controller.GetFingerBone

Return the pose of a specific finger bone as a matrix.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from (from 0 as thumb to 4 as pinky).|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip.|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Matrix4x4_ |m|The returned pose of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetFingerBone

Return the pose of a specific finger bone as a matrix.

| _Transform_ |wrist|The wrist transform of the hand to get bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from (from 0 as thumb to 4 as pinky).|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip.|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Matrix4x4_ |m|The returned pose of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetFingerBone

Return the pose (i.e. position and orientation) of a specific finger bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from (from 0 as thumb to 4 as pinky).|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip if there is original rig has no finger tip transform..|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Vector3_ |p|The returned position of the bone.|
| _**out** Quaternion_ |q|The returned rotation of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetFingerBone

Return the pose (i.e. position and orientation) of a specific finger bone.

| _Transform_ |wrist|The wrist transform of the hand to get bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from (from 0 as thumb to 4 as pinky).|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip if there is original rig has no finger tip transform..|
| _**out** int_ |instanceID|The returned ID of the bone transform.|
| _**out** Vector3_ |p|The returned position of the bone.|
| _**out** Quaternion_ |q|The returned rotation of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.GetFingerBone

Reflect the pose of a specific bone on a Transform.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from (from 0 as thumb to 4 as pinky).|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip if there is original rig has no finger tip transform.|
| _**out** Transform_ |t|The returned pose of the bone.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|

Used in: [VG_HandVisualizer](unity_component_vghandvisualizer.1.5.0.html)


### VG_Controller.MakeGesture

Make a gesture with a hand.

| _int_ |avatarID|The avatar to make gesture for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to make gesture for.|
|[*VG_GestureType*](#vg_gesturetype) | gesture|The gesture to make with the [side] hand of avatar [avatarID].|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.ReleaseGesture

Release a gesture on a hand.

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetBlockReleaseObject

Specify if on all hands of this avatar should block releasing the interaction (grasp or push) with an object or not in runtime.

| _int_ |avatarID|The avatar to block release for.|
| _bool_ |block|If block release signal or not on this avatar.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetBlockReleaseObject

Specify if on this hand should block releasing the interaction (grasp or push) with an object or not in runtime.

| _int_ |avatarID|The avatar to block release for.|
|[*VG_HandSide*](#vg_handside) | side|The hand of the avatar to block release for.|
| _bool_ |block|If block release signal or not on this hand.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetGlobalInteractionType

Set the global interaction type method. The interaction type defines how the hand and the object should get together during a grasp.


**Remark:**
 This will overwrite the specific grasp interaction type (see SetInteractionTypeForObject) for all objects.

|[*VG_InteractionType*](#vg_interactiontype) | interactionType|The method to switch to for all objects.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetGlobalThrowAngularVelocityScale

Set the global throw angular velocity scale. The throw angular velocity scale defines how powerful the throw is in terms of rotation movement.


**Remark:**
 This will overwrite the specific throw angular velocity scale (see SetThrowAngularVelocityScaleForObject) for all objects.

| _float_ |throwAngularVelocityScale|The throw angular velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetGlobalThrowVelocityScale

Set the global throw velocity scale. The throw velocity scale defines how powerful the throw is in terms of linear movement.


**Remark:**
 This will overwrite the specific throw velocity scale (see SetThrowVelocityScaleForObject) for all objects.

| _float_ |throwVelocityScale|The throw translational velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetInteractionTypeForObject

Set the interaction type for a selected object. The interaction type defines how the hand and the object should get together during a grasp.


**Remark:**
 This will overwrite the global interaction type (see SetGlobalInteractionType) for that object.

| _Transform_ |selectedObject|The object to modify the interaction type for.|
|[*VG_InteractionType*](#vg_interactiontype) | interactionType|The interaction type to switch to for the object.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetInteractionTypeForSelectedObject

Set the interaction type for a selected object. The interaction type defines how the hand and the object should get together during a grasp.


**Remark:**
 This will overwrite the global interaction type (see SetGlobalInteractionType) for that object.

| _int_ |avatarID|The avatar which is selecting an object.|
|[*VG_HandSide*](#vg_handside) | side|The hand which is selecting an object.|
|[*VG_InteractionType*](#vg_interactiontype) | interactionType|The interaction type to switch to for the object that is selected by the [side] hand of avatar [avatarID].|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetThrowAngularVelocityScaleForObject

Set the throw angular velocity scale for a selected object. The throw angular velocity scale defines how powerful the throw is in terms of rotation movement.


**Remark:**
 This will overwrite the global throw angular velocity scale (see SetGlobalThrowAngularVelocityScale) for that object.

| _Transform_ |selectedObject|The object to modify the throw velocity scale for.|
| _float_ |throwAngularVelocityScale|The throw angular velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetThrowAngularVelocityScaleForSelectedObject

Set the throw angular velocity scale for a selected object. The throw angular velocity scale defines how powerful the throw is in terms of rotation movement.


**Remark:**
 This will overwrite the global throw angular velocity scale (see SetGlobalThrowAngularVelocityScale) for that object.

| _int_ |avatarID|The avatar which is selecting an object.|
|[*VG_HandSide*](#vg_handside) | side|The hand which is selecting an object.|
| _float_ |throwAngularVelocityScale|The throw angular velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetThrowVelocityScaleForObject

Set the throw velocity scale for a selected object. The throw velocity scale defines how powerful the throw is in terms of linear movement.


**Remark:**
 This will overwrite the global throw velocity scale (see SetGlobalThrowVelocityScale) for that object.

| _Transform_ |selectedObject|The object to modify the throw velocity scale for.|
| _float_ |throwVelocityScale|The throw translational velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|


### VG_Controller.SetThrowVelocityScaleForSelectedObject

Set the throw velocity scale for a selected object. The throw velocity scale defines how powerful the throw is in terms of linear movement.


**Remark:**
 This will overwrite the global throw velocity scale (see SetGlobalThrowVelocityScale) for that object.

| _int_ |avatarID|The avatar which is selecting an object.|
|[*VG_HandSide*](#vg_handside) | side|The hand which is selecting an object.|
| _float_ |throwVelocityScale|The throw translational velocity scale.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|



## [SENSOR_INTERFACE_API](#sensor_interface_api)

### VG_Controller.GetGrabStrength

Returns the current grab strength of a hand. The grab strength is 0 for a fully open hand, 1 for a fully closed hand.

| _int_ |avatarID|The avatar to receive the grab strength for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive the grab strength for.|
| **returns** | _float_ | The current grab strength of the [side] hand.|


### VG_Controller.GetGrabStrength

Returns the current grab strength of a hand. The grab strength is 0 for a fully open hand, 1 for a fully closed hand.

| _int_ |wristID|The id of wrist corresponding to the hand to receive the grab strength for.|
| **returns** | _float_ | The current grab strength of the [side] hand.|


### VG_Controller.GetGrabVelocity

Returns the current grab velocity of a hand. The current velocity of the grab strength (see GetGrabStrength), so negative when the hand is opening, and positive when the hand is closing.

| _int_ |avatarID|The avatar to receive the grab velocity for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive the grab velocity for.|
| **returns** | _float_ | The current grab velocity of the [side] hand.|


### VG_Controller.GetPushCircle

Get the push circle for this hand side of an avatar as a visual hint for object selection for push without physics.

| _int_ |avatarID|The avatar to get the push circle for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand to get the push circle for.|
| _**out** Vector3_ |p|The push circle's position.|
| _**out** Quaternion_ |r|The push circle's rotation (z-axis is normal).|
| _**out** float_ |radius|Radius of the push circle,|
| _**out** bool_ |inContact|True if contact (i.e. pushing), False otherwise.|
| **returns** | _Transform_ | The selected object's Unity Transform, or null if none.|

Used in: [VG_HintVisualizer](unity_component_vghintvisualizer.1.5.0.html)


### VG_Controller.IsMissingSensorData

Check if a hand has invalid sensor data.

| _int_ |avatarID|The avatar to check for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to check for.|
| **returns** | _bool_ | True if sensor data is invalid, False otherwise.|


### VG_Controller.SetAvatarActive

Set the active state of the avatar sensor(s) and mesh.

| _int_ |avatarID|The avatar id.|
| _bool_ |enableSensors|If the sensor(s) that control this hand should be active or not.|
| _bool_ |enableMesh|If the mesh of this hand should be visible or not.|
| _Vector3_ |resetPos|If an avatar is deactivated, hand positions will be reset to here (default (0,0,0)).|


### VG_Controller.SetCalibrationMode

Enable or disable wrist calibration mode (WCM). During enabled WCM, different ranges of motion of the wrist or grab strength will be calibrated.


**Remark:**
 untested

| _int_ |avatarID|The avatar for which to enable/disable WCM.|
| _bool_ |enabled|True for enabling WCM, False for disabling it.|


### VG_Controller.SetExternalGrabStrength

Send an external controller grab signal to the plugin (for EXTERNAL_CONTROLLER sensors).

| _int_ |avatarID|The avatar to set external sensor pose for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to set external sensor pose for.|
| _float_ |strength|The grab strength signal to set.|

Used in: [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.5.0.html)


### VG_Controller.SetFingerCalibrationMode

Enable or disable finger calibration mode (FCM). During enabled FCM, the hand opening range will be calibrated. After disabling it, grasp and release signals will work in this range.

| _int_ |avatarID|The avatar for which to enable/disable FCM.|
| _bool_ |enabled|True for enabling FCM, False for disabling it.|


### VG_Controller.SetSensorActive

Set the active state of the sensor(s) that control the specified hand of an instance avatar.

| _int_ |avatarID|The avatar id.|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand (remark: UNKNOWN will not have any effect).|
| _bool_ |active|If the sensor(s) that control this hand should be active or not.|
| _Vector3_ |resetPos|If a hand is deactivated, its position will be reset to here (default (0,0,0)).|

**Remark:**
 By default sensors are all active, and this function can be used in runtime to change this.



### VG_Controller.SetSensorOffset

Change the sensor offset in runtime. The sensor offset is the offset between the pose that the current sensor is measuring and where the virtual hand is appearing in the scene.


**Remark:**
 Also treating left hand (LHS) and right hand (RHS) is considered, so the offset is applied symmetrically.

| _int_ |avatarID|The avatar to set the offset for.|
|[*VG_SensorType*](#vg_sensortype) | sensor|The sensor type to change the offset for.|
| _Vector3?_ |position|The offset position. Set to null if position should not be modified.|
| _Vector3?_ |rotation|The offset rotation. Set to null if rotation should not be modified.|
| **returns** |[VG_ReturnCode](#vg_returncode) | VG_ReturnCode describing the error state of the function call.|



<hr><b>Tags</b>
<table>
<tr><td><span class="label label-primary">pro</span></td><td>this function is related to a feature that is not part of the free version.
Calling it when not supported should result in a VG_ReturnCode.UNSUPPORTED_FUNCTION.</td></tr>
<tr><td><span class="label label-default">video</span></td><td>this function is related to a tutorial movie.</td></tr>
</table><hr>

