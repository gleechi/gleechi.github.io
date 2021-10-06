---
title: Getting Started in Unity - Objects
series: "Getting Started in Unity series"
weight: 4
sidebar: unity_sdk_sidebar
keywords: hand, object, avatar, install, quickstart
permalink: unity_get_started_objects.html
folder: mydoc
toc: false
---

## Make an Object Interactable in a Few Seconds

VirtualGrasp is using tags or layers to mark objects as interactable. By default, it searches for "Object" as a layer or tag name. 

In Unity, the very simple way to make an object interactable is to

* add the object into your scene, and
* add the "Object" tag to the object.

<table>
<thead>
<tr class="header">
<th>Inspector View</th>
<th>Layer Menu</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">{% include image.html file="unity/object_tag1.png" alt="Unity tags 1." %}<i>Tag entry for each GameObject.</i></td>
<td markdown="span">{% include image.html file="unity/object_tag2.png" alt="Unity tags 2." %}<i>Layer dropdown in Unity.</i></td>
</tr>
</tbody>
</table>

Be aware of the following:

* Note that this will make an object interactable (i.e. selectable and movable) with the hands through the VG Interaction Engine. If you also get natural grasps depends on if  the object has been "baked." Read more on baking in the [Knowledge Base - Baking](grasp_baking.html).
* Only GameObjects with a Mesh connected to it should receive the "Object" tag. Otherwise, you will receive a warning.
* All of these meshes need to be marked as "readable" in the model inspector. Otherwise, you will receive a warning / error.

<!--
### Video Tutorial 

The following video content is outdated in the sense that VG has been updated to NOT consider names anymore (due to the issues addressed in the video). VG is directly identifying duplicates or differences based on the shape.

{% include youtube.html id="oVILrei1LGA" %}
-->

### Customizing Layers and Tags

If you like, you can customize the tag and layer names that are used to identify VG objects in the MyVirtualGrasp → Show Advanced → Selection Settings → Object Identifiers.

Note that "Object" is always a tag identifier for VG, independent of the content of the list. The default entry is only shown in the List to remind you about it.

{% include image.html file="unity/unity_object_identifiers.png" alt="Unity Object Identifiers." caption=""%}


{% include custom/series_acme_next.html %}