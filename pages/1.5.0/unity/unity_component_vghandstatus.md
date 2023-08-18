---
title: VG_HandStatus Class
keywords: editor, script
sidebar: main_sidebar_1_5_0
permalink: unity_component_vghandstatus.1.5.0.html
folder: mydoc
---

## Description

The VG_HandStatus is a class that contains data about the current status of hands during runtime in the Editor. 

The [VG_HandStatusDebugger](unity_component_vghandstatusdebugger.1.5.0.html) provides a simple debug tool to runtime observe changes of VG_Handstatus.

{% include image.html file="unity/unity_vg_handstatusdebugger.png" alt="VG HandStatusDebugger" caption="The VG HandStatusDebugger showing runtime update of HandStatus data." %}

## Publc Member Variables

| Type | Name | Description |
| bool | m_valid | If this hand is currently valid. |
| int | m_avatarID | The ID of the avatar to which this hand belongs. |
| VG_HandSide | m_side | The side of this hand. |
| Transform | m_hand | The transform of this hand's wrist. |
| bool | m_triggerHaptics | Trigger external controller haptics. |
| Transform | m_selectedObject | The currently selected object in this hand. |
| float | m_grabStrength | The current grab / closing value (0=open hand; 1=closed hand). |
| [VG_InteractionMode](virtualgrasp_unityapi.1.5.0.html#vg_interactionmode) | m_mode | The interaction mode of the hand. |
| Vector3 | m_graspPos | The wrist position relative to grasped object. |
| Quaternion | m_graspRot | The wrist rotation relative to grasped object. |
| bool | m_isRemote | If this is a remote proxy hand (for multiplayer feature). |
| List<Transform> | m_linkedObjects | Store linked object of this hand, i.e. the set of objects whose movement will be controlled by this hand. |
| float | m_jointState1 | Joint state at moment of grasp (or push) start or stop. If object has revolute or prismatic joint, if planar joint this is the state along xaxis of the joint anchor. |
| float | m_jointState2 | Joint state at moment of grasp (or push) start or stop. If object has planar joint, the state along yaxis of the joint anchor. |

## Publc Member Functions

| Type | Name | Description |
| bool | IsHolding() | If the hand is currently holding an object. |
| bool | IsMultiHandHolding() | If an object is held in this hand and if it is currently held by other hand(s) as well. |
| bool | IsPushing() | If hand is pushing the selected object. |