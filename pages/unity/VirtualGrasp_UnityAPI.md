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

MyVirtualGrasp is a customizable main tutorial component.  MyVirtualGrasp inherits from VG_MainScript, which wraps the main communication functions of the VirtualGrasp API. VG_MainScript inherits from Monobehavior so you can use this as a component to a GameObject in Unity. All the API functions you want to use in your own scripts can be accessed through VG_Controller.  



### MyVirtualGraspBurst

MyVirtualGraspBurst is a customizable main tutorial component.  MyVirtualGraspBurst inherits from VG_MainScript, which wraps the main communication functions of the API. VG_MainScript inherits from Monobehavior so you can use this as a component to a GameObject in Unity. In contrast to MyVirtualGrasp, this component uses Burst Jobs to isolate VG updates on a seperate thread. */  



### VG_ExternalControllerManager

VG_ExternalControllerManager exemplifies how you could provide custom controller scripts for your application. The class, used in MyVirtualGrasp.cs, provides a tutorial on the VG API functions for external sensor control.  



### VG_Gestures

VG_Gestures exemplifies how you could let a hand make a specific gesture (such as pointing). The MonoBehavior provides a tutorial on the VG API functions for gesture animation.  



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



### VG_EC_LeapHand

This is an external controller class that supports the LeapMotion controller as an external controller. Please refer to https://docs.gleechi.com/controllers.html for the definition of an external controller for VG.  - You have a Core Assets plugin from https://developer.leapmotion.com/releases imported into your Unity project. - Note that Core Assets > 4.4.0 are for LeapMotion SDK 4, older are for LeapMotion SDK 3 (lastest CA 4.3.4). - You have the corresponding LeapMotion SDK (https://developer.leapmotion.com/sdk-leap-motion-controller/) installed on your computer.  



### VG_EC_MouseHand

This is an external controller class that supports a Mouse controller as an external controller. Please refer to https://docs.gleechi.com/controllers.html for the definition of an external controller for VG.  



### VG_EC_OculusHand

This is an external controller class that supports the Oculus Finger Tracking controller as an external controller. Please refer to https://docs.gleechi.com/controllers.html for the definition of an external controller for VG.  - You have the Oculus SDK (https://www.oculus.com/setup/) installed on your computer. - You have the Oculus Integration plugin from https://assetstore.unity.com/packages/tools/integration/oculus-integration-82022 imported into your Unity project. - You have the same Oculus Integration plugin version as the one on your headset AND Oculus App.  



### VG_EC_UnityXRHand

This is an external controller class that supports the UnityXR controller as an external controller. Please refer to https://docs.gleechi.com/controllers.html for the definition of an external controller for VG.  - You have the Unity XR Management package installed into your Unity project.  




## [ENUMS](#)

### VG_AvatarType

An enum to descibe an avatar type

|DEFAULT||
|REMOTE||
|REPLAY||


### VG_QueryGraspMethod

The query grasp method for GetGrasp() function

|BY_INDEX|get grasp by index|
|BY_ID|get grasp by ID|
|BY_TCP|get grasp by TCP|


### VG_InteractionMode

An important information for designing your gameplay with VirtualGrasp is what to do dependent onwhat state the hand is in. For this purpose, VG_InteractionMode defines different interaction modesthat are used by the library (such as grasping or empty). You can access a specific hand's modethrough its VG_HandStatus.

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


### VG_Affordance

An object-related affordance, i.e. what interaction can be done with this object.@remark bitmask convention.

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
|OBJECT_NO_GRASPS|Failed in processing function because baking is unsupported.|
|OBJECT_INCONSISTENT|Failed in processing function because a baking process failed.|
|OBJECT_REDUNDANT|Warning in processing function because the provided object is redundant.|


### VG_EditorAction

Action towards the grasp editor, see EditGrasp()@tag movie:https://www.youtube.com/watch?v=Z1j6BgosFVA

|PRIMARY_CURRENT|Label the current grasp as primary, so it will be the only grasp for this object|
|DISABLE_CURRENT|Label the current grasp as disabled, so it will not be accessible for static grasping.|
|DELETE_CURRENT|Currently the same as DISABLE_CURRENT, since we do not really want to remove grasps.|
|ADD_CURRENT|Add the current grasp as a valid one, so it becomes accessible for static grasping.|
|CLEAR_PRIMARY|Remove the label of the current object's primary grasp, so all grasps will be valid again.|
|CLEAR_DISABLED|Remove the label of the current object's disabled grasps, so all grasps will be valid again.|
|TOGGLE_SYNTHESIS|Toggle synthesis mode for this object between static grasping and dynamic grasping (see VG_SynthesisMethod).|
|TOGGLE_INTERACTION|Toggle interaction type for this object between TRIGGER_GRASP and JUMP_PRIMARY_GRASP (see VG_InteractionType).|


### VG_AutoSetup

Enum for quickly setting up projects for a specific controller / build.

|NONE|No setup|
|QUEST|Setup for Quest / Touch controllers|
|QUEST_FT|Setup for Quest / finger tracking|
|STEAMVR|Setup for SteamVR|
|STEAMVR_FT|Setup for SteamVR finger tracking / Knuckles|
|MOUSE|Setup for Mouse|
|BEBOP_FT|Setup for Bebop Haptic Gloves|
|LEAP_EXT|Setup for LeapMotion finger tracking (external controller)|
|LEAP_VG|Setup for LeapMotion finger tracking (internal controller)|
|OPENVR|Setup for OpenVR|


### VG_VrButton

Enum for setting which (VR) controller buttons.

|TRIGGER||
|GRIP||


### VG_HandSide

We support two hands per avatar, left and right in this enum.

|LEFT|Left hand|
|UNKNOWN_HANDSIDE|Unknown hand side|
|RIGHT|Right hand|


### VG_AvatarInputType

Need to know what type made the avatar registration for scaling.

|MESH||
|URDF||


### VG_UrdfType

Avatar's hand template type as URDF.

|HUMANOID_HAND|A humanoid hand|
|PARALLEL_GRIPPER|A parallel jaw gripper (Automed, yumi_gripper_angled1_2hands)|
|SUCTION_PIN_GRIPPER|A suction pin gripper (Digiload, suction_pin_gripper)|


### VG_SensorType

SensorType defines different sensor types that can be used by the library.

|NO_CONTROLLER|no controller|
|LEAP|Leap motion 3D camera|
|RAZER_HYDRA|Razer Hydra controllers|
|INTEL_REALSENSE|Intel Realsense 3D camera|
|MANUS|Manus VR gloves|
|KNUCKLES|Valve Knuckles controller|
|VIVE|HTC Vive controllers, supported through OpenVR|
|OCULUS_TOUCH_OPENVR|Oculus Touch controllers, supported through OpenVR|
|VIVE_TRACKER|A ViveTracker|
|OCULUS_TOUCH_OVR|Oculus Touch controllers, supported through OculusVR (not supported).|
|EXTERNAL_CONTROLLER|An external, customized controller|
|BEBOP|Bebop VR gloves|


### VG_GraspType

Animation grasp type enum.

|UNKNOWN_GRASPTYPE|Unknown grasp type|
|POWER|Power grasp (like on bottle)|
|PINCH|Pinch grasp (like on coin)|
|FLAT|Flat grasp (like on basketball)|
|PUSH|Push grasp|
|GMANUS|used for sensor animation|
|OPENING|this is for opening grasp in order to grasp inside a hole of the object|
|CLOSING|this is for closing grasp for parallel gripper|


### VG_FingerControlType

An enum to describe how fingers are controlled.

|BY_NOTHING|When not grasping, fingers are not controlled at all.|
|BY_SENSOR_FULL_DOFS|When not grasping, fingers are fully controlled by sensor|
|BY_SENSOR_LOW_DOFS|When not grasping, fingers are controlled by sensor, but less DOF.|
|BY_ANIMATION|When not grasping, fingers are controlled by animation.|
|BY_OSCILLATED_ANIMATION|When not grasping, fingers are controlled by oscillating between two state of animations|


### VG_BoneType

An enum to describe a bone type, used for accessing of bones from outside the library.

|WRIST|The wrist bone of a hand|
|ELBOW|The elbow bone of an arm|
|SHOULDER|The shoulder bone of an arm|
|CLAVICLE|The clavicle bone of an arm|
|APPROACH|The approach handle of a grasp|


### VG_JointType

Different articulated joint types supported by VG.

|REVOLUTE|revolute joint restricted around an axis, such as wheel|
|PRISMATIC|prismatic joint restricted along an axis, such as drawer|
|FIXED|fixed, not-moveable joint|
|FLOATING|floating, unrestricted joint|
|CONE|2-DOF universal joint (non-functional)|
|UNKNOWN_JOINTTYPE|Unknown joint type|


### VG_GraspLabel

For labeling grasps (grasp editor functionality).

|DISABLED|Labels a grasp as disabled (i.e. removed)|
|PRIMARY|Labels a grasp as primary (i.e. only grasp for an object)|
|SUCCEEDED|Labels a grasp as succeeded (for training in robotics scenario)|
|FAILED|Labels a grasp as failed (for training in robotics scenario)|
|RANK|TBD|


### VG_InteractionType

An enum to describe a hand interaction type (i.e. a mode on grasp visualization).

|TRIGGER_GRASP|Original, hand goes to object at grasp position|
|PREVIEW_GRASP|Grasp is always previewed, trigger switch to MANIPULATE/HOLD mode|
|PREVIEW_ONLY|like vgsPREVIEW_GRASP, but never trigger to hold an object|
|JUMP_GRASP|Object jumps to hand when grasp is triggered|
|STICKY_HAND|Object sticks to hand without grasp when grasp is triggered. NOTE|
|JUMP_PRIMARY_GRASP|Using mechanism like JUMP_GRASP, but search for the first grasp in db that is primary.|


### VG_QueryGraspMode

Decide when query grasp if object and hand move and how to move hand.

|NO_MOVE|will not move internal object and hand|
|MOVE_HAND_SMOOTHLY|will move object and hand moves smoothly with GRASP transition|
|MOVE_HAND_DIRECTLY|will move object and hand move directly to target grasp pose|


### VG_GraspSelectionMethod

An enum to specify which kind of method is used for pose-based grasp selection.

|POS_ROT_COMBINED|choose grasp that has minimum combined distance, which is a weighted sum of position and rotation distances|
|MIN_POS|among a set of grasps that satisfy rotation distance threshold, choose the grasp with minimum position distance|
|MIN_ROT|among a set of grasps that satisfy position distance threshold, choose the grasp with minimum rotation distance|


### VG_SynthesisMethod

Identifier for a grasp synthesis algorithm.

|NONE|No grasp synthesis method (no grasping)|
|STATIC|Static grasp synthesis method (accessing generated set of discrete grasps)|
|DYNAMIC|Dynamic grasp synthesis method (generating grasps online based on prebaked object representation)|


### VG_GraspConstraintType

Specify for an object how to constrain grasp synthesis.

|NO_CONSTRAINT|No constraint on grasp|
|GRASP_ALONG_AXIS|Grasp opposing targets on the two ends of a provided axis|
|GRASP_ON_PLANE|Grasp opposing targets on the plane whos normal defined by the provided axis|


### VG_QueryObjectTransformMode

Decide when query grasp if object and hand move and how to move hand.

|ALL|will get all registered objects including the empty object nodes|
|ACTIVE_NON_PHYSICAL|will get active non physical object transforms|
|ACTIVE_ARTICULATED_PHYSICAL|will get active physical object that has constrained joint type (non-floating)|


### VG_SelectObjectMethod

Different object selection methods.

|INTERNAL_SELECTION|Object is selected internally in the library|
|EXTERNAL_SELECTION|Object is selected externally in the client engine such as Unity or Unreal|



## [COMPONENTS](#)

### VG_SelectionSettings

VG_SelectionSettings can be used to initialize the object and grasp selection settings. 

| _List<string>_ |m_objectIdentifiers|Tags and Layers of these names will mark interactable objects. |


### VG_DebugSettings

VG_DebugSettings can be used to configure some debug options. 

| _bool_ |m_saveDebugFiles|Enable this if you need VG to save some debug files.|
| _bool_ |m_useObjectIK|Enable this if you want to enable VG's object IK module.|
| _float_ |m_physicsDefaultContactOffset|Overwrite Unity physics contact offset for more accurate collision detection. |


### VG_SensorSettings

VG_SensorSettings is ued to configure global parameters of VirtualGrasp sensor interaction.

IMAGE: Unity_VG_SensorSettings.png

|[*VG_FingerControlType*](#vg_fingercontroltype) | m_fingerControlType|Allow free moving fingers or just use a single grab movement.|
|[*VG_VrButton*](#vg_vrbutton) | m_triggerButton|Which button to use for triggering an interaction (VR only). |


### VG_GraspInteractionSettings

VG_GlobalGraspInteractionSettings is ued to configure global parameters of VirtualGrasp grasp interaction.

Missing image: Unity_VG_GraspInteractionSettings.png

|[*VG_SynthesisMethod*](#vg_synthesismethod) | m_synthesisMethod|Define the mode in which grasps are synthesized.|
|[*VG_InteractionType*](#vg_interactiontype) | m_interactionType|Choose between different grasp interaction types.|
| _float_ |m_graspSpeed|Transition duration controls the snappiness of grasp motion (lower value = faster grasp).|
| _float_ |m_releaseSpeed|Transition duration controls the snappiness of release motion (lower value = faster release). |


### VG_SensorSetup

VG_SensorSetup is part of the VG_SensorConfiguration component and is used to set hand- and sensor-specific settings.

IMAGE: Unity_VG_SensorSetup.png

| _List<VG_Avatar>_ |m_avatars|Assign game avatars / hands here.|
|[*VG_SensorType*](#vg_sensortype) | m_sensor|Choose a sensor that you want to control the hands.|
| _bool_ |m_position|If this sensor's position data shall be used to control the hand.|
| _bool_ |m_rotation|If this sensor's rotation data shall be used to control the hand.|
| _bool_ |m_fingers|If this sensor's finger data shall be used to control the hand.|
| _bool_ |m_grasp|If this sensor's trigger/grasp data shall be used to control the hand.|
| _bool_ |m_haptics|Enable this if you want to send haptic signals in certain occasions (such as collisions). |


### VG_ArticulationBase

VG_ArticulationBase is an abstract class, so only inherited components (such as VG_Articulation) can be attached to an object. An articulation can be attached to an object that should follow an articulated constraint, such as a prismatic or revolute joint. 

|[*VG_JointType*](#vg_jointtype) | m_type|Set the type of this articulated joint.|
| _float_ |m_min|Set the lower range value of this articulated joint.If CONE this is the swing angle.This value has to be provided in angular degree if REVOLUTE or CONE.|
| _float_ |m_max|Set the upper range value of this articulated joint. If CONE this is the twist angle. This value has to be provided in angular degree if REVOLUTE or CONE.|
| _protected_ |float|Set the velocity of this articulated joint [not used].|
| _VG_Affordances_ |m_affordances;|Set the affordances of this object.|
| _float_ |m_screwRate|The screw rate describes how much (>=0, in cm) to translate at one degree of rotation for revolute joint type. If set to 0 then is regular revolute joint without screwing in or out.|
| _bool_ |m_dualHandsOnly|Set if an object can only be manipulated by dual hands (from the same avatar).|
| _List<float>_ |m_discreteStates|Set the discrete states to which this object will be snapped into. |


### VG_Articulation

VG_Articulation inherits from VG_ArticulationBase. An articulation can be attached to an object that should follow an articulated constraint, such as a prismatic or revolute joint. The pivot describes the axis of the constraint (such as the axis of movement for prismatic joints like buttons or drawers; or the axis of rotation for revolute joints such as wheels or levers). The push pivot describes the direction of push for pushable objects.

IMAGE: Unity_VG_Articulation.png

| _Transform_ |m_pivot|The local articulation joint of the object. Important: z-axis of transform is joint axis.|
| _Transform_ |m_pushPivot|The push pivot (direction) of the object. Important: z-axis of transform is push axis. |


### VG_Interactable

VG_Interactable allows to specifiy interaction parameters specifically for an object. An VG_Interactable can be attached to an object that should follow a different interaction behavior than defined in the global VG_SensorSettings.

IMAGE: Unity_VG_Interactable.png

|[*VG_SynthesisMethod*](#vg_synthesismethod) | m_synthesisMethod|The type of synthesis method to use for this object.|
|[*VG_InteractionType*](#vg_interactiontype) | m_interactionType|The type of interaction to use for this object. |


### VG_HandStatus

VG_HandStatus is used as a helping data structure in which the most important grasp state of a hand is stored. Its use in the FixedUpdate() function of the MyVirtualGrasp.cs template will provide you with a good example on how to use the VG_HandStatus from the VirtualGrasp plugin. 

| _bool_ |m_valid|If this hand is currently valid.|
| _Transform_ |m_hand|The transform of this hand's wrist.|
|[*VG_HandSide*](#vg_handside) | m_side|The side of this hand.|
| _int_ |m_avatarID|The ID of the avatar to which this hand belongs.|
| _float_ |m_grabStrength|The current grab / closing value (0=open hand; 1=closed hand).|
| _float_ |m_grabVelocity|The current closing velocity.|
|[*VG_InteractionMode*](#vg_interactionmode) | m_mode|The current mode of the hand.|
| _Transform_ |m_selectedObject|The currently selected object in this hand.|
| _float_ |m_distance|The distance of this hand to its currently selected object.|
| _Transform_ |m_formerSelectedObject|The currently selected object in this hand. |



## [EVENTS](#)

### OnObjectGrasped

This event is invoked when a hand is starting to grasp an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: VG_GrabAndThrow


### OnObjectReleased

This event is invoked when a hand is starting to release an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: VG_GrabAndThrow


### OnObjectFullyReleased

This event is invoked when a hand is starting to release an object. The VG_HandStatus it carries includes more information about the interaction.


Tutorial: VG_GrabAndThrow


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


### IsolatedUpdateDataIn

The Update() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdateDataIn() isolates data communication from Unity to VG.



### IsolatedUpdate

The Update() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdate() runs the main update loop in VG.



### IsolatedUpdateDataOut

The Update() method has been divided into three parts: IsolatedUpdateDataIn(), IsolatedUpdate() and IsolatedUpdateDataOut() for application of the Burst compiler. IsolatedUpdateDataOut() isolates data communication from VG to Unity.



### GetHands

Receive an enumerator of all registered hands and their status.

| _bool_ |onlyValids|If TRUE, only return valid hands, otherwise return all.|
| **returns** | _IEnumerable<VG_HandStatus>_ | Enumerator over VG_HandStatus.|


### GetHand

Receive a specific hand and its status.

| _int_ |avatarID|The avatar to get the hand status for.|
|[*VG_HandSide*](#vg_handside) | side|The hand side to get the avatar from.|
| **returns** | _VG_HandStatus_ | Enumerator over VG_HandStatus.|


### RegisterAvatarOnline

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


### GetObjectJointType

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
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Enable or disable a specific avatar to replay a recording.

| _int_ |avatarID|The avatar to set to replay mode.|
| _bool_ |setToRecording|True = enable; False = disable|

Tutorial: [VG_Recorder](#vg_recorder)


### StartRecording
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Start recording sensor signal.


Tutorial: [VG_Recorder](#vg_recorder)


### StopRecording
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Stop recording sensor signal and store to a file

| _string_ |filename|The filename to save the recording to.|

Tutorial: [VG_Recorder](#vg_recorder)


### LoadRecording
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Load recorded sensor signal from a file, but do not start replay

| _string_ |filename|The filename to load the recording from.|

Tutorial: [VG_Recorder](#vg_recorder)


### StartReplay
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

Start full replay of all recorded interactions.


Tutorial: [VG_Recorder](#vg_recorder)


### StartReplayOnObject
Tags: [video](https://www.youtube.com/watch?v=o5F5tUb8RQM)

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

Tutorial: VG_Editor


### GetInteractionTypeForObject

Receive the current VG_InteractionType of an interactable object.

| _Transform_ |selectedObject|The object to query the VG_InteractionType for.|
| **returns** [VG_InteractionType](#abc.html#vg_interactiontype) The current VG_InteractionType or VG_InteractionType.TRIGGER if invalid.|

Tutorial: VG_Editor


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
Tags: [video](https://www.youtube.com/watch?v=Z1j6BgosFVA)

Call grasp editor functionality on a currently selected object and grasp.

| _int_ |avatarID|The avatar to call grasp editor functionality on.|
|[*VG_HandSide*](#vg_handside) | handSide|The hand side to call grasp editor functionality on.|
|[*VG_EditorAction*](#vg_editoraction) | action|The grasp editor function / action to call.|
| _Transform_ |obj|The object to call the action on (if not provided, the object in the hand).|
| _int_ |grasp|The grasp ID to call the action on (if not provided, the current grasp of the hand).|

Tutorial: VG_Editor



