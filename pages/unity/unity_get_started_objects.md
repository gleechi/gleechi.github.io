---
title: Getting Started in Unity - Objects
series: "Getting Started in Unity series"
weight: 4
sidebar: main_sidebar
keywords: hand, object, avatar, install, quickstart
permalink: unity_get_started_objects.html
folder: mydoc
toc: false
---

## Make an Object Interactable in a Few Seconds

In Unity, the easiest way to make a GameObject interactable is to add a [VG_Articulation](unity_component_vgarticulation.html) component.

### Conditions for Interactable Objects

The following two conditions have to be met:

1. The GameObject must have a MeshRenderer component (representing the actual 3D shape data) assigned to it.
1. The source of that MeshRenderer must have the "Read/Write enabled" checkbox checked in the model inspector.

Only the MeshRenderer on that GameObject will be interactable, i.e. no MeshRenderers in the hierarchy below it.

The GameObject will be made interactable (i.e. selectable and movable) with the hands through the VG Interaction Engine. However, if you also get natural grasps depends on if the object has been "baked." You can read more on baking in [Knowledge Base - Baking](grasp_baking.html).

### Customizing Layers and Component Names

VirtualGrasp is using names to identify which objects are marked as interactable. You can customize component and layer names in MyVirtualGrasp → Object Identifiers. 
"VG_Articulation" is a default entry, but this method also allows you to quickly adjust your project if you already have a layer or a component that marks your interactable objects.

{% include image.html file="unity/unity_object_identifiers.png" alt="Unity Object Identifiers." caption="VG will use the Object Identifier list to browse components and layers for interactable objects."%}

{% include custom/series_acme_next.html %}