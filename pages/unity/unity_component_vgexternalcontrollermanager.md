---
title: VG_ExternalControllerManager Component
keywords: component, external-controller manager
sidebar: main_sidebar
permalink: unity_component_vgexternalcontrollermanager.html
folder: mydoc
---

## Description 

VG_ExternalControllerManager is a static class representing the controller abstraction towards VirtualGrasp. 

It should be used in any VG_MainScript, such as [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.html), where it is initialized after the VG_Controller itself initialized:

```js
override public void Awake()
{
    base.Awake();
    VG_Controller.Initialize();
    VG_ExternalControllerManager.Initialize(this);
}
````

VG_ExternalControllerManager.cs is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} so that is is extendable, for example to add more controllers or functionalities.

It is called external, because - instead of an internal native library - an external source is feeding VG with the input data. In most cases, this external source is a plugin provided by the hardware manufacturer for your engine of choice.

{% include image.html file="knowledge/external_controllers.png" alt="Internal controllers." caption="External controller pipeline." %}

