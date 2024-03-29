### Downloading the VirtualGrasp plugin for Unity

The VirtualGrasp SDK for Unity is currently available in the two versions FREE and PRO:

| Version | [PRO](https://assetstore.unity.com/packages/tools/utilities/virtualgrasp-pro-239348) | [FREE](https://assetstore.unity.com/packages/tools/utilities/virtualgrasp-free-240823) |
| VG SDK & Interaction Engine | ✔ | ✔ |
| Android & Windows support | ✔ | ✔ |
| [Object Baking](object_baking.1.1.0.html) | ✔ | |
| [Grasp Editing](unity_component_vggraspeditor.1.1.0.html) | ✔ | |
| [Custom Hand Models](avatars.1.1.0.html#custom-hand-models) | ✔ | |
| [Replay Features](sensor_record_replay.1.1.0.html) | ✔ | |
| Commercial License | ✔ | |


### Supported Unity Engine Versions

In our experience Unity and the VirtualGrasp SDK are very robust in terms of up- or downgrading inside a major Unity version (e.g., 2020.x.x, 2021.x.x, etc) for your projects.

Note that VirtualGrasp SDK supports Windows and Android builds, but not MacOS.

The following is a list of Unity Engine versions that we have tested the VirtualGrasp SDK with:

* **Unity 2019.x and earlier** is not and will not be supported due to the lack of ArticulationBody components. 
* <ins>**Unity 2020.x**</ins> is supported and has been tested successfully.
* <ins>**Unity 2021.x**</ins> is supported and has been tested successfully.
  * **Unity 2021.3** is the version that we are currently using to create the SDK.
* <ins>**Unity 2022.1**</ins> is supported and has been tested successfully. 
  * For Unity 2022.1.0b, there is an Inspector GUI artifact in VG_MainScript/Sensors, but it is a known [Unity issue](https://issuetracker.unity3d.com/issues/first-array-element-expansion-is-broken-for-arrays-that-use-custom-property-drawers).

### Installing the VirtualGrasp plugin for Unity

If you start from scratch, just create a new, empty project in Unity. 

{% include image.html file="unity/unity_new_project.png" alt="New Unity Project" caption="Create a New Project in Unity" %}

To import VirtualGrasp into your Unity project, go to Assets → Import Package → Custom Package and import the VirtualGrasp *.unitypackage. After doing this, you should find the main VirtualGrasp installation under ThirdParty/VirtualGrasp in your Unity project. 

### Updating the VirtualGrasp plugin for Unity

If you are updating the VG SDK in your project, it we **strongly recommend to remove the old version before importing the new one**, to avoid clutter of old files. The whole VG SDK is placed into a single folder (by default ThirdParty/VirtualGrasp) to make the update process as convenient as possible for you. If you are customizing files inside the VG SDK, you should backup your old state or use a versioning system such as git.

### Getting Started with VirtualGrasp and the Console View

There is only one minimal main component you have to add by default to use and configure VirtualGrasp: [MyVirtualGrasp.cs](unity_component_myvirtualgrasp.1.1.0.html). Adding a component to your scene and playing your scene, you should see some messages produced by the plugin in the Console Window.

You can identify that VG has been successfully initialized when a message like these appear on the Console, also informing you of the SDK version:

{% include callout.html content="Initialized VirtualGrasp SDK (version 1.1.0-full)." %}

<!--{% include image.html file="unity/unity_console_initialization.png" alt="VG Console Initialization" caption="VirtualGrasp initialization message in the Unity console." %}-->

{% include tip.html content="Whenever something related to the VirtualGrasp plugin does not work as expected, first have a look at the Console. In most cases, you will be able to identify issues through error messages that are generated by the plugin." %}