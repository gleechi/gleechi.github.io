---
title: VG_HandProfile [Scriptable Object]
keywords: editor, script
sidebar: main_sidebar_1_6_3
permalink: unity_component_vghandprofile.1.6.3.html
folder: mydoc
---

## Description

VirtualGrasp provides VG_HandProfiles (in Unity as ScriptableObjects) to configure a number of hand model-related settings and thereby allows you to quickly switch between different hand models.

{% include callout.html content="You only need to create a new instance of a VG_HandProfile if you import a new hand model into your game that deviates from a hand model that you already have. You then potentially need to configure the hand rotation mappings as well as the hand bone mappings (see below) for your new VG_HandProfile." %}

{% include image.html file="unity/unity_vg_ec_handprofile_1_4_0.png" alt="VG_HandProfile in Unity." caption="Example of a VG_HandProfile as a scriptable object in Unity." %}

## Hand Mapping Rotations

For various hand models, the artists may have designed the coordinate frames differently. To compensate for these rotation offset, you have configure VG_HandProfile's **Left Hand Mapping** and **Right Hand Mapping** settings. Rotation Types and Hand Mappings define how the hand model deviates in terms of bone pose orientations. 

See [Axis mappings](axis_mappings.1.6.3.html) for a more detailed explanation.

## Hand Bone Mapping

The [Gleechi hand model standard](avatars.1.6.3.html#hand-model-standard) shows the requirement of the hiearchical structure of hand bones in order for VG to automatically identify and assign hand bones to VG's internal representation. 

When your hand model is not following this standard, then VG may fail to find hands in your model (indicated by console error output), or even VG finds the hands, the automatically identified hand bones may be off. For example, the first finger bone (index 0) may be mapped to the metacarpal bone. To fix this, you can manually provide a hand bone map by loading your hand skinned mesh and editing the Left and Right Hand Bone Maps (correct the mapped bone transforms), then click **Assign Hand Bone Indices** to save the map as "hand bone indices" in the hand profile. 

Image below shows an example of assigned "hand bone indices" (shown in "[]") on Left Hand Bone Map for Oculus hands. "Wrist_L [0]" means the left wrist bone is represented by the 1st transform of the supported Oculus hands model. If the value is [-1] means this bone is not mapped. In a valid map, [-1] can only possibily be on the finger tip bones in the case the hand model does not have finger tip transforms.  (However we highly recommend you to add finger tip transforms, [Gleechi hand model standard](avatars.1.6.3.html#hand-model-standard).)

{% include important.html content= "Hand bone mapping is not needed if your hand model follows the Gleechi hand model standard. For example the provided **Resources/VG_HandProfiles/VG_HP_GleechiHands** does not need the bone map, i.e. the hand bone indices are not assigned. In this situation all bone indices are [-1]."%}. 

* If hand bone mapping is provided (i.e. Hand Bone Indices assigned), then VG will identify the hand according to the provided indices. 
* If hand bone mapping is not provided (i.e. Hand Bone Indices not assigned, all values are [-1]), then VG will try to automatically identify hands. 

{% include image.html file="unity/unity_vg_ec_handprofile_handboneindices.png" alt="Hand Bone Indices in VG_HandProfile in Unity." caption="Example of assigned Hand Bone Indices in VG_HandProfile in Unity. Note the transforms for bones are only assigned if a hand model skinned mesh is loaded." %}

### How to create hand bone mapping for a custom hand model?

If you have created a hand profile for this hand model for the [rotation mappings](unity_component_vghandprofile.1.6.3.html#hand-mapping-rotations), then in the same profile, load your hand skinned mesh. Since no bone map has been created (all indices are [-1]), the moment you load the hand skinned mesh, VG will try to identify the hand bones automatically. Two situations may occur:
1. VG fails to identify any hands, thus no corresponding bone transforms are assigned in either Left or Right Hand Bone Map drop down menu. 
2. VG identified left and/or right hands (depending on if your model contains both hands or only one hand side). In such case, the identified hand bone transforms should be filled in Left and/or Right Hand Bone Map drop down menu.

In situation 2, you should then check if identified hand bone transforms are correct or not. The GUI has tooltips explaining which hand bones VG is looking for with the names following common hands anatomy. If everything is correct, then you don't need to click **Assign Hand Bone Indices**. (Assigning will not hurt of course).

If however some bones are mis-represented then you need to correct them. For example, if Index0_L is mapped wrongly to a transform representing the metacarpal, then you need to correct it by dragging the correct transform representing the proximal phalange to this slot. Make sure all bones are correctly mapped, and then click **Assign Hand Bone Indices** to save the indices. 

In situation 1, since VG has failed to identify any hand bones, you have to manually assign transforms to all corresponding hand bones, then click **Assign Hand Bone Indices**. 

In both situations, when **Assign Hand Bone Indices** is pushed, VG will verify the validity of your manually assigned bone map and give hints if something is not correct. 
