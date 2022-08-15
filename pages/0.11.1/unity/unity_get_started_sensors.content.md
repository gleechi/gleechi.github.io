### A First Look at the Sensor Setup

{% include callout.html content="In VirtualGrasp we use the terms \"sensor\" and \"controller\" exchangeably since a VR controller is essentially a sensing device for hand poses." %}

In any VG_MainScript, such as [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.0.11.1.html), a sensor setting can be configured for any {% include tooltip.html tooltip="Controller" text="controller" %} (or {% include tooltip.html tooltip="Sensor" text="sensor" %}) supported through various [VG_ExternalControllers](unity_component_vgexternalcontrollermanager.0.11.1.html).

As you can see in the top of the MyVirtualGrasp component, you can "Auto-Setup" the whole configuration for some of the most commonly used {% include tooltip.html tooltip="Sensor" text="sensors" %}, to quickly switch between Oculus controllers, mouse control, finger tracking, and other controllers. 

You can use VirtualGrasp without a VR headset and your scene does not need to be a VR-enabled scene. 

{% include callout.html content="If you do not have a headset, you can use the \"MOUSE\" auto-setup to get started and control the hands with the mouse. " type="warning" %}

{% include callout.html content="If you do have a headset, we recommend to use the \"UNITYXR\" auto-setup (after assuring that you enabled your scene for VR) to get started, through [UnityXR](https://docs.unity3d.com/Manual/XR.html)." type="info" %}

<!--See [AutoSetup & Sensors](unity_component_myvirtualgrasp.0.11.1.html#autosetup--sensors) to learn more details about sensor setup.-->

{% if include.skip != "true" %}
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
                <li> Select "Enable Oculus Link" inside the headset</li>
                </ul>
                {% include image.html file="unity/unity_xr_plugin.png" alt="Unity XR Plugin." caption="Installing Unity XR Management." %}
            </div>
        </div>
    </div>
</div>
{% endif %}

{% include image.html file="unity/unity_vg_myvirtualgrasp_0_11_1.png" alt="VG control flags." caption="MyVirtualGrasp is the default main configuration component for VirtualGrasp." %}