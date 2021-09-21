---
title: VG_Articulation Component
#tags: [getting_started]
keywords: component, articulation
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: unity_component_vgarticulation.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

To use the VG_Articulation component (as shown in image above), you should first understand the meaning of VirtualGrasp's  
[Object Articulation](object_articulation.html#object-articulation).


### Initial Setting

For each interactable object in your Unity scene, you can add this VG_Articulation component to specify the articulation setup of this object. 

By default, if you do not add this component, this object has "floating" joint type. 

### Runtime Changes

Regardless of what is the initial setting of an object's articulation, you can change the object's articulation parameters in runtime 
through scripting through API functions [ChangeObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) 
and [RecoverObjectJoint](VirtualGrasp_UnityAPI.html#changeobjectjoint) functions.

#### ChangeObjectJoint

As you can see ChangeObjectJoint has two interfaces, and one of them can directly recieve this VG_Articulation component. 

To do that, you can add an disabled VG_Articulation component to the object, then your script can recieve this component 
and use this as the argument in ChangeObjectJoint function.

And when the VG_Articulation component is used in ChangeObjectJoint function, all the parameters set in the component will be specified
in runtime on the object. 

#### RecoverObjectJoint

Currently, if you want to "change" object joint to the initial (original) type, then only way to do it is to call RecoverObjectJoint. 

{% include important.html content="Known issue for this is if you want to change other articulation parameters on the origial joint type, it is not supported yet. 
This will be fixed in next release. " %}
