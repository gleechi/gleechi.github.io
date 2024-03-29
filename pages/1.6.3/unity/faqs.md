---
title: FAQs
#tags: [getting_started]
keywords: faqs
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_6_3
permalink: faqs.1.6.3.html
folder: mydoc
---

## Installation

### Where is the GleechiLib Prefab?

If you see the use of GleechiLib prefab in one of our videos, but can not find it in the SDK: the GleechiLib Prefab was removed in version 0_9_6. You are expected to just insert [MyVirtualGrasp](unity_component_myvirtualgrasp.1.6.3.html) component on a GameObject of your choice. Runtime/Resources/Prefabs/ includes two prefabs **SensorAvatar** and **SensorAndReplayAvatars** that have pre-setup basic avatar and sensor settings with MyVirtualGrasp, and you can use them to quick start your project.

## Hands and Controllers

<!--### I used the VG_AutoSetup with a controller but the hands don't move.

Assure that all the requirements of the controller you picked are met. You can find these requirements at the top of each script in ThirdParty/VirtualGrasp/VG_ExternalControllers/VG_EC_***.cs, as well as on the specific [documentation pages](unity_component_vgexternalcontrollermanager.1.6.3.html#vg_externalcontroller-class). Do not forget to uncomment the #define in the script as soon as you have installed all prerequisites.
-->

### I have a compilation error from VG_EC_Mouse.cs when VG_ENABLE_INPUT_SYSTEM.

The reason is probably that the "Input System" Unity package API has been updated (e.g. that the "value" has been replaced by "ReadValue()" or alike). We are trying with each update to align with the newest version of the package. If you experience issues, please refer to the package API that you are using.


### I have setup the avatar but the hands don't move.

Make sure you do not tick _Replay_ option in MyVirtualgrasp → Avatars window, see [Avatar Types](unity_component_myvirtualgrasp.1.6.3.html#replay-physical-and-mirror) to understand more.

### Does VG support other headsets / controllers?

The VG SDK is hardware-agnostic and does not depend on a headset. Thus, the question of headset support goes more towards Unity. In terms of controllers, VG SDK provides a customizable controller abstraction (see [Controllers](controllers.1.6.3.html)) for a few stand-alone controllers and abstractions (such as UnityXR) which require their Unity SDKs. If your controller is not supported, you can either write a VG_ExternalController for it yourself, or contact us.  

### I am using my own hand models and the fingers bend strangely.

Each hand models maybe represented differently in terms of how all the bones are oriented. If you have a representation that is not aligned with the [VG_HandProfile](unity_component_vghandprofile.1.6.3.html), you will experience wrists or finger bones bending into the wrong axis direction. You can resolve this problem by creating your own Hand Profile. Read more on using [custom hand models](avatars.1.6.3.html#custom-hand-models).

### Are there any concerns when using Oculus's OVR Player Controller?

When you use VirtualGrasp, you should not put the hand rig under the OVRPlayerController / TrackingSpace. The background of this is that the hand rig is controlled under-the-hood by VG continuously, thus you do not need to put the hands into the TrackingSpace in order to move them. 

When you put the avatar also under TrackingSpace, the hands will in addition be affected by the movement of that Transform (as a child of it) - which in the case of OVRPlayerController seems is some acceleration-based movement with damping. This movement induced by the PlayerController will then create a wiggeling behavior when moving the player while holding an object with VG.

### I want to use use _OVR Hand_ with VirtualGrasp, but my hands can not grasp any object, why?
You can not use _OVR Hand_ (which can be found in the Oculus Integration under Oculus\VR\Scripts\Util\OVRHand.cs) together with VG controllers as they both are independently affecting the hand model. Since OVR hand controller is updating hand pose in Unity's Update() loop, it will always overwrite VG's hand controller which is updating in the FixedUpdate() loop, therefore showing the symptom of hands not able to grasp an object. Because VG needs to handle interaction with physical objects, we cannot move VG update to Update() loop to avoid this overwritting. 

Compared to _OVR Hand_, VG's sensor integration with Oculus finger tracking (through [VG_EC_Oculus](unity_vg_ec_oculus.1.6.3.html)) has equivalent hand control quality, because VG consumes the same Oculus finger tracking signal and integrates it into VG's hand interaction engine.

The OculusIntegration sample scene provided by VirtualGrasp package shows the comparison of OVR hand controller with VG's Oculus integration. Video below recorded this scene. The bottom hand pair is controlled by the OVR hand controller and the top pair is controlled by VG's Oculus integration. You can see that they have equivalent tracking quality when the hands are moving in the air with no object interaction. When interaction with the object, OVR hands can't grasp object (because OVR is overwriting the hand after VG), but VG's can. 

{% include youtube.html id="HFrPH0P0nRM" %}

## Interaction

### I added a VG_Articulation component to my game object, but I could not interact with the object when I play.

There could be four reasons:
1. [Mesh is not readable](#mesh-not-readable).
2. The added [VG_Articulation](unity_component_vgarticulation.1.6.3.html) component is disabled (unchecked).
3. You have in runtime disabled this [VG_Articulation](unity_component_vgarticulation.1.6.3.html) component.
4. You have in runtime [SetObjectSelectionWeight](virtualgrasp_unityapi.1.6.3.html#vg_controllersetobjectselectionweight) to value <=0. 

### I runtime changed the VG_Articulation component on an object with different joint type and/or other joint parameters. Why the interaction with this object does not correspond to these changes?

You can only runtime change object articulation by using API function [ChangeObjectJoint](virtualgrasp_unityapi.1.6.3.html#vg_controllerchangeobjectjoint-1). See page [runtime changes](unity_component_vgarticulation.1.6.3.html#runtime-changes). 

### When I tried to catch a fast moving object, the hand is following the object for a little which looks strange.

The default interaction type for all objects is {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} and Grasp Animation Speed 0.05 (see [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.6.3.html#global-grasp-interaction-settings)) which means that the a grasp moves the hand to the object in 0.05 seconds.

So, when you are trying to catch a fast moving object such as a falling one, the hand will follow the object for 0.05 sec to grab it while falling. There are two quick options to get a better experience: 

1. Decrease the Grasp Animation Speed to 0.01 (which is the minimum). This makes the grasp happen quicker, while still moving the hand to the object. 
2. Change the interaction type to {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %} for this object and the object will move towards the hand instead. Note that it will now still take the time of the Grasp Animation Speed for the object to interpolate into the hand. The {% include tooltip.html tooltip="InteractionType" text="interaction type" %} are documented [here](grasp_interaction.1.6.3.html#grasp-interaction-type).

Note that you cannot define the Grasp Animation Speed for a specific object. You can switch the interaction type for a specific object, either by using a [VG_Interactable](unity_component_vginteractable.1.6.3.html) on your object to change it from the start, or by using the API function [SetInteractionTypeForObject](virtualgrasp_unityapi.1.6.3.html#vg_controllersetinteractiontypeforobject) from your code during runtime.

### All my objects are baked but why do I still get unnatural looking grasps?

The unnatrual looking grasps could be caused by you have set the {% include tooltip.html tooltip="InteractionType" text="interaction type" %} of this object to be {% include tooltip.html tooltip="StickyHand" text="STICKY_HAND" %}. You could have set it by either globally for all objects in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.6.3.html#global-grasp-interaction-settings), or on specific object through [VG_Interactable](unity_component_vginteractable.1.6.3.html) component, which overwrite the global settings. To fix it just switch to the commonly used {% include tooltip.html tooltip="InteractionType" text="interaction type" %}: {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} or {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %}. See [Grasp Interaction Type](grasp_interaction.1.6.3.html#grasp-interaction-type) for more information.

If the interaction type is not the reason, check if have forgotten to set the baking output grasp db to [MyVirtualGrasp -> Grasp DB](unity_component_myvirtualgrasp.1.6.3.html#grasp-db).

The last reason is you did not bake this object successfully, which should have console warning output while baking. Please check question [Why some of my interactable object not baked?](faqs.1.6.3.html#why-are-some-of-my-interactable-objects-not-baked)

### Why on some small tiny objects I sometimes get bad grasps?

As a backgroud, for tiny objects that need precision grasps, currently VG adopts two alternative dynamic grasp synthesis algorithms with differet levels of grasp quality. When {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} interaction type is used on the object, the algorithm that result in lower grasp quality is used because this algorithm create less wrist rotation offset to prevent breaking the immersion. 
When {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %} interaction type is used, the other algorithm that result in higher grasp quality is used because the higher quality is at the cost of big wrist rotation offset. However since object is "jumping" into the hand therefore wrist will not leave its {% include tooltip.html tooltip="SensorPose" text="sensor pose" %} thus not breaking the immersion. 

So if you notice tiny objects having bad grasps, it might be due to {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} interaction type being used on this object. You can switch the interaction type to {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %}. To switch interaction type for a specific object, you can either add [VG_Interactable](unity_component_vginteractable.1.6.3.html) on your object to change it from the start, or by using the API function [SetInteractionTypeForObject](virtualgrasp_unityapi.1.6.3.html#vg_controllersetinteractiontypeforobject) from your code during runtime.

You can read [Grasp Interaction Type](grasp_interaction.1.6.3.html#grasp-interaction-type) for more detailed explanation.

### Why I can grasp an object with a primary grasp on one hand, but the other hand can not grasp the object at all?

When an object is set to use {% include tooltip.html tooltip="JumpPrimaryGrasp" text="jump primary grasp"%} as {% include tooltip.html tooltip="InteractionType" text="interaction type"%}, it requires there are {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasp"%}(s) added to this object for both hands. If you only added primary grasp(s) for one hand, then the other hand will not be able to grasp the object. There is console warning message accordingly. 

## Baking

### How am I supposed to import the .obj files (in vg_tmp) into my project?

You are not supposed to import the .obj files in your own scenes (since you have your original models there). The main purpose of the .obj files is to represent the raw mesh data of objects when they shall be sent through the [Baking Client](unity_component_vgbakingclient.1.6.3.html) to the cloud baking service. You can read more information on [Debug Files](debug_files.1.6.3.html#debug-files-content).

### Why are some of my interactable objects not baked?

This can be caused by multiple things:
* [Mesh not readable](#mesh-not-readable) error, or
* The objects are runtime spawned and were not exported correctly in [Packaging](unity_component_vgbakingclient.1.6.3.html#step-2-packaging) step. 

## Sensor Recording and Replaying

### Can I use an avatar with different shaped/sized hands to replay recorded sensor data?

Yes and no. You can always replay recorded sensor data on any avatar's hands since [what is recorded](sensor_record_replay.1.6.3.html#what-is-recorded-exactly) is the sensor data that applies to any hand. However you can not guaranttee creating same interactive behaviors. This is because if hands are of different skeleton or size, its relative pose w.r.t the objects will result in, for example, different grasp synthesized or even no grasp synthesized.  

## Common Unity Error Messages

### "Root actors empty"
```js
[VG] [ObjectSelector] [error] Object keypadbutton0/20174 root actors are empty!
````
This can be caused by multiple things e.g:

* Static geometry flag is enabled for object, or
* Transform scale is 0 (maybe during animation) on the object or any parent in the hierarchy.


### Mesh not readable

```js
[12:22:57] The mesh for screwdriver is not readable. Object cannot be processed.
````

This is because the source of that MeshRenderer have not checked “Read/Write enabled” checkbox in the model inspector. VG has an utility script you could use as shown in below image. Clicking _Make interactables readable_ will check this Read/Write checkbox for all objects that have been marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. 

{% include image.html file="unity/unity_vg_make_interactables_readable_1_0_0.png" alt="VG utility make interactables readable" caption="VG Utility: Make interactables readable" %}


## Others

### .NET target framework mismatch when using VS Code
```js
Error: The primary reference "virtualgrasp.CSharp.Unity.NET3.5" could not be resolved because it was built against the ".NETFramework,Version=v4.8" framework.
````
There are many threads with the same underlying issue of a dependency being compiled against 4.8 while Unitys VSCode plugin is hardcoded at the time of writing to 4.7.1. The culprit is the project file Assembly-CSharp.csproj where this dependency is hardcoded:
```js
<TargetFrameworkVersion>v4.7.1</TargetFrameworkVersion>
````
The following can be added to that .csproj file to let the IDE ignore these mismatches:
```js
<ResolveAssemblyReferenceIgnoreTargetFrameworkAttributeVersionMismatch>true</ResolveAssemblyReferenceIgnoreTargetFrameworkAttributeVersionMismatch>
````