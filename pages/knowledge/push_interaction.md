---
title: Knowledge Base - Push Interaction
sidebar: knowledge_sidebar
keywords: affordance, push, index_finger_pushable
permalink: push_interaction.html
folder: knowledge
toc: true
---

### Background

VirtualGrasp not only provides solutions to <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Grasp Synthesis</a>
challenges in VR (see [Grasp Interaction](grasp_interaction.html#grasp-interaction)), 
but also provides solutions for push interactions.

Button push as an action in real world is very simple process due to the very physical laws existing in the nature. 
When the same problem is ported into VR, a realistic button push behavior requires some tedius steps that often needs complex setup of physical properties on 
both button and the hand.

VirtualGrasp provides a solution to make push interaction setup easier and intuitive, through [Object Articulation](object_articulation.html#object-articulation), with and without relying on physical simulations.

{% include important.html content="To fully benefit from VG's push interaction, it is important to understand [Object Articulation](object_articulation.html#object-articulation)." %}


### Push Without Physics

Through VirtualGrasp's [Object Articulation](object_articulation.html#object-articulation) feature, a VR developer can setup a pushable object with various behaviors 
simulating real world's button object in any game engine. And this setup does not require the developer to add physical qualities to either objects or hands in the game engine. 

Using Unity game engine as an example, to create a button that can be pushed with index finger tip, 
you add the component [VG_Articulation](unity_component_vgarticulation.html#unity-component-vgarticulation) to the object, 
and the example below can create a button that can be pushed by index finger, and will always bounce back when not pushed. 

{% include image.html file="unity/unity_vg_articulation.png" alt="VG Articulation" caption="VG_Articulation Component." %}

* Since button is moving along a single axis linearly, we select the joint type to be PRISMATIC.
* For PRISMATIC joint, we need to provide <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Pivot}}">Pivot</a> which specifies the axis along which object moves.
* For PRISMATIC joint, we also need to provide <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.JointLimit}}">Joint Limit</a>, i.e. linear movement range between 0 and 0.014 meter. 
* For push without physics, you need to select <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> as INDEX_PUSHABLE.
* To let object bounce back when not pushed, you need to set the <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.StateAffordance}}">State Affordance</a>
 to be <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Bounce}}">BOUNCE</a>. 

{% include tip.html content="When you do not define Discrete States, they will be the same as joint limits. In such cases, object's 
Joint State will bounce back to min value of defined joint limit. 
But when you defines them differently, as shown in above image, (0.004 > joint min 0), the object's Joint State will bounce back to 0.004." %}


### Push With Physics

Though VirtualGrasp can create push interaction without relying on physical simulation, there are certain limitations:
1. Only the index tip finger push is supported (by setting <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.InteractionAffordance}}">Interaction Affordance</a> to INDEX_PUSHABLE)
2. There are some directions on the object the finger can not apply push action (see Push Pivot in [Object Articulation](object_articulation.html#object-articulation)). 


