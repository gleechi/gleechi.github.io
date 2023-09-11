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

## V1.6.0 - rc1 (2023-09-1)

##### Major Functionality Changes:

 * TBD

##### GUI / Component Changes:

 * TBD

##### API Changes:

 * TBD

##### Other / Internal Changes:

 * TBD

##### Known Issues:

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.4.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup. 

* [StartReplay](virtualgrasp_unityapi.1.4.0.html#vg_controllerstartreplay) entering selectedObject will not fully support object-centered replay.



{% include_relative release_notes.1.5.0.content.md %}