### A First Look at the Sensor Setup

{% include callout.html content="In VirtualGrasp we use the terms \"sensor\" and \"controller\" exchangeably since a VR controller is essentially a sensing device for hand poses." %}

In [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.1.1.0.html), a sensor setup can be configured for any {% include tooltip.html tooltip="Controller" text="controller" %} (or {% include tooltip.html tooltip="Sensor" text="sensor" %}) supported through various [VG_ExternalControllers](unity_component_vgexternalcontrollermanager.1.1.0.html). A number of controller profiles are already included in VirtualGrasp, such as Oculus controllers, mouse control, finger tracking, among others. See [Sensors page](unity_component_myvirtualgrasp.1.1.0.html#sensors) for detailed instruction.

{% include image.html file="unity/unity_vg_myvirtualgrasp_1_0_0.png" alt="VG control flags." caption="MyVirtualGrasp is the default main configuration component for VirtualGrasp.<br>Note that \"Replay\" only appears in Pro-versions of VG." %}

You can use VirtualGrasp without a VR headset and your scene does not need to be a VR-enabled scene. 

{% include callout.html content="If you do not have a headset, you can use the \"VG_EC_Mousehand\" profile to get started and control the hands with the mouse. " type="warning" %}

{% include callout.html content="If you do have a headset, we recommend to use the \"VG_EC_UnityXRHand\" profile (after assuring that you enabled your scene for VR) to get started, through [UnityXR](https://docs.unity3d.com/Manual/XR.html)." type="info" %}

<!--See [AutoSetup & Sensors](unity_component_myvirtualgrasp.1.1.0.html#autosetup--sensors) to learn more details about sensor setup.-->

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
