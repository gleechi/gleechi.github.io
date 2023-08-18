### Installation

To quickstart, first [download and install](unity_get_started_installation.1.5.0.html#downloading-the-virtualgrasp-plugin-for-unity) the VirtualGrasp SDK into a project.

### Play the Onboarding Scene

We recommend to start playing the onboarding scene that can be found in the Samples/Onboarding folder to see if your project is set up properly. 

The project is setup for XR use, so if it is not yet installed, install the XR Management package through the package manager or the VirtualGrasp Welcome Dialogue: 

{% include image.html width="70" file="unity/unity_vg_welcome.png" alt="VirtualGrasp Welcome Dialog." caption="Open the VirtualGrasp Welcome dialogue to install XR and Tutorials packages."%}

### Follow the In-Editor Tutorials

We strongly recommend to install the the Unity tutorials framework package to get access to In-Editor tutorial that lead you through the most important processes of the SDK, such as setting up your project, object baking (PRO version only) and hand tracking:

{% include image.html width="50" file="unity/unity_vg_tutorials.png" alt="VirtualGrasp In-Editor Tutorials." caption="VirtualGrasp In-Editor Tutorials."%}

With every new update to VirtualGrasp, we will optimize and expand those tutorials.

### Build an APK for your VR headset

You can also build an apk from within Unity from the Onboarding scene to start playing it in VR.

It is important that VirtualGrasp only supports 64 bit for Android. You therefore have to ensure that you use **IL2CPP** as Scripting Backend and **ARM64** as Target Architecture in your Build Settings, see image below:

{% include image.html width="70" file="unity/unity_build_settings.png" alt="VG Build Settings" caption="Ensure that build settings are configured for 64 bit on Android." %}

<!--

### A First Look at the Hand Model

### Customized Avatars and Hand Models

**In Pro-versions of VG,** you can replace this model by any other skinned mesh renderer that you import into the scene.

In this case, you potentially need to create and configure a new [VG_HandProfile](unity_component_vghandprofile.1.5.0.html) for your model, and link it into its place under Avatars → HandProfile. 
In addition, there are certain conditions on which kind of skeletal meshes are supported, and check out [Gleechi hand model standard](avatars.1.5.0.html#hand-model-standard) for details. 

We recommend you to include both left and right hands in one avatar model like in Gleechi's avatar model. But if you do have two separate models for left and right hands, you can set it up following [separate hand models](avatars.1.5.0.html#separate-hand-models). 

More about the use of custom hand models and configuring them is described in [Avatars](avatars.1.5.0.html).
-->

<!--
### Make an Object Interactable in a Few Seconds

To make a GameObject {% include tooltip.html tooltip="VGInteractable" text="interactable" %} you simply add an active [VG_Articulation](unity_component_vgarticulation.1.5.0.html) component to it.

### Conditions for Interactable Objects

The following two conditions have to be met:

1. The {% include tooltip.html tooltip="GameObject" text="GameObject" %} must have a MeshRenderer component (representing the actual 3D shape data) assigned to it.
2. The source of that MeshRenderer must have the "Read/Write enabled" checkbox checked in the model inspector. You can either do that manually or use the "VirtualGrasp → Make Interactables Readable" helper function after you have equipped your objects with VG_Articulations.

Only the MeshRenderer on that {% include tooltip.html tooltip="GameObject" text="GameObject" %} will be interactable, i.e. no MeshRenderers in the hierarchy below it.

The {% include tooltip.html tooltip="GameObject" text="GameObject" %} will be made {% include tooltip.html tooltip="VGInteractable" text="interactable" %} with the hands through VG's [object articulation](object_articulation.1.5.0.html) feature. 

However, if you also want to get natural grasps then a preprocessing step called [object baking](object_baking.1.5.0.html) is needed.
-->

<!--
### Customizing Layers and Component Names

VirtualGrasp is using names to identify which objects are marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. You can customize component and layer names in MyVirtualGrasp → Object Identifiers. 
"VG_Articulation" is a default entry, but this method also allows you to quickly adjust your project if you already have a layer or a component that marks your {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects.

{% include image.html file="unity/unity_object_identifiers.png" alt="Unity Object Identifiers." caption="VG will use the Object Identifier list to browse components and layers for interactable objects."%}
-->
