---
title: FAQs
#tags: [getting_started]
keywords: faqs
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_1_1_0
permalink: faqs.1.1.0.html
folder: mydoc
---

## Installation

### Where is the GleechiLib Prefab?

If you see the use of GleechiLib prefab in one of our videos, but can not find it in the SDK: the GleechiLib Prefab was removed in version 0_9_6. You are expected to just insert [MyVirtualGrasp](unity_component_myvirtualgrasp.1.1.0.html) component on a GameObject of your choice.

## Hands and Controllers

<!--### I used the VG_AutoSetup with a controller but the hands don't move.

Assure that all the requirements of the controller you picked are met. You can find these requirements at the top of each script in ThirdParty/VirtualGrasp/VG_ExternalControllers/VG_EC_***.cs, as well as on the specific [documentation pages](unity_component_vgexternalcontrollermanager.1.1.0.html#vg_externalcontroller-class). Do not forget to uncomment the #define in the script as soon as you have installed all prerequisites.
-->

### I have setup the avatar but the hands don't move.

Make sure you do not tick _Replay_ option in MyVirtualgrasp → Avatars window, see [Avatar Types](avatars.1.1.0.html#avatar-types) to understand more.

### Does VG support other headsets / controllers?

The VG SDK is hardware-agnostic and does not depend on a headset. Thus, the question of headset support goes more towards Unity. In terms of controllers, VG SDK provides a customizable controller abstraction (see [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.1.1.0.html#coordinate-frame-corrections)) for a few stand-alone controllers and abstractions (such as UnityXR) which require their Unity SDKs. If your controller is not supported, you can either write a VG_ExternalController for it yourself, or contact us.  

### I am using my own hand models and the fingers bend strangely.

Each hand models maybe represented differently in terms of how all the bones are oriented. If you have a representation that is not aligned with the [VG_HandProfile](avatars.1.1.0.html#hand-profile), you will experience wrists or finger bones bending into the wrong axis direction. You can resolve this problem by creating your own Hand Profile. Read more on using [custom hand models](avatars.1.1.0.html#custom-hand-model).

### Are there any concerns when using Oculus's OVR Player Controller?

When you use VirtualGrasp, you should not put the hand rig under the OVRPlayerController / TrackingSpace. The background of this is that the hand rig is controlled under-the-hood by VG continuously, thus you do not need to put the hands into the TrackingSpace in order to move them. 

When you put the avatar also under TrackingSpace, the hands will in addition be affected by the movement of that Transform (as a child of it) - which in the case of OVRPlayerController seems is some acceleration-based movement with damping. This movement induced by the PlayerController will then create a wiggeling behavior when moving the player while holding an object with VG.

## Interaction

### I added a VG_Articulation component to my game object, but I could not interact with the object when I play.

There could be four reasons:
1. [Mesh is not readable](#mesh-not-readable).
2. The added [VG_Articulation](unity_component_vgarticulation.1.1.0.html) component is disabled (unchecked).
3. You have in runtime disabled this [VG_Articulation](unity_component_vgarticulation.1.1.0.html) component.
4. You have in runtime [SetObjectSelectionWeight](virtualgrasp_unityapi.1.1.0.html#setobjectselectionweight) to value <=0. 

### I runtime changed the VG_Articulation component on an object with different joint type and/or other joint parameters. Why the interaction with this object does not correspond to these changes?

You can only runtime change object articulation by using API function [ChangeObjectJoint](virtualgrasp_unityapi.1.1.0.html#changeobjectjoint-1). See page [runtime changes](unity_component_vgarticulation.1.1.0.html#runtime-changes). 

### When I tried to catch a fast moving object, the hand is following the object for a little which looks strange.

The default interaction type for all objects is {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} and Grasp Animation Speed 0.05 (see [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.1.0.html#global-grasp-interaction-settings)) which means that the a grasp moves the hand to the object in 0.05 seconds.

So, when you are trying to catch a fast moving object such as a falling one, the hand will follow the object for 0.05 sec to grab it while falling. There are two quick options to get a better experience: 

1. Decrease the Grasp Animation Speed to 0.01 (which is the minimum). This makes the grasp happen quicker, while still moving the hand to the object. 
2. Change the interaction type to {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %} for this object and the object will move towards the hand instead. Note that it will now still take the time of the Grasp Animation Speed for the object to interpolate into the hand. These and more [interaction types](grasp_interaction.1.1.0.html#grasp-interaction-type) are documented [here](grasp_interaction.1.1.0.html#grasp-interaction-type).

Note that you cannot define the Grasp Animation Speed for a specific object. You can switch the interaction type for a specific object, either by using a [VG_Interactable](unity_component_vginteractable.1.1.0.html#unity-component-vginteractable) on your object to change it from the start, or by using the API function [VG_Controller.SetInteractionTypeForObject](virtualgrasp_unityapi.1.1.0.html#setinteractiontypeforobject) from your code during runtime.

### All my objects are baked but why do I still get unnatural looking grasps?

The unnatrual looking grasps could be caused by you have set the {% include tooltip.html tooltip="InteractionType" text="interaction type" %} of this object to be {% include tooltip.html tooltip="StickyHand" text="STICKY_HAND" %}. You could have set it by either globally for all objects in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.1.1.0.html#global-grasp-interaction-settings), or on specific object through [VG_Interactable](unity_component_vginteractable.1.1.0.html) component, which overwrite the global settings. To fix it just switch to the commonly used {% include tooltip.html tooltip="InteractionType" text="interaction type" %}: {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} or {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %}. See [Grasp Interaction Type](grasp_interaction.1.1.0.html#grasp-interaction-type) for more information.

### Why I can grasp an object with a primary grasp on one hand, but the other hand can not grasp the object at all?

When an object is set to use {% include tooltip.html tooltip="JumpPrimaryGrasp" text="jump primary grasp"%} as {% include tooltip.html tooltip="InteractionType" text="interaction type"%}, it requires there are {% include tooltip.html tooltip="PrimaryGrasp" text="primary grasp"%}(s) added to this object for both hands. If you only added primary grasp(s) for one hand, then the other hand will not be able to grasp the object. There is console warning message accordingly. 

## Baking

### How am I supposed to import the .obj files (in vg_tmp) into my project?

You are not supposed to import the .obj files in your own scenes (since you have your original models there). The main purpose of the .obj files is to represent the raw mesh data of objects when they shall be sent through the [Baking Client](unity_component_vgbakingclient.1.1.0.html) to the cloud baking service. You can read more information on [Debug Files](debug_files.1.1.0.html#debug-files-content).

### Why are some of my interactable objects not baked?

This can be caused by multiple things:
* [Mesh not readable](#mesh-not-readable) error, or
* The objects are runtime spawned and were not exported correctly in [Prepare project](unity_component_vgbakingclient.1.1.0.html#step-2-preparation) step. 

## Sensor Recording and Replaying

### Can I use an avatar with different shaped/sized hands to replay recorded sensor data?

Yes and no. You can always replay recorded sensor data on any avatar's hands since [what is recorded](sensor_record_replay.1.1.0.html#what-is-recorded-exactly) is the sensor data that applies to any hand. However you can not guaranttee creating same interactive behaviors. This is because if hands are of different skeleton or size, its relative pose w.r.t the objects will result in, for example, different grasp synthesized or even no grasp synthesized.  

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