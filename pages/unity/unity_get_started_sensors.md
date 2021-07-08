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

In the default prefab, a sensor setting is configured for the any controller supported through Unity by UnityXR.

As you can see in the top of the MyVirtualGrasp, you can "auto-setup" the whole configuration for some most commonly used sensors, to quickly switch between Oculus controllers, mouse control, finger tracking, and other controllers.

If you do not have a headset, you can use the "Mouse" autosetup and control the hands with the mouse.

### Setting up VR with UnityXR

If you have a headset the easiest way is to setup Unity XR Management for your project as follows:

* in the "Edit" menu, choose Project Settings→XR Plugin Management and "Install XR Plugin Management"
* enable "Oculus" as Plugin-Provider (assuming you are using a Quest)
* Right click "Camera" in Hierarchy and select "XR→Convert Camera To XR Rig"
* connect Quest with USB cable (the charging cable)
* Click "Enable Link" inside the headset

{% include image.html file="unity/unity_xr_plugin.png" alt="Unity XR Plugin." caption="Installing Unity XR Management." %}

Then, the "XRRig" transform that is created should be assigned to the sensor origin.

{% include image.html file="unity/unity_control_flags.png" alt="VG control flags." caption="" %}

{% include note.html content="You will have noticed that (if you used a fresh project) you did not even need to setup your scene for VR. You can run VirtualGrasp without a VR headset and your scene does not need to be a VR scene." %}

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
                There are a few controllers that are supported "out of the box" by VirtualGrasp, called INTERNAL_CONTROLLERS, which means that no additional Unity plugins are needed. Read more on this on <a href="mydoc_external_controllers.html">External Controllers</a>.).
            </div>
        </div>
    </div>
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
</div>


{% include custom/series_acme_next.html %}