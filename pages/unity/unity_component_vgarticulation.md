---
title: VG_Articulation Component
keywords: component, articulation
sidebar: main_sidebar
permalink: unity_component_vgarticulation.html
folder: mydoc
---

## Description

VG_Articulation is an <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGInternalScript}}">internal script</a> that provides the main interface to mark an object as <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGInteractable}}">interactable</a> (see [object identifiers](unity_get_started_objects.html#customizing-layers-and-component-names)), as well as to parametrize its [object articulation](object_articulation.html#object-articulation) and <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behavior</a>. 

By default, the VG_articulation component sets an object to have floating <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">joint type</a>. 

{% include image.html file="unity/unity_vg_articulation_default.png" alt="VG Articulation" caption="The default VG_Articulation Component (floating joint type)." %}

As soon as you change the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">joint type</a>, the interface will change dynamically.

{% include image.html file="unity/unity_vg_articulation_full.png" alt="VG Articulation" caption="VG_Articulation interface after changing to  prismatic joint type." %}

All the parameters are explained in detail in [object articulation](object_articulation.html#object-articulation).

{% include multiple_script.html %}

## Runtime Changes

Regardless of what is the initial setting of an object's articulation, you can change the object's articulation parameters in runtime 
through scripting using the API functions [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) 
and [RecoverObjectJoint](VirtualGrasp_UnityAPI.html#recoverobjectjoint).

### ChangeObjectJoint

One of the two [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) API functions receives an VG_Articulation component as input for the [object articulation](object_articulation.html#object-articulation) settings you want to apply.

To do that, you can add a **disabled** VG_Articulation component to the object, which your script can receive and use as the argument in the [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) function.

As a result, all the parameters set in the component will be specified in runtime on the object. 

### RecoverObjectJoint

If you want to recover the object joint to its original parameters set by the **enabled** VG_Articulation component, you can call the [RecoverObjectJoint](VirtualGrasp_UnityAPI.html#recoverobjectjoint) API function.
