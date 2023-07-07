---
title: VG_HandStatus Class
keywords: editor, script
sidebar: main_sidebar_1_4_0
permalink: unity_component_vghandstatus.1.4.0.html
folder: mydoc
---

## Description

The VG_HandStatus is a class that contains data about the current status of hands during runtime in the Editor. 

The [VG_HandStatusDebugger](unity_component_vghandstatusdebugger.1.4.0.html) provides a tutorial on some of the members of [VG_HandStatus](unity_component_vghandstatus.1.4.0.html) which are central to many of the API functions, such as [GetHands()](virtualgrasp_unityapi.1.4.0.html#vg_controllergethands) or some [Events](virtualgrasp_unityapi.1.4.0.html#events). All hands and their VG_Handstatus containers are updated in each frame the VG update is called.

As you can see in the example video, this is data such as the current avatar ID, the hand side, the wrist transform of that hand, the currently selected object, and the grab strength.

{% include youtube.html id="8YOEeZmeil8" caption="The VG_HandStatusDebugger will continuously update the list of VG_HandStatus in the Inspector." %}

## Publc Member Variables

| Type | Name | Description |
| bool | m_valid | If this hand is currently valid. |
| int | m_avatarID | The ID of the avatar to which this hand belongs. |
| VG_HandSide | m_side | The side of this hand. |
| Transform | m_hand | The transform of this hand's wrist. |
| bool | m_triggerHaptics | Trigger external controller haptics. |
| Transform | m_selectedObject | The currently selected object in this hand. |
| float | m_grabStrength | The current grab / closing value (0=open hand; 1=closed hand). |

## Publc Member Functions

| Type | Name | Description |
| bool | IsHolding() | If the hand is currently holding an object. |
| bool | IsTwoHandHolding() | If an object is held in this hand and if it is currently held by another hand as well. |