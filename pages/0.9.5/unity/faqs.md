---
title: FAQs
#tags: [getting_started]
keywords: faqs
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: main_sidebar_0_9_5
permalink: faqs.0.9.5.html
folder: mydoc
---

## Common Unity Errors

### Root actors empty
```js
[VG] [ObjectSelector] [error] Object keypadbutton0/20174 root actors are empty!
````
This can be caused by multiple things e.g:

* Static geometry flag is enabled for object, or
* Transform scale is 0 (maybe during animation) on the object or any parent in the hierarchy.


### Mesh not readable

```js
[12:22:57] The mesh for screwdriver is not readable. Object cannot be processed.
````

This is because the source of that MeshRenderer have not checked “Read/Write enabled” checkbox in the model inspector. VG has an utility script you could use as shown in below image. Clicking _Make interactables readable_ will check this Read/Write checkbox for all objects that have been marked as interactable. 

{% include image.html file="unity/unity_vg_make_interactables_readable.png" alt="VG utility make interactables readable" caption="VG Utility: Make interactables readable" %}

### I am using my own hand models and the finger bend strangely

The reason for the mismatch is that each controller (for example, VG_EC_OculusHands.cs) is adjusting the raw finger orientations that come directly from the controller API (for example, from the Oculus Integration plugin) to match the hand model representation that is provided with the SDK. Read more on ways to resolve this issue on the [VG_ExternalControllerManager](unity_component_vgexternalcontrollermanager.0.9.5.html#coordinate-frame-corrections) page.