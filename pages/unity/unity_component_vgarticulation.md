---
title: VG_Articulation Component
#tags: [getting_started]
keywords: component, articulation
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar
permalink: unity_component_vgarticulation.html
folder: mydoc
---

The VG_Articulation component provides a graphical user interface in Unity to specify [object articulation](object_articulation.html#object-articulation)
that defines an object's 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behaviors</a>. 

{% include callout.html content="All the parameters in the VG_Articulation component is explained in detail in [object articulation](object_articulation.html#object-articulation)." %}

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

### Initial Setting

For each interactable object in your Unity scene, you can add this VG_Articulation component to specify the [articulation setup of this object](object_articulation.html#object-articulation). 
By default the VG_articulation component sets an object to have floating <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointType}}">joint type</a>; and adding this component to the object also specifies this object to be <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.VGInteractable}}">interactable</a> (see [object identifiers](unity_get_started_objects.html#customizing-layers-and-component-names)). 

### Runtime Changes

Regardless of what is the initial setting of an object's articulation, you can change the object's articulation parameters in runtime 
through scripting through API functions [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) 
and [RecoverObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) functions.

#### ChangeObjectJoint

As you can see one [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) API function receives this VG_Articulation component as input for destination [object articulation settings](object_articulation.html#object-articulation).

To do that, you can add an **disabled** VG_Articulation component to the object, then your script can receive this component and use this as the argument in [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) function.
As a result, all the parameters set in the component will be specified in runtime on the object. 

#### RecoverObjectJoint

Currently, if you want to "change" object joint to the initial (original) type, the only way to do it is to call RecoverObjectJoint. 

{% include warning.html content="Known issue for this is if you want to change other articulation parameters on the original joint type, it is not supported yet. 
This will be fixed in next release. " %}
