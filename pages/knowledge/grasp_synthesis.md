---
title: Knowledge Base - Static and Dynamic Grasping
sidebar: knowledge_sidebar
keywords: grasp, static, dynamic
permalink: grasp_synthesis.html
folder: knowledge
toc: true
---

## Comparison of Synthesis Methods

VirtualGrasp allows different methods of creating or "synthesizing" grasps. This is why we call this the "grasp synthesis method," where the most common ones are static and dynamic grasps:

<table border="1">
<colgroup>
<col width="40%" />
<col width="10%" />
<col width="10%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" style="text-align: right">Static Grasps</th>
<th colspan="2">Dynamic Grasps</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span" colspan="2" style="text-align: right">
Static Grasping describes the process of analyzing objects and hands, and simulating and analyzing grasps beforehand. Results are saved in a database that can be accessed and modified.<!-- While full baking is needed, it only uses grasp baking results during runtime.are created by a limited set of grasps around an object depending on a pre-baked grasp database.--></td>
<td markdown="span" colspan="2">Dynamic grasping describes the process of analyzing objects and hands, and simulating each grasp “on demand,” i.e. during runtime.<!--While full baking is currently enabled (so one can switch between static and dynamic grasping per object), it only uses shape baking results. --><!--are unlimited grasps that are generated during runtime.--></td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Limited number of and sparse grasps unless parameterized to be denser</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Infinite, flexible grasps</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">No overhead during runtime (simple DB access)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Some overhead during runtime (generative algorithm)</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Easy to edit grasps, such as removing bad grasps.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">Not possible to edit grasps.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Hand-sensor-immersion breaks in case of very sparse grasps.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Hand-sensor-immersion does not break.</td>
</tr>
<!--
<tr>
<td markdown="span" style="text-align: right">Difficult to transfer animation signals tuned for one hand to another (needs motion retargeting)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Potentially no need to transfer animation signals tuned for one hand to another.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Difficult to re-use the results of one hand with another (grasp transfer)</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">No need to re-use the results of one hand with another.</td>
</tr>
<tr>
<td markdown="span" style="text-align: right">Grasp baking time</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Only shape baking time</td>
</tr>
-->
<tr>
<td markdown="span" style="text-align: right">Potentially high baking time dependent on object complexity.</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Low baking time if only dynamic grasps are needed. Otherwise same as for static grasps.</td>
</tr>
<!--
<tr>
<td markdown="span" style="text-align: right">Higher baking time dependent on number of grasp types supported</td>
<td markdown="span" style="text-align: right">{% include inline_image.html file="icons/minus.png" alt="-" %}{% include inline_image.html file="icons/minus.png" alt="-" %}</td>
<td markdown="span">{% include inline_image.html file="icons/plus.png" alt="+" %}</td>
<td markdown="span">Grasp types are more freely chosen by the user and our internal algorithms, depending on how the user places wrist/fingers around an object.</td>
</tr>
-->
</tbody>
</table>

## Choosing the Synthesis Method

You can set the default method for all objects in the scene, in VG_SensorConfiguration → Settings → Global Synthesis Method:

{% include image.html file="unity/unity_vg_settings.png" alt="VG Settings." caption="VG_Settings" %}

You can also overwrite this for particular objects, by adding a VG_Interactable to the object and setting interaction type and synthesis method.

{% include image.html file="unity/unity_vg_interactable.png" alt="VG interactable." caption="VG_Interactable" %}

Note that all objects without a customized VG_Interactable will follow the global settings (see above), but those with VG_Interactable will follow their local settings.
