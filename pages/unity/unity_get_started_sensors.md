---
title: Getting Started in Unity - Sensors
series: "Getting Started in Unity series"
weight: 3
sidebar: main_sidebar
keywords: hand, object, avatar, install, quickstart
permalink: unity_get_started_sensors.html
folder: mydoc
toc: false
---

## A First Look at the Sensor Setup

{% include callout.html content="In VirtualGrasp we use the terms sensor and controller exchangeably since a VR controller is essentially a sensing device for hand poses." %}

In the default prefab, “GleechiLib”, a sensor setting is configured for any {% include tooltip.html tooltip="Controller" text="controller" %} (or {% include tooltip.html tooltip="Sensor" text="sensor" %}) supported through Unity by [UnityXR](https://docs.unity3d.com/Manual/XR.html).

As you can see in the top of the MyVirtualGrasp component, you can "auto-setup" the whole configuration for some of the most commonly used {% include tooltip.html tooltip="Sensor" text="sensors" %}, to quickly switch between Oculus controllers, mouse control, finger tracking, and other controllers. 

You can use VirtualGrasp without a VR headset and your scene does not need to be a VR-enabled scene. 

If you do not have a headset, you can use the "MOUSE" auto-setup and control the hands with the mouse. 

If you do have an Oculus Quest headset, we recommend to use "QUEST" auto-setup after enabling your scene for VR. 
<!--See [AutoSetup & Sensors](unity_component_myvirtualgrasp.html#autosetup--sensors) to learn more details about sensor setup.-->

<div class="panel-group" id="accordion1">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapseOne1">Quick Setup: enable VR in Unity with UnityXR</a>
            </h4>
        </div>
        <div id="collapseOne1" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                If you have a headset the easiest way is to setup Unity XR Management for your project as follows:
                <ul>
                <li> in the "Edit" menu, choose Project Settings→XR Plugin Management and "Install XR Plugin Management"</li>
                <li> enable "Oculus" as Plugin-Provider (assuming you are using a Quest)</li>
                <li> Right click "Camera" in Hierarchy and select "XR→Convert Camera To XR Rig"</li>
                <li> connect Quest with USB cable (the charging cable)</li>
                <li> Click "Enable Link" inside the headset</li>
                </ul>
                {% include image.html file="unity/unity_xr_plugin.png" alt="Unity XR Plugin." caption="Installing Unity XR Management." %}
            </div>
        </div>
    </div>
</div>

{% include image.html file="unity/unity_vg_myvirtualgrasp.png" alt="VG control flags." caption="MyVirtualGrasp is the default main configuration component for VirtualGrasp." %}

{% include custom/series_acme_next.html %}