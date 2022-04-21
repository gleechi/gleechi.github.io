---
title: FAQs
#tags: [getting_started]
keywords: faqs
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_12_0
permalink: faqs.0.12.0.html
folder: mydoc
---

## Installation

### Where is the GleechiLib Prefab?

If you see the use of GleechiLib prefab in one of our videos, but can not find it in the SDK: the GleechiLib Prefab was removed in version 0_9_6. You are expected to just insert a VG_MainScript component (such as MyVirtualGrasp) on a GameObject of your choice.

## Hands and Controllers

### I used the VG_AutoSetup with a controller but the hands don't move.

Assure that all the requirements of the controller you picked are met. You can find these requirements at the top of each script in ThirdParty/VirtualGrasp/VG_ExternalControllers/VG_EC_***.cs, as well as on the specific [documentation pages](unity_component_vgexternalcontrollermanager.0.12.0.html#vg_externalcontroller-class). Do not forget to uncomment the #define in the script as soon as you have installed all prerequisites.

### Does VG support other headsets / controllers?

The VG SDK is hardware-agnostic and does not depend on a headset. Thus, the question of headset support goes more towards Unity. In terms of controllers, VG SDK provides a customizable controller abstraction (see [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.0.12.0.html#coordinate-frame-corrections)) for a few stand-alone controllers and abstractions (such as UnityXR) which require their Unity SDKs. If your controller is not supported, you can either write a VG_ExternalController for it yourself, or contact us.  

### I am using my own hand models and the fingers bend strangely.

The reason for the mismatch is that each controller (for example, VG_EC_OculusHands.cs) is adjusting the raw finger orientations that come directly from the controller API (for example, from the Oculus Integration plugin) to match the hand model representation that is provided with the SDK. Read more on ways to resolve this issue on the [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.0.9.6.html#coordinate-frame-corrections) page.

## Interaction

### I added a VG_Articulation component to my game object, but I could not interact with the object when I play.

There could be four reasons:
1. [Mesh is not readable](#mesh-not-readable).
2. The added [VG_Articulation](unity_component_vgarticulation.0.12.0.html) component is disabled (unchecked).
3. You have in runtime disabled this [VG_Articulation](unity_component_vgarticulation.0.12.0.html) component.
4. You have in runtime [SetObjectSelectionWeight](virtualgrasp_unityapi.0.12.0.html#setobjectselectionweight) to 0. 

### I runtime changed the VG_Articulation component on an object with different joint type and/or other joint parameters. Why the interaction with this object does not correspond to these changes?

You can only runtime change object articulation by using API function [ChangeObjectJoint](virtualgrasp_unityapi.0.12.0.html#changeobjectjoint-1). See page [runtime changes](unity_component_vgarticulation.0.12.0.html#runtime-changes). 

### When I tried to catch a fast moving object, the hand is following the object for a little which looks strange.

The default interaction type for all objects is {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} and Grasp Animation Speed 0.05 (see [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.12.0.html#global-grasp-interaction-settings)) which means that the a grasp moves the hand to the object in 0.05 seconds.

So, when you are trying to catch a fast moving object such as a falling one, the hand will follow the object for 0.05 sec to grab it while falling. There are two quick options to get a different experience: 

1. Decrease the Grasp Animation Speed to 0.01 (which is the minimum). This makes the grasp happen quicker, while still moving the hand to the object. 
2. Change the interaction type to {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %} for this object and the object will move towards the hand instead. Note that it will now still take the time of the Grasp Animation Speed for the object to interpolate into the hand. These and more [interaction types](grasp_interaction.0.12.0.html#grasp-interaction-type) are documented [here](grasp_interaction.0.12.0.html#grasp-interaction-type).

Note that you cannot define the Grasp Animation Speed for a specific object. You can switch the interaction type for a specific object, either by using a [VG_Interactable](unity_component_vginteractable.0.12.0.html#unity-component-vginteractable) on your object to change it from the start, or by using the API function [VG_Controller.SetInteractionTypeForObject](virtualgrasp_unityapi.0.12.0.html#setinteractiontypeforobject) from your code during runtime.

### All my objects are baked but why do I still get unnatural looking grasps?

The unnatrual looking grasps could be caused by you have set the {% include tooltip.html tooltip="InteractionType" text="interaction type" %} of this object to be {% include tooltip.html tooltip="StickyHand" text="STICKY_HAND" %}. You could have set it by either globally for all objects in [Global Grasp Interaction Settings](unity_component_myvirtualgrasp.0.12.0.html#global-grasp-interaction-settings), or on specific object through [VG_Interactable](unity_component_vginteractable.0.12.0.html) component, which overwrite the global settings. To fix it just switch to the commonly used {% include tooltip.html tooltip="InteractionType" text="interaction type" %}: {% include tooltip.html tooltip="TriggerGrasp" text="TRIGGER_GRASP" %} or {% include tooltip.html tooltip="JumpGrasp" text="JUMP_GRASP" %}. See [Grasp Interaction Type](grasp_interaction.0.12.0.html#grasp-interaction-type) for more information.

## Baking

### How am I supposed to import the .obj files (in vg_tmp) into my project?

You are not supposed to import the .obj files in your own scenes (since you have your original models there). The main purpose of the .obj files is to represent the raw mesh data of objects when they shall be sent through the [Baking Client](unity_component_vgbakingclient.0.12.0.html) to the cloud baking service. You can read more information on [Debug Files](debug_files.0.12.0.html#debug-files-content).

### Why are some of my interactable objects not baked?

This can be caused by multiple things:
* [Mesh not readable](#mesh-not-readable) error, or
* The objects are runtime spawned and were not exported correctly in [Prepare project](unity_component_vgbakingclient.0.12.0.html#step-2-preparation) step. 

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

This is because the source of that MeshRenderer have not checked “Read/Write enabled” checkbox in the model inspector. VG has an utility script you could use as shown in below image. Clicking _Make interactables readable_ will check this Read/Write checkbox for all objects that have been marked as interactable. 

{% include image.html file="unity/unity_vg_make_interactables_readable.png" alt="VG utility make interactables readable" caption="VG Utility: Make interactables readable" %}
