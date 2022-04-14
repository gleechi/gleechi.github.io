---
title: Object Baking
sidebar: main_sidebar_0_12_0
keywords: grasp, baking, cabvg
permalink: object_baking.0.12.0.html
folder: knowledge
toc: true
---

In order to runtime synthesize natural looking grasps on objects during [grasp interaction](grasp_interaction.0.12.0.html), 
VirtualGrasp requires a preprocessing step of these objects. 
Like game developers know the concepts of "light baking" or "texture baking" in order to preprocess expensive computations and have faster access during runtime, we call the preprocessing of the objects {% include tooltip.html tooltip="ObjectBaking" text="object baking" %}.

To bake an object, we need to access the 3D mesh data of the object. 
So if the 3D mesh data of the object changed, a new object baking is needed. 
Table below lists when a new bake is needed:

| When do we need new baking | Why? |
|-------|--------|---------|---------|
| Object mesh changed|  Because mesh defines object shape. | 
| Object scale changed |  Because grasp depends on the object size. | 
| Object pivot (origin) changed |  Because the shape analysis result is stored in the object's coordinate frame. | 

{% include callout.html content="If you have not baked your project, you can still enjoy 
the object interactive behaviors supported by [object articulation](object_articulation.0.12.0.html#object-articulation). 
However, note that there will only be unnatural looking sticky hand like grasps
 (see [grasp interaction type](grasp_interaction.0.12.0.html#grasp-interaction-type))." %}

See [VG_BakingClient](unity_component_vgbakingclient.0.12.0.html) to learn how to bake the objects in your Unity project.
