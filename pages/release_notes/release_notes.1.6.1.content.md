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

## V1.6.1 (2023-09-19)

##### Major Functionality Changes:

 * [VG_Articulation](unity_component_vgarticulation.1.6.1.html) added **Simulated Weight** feature to simulate the "heavy object lifting" effect. Note that this effect is not through physics simulation, but rather artificially slowing down the lifting of an object with non-zero simulated weight. 

 * **Breaking change:** [VG_Assemble](unity_component_vgassemble.1.6.1.html) is improved to cover assembling object with different symmetric levels. Developers who used this component in previous versions just need to convert 3D vector of **Assemble Axis** to the corresponding axis type, for example [0, 1, 0] corresponds to "Y Axis".
If [0, 0, 0] was used to require whole rotation match, for this new version, the corresponding setting is to select any assymetric axis (e.g. "X Axis") for **Assemble Axis**, and set 1 for **Assemble Symmetry Steps** which is a new option added in this version. 
Please check documentation [VG_Assemble](unity_component_vgassemble.1.6.1.html) and example onboarding [task 10](unity_vgonboarding_task10.1.6.1.html) to see how this improved component can cope with a whole range of symmetric conditions.

* Another internal change in [VG_Assemble](unity_component_vgassemble.1.6.1.html) is that previusly automatically disabling and enabling the desired pose transform when an object is assembled and disassembled respectively is now removed. Instead a public function _SetTargetTransformActive_ is added that can be hooked to _On Assembled_ and _On Disassembled_ to achieve the same effect. 

##### GUI / Component Changes:

 * [VG_Articulation](unity_component_vgarticulation.1.6.1.html) added **Simulated Weight** feature to simulate the "heavy object lifting" effect.

 * [VG_Assemble](unity_component_vgassemble.1.6.1.html) is improved to cover assembling object with different symmetric levels. The GUI changes include:
    1. **Assemble Axis** changed from entering a 3D vector to an enum of axis types. 
    2. **Assemble Symmetry Steps** is added to provide a number of evenly distributed steps around 360 degree around the Assemble Axis. 

##### Other / Internal Changes:

 * With the improvement of VG_Assemble, this bug is also resolved: when "Assemble Axis" is Y axis, the angular difference is not taken into account when measuring closeness of the object to the target. **(fixed known issue from 1.5.0)**


##### Known Issues:

* VG main loop currently runs in FixedUpdate rather than Update in order to synchronize VG powered hand object interaction with physics calculation in Unity. This can cause some visual inconsistency showed as non-smooth hand movement with/without holding an object. We recommend you to resolve this by setting the Time.fixedDeltaTime to match the refresh rate of the device you are targetting (e.g. 1f / 72f to target 72 hz displays). 

* When a game object with ArticulationBody (with constrained joint like prismatic) is released from grasp, the object may move to a direction not intended by the released hand.

* An internal component VG_ColliderTest should not be allowed to be added to a GameObject, but now there is no prevension on this yet.

* Combinig two sensors -- Primary and Secondary [Sensors](unity_component_myvirtualgrasp.1.4.0.html#sensors) -- for an avatar is not working properly. Note for majority use cases you only need one Primary Sensor Setup. 

* [StartReplay](virtualgrasp_unityapi.1.4.0.html#vg_controllerstartreplay) entering selectedObject will not fully support object-centered replay.


{% include_relative release_notes.1.5.0.content.md %}