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

## V1.7.0 (2024-01-30)

##### Major Functionality Changes:

 * The [Record & Replay](sensor_record_replay.1.7.0.html) functionality (earlier only a feature of the PRO version), is now also available in the free Test version.

 * To support that change in [Record & Replay](sensor_record_replay.1.7.0.html) functionality, the free Test version now also allows for up to 2 avatars in the scene.

 * We have included unit and regression tests on a subset of functionality of the API. These tests are supported by Unity TestRunner and many of them exemplify the [Record & Replay](sensor_record_replay.1.7.0.html) functionality through pre-recorded actions.

 * Internal development version for VG was changed to Unity 2022.3.18f1. From now on, VG will be packaged using Unity 2022 instead of Unity 2021. In addition, the packaged SDK was tested to work properly with Unity 2023.2.7f1 (see [Installation](unity_get_started_installation.1.7.0.html)).

##### GUI / Component Changes:

 * The OculusIntegration sample was removed from the SDK since it assumed dependency on Oculus prefabs and the Oculus Integration which is not by default installed or needed in many customers' projects.

 * Overhaul and optimization of the OpenXR based external controller code ([VG_EC_UnityXRInteraction controller](unity_vg_ec_unityxrinteraction.1.7.0.html)). 
 
 * The "XRInteraction" Sample was included in the PRO version. It includes a scene to present the use of this controller in an example for runtime-registration of differently scaled avatars (which are "custom hand models" and thus only supported in the PRO version).

 * The VirtualGrasp menu was moved to Tools/VirtualGrasp menu to conform with Unity's asset packaging rules.

##### API Changes:

 * There are no API changes in this version. 

##### Other / Internal Changes:

 * Various internal bugfixes and optimizations.

 * Updated various administrative content related to the company reconstruction of Gleechi AB to Gleechi Technology AB.


##### Known Issues (still the same as in 1.6.3):

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.7.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup. 

* [StartReplay](virtualgrasp_unityapi.1.7.0.html#vg_controllerstartreplay) entering selectedObject will not fully support object-centered replay.


{% include_relative release_notes.1.6.3.content.md %}