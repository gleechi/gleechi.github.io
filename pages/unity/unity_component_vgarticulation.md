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

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

The VG_Articulation component provide a graphical user interface in Unity to specify [object articulation](object_articulation.html#object-articulation)
that defines an object's 
<a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractiveBehaviors}}">interactive behaviors</a>. 

{% include important.html content="Before using the VG_Articulation component, please first read [object articulation](object_articulation.html#object-articulation) page." %}

### Initial Setting

For each interactable object in your Unity scene, you can add this VG_Articulation component to specify the articulation setup of this object. 

### Runtime Changes

Regardless of what is the initial setting of an object's articulation, you can change the object's articulation parameters in runtime 
through scripting through API functions [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) 
and [RecoverObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) functions.

#### ChangeObjectJoint

As you can see [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) has two interfaces, and one of them can directly receive this VG_Articulation component. 

To do that, you can add an disabled VG_Articulation component to the object, then your script can receive this component 
and use this as the argument in ChangeObjectJoint function.

And when the VG_Articulation component is used in ChangeObjectJoint function, all the parameters set in the component will be specified
in runtime on the object. 

#### RecoverObjectJoint

Currently, if you want to "change" object joint to the initial (original) type, then only way to do it is to call RecoverObjectJoint. 

{% include important.html content="Known issue for this is if you want to change other articulation parameters on the original joint type, it is not supported yet. 
This will be fixed in next release. " %}
