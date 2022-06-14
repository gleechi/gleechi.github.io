---
title: VG_Articulation Component
keywords: component, articulation
sidebar: main_sidebar_0_14_0
permalink: unity_component_vgarticulation.0.14.0.html
folder: mydoc
---

## Description

VG_Articulation is an {% include tooltip.html tooltip="VGInternalScript" text="internal script" %} that provides the main interface to mark an object as {% include tooltip.html tooltip="VGInteractable" text="interactable" %} (see [object identifiers](unity_get_started_objects.0.14.0.html#customizing-layers-and-component-names)), as well as to parametrize its [object articulation](object_articulation.0.14.0.html#object-articulation) and {% include tooltip.html tooltip="InteractiveBehaviors" text="interactive behavior" %}. 

By default, the VG_articulation component sets an object to have floating {% include tooltip.html tooltip="JointType" text="joint type" %}. If an object is non-physical (i.e. no Rigidbody or ArticulationBody component), constrained (non-floating) joint types can be specified. 

{% include image.html file="unity/unity_vg_articulation_default.png" alt="VG Articulation" caption="The default VG_Articulation Component (FLOATING joint)." %}

As soon as you change the {% include tooltip.html tooltip="JointType" text="joint type" %}, the interface will change dynamically.

{% include image.html file="unity/unity_vg_articulation_full_0_11_0.png" alt="VG Articulation" caption="VG_Articulation dynamic interface after changing to REVOLUTE joint." %}

All the parameters are explained in detail in [object articulation](object_articulation.0.14.0.html#object-articulation).

{% include multiple_script.html %}

{% include callout.html content="If you add multiple VG_Articulation components to a game object, the first active component will be used to configure your initial object articulation." %}

{% include callout.html content="If only an inactive VG_Articulation component is added to a game object, the object will be registered to VirtualGrasp and included in the [baking process](unity_component_vgbakingclient.0.14.0.html#step-2-preparation), however its interactability is temporarily disabled (equivalent to [SetObjectSelectionWeight](virtualgrasp_unityapi.0.14.0.html#setobjectselectionweight) to 0)." %}

## Runtime Changes

Regardless of what is the initial setting of an object's articulation, you can change the object's articulation parameters in runtime 
through scripting using the API functions [ChangeObjectJoint](virtualgrasp_unityapi.0.14.0.html#changeobjectjoint) 
and [RecoverObjectJoint](virtualgrasp_unityapi.0.14.0.html#recoverobjectjoint).

### ChangeObjectJoint

One of the two [ChangeObjectJoint](virtualgrasp_unityapi.0.14.0.html#changeobjectjoint) API functions receives an VG_Articulation component as input for the [object articulation](object_articulation.0.14.0.html#object-articulation) settings you want to apply.

To do that, you can add a **disabled** VG_Articulation component to the object, which your script can receive and use as the argument in the [ChangeObjectJoint](virtualgrasp_unityapi.0.14.0.html#changeobjectjoint) function.

As a result, all the parameters set in the component will be specified in runtime on the object. 

{% include important.html content="Runtime disabling one VG_Articulation and enabling another VG_Articulation with different joint parameters, or directly modifying the parameters of an active VG_Articulation component will not achieve joint change. [ChangeObjectJoint](virtualgrasp_unityapi.0.14.0.html#changeobjectjoint-1) has to be used to change joint in runtime." %}

### RecoverObjectJoint

If you want to recover the object joint to its original parameters set by the **enabled** VG_Articulation component, you can call the [RecoverObjectJoint](virtualgrasp_unityapi.0.14.0.html#recoverobjectjoint) API function.

{% include important.html content="Switch an object to a non-floating joint type (whether through ChangeObjectJoint or RecoverObjectJoint) is not allowed if an object is physical, i.e. with Rigidbody or ArticulationBody components." %}
