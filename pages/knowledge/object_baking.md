---
title: Object Baking
sidebar: main_sidebar
keywords: grasp, baking, cabvg
permalink: object_baking.html
folder: knowledge
toc: true
---

In order to runtime synthesize natural looking grasps on objects during [grasp interaction](grasp_interaction.html), 
VirtualGrasp requires a preprocessing step of these objects. 
Like game developers know the concepts of "light baking light" or "texture baking" in order to preprocess expensive computations and have faster access during runtime, 
we call the preprocessing of the objects <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ObjectBaking}}">Object Baking</a>.


In order to bake an object, we need to access the 3D mesh data of the object. 
So if the 3D mesh data of the object changed, a new object baking is needed. 
Table below explains when a new bake is needed:

| When do we need new baking | Why? |
|-------|--------|---------|---------|
| Object mesh changed|  Because mesh defines object shape. | 
| Object scale changed |  Bcause grasp depends on the object size. | 
| Object pivot (origin) changed |  Because the shape analysis result is stored in the object's coordinate frame. | 

{% include important.html content="If you have not baked your project, you can still enjoy 
the object interactive behaviors supported by [Object Articulation](object_articulation.html#object-articulation). 
However, note that there will only be unnatural looking sticky hand like grasps
 (see [Grasp Interaction Type](grasp_interaction.html#grasp-interaction-type))." %}

See [VG_BakingClient](unity_component_vgbakingclient.html) to learn how to bake the objects in your project.

