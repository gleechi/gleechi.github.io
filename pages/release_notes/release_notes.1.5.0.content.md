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

## V1.5.0 - rc1 (2023-08-25)

##### Major Functionality Changes:

 * **Breaking change:** Two overloaded functions [SetBlockRelease](virtualgrasp_unityapi.1.4.0.html#vg_controllersetblockrelease) changed names to SetBlockReleaseObject to make it consistent with ForceReleaseObject function.

 * **Breaking change:** Changed external controller class name from VG_EC_UnityInteraction to [VG_EC_UnityXRInteraction](unity_vg_ec_unityxrinteraction.1.5.0.html) to be consistent with the corresponding controller profile, VG_CP_Unity.XRInteraction. Also changed the scripting define symbol for this controller class from VG_USE_UNITYINTERACTION_HAND to VG_USE_UNITYXRINTERACTION_HAND for Unity player settings (Project Settings → Player → Script Compilation) **(fixed known issue from 1.4.0)**
 
 * Fixed the algorithm error on [VG_FingerAnimator](unity_component_vgfingeranimator.1.4.0.html) that leads to the absolute target rotation keep changing, resulting in flickering finger animation. **(fixed known issue from 1.4.0)**

 * [Index pushing interaction](push_interaction.1.5.0.html#why-the-finger-penetrates) now has an improvement on user experience: a proxy hand feature is introduced to force index finger tip to stay on the pushing surface unless the hand is pushing too "hard" into the surface. 

##### GUI / Component Changes:
* [VG_Recorder](unity_component_vgrecorder.1.5.0.html) fixed a bug of clicking on the defined **Replay Sequence Key** or **Replay Segment Key** can not replay just recorded data. **(fixed known issue from 1.4.0)**
  * as a result _Replay From Memory_ option is removed on the GUI of [VG_Recorder](unity_component_vgrecorder.1.5.0.html) since directly hitting replay key after recording is replaying from memory. 
* Added [VG_Utility](unity_component_vgutility.1.5.0.html) scriptable object in _Runtime/Resources/_ that covers most of VG's static API functions.
* Added [VG_Locomotion](unity_component_vglocomotion.1.5.0.html) component that originats from _Samples/onboarding/Scripts/Move.cs_. In addition to the original functionalities in Move.cs, on VG_Locomotion speed control and keyboard control are added. 
* Added more prefabs and improved existing ones in _Runtime/Resources/Prefabs/_
  * _SensorAvatar_ and _SensorAndReplayAvatars_ were refactored to avoid conflicting control of avatar movement by different mechanisms. 
  * _SensorAvatarLeap_ was added as prefab varient of _SensorAvatar_ to directly support Leap motion sensor control.
  * _SeparateHandsSensorAvatar_ was added. It is comparible to _SensorAvatar_ with the difference of using the newly added singular left hand model _Runtime/Resources/GleechiHands/GleechiLeftHand.fbx_. This prefab was added mainly to show an example of how to set up VG {% include tooltip.html tooltip="SensorAvatar" text="sensor avatar" %}  with separate hand models. 
  * _SeparateHandsSensorAndReplayAvatars_ was added as prefab varient of _SeparateHandsSensorAvatar_. It is comparible to _SensorAndReplayAvatars_ also with the difference of using the newly added singular left hand model. This was added mainly to show an example of how to setup VG library for sensor recording and replaying with separate hand models. 


##### API Changes:
* Fixed the bug on [SetBlockRelease](virtualgrasp_unityapi.1.4.0.html#vg_controllersetblockrelease) overload function with no hand side input: if input avatarID corresponds to an avatar that has only right hand, then this function will not set block release on the right hand because an early return happens when left hand is not found. **(fixed known issue from 1.4.0)**

* Fixed the bug on [ForceReleaseObject](virtualgrasp_unityapi.1.4.0.html#vg_controllerforcereleaseobject) overload function with no hand side input: if input avatarID corresponds to an avatar that has only right hand, then this function will not force release the right hand because an early return happens when left hand is not found. **(fixed known issue from 1.4.0)**

* Added [IsReplaying](virtualgrasp_unityapi.1.5.0.html#vg_controllerisreplaying-1) overloaded function that just recieve avatar id as input. 

##### Other / Internal Changes:
* Fixed the issue when graspable object is close to an index pushable object, after grasping the object, pushing gesture may not form. **(fixed known issue from 1.4.0)**

* Fixed the issue when index finger tip moves in a different direction from wrist, pushing can get double triggered. **(fixed known issue from 1.4.0)**

##### Known Issues:

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.4.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup. 

* [StartReplay](virtualgrasp_unityapi.1.4.0.html#vg_controllerstartreplay) entering selectedObject will not fully support object-centered replay.



{% include_relative release_notes.1.4.0.content.md %}