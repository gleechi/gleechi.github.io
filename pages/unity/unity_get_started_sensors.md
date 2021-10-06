---
title: Getting Started in Unity - Sensors
series: "Getting Started in Unity series"
weight: 3
sidebar: unity_sdk_sidebar
keywords: hand, object, avatar, install, quickstart
permalink: unity_get_started_sensors.html
folder: mydoc
toc: false
---

## A First Look at the Sensor Setup

In the default prefab, a sensor setting is configured for the any controller supported through Unity by [UnityXR](https://docs.unity3d.com/Manual/XR.html).

As you can see in the top of the MyVirtualGrasp component, you can "auto-setup" the whole configuration for some most commonly used sensors, to quickly switch between Oculus controllers, mouse control, finger tracking, and other controllers.

AutoSetup will take care of a number of settings in the MyVirtualGrasp component. You can use VirtualGrasp without a VR headset and your scene does not need to be a VR-enabled scene. If you do not have a headset, you can use the "Mouse" auto-setup and control the hands with the mouse. If you do have an Oculus Quest headset, we recommend to use "Quest" auto-setup after enabling your scene for VR. 

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


### FAQs

<div class="panel-group" id="accordion">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">What's an EXTERNAL_CONTROLLER?</a>
            </h4>
        </div>
        <div id="collapseOne" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                There are a few controllers that are supported "out of the box" by VirtualGrasp, called INTERNAL_CONTROLLERs, which means that no additional Unity plugins are needed. EXTERNAL_CONTROLLERs are enabled through separate Unity plugins. Read more on this on <a href="controllers.html">External Controllers</a>.).
            </div>
        </div>
    </div>
    <!--
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">What kind of sensor would I choose for the Oculus Quest that I have? One of the Oculus Touch options? Or perhaps external controller? </a>
            </h4>
        </div>
        <div id="collapseTwo" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                You can have to use the EXTERNAL_CONTROLLER setting and "UnityXR". You may also want to check out [Building for Quest](mydoc_external_controllers.html).
            </div>
        </div>
    </div>
    -->
</div>


{% include custom/series_acme_next.html %}