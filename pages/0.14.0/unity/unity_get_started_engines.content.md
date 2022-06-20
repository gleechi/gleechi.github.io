In our experience Unity and the VirtualGrasp SDK are very robust in terms of up- or downgrading inside a major Unity version (e.g., 2020.x.x, 2021.x.x, etc) for your projects.

Note that VirtualGrasp SDK supports Windows and Android builds, but not MacOS.

The following is a list of Unity Engine versions that we have tested the VirtualGrasp SDK with:

* **Unity 2019.x and earlier** is not and will not be supported due to the lack of ArticulationBody components. 
* <ins>**Unity 2020.x**</ins> is supported and has been tested successfully.
* <ins>**Unity 2021.x**</ins> is supported and has been tested successfully.
  * **Unity 2021.3** is the version that we are currently using to create the SDK.
* <ins>**Unity 2022.1**</ins> is supported and has been tested successfully. 
  * For Unity 2022.1.0b, there is an Inspector GUI artifact in VG_MainScript/Sensors, but it is a known [Unity issue](https://issuetracker.unity3d.com/issues/first-array-element-expansion-is-broken-for-arrays-that-use-custom-property-drawers).
