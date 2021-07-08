---
title: Unity API
sidebar: unity_sdk_sidebar
keywords: grasp, baking, cabvg
permalink: VirtualGrasp_UnityAPI.html
folder: unity
toc: true
---
## [SCRIPTS](#)

### MyVirtualGrasp

MyVirtualGrasp is the customizable main tutorial component. It showcases how you could minimally setup a scene by dragging this component into your scene.  MyVirtualGrasp inherits from VG_MainScript, which wraps the main communication functions of the API. VG_MainScript inherits from Monobehavior so you can use this as a component to a GameObject in Unity.  



### VG_Editor

VG_Editor exemplifies how you could provide simple keyboard- or mouse-based grasp labeling functionality for your application. The MonoBehavior provides a tutorial on the VG API functions for labeling grasps.  



### VG_ExternalControllerManager

VG_ExternalControllerManager exemplifies how you could provide custom controller scripts for your application. The class, used in MyVirtualGrasp.cs, provides a tutorial on the VG API functions for external sensor control.  



### VG_Gestures

VG_Gestures exemplifies how you could let a hand make a specific gesture (such as pointing). The MonoBehavior provides a tutorial on the VG API functions for gesture animation.  



### VG_GrabAndThrow

VG_GrabAndThrow exemplifies how you can effect the object's properties after grabbing and releasing an object in order to let it follow the hand. The MonoBehavior provides a tutorial on the VG API functions for using some of the VG_Controller event functions, such as OnObjectGrasped and OnObjectReleased.  



### VG_GraspHypothesizer

VG_GraspHypothesizer exemplifies how you could request and visualize grasps for a specific object. The MonoBehavior provides a tutorial on the VG API functions for accessing static grasps directly.  



### VG_GraspStudio

VG_GraspStudio provides a tool to visualize, label, and edit grasps. The MonoBehavior provides a tutorial on the VG API functions for accessing static grasps as well as using the labeling interface.  



### VG_HandVisualizer

VG_HandVisualizer provides a tool to visualize the hand bones in Unity. The MonoBehavior provides a tutorial on the VG API functions for accessing specific bones / elements of the hands.  



### VG_Highlighter

VG_Highlighter exemplifies how you could enable object highlighting based on the current hand status. The MonoBehavior provides a tutorial on the VG API functions for some of the VG_Controller event functions, such as OnObjectSelected and OnObjectDeselected.  



### VG_HintVisualizer

VG_HintVisualizer provides a tool to visualize some hints such as a selection sphere to debug object selection or a push sphere to guide pushing interactions. The MonoBehavior provides a tutorial on the VG API functions for accessing the push state (GetPushCircle).  



### VG_JointChanger

VG_JointChanger shows as a tutorial on how to use the VG_Controller.ChangeObjectJoint function. The function can be used to modify the articulation type of an articulated object. In this case, when the script is attached to a child of another object (such as a lock to a bottle), it switches between fixed and floating stage.  



### VG_NetworkManager

VG_NetworkManager exemplifies how you can communicate network messages for grasp interactions handled by VirtualGrasp. The MonoBehavior provides a tutorial on the VG API functions for broadcasting interactions between various instances.  



### VG_PostAnimator

VG_PostAnimator exemplifies how you could overwrite (post-animate) grasp animations that are handled by VirtualGrasp.  



### VG_Recorder

VG_Recorder provides a tool to record and replay hand interactions in an object-independent manner. The MonoBehavior provides a tutorial on the VG API functions for recording and replaying interactions.  



### VG_StateVisualizer

VG_StateVisualizer provides an editor window to print the current state of hands (VG_HandStatus). The EditorWindow provides a tutorial on the elements of VG_HandStatus.  




## [ENUMS](#)

### VG_HandSide

A hand side identifier. Usually a hand is LEFT or RIGHT. UNKNOWN could be caused by an error. 

|LEFT|Left side|
|RIGHT|Right side|
|UNKNOWN|Unknown hand side|


### VG_SensorType

SensorType defines different sensor types that can be used by the library. 

|NO_CONTROLLER|No controller.|
|LEAP|LeapMotion 3D camera.|
|HYDRA|Razer Hydra (Sixense) controllers.|
|INTEL_REALSENSE|Intel Realsense 3D camera.|
|MANUS|Manus VR gloves.|
|KNUCKLES|Steam Knuckles controllers, supported through OpenVR.|
|VIVE|HTC Vive controllers, supported through OpenVR.|
|OCULUS_TOUCH_OPENVR|Oculus Touch controllers, supported through OpenVR.|
|EXTERNAL_CONTROLLER|A controller that must be fed with external sensor signals from the client.|
|BEBOP_GLOVE|Bebop Haptic VR gloves|


### VG_FingerControlType

An enum to describe how fingers are controlled 

|BY_NOTHING|When not grasping, fingers are not controlled at all.|
|BY_SENSOR_FULL_DOFS|When not grasping, fingers are fully controlled by sensor|
|BY_SENSOR_LOW_DOFS|When not grasping, fingers are controlled by sensor, but less degrees-of-freedom.|
|BY_ANIMATION|When not grasping, fingers are controlled by grasp animation.|
|BY_OSCILLATED_ANIMATION||


### VG_BoneType

BoneType defines different enumerable bone types that can be accessed from the library. 

|WRIST|The wrist bone of a hand|
|ELBOW|The elbow bone of an arm|
|SHOULDER|The shoulder bone of an arm|
|CLAVICLE|The clavicle bone of an arm|
|GRASPER|The approach handle of a grasp|


### VG_JointType

JointType defines different articulated joint types that are used by the library. They are commonly used on VG_Articulation components. 

|REVOLUTE|revolute joint restricted around an axis, such as wheel|
|PRISMATIC|linear joint restricted along an axis, such as drawer|
|FIXED|fixed, not-moveable joint|
|FLOATING|floating, unrestricted joint|
|CONE|2-DOF cone joint|
|UNKNOWN_JOINTTYPE|Unknown joint type|


### VG_GraspLabel

For labeling grasps (grasp editor functionality). 

|DISABLED|Labels a grasp as disabled (i.e. removed)|
|PRIMARY|Labels a grasp as primary (i.e. only grasp for an object)|
|SUCCEEDED|Labels a grasp as succeeded (for training in robotics scenario)|
|FAILED|Labels a grasp as failed (for training in robotics scenario)|
|RANK|TBD|


### VG_InteractionType

An enum to describe a hand interaction type (i.e. a mode on grasp visualization). Interaction types mainly define various ways of how a hand interacts with an object. 

|TRIGGER_GRASP|Original, hand goes to object at grasp position|
|PREVIEW_GRASP|Grasp is always previewed, trigger switch to MANIPULATE/HOLD mode|
|PREVIEW_ONLY|like PREVIEW_GRASP, but never trigger to hold an object|
|JUMP_GRASP|Object jumps to hand when grasp is triggered|
|STICKY_HAND|Object sticks to hand without grasp when grasp is triggered. NOTE: SetGraspTriggerByStrength(false) for this type|
|JUMP_PRIMARY_GRASP|Using mechanism like JUMP_GRASP, but search for the first grasp in db that is primary.|


### VG_QueryGraspMode

Decide when query grasp if object and hand move and how to move hand. 

|NO_MOVE|will not move internal object and hand|
|MOVE_HAND_SMOOTHLY|will move object and hand moves smoothly with GRASP transition|
|MOVE_HAND_DIRECTLY|will move object and hand move directly to target grasp pose|


### VG_QueryGraspMethod

The query grasp method for GetGrasp() function 

|BY_INDEX|get grasp by index|
|BY_ID|get grasp by ID|
|BY_TCP|get grasp by TCP|


### VG_GraspSelectionMethod

An enum to specify which kind of method is used for pose-based grasp selection. 

|POS_ROT_COMBINED|choose grasp that has minimum combined distance, which is a weighted sum of position and rotation distances|
|MIN_POS|among a set of grasps that satisfy rotation distance threshold, choose the grasp with minimum position distance|
|MIN_ROT|among a set of grasps that satisfy position distance threshold, choose the grasp with minimum rotation distance|


### VG_SynthesisMethod

Identifier for a grasp synthesis algorithm. 

|NONE|No grasp synthesis method (no grasping)|
|STATIC|Static grasp synthesis method (accessing generated set of discrete grasps)|
|HYBRID|TBD|
|DYNAMIC|Dynamic grasp synthesis method (generating grasps online based on prebaked object representation)|


### VG_InteractionMode

An important information for designing your gameplay with VirtualGrasp is what to do dependent on what state the hand is in. For this purpose, VG_InteractionMode defines different interaction modes that are used by the library (such as grasping or empty). You can access a specific hand's mode through its VG_HandStatus. 

|RELEASE|when wrist and finger toward sensor pose|
|GRASP|when wrist and finger towards target grasp pose|
|HOLD|when hand hold the object, and wrist towards following sensor pose|
|EMPTY|when hand not hold the object, wrist and finger fully follow sensor pose|
|PREVIEW|when grasp is to be previewed before change to HOLD by grasp trigger|
|MANIPULATE|when wrist is controlled by sensor relative pose|
|HOLD2|when doing two hands manipulation|
|MANIPULATE2|when doing two hands manipulation|
|PREVIEW_RELEASE|when release from PREVIEW mode, wrist and finger interpolate toward sensor pose|
|GRASP_TO_PREVIEW|when wrist and finger interpolate towards target grasp pose synthesized once a new object is selected|
|PHYSICAL_PUSHING|when index finger tip do physical push on object|
|PHYSICAL_PUSHING2|when both hand's index finger tip do physical push on same object|


### VG_SelectObjectMethod

Different object selection methods 

|INTERNAL_SELECTION|Object is selected internally in the library|
|EXTERNAL_SELECTION|Object is selected externally in the client engine such as Unity or Unreal|


### VG_Affordance

An object-related affordance, i.e. what interaction can be done with this object.


Remark
 bitmask convention. 

|NOTHING||
|ONLY_GRASPABLE|000001|
|ONLY_FINGER_PUSHABLE|000010|
|GRASPABLE_AND_FINGER_PUSHABLE|000011|
|ONLY_PALM_PUSHABLE|000100|
|GRASPABLE_AND_PALM_PUSHABLE|000101|
|FINGER_PUSHABLE_AND_PALM_PUSHABLE|000110|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_PALM_PUSHABLE|000111|
|GRASPABLE_AND_BOUNCE|001001|
|FINGER_PUSHABLE_AND_BOUNCE|001010|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_BOUNCE|001011|
|PALM_PUSHABLE_AND_BOUNCE|001100|
|GRASPABLE_AND_PALM_PUSHABLE_AND_BOUNCE|001101|
|FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_BOUNCE|001110|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_BOUNCE|001111|
|GRASPABLE_AND_BOUNCE2STAGE|010001|
|FINGER_PUSHABLE_AND_BOUNCE2STAGE|010010|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_BOUNCE2STAGE|010011|
|PALM_PUSHABLE_AND_BOUNCE2STAGE|010100|
|GRASPABLE_AND_PALM_PUSHABLE_AND_BOUNCE2STAGE|010101|
|FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_BOUNCE2STAGE|010110|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_BOUNCE2STAGE|010111|
|GRASPABLE_AND_SNAP|100001|
|FINGER_PUSHABLE_AND_SNAP|100010|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_SNAP|100011|
|PALM_PUSHABLE_AND_SNAP|100100|
|GRASPABLE_AND_PALM_PUSHABLE_AND_SNAP|100101|
|FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_SNAP|100110|
|GRASPABLE_AND_FINGER_PUSHABLE_AND_PALM_PUSHABLE_AND_SNAP|100111|


### VG_ReturnCode

ReturnCode for various VirtualGrasp functions. Most functions in this API provide such a return code. 

|SUCCESS|Succeeded in processing function|
|DLL_NOT_INITIALIZED|Failed in processing function because library has not been initialized.|
|DLL_FUNCTION_FAILED|Failed in processing function because library has not been initialized.|
|INVALID_AVATAR|Failed in processing function because the provided avatar is invalid.|
|INVALID_LIMB|Failed in processing function because the provided limb or object is invalid.|
|INVALID_GRASP|Failed in processing function because the provided grasp is invalid.|
|INVALID_TARGET|Failed in processing function because the provided target is invalid.|
|ARGUMENT_ERROR|Failed in processing function because a provided argument is invalid.|
|UNSUPPORTED_FUNCTION|Failed in processing function because it is unsupported.|
|OBJECT_NO_GRASPS|Failed in processing function because baking is unsupported.|
|OBJECT_INCONSISTENT|Failed in processing function because a baking process failed.|
|OBJECT_REDUNDANT|Warning in processing function because the provided object is redundant.|


### VG_EditorAction
Tags: [movie](https://www.youtube.com/watch?v=Z1j6BgosFVA)

Action towards the grasp editor, see EditGrasp()

|PRIMARY_CURRENT|Label the current grasp as primary, so it will be the only grasp for this object|
|DISABLE_CURRENT|Label the current grasp as disabled, so it will not be accessible for static grasping.|
|DELETE_CURRENT|Currently the same as DISABLE_CURRENT, since we do not really want to remove grasps.|
|ADD_CURRENT|Add the current grasp as a valid one, so it becomes accessible for static grasping.|
|CLEAR_PRIMARY|Remove the label of the current object's primary grasp, so all grasps will be valid again.|
|CLEAR_DISABLED|Remove the label of the current object's disabled grasps, so all grasps will be valid again.|
|TOGGLE_SYNTHESIS|Toggle synthesis mode for this object between static grasping and dynamic grasping (see VG_SynthesisMethod).|
|TOGGLE_INTERACTION|Toggle interaction type for this object between TRIGGER_GRASP and JUMP_PRIMARY_GRASP (see VG_InteractionType).|


### VG_UrdfType

Avatar's hand template type as URDF 

|HUMANOID_HAND|A humanoid hand|
|PARALLEL_GRIPPER|A parallel jaw gripper (Automed, yumi_gripper_angled1_2hands)|
|SUCTION_PIN_GRIPPER|A suction pin gripper (Digiload, suction_pin_gripper)|


### VG_GraspType

Animation grasp type enum 

|UNKNOWN_GRASPTYPE|Unknown grasp type|
|POWER|Power grasp (like on bottle)|
|PINCH|Pinch grasp (like on coin)|
|FLAT|Flat grasp (like on basketball)|
|PUSH|Push grasp|
|GMANUS|used for sensor animation|
|OPENING|this is for opening grasp in order to grasp inside a hole of the object|
|CLOSING|this is for closing grasp for parallel gripper|


### VG_GraspTypes

Enum to describe possible combinations of grasp types specified for an object. 

|AUTO|Automatic (VirtualGrasp algorithms decide|
|POWER|Only Power grasps (like on bottle)|
|PINCH|Only Pinch grasps (like on coin)|
|POWER_PINCH|both Power and Pinch|
|FLAT|Only Flat grasps (like on basketball)|
|POWER_FLAT|both Power and Flat|
|PINCH_FLAT|both Pinch and Flat|
|ALL|Power, Pinch, and Flat|


### GetObjectSpecifier

GetObjectSpecifier. Temporary to check different hierarchy update strategies. 

|NONE||
|ONLY_INTERACTABLES||
|ALL_OBJECTS||


### VG_AutoSetup

Enum for quickly setting up projects for a specific controller / build. 

|NONE|No setup|
|QUEST|Setup for Quest / Touch controllers|
|QUEST_FT|Setup for Quest / finger tracking|
|STEAMVR|Setup for SteamVR|
|STEAMVR_FT|Setup for SteamVR finger tracking / Knuckles|
|MOUSE|Setup for Mouse|
|BEBOP_FT|Setup for Bebop Haptic Gloves|
|LEAP|Setup for LeapMotion finger tracking|
|OPENVR|Setup for OpenVR|


### VG_VrButton

Enum for setting which (VR) controller buttons. 

|TRIGGER||
|GRIP||



## [EVENTS](#)

### OnObjectGrasped

This event is invoked when a hand is starting to grasp an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: [VG_GrabAndThrow](#vg_grabandthrow)


### OnObjectReleased

This event is invoked when a hand is starting to release an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: [VG_GrabAndThrow](#vg_grabandthrow)


### OnObjectSelected

This event is invoked when a hand is starting to select an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: [VG_Highlighter](#vg_highlighter)


### OnObjectDeselected

This event is invoked when a hand is starting to deselect an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: [VG_Highlighter](#vg_highlighter)


### OnObjectCollided

This event is invoked when a grasped object is colliding with another object. The VG_HandStatus it carries includes more information about the interaction.


Tutorials: [VG_ExternalControllerManager](#vg_externalcontrollermanager),  [VG_HintVisualizer](#vg_hintvisualizer)


### OnPreUpdate

This event is invoked in the fixed update loop before VG runs its update. Thus, all other scripts that should update before the VG cycle should listen to this event.  



### OnPostUpdate

This event is invoked in the fixed update loop after VG runs its update. Thus, all other scripts that should update after the VG cycle should listen to this event.  




## [VIRTUALGRASP_CONTROLLER_FUNCTIONS](#)

### Initialize

Initialize the plugin.



### IsEnabled

Check if the plugin has been initialized and is ready to use.



### GetDebugPath

Return the path where VG stores debug files.

| **returns** | _string_ | The path (platform dependent).|


### Update

The heartbeat of the plugin.



### GetHands

Receive an enumerator of all registered hands and their status.

| **returns** | _IEnumerable<VG_HandStatus>_ | Enumerator over VG_HandStatus.|


### GetHand

Receive a specific hand and its status.

| _int_ |avatarID|The avatar to get the hand status for.|
|[*VG_HandSide*](#vg_handside) | side|The hand side to get the avatar from.|
| **returns** | _VG_HandStatus_ | Enumerator over VG_HandStatus.|


### RegisterRemoteAvatarOnline

Register a remotely controlled avatar


Tutorial: [VG_NetworkManager](#vg_networkmanager)


### RegisterObjectAtRuntime

Sync a new object in the scene to the plugin, e.g. if the object is spawned.

| _Transform_ |obj|The object that should be synced.|


### RegisterObjectsAtRuntime

Sync new objects from the scene to the plugin, e.g. if these object are newly spawned.

| _List<Transform>_ |objects|The objects that should be synced.|


### DeleteDistalObjectAtRuntime

Sync deleted objects from the scene to the plugin, e.g. if the object has been deleted.

| _Transform_ |obj|The object that has been deleted.|

Remark
 Works only for distal objects?



### Clear

Reset the plugin.



### Release

Release the plugin.



### SaveState

Save the object hierarchy debug state. This is done automatically when closing VirtualGrasp.




## [NETWORK_INTERFACE_API](#)

### SetBroadcastSignal

Set (to VG) a multiplayer broadcast message as a binary byte array.

| _byte[]_ |message|The message (raw bytes) to be sent and processed by VG.|

Tutorial: [VG_NetworkManager](#vg_networkmanager)


### GetBroadcastSignal

Receive (from VG) a multiplayer broadcast message as a binary byte array.

| **returns** | _byte[]_ | The message received by VG.|

Tutorial: [VG_NetworkManager](#vg_networkmanager)



## [OBJECT_SELECTION_API](#)

### SetPhysicalObject

Specify if an object is a physical object or not.

| _Transform_ |obj|The object to specify if physical object|
| _bool_ |isPhysical|If this object is physical|


### SelectObject

If external object selection is used (and not the internal one that the plugin provides, use this function to sync the selected object from the scene to the plugin.

| _int_ |avatarID|The ID of the avatar that the selected object should be set.|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand that the selected object should be set.|
| _Transform_ |obj|The object that should be selected.|


### JumpGraspObject

Externally select an object and jump grasp it (object jump to hand)

| _int_ |avatarID|instance avatar id (>0)|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand|
| _Transform_ |obj|The id of externally selected object to jump grasped by this hand|

Remark
 Note you do NOT need to use vgsSetSelectObjectMethod() to set select object externally before call this function



### SetObjectSelectionWeight

Specify the object selection weights for grasping interaction

| _Transform_ |obj|Which object to specify weight|
| _float_ |weight|Should be >=0 value to specify the preferences to select this object. If 0 exclude this object in selection process|

Remark
 Note by default this weight is 1 for all objects.


Remark
 Use case is mainly to specify relative selection preferences for cluttered objects.



### ResetObject

Reset a specific object's initial pose and initial zero pose.

| _Transform_ |transform|The object to reset.|


### ResetAllObjects

Reset all objects' initial pose and initial zero pose.



### GetTriggerButton

Return the currently selected TriggerButton.



### GetSensorPose

Receive the sensor pose of a given avatar and hand.

| _int_ |avatarID|The avatar to get the pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the pose from.|
| _out Vector3_ |p|The returned position.|
| _out Quaternion_ |q|The returned rotation.|
| _bool_ |absolute|Set True (default) to return the absolute pose, and False to return the relative pose.|


### HasAffordance

Return the object affordance of a particular object.

| _Transform_ |selectedObject|The object to return its affordance for.|
| **returns** | _bool_ | The affordance for [selectedObject]|


### IsArticulated

Returns if a selected object is an articulated object.

| _Transform_ |selectedObject|The object to check if it is an articulated object.|
| **returns** | _bool_ | TRUE if object is articulated, FALSE otherwise.|


### GetObjectState

Returns the state (current value) of an articulated object.

| _Transform_ |selectedObject|The object to get the current articulation value for.|
| **returns** | _float_ | [selectedObject]'s current articulation value.|


### ChangeObjectJoint

Change an object's joint type in runtime, if this is an articulated object.

| _Transform_ |selectedObject|The object to change the joint type for.|
|[*VG_JointType*](#vg_jointtype) | new_jointType|The joint type to switch to.|
| _Vector2_ |new_limit|The new limit of the new joint type.|
| _float_ |new_screwRate|The new screw rate (>=0, in cm per degree) of the new joint type.|

Remark
 Note that the former joint type can be recovered (see RecoverObjectJoint).


Remark
 If new_screwRate is set to 0 then do not screw.



### ChangeObjectJoint

Change an object's joint type in runtime, if this is an articulated object.

| _Transform_ |selectedObject|The object to change the joint type for.|
| _VG_Articulation_ |articulation|An articulation describing the new articulation parameters.|


### GetObjectJoint

Return an object's original or current joint type.

| _Transform_ |selectedObject|The object to get the joint type for.|
| _bool_ |original|If True, return the original joint type, otherwise return the current.|


### RecoverObjectJoint

Recover an object's original joint type, after it has been changed by ChangeObjectJoint().

| _Transform_ |selectedObject|The object to recover the joint type for.|


### SetDualHandsOnly

Set if an object can only be manipulated by dual hands from a same avatar

| _Transform_ |selectedObject|The object to change the dual hand type for.|
| _bool_ |dualHandsOnly|If dual hand only|


### GetSelectableObjects

Return all interactable objects.

| _bool_ |excludeHidden|If to exclude objects that have been hidden in the scene.|
| _bool_ |excludeUntagged|If to exclude objects that have been untagged in the scene.|
| **returns** | _IEnumerable<Transform>_ | All interactable objects in the scene.|


### GetSelectableObjectsFromScene

Return all interactable objects from the editor scene.

| _bool_ |excludeHidden|If to exclude objects that have been hidden in the scene.|
| _bool_ |excludeUntagged|If to exclude objects that have been untagged in the scene.|
| **returns** | _List<Transform>_ | All interactable objects in the editor scene.|


### GetNonSelectableObjects

Return all non-interactable objects. Note this will only include objects that have been tagged as interactable at start.

| _bool_ |includeHidden|If to include objects that have been hidden in the scene.|
| _bool_ |includeUntagged|If to include objects that have been untagged in the scene.|
| **returns** | _static internal List<Transform>_ | All non-interactable objects in the scene.|


### GetGraspingAvatars

Return the avatar/hand pairs that are currently grasping a specified object.

| _Transform_ |objectToCheck|The object to be checked if it is currently grasped.|
| _VG_HandSide>>_ |hands|An output list of avatar-handside-pairs describing which hands are currently grasping that object.|
@params return Number of hands grasping the object.



### GetUnbakedObjects

Return all unbaked objects.

| **returns** | _List<Transform>_ | All unbaked objects in the scene.|


### RegisterObjectsForSelection

If you want to restrain the selectable objects (e.g. to those close to the avatar), inform the plugin about selectable objects.

| _List<Transform>_ |objects|The selectable objects.|



## [SENSOR_INTERFACE_API](#)

### SetExternalGrabStrength

Send an external controller grab signal to the plugin (for EXTERNAL_CONTROLLER sensors).

| _int_ |avatarID|The avatar to set external sensor pose for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to set external sensor pose for.|
| _float_ |trigger|The trigger signal to set.|

Tutorial: [VG_ExternalControllerManager](#vg_externalcontrollermanager)


### ProcessExternalAvatarPose

Call to process any external avatar poses that have been set with functions such as SetExternalSensorPose().

| _int_ |avatarID|The avatar to process external avatar poses for.|

Tutorial: [VG_ExternalControllerManager](#vg_externalcontrollermanager)


### IsMissingSensorData

Check if a hand has invalid sensor data.


Remark
 AvatarID needed?

| _int_ |avatarID|The avatar to check for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to check for.|
| **returns** | _bool_ | True if sensor data is invalid, False otherwise.|


### SetSensorActive

Set the active state of the sensor(s) that control the specified hand of an instance avatar

| _int_ |avatarID|The instance avatar id|
|[*VG_HandSide*](#vg_handside) | handSide|The side of the hand (remark: UNKNOWN will not have any effect)|
| _bool_ |active|If the sensor(s) that control this hand should be active or not|
| _Vector3_ |resetPos|If a hand is activated, its position will be reset to here (default (0,0,0)).|

Remark
 By default sensors are all active, and this function can be used in runtime to change this.



### SetFingerCalibrationMode

Enable or disable finger calibration mode (FCM). During enabled FCM, the hand opening range will be calibrated. After disabling it, grasp and release signals will work in this range.

| _int_ |avatarID|The avatar for which to enable/disable FCM.|
| _bool_ |enabled|True for enabling FCM, False for disabling it.|


### SetCalibrationMode

Enable or disable wrist calibration mode (WCM). During enabled WCM, different ranges of motion of the wrist will be calibrated.


Remark
 untested

| _int_ |avatarID|The avatar for which to enable/disable WCM.|
| _bool_ |enabled|True for enabling WCM, False for disabling it.|


### GetGrabStrength

Returns the current grab strength of a hand. The grab strength is 0 for a fully open hand, 1 for a fully closed hand.

| _int_ |avatarID|The avatar to receive the grab strength for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive the grab strength for.|
| **returns** | _float_ | The current grab strength of the [handSide] hand.|


### GetGrabVelocity

Returns the current grab velocity of a hand. The current velocity of the grab strength (see GetGrabStrength), so negative when the hand is opening, and positive when the hand is closing.

| _int_ |avatarID|The avatar to receive the grab velocity for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive the grab velocity for.|
| **returns** | _float_ | The current grab velocity of the [handSide] hand.|


### SetSensorOffset

Change the sensor offset in runtime. The sensor offset is the offset between the pose that the current sensor is measuring and where the virtual hand is appearing in the scene.


Remark
 Also treating left hand (LHS) and right hand (RHS) is considered, so the offset is applied symmetrically.

| _int_ |avatarID|The avatar to set the offset for.|
|[*VG_SensorType*](#vg_sensortype) | sensor|The sensor type to change the offset for.|
| _Vector3?_ |position|The offset position. Set to null if position should not be modified.|
| _Vector3?_ |rotation|The offset rotation. Set to null if rotation should not be modified.|


### SetLimbPositionOffset

Set an offset onto a specific finger tip bone.

|[*VG_HandSide*](#vg_handside) | side|The hand side to set the offset on.|
| _int_ |fingerId|The finger to set the offset.|
| _Vector2_ |offset|The offset as a scale factor on the finger last bone's half dimension, as a 2D-coordinate of (towards tip of the finger, towards inner surface of the finger)|


### GetSensorVelocities

Return the positional and rotational sensor velocities of a specific hand.

| _int_ |avatarID|The avatar to get the velocities from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the velocities from.|
| _out Vector3_ |positionalVelocity|The returned positional velocity.|
| _out Vector3_ |rotationalVelocity|The returned rotational velocity.|


### GetInteractionMode

Returns the current interaction mode of a grasped object.

| _int_ |avatarID|The avatar holding the object to receive the interaction mode for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand holding the object to receive the interaction mode for.|
| **returns** [VG_InteractionMode](#abc.html#vg_interactionmode) The current interaction mode of the object held by avatar [avatarID]'s [handSide] hand.|


### GetPushCircle
Tags: untested

Get the physical push cirle for a this hand side of an avatar

| _int_ |avatarID|The avatar to get the push circle for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand to get the push circle for.|
| _out Vector3_ |p|The push circle's position.|
| _out Quaternion_ |r|The push circle's rotation (zaxis is normal).|
| _out float_ |radius|Radius of the push circle,|
| _out bool_ |inContact|True if contact (i.e. pushing), False otherwise.|
| **returns** | _Transform_ | The selected object, NULL if none.|

Tutorial: [VG_HintVisualizer](#vg_hintvisualizer)



## [RECORDING_INTERFACE_API](#)

### SetProcessByRecordedFrame
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Enable or disable a specific avatar to replay a recording.

| _int_ |avatarID|The avatar to set to replay mode.|
| _bool_ |setToRecording|True = enable; False = disable|

Tutorial: [VG_Recorder](#vg_recorder)


### StartRecording
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Start recording sensor signal.


Tutorial: [VG_Recorder](#vg_recorder)


### StopRecording
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Stop recording sensor signal and store to a file

| _string_ |filename|The filename to save the recording to.|

Tutorial: [VG_Recorder](#vg_recorder)


### LoadRecording
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Load recorded sensor signal from a file, but do not start replay

| _string_ |filename|The filename to load the recording from.|

Tutorial: [VG_Recorder](#vg_recorder)


### StartReplay
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Start full replay of all recorded interactions.


Tutorial: [VG_Recorder](#vg_recorder)


### StartReplayOnObject
Tags: [movie](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Start replaying a specific interaction on one object.

| _Transform_ |obj|The object to play the interaction on.|
| _int_ |avatarID|The avatar to play the interaction with.|
|[*VG_HandSide*](#vg_handside) | handSide|The handSide of the avatar to play the interaction with.|
| _int_ |interactionId|The interaction ID to play for this object|

Tutorial: [VG_Recorder](#vg_recorder)


### IsReplaying

Check if a hand is currently replaying a recorded sequence.

| _int_ |avatarID|The avatar to check.|
|[*VG_HandSide*](#vg_handside) | handSide|The handSide of the avatar to check.|
| **returns** | _bool_ | True if replaying, False otherwise.|

Tutorial: [VG_Recorder](#vg_recorder)



## [GRASP_SELECTION_API](#)

### GetNumGrasps

Receive the number of grasps for a specific object.

| _Transform_ |selectedObject|The object to get the number of available grasps for.|
| _int_ |avatarID|If a valid avatarID together with handSide, receive only the available grasps for this hand (otherwise all available grasps).|
|[*VG_HandSide*](#vg_handside) | handSide|If a valid handSide together with avatarID, receive only the available grasps for this hand (otherwise all available grasps).|
| **returns** | _int_ | The number of grasps for the selected object (either all or for the specified hand).|

Tutorial: [VG_HintVisualizer](#vg_hintvisualizer)


### ForceReleaseObject
Tags: untested

Force the release of a grasp.

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|


### MakeGesture

Make a gesture with a hand.

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|
|[*VG_GraspType*](#vg_grasptype) | gesture|The gesture to make with the [side] hand of avatar [avatarID].|

Tutorial: [VG_Gestures](#vg_gestures)


### ReleaseGesture

Release a gesture on a hand

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|


### SetBlockRelease

Specify if on this hand should block release or not in runtime.

| _int_ |avatarID|The avatar to release a grasp for.|
|[*VG_HandSide*](#vg_handside) | side|The hand which to release the grasp for.|
| _bool_ |block|If block release signal or not on this hand|


### SetGestureDuration
Tags: deprecated

Set all controller's gesture forming and releasing interpolation duration

| _float_ |duration|The duration in sec forming and releasing gesture|

Remark
 Default is 0.1 sec



### SetPushAngleThreshold
Tags: deprecated

Set the angle threshold above which the angle between hand push dir with the push axis for an object, push not allowed.

| _float_ |angle|The angle in range [0;180] degrees. Default is 90 degrees.|


### GetSynthesisMethodForObject

Receive the current VG_SynthesisMethod of an interactable object.

| _Transform_ |selectedObject|The object to query the VG_SynthesisMethod for.|
| **returns** [VG_SynthesisMethod](#abc.html#vg_synthesismethod) The current VG_SynthesisMethod or VG_SynthesisMethod.NONE if invalid.|

Tutorial: [VG_Editor](#vg_editor)


### GetInteractionTypeForObject

Receive the current VG_InteractionType of an interactable object.

| _Transform_ |selectedObject|The object to query the VG_InteractionType for.|
| **returns** [VG_InteractionType](#abc.html#vg_interactiontype) The current VG_InteractionType or VG_InteractionType.TRIGGER if invalid.|

Tutorial: [VG_Editor](#vg_editor)


### SetGlobalSynthesisMethod

Set the global grasp synthesis method. The synthesis method defines the algorithm with which grasps are generated.


Remark
 This will overwrite the specific grasp synthesis method (see SetSynthesisMethodForSelectedObject) for all objects.

|[*VG_SynthesisMethod*](#vg_synthesismethod) | synthesisMethod|The method to switch to for all objects.|


### SetSynthesisMethodForSelectedObject

Set the grasp synthesis method for a selected object. The synthesis method defines the algorithm with which grasps are generated.


Remark
 This will overwrite the global grasp synthesis method (see SetSynthesisMethod) for that object.

| _int_ |avatarID|The avatar which is selecting an object.|
|[*VG_HandSide*](#vg_handside) | side|The hand which is selecting an object.|
|[*VG_SynthesisMethod*](#vg_synthesismethod) | synthesisMethod|The synthesis method to switch to for the object that is selected by the [side] hand of avatar [avatarID].|


### SetSynthesisMethodForObject

Set the grasp synthesis method for a selected object. The synthesis method defines the algorithm with which grasps are generated.


Remark
 This will overwrite the global grasp synthesis method (see SetSynthesisMethod) for that object.

| _Transform_ |selectedObject|The object to modify the synthesis method for.|
|[*VG_SynthesisMethod*](#vg_synthesismethod) | synthesisMethod|The synthesis method to switch to for the selected object.|


### SetGlobalInteractionType

Set the global interaction type method. The interaction type defines how the hand and the object should get together during a grasp.


Remark
 This will overwrite the specific grasp interaction type (see SetInteractionTypeForSelectedObject) for all objects.

|[*VG_InteractionType*](#vg_interactiontype) | type|The method to switch to for all objects.|


### SetInteractionTypeForSelectedObject

Set the interaction type for a selected object. The interaction type defines how the hand and the object should get together during a grasp.


Remark
 This will overwrite the global interaction type (see SetInteractionType) for that object.

| _int_ |avatarID|The avatar which is selecting an object.|
|[*VG_HandSide*](#vg_handside) | side|The hand which is selecting an object.|
|[*VG_InteractionType*](#vg_interactiontype) | interactionType|The interaction type to switch to for the object that is selected by the [side] hand of avatar [avatarID].|


### SetInteractionTypeForObject

Set the interaction type for a selected object. The interaction type defines how the hand and the object should get together during a grasp.


Remark
 This will overwrite the global grasp synthesis method (see SetSynthesisMethod) for that object.

| _Transform_ |selectedObject|The object to modify the interaction type for.|
|[*VG_InteractionType*](#vg_interactiontype) | interactionType|The interaction type to switch to for the selected object.|


### GetBone

Return the pose (i.e. position and orientation) of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _out Transform_ |t|The returned pose of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetBone

Return the Transform that corresponds to a provided instance ID.

| _int_ |transformID|The instance ID.|
| **returns** | _Transform_ | The Transform that corresponds to the transformID.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetBone

Return the pose (i.e. position and orientation) of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _out int_ |instanceID|The returned ID of the bone transform.|
| _out Vector3_ |p|The returned position of the bone.|
| _out Quaternion_ |q|The returned rotation of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetBone

Return the pose matrix of a specific bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
|[*VG_BoneType*](#vg_bonetype) | boneType|The BoneType to get.|
| _out int_ |instanceID|The returned ID of the bone transform.|
| _out Matrix4x4_ |m|The returned pose matrix of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetFingerBone

Return the pose of a specific finger bone as a matrix.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from.|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip.|
| _out int_ |instanceID|The returned ID of the bone transform.|
| _out Matrix4x4_ |m|The returned pose of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetFingerBone

Return the pose (i.e. position and orientation) of a specific finger bone.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from.|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip.|
| _out int_ |instanceID|The returned ID of the bone transform.|
| _out Vector3_ |p|The returned position of the bone.|
| _out Quaternion_ |q|The returned rotation of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetFingerBone

Reflect the pose of a specific bone on a Transform.

| _int_ |avatarID|The avatar to get the bone pose from.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to get the bone pose from.|
| _int_ |fingerID|The finger to get the bone pose from.|
| _int_ |boneID|The bone index (from 0 as proximal to N as distal) to get the bone pose from. Use -1 for fingertip.|
| _out Transform_ |t|The returned pose of the bone.|

Tutorial: [VG_HandVisualizer](#vg_handvisualizer)


### GetGrasp

Receive a grasp by index.

| _Transform_ |selectedObject|The object to receive a grasp for.|
| _int_ |avatarID|The avatar to receive a grasp for.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to receive a grasp for.|
| _int_ |graspIndex|The index of grasp to receive.|
| _out Vector3_ |p|The received wrist position of the grasp.|
| _out Quaternion_ |q|The received wrist orientation of the grasp.|
| _out VG_GraspType_ |type|The received VG_GraspType of the grasp.|
| _out VG_GraspLabel_ |label|The received VG_GraspLabel of the grasp.|
|[*VG_QueryGraspMode*](#vg_querygraspmode) | queryGraspMode|Can be used to define if and how the grasp should be applied also.|
|[*VG_QueryGraspMethod*](#vg_querygraspmethod) | queryGraspMethod|Can be used to define how the graspIndex should be interpreted.|

Tutorial: [VG_GraspHypothesizer](#vg_grasphypothesizer)



## [GRASP_EDITOR_API](#)

### EditGrasp
Tags: [movie](https://www.youtube.com/watch?v=Z1j6BgosFVA)

Call grasp editor functionality on a currently selected object and grasp.

| _int_ |avatarID|The avatar to call grasp editor functionality on.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to call grasp editor functionality on.|
|[*VG_EditorAction*](#vg_editoraction) | action|The grasp editor function / action to call.|
| _Transform_ |obj|The object to call the action on (if not provided, the object in the hand).|
| _int_ |grasp|The grasp ID to call the action on (if not provided, the current grasp of the hand).|

Tutorial: [VG_Editor](#vg_editor)


