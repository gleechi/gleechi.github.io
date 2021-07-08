---
title: Knowledge Base - Grasp Baking
sidebar: knowledge_sidebar
keywords: grasp, baking, cabvg
permalink: grasp_baking.html
folder: knowledge
toc: true
---

Like game developers know the concepts of "baking light" or "baking textures" in order to preprocess expensive computations and have faster access during runtime, we call our the preprocessing of interactions "baking." Eventually, the goal is to have grasps for any object, but to get there, we also bake the shape of the object. We thus include "shape baking" as well as "grasp baking" into the baking process.

* In order to bake shape, we need access to the 3D mesh data of the object. The input is the object mesh, the output is a semantic shape analysis of the object (such as its parts).

* In order to bake grasps, we additionally need access to the 3D rig and 3D mesh of the hand. The input is the baked shape and the hand, the output is a set of generated grasps. 

{% include important.html content="If any of these inputs changes, the object needs to be rebaked." %}

The final baking is encoded in each deployed plugin version. This means that each plugin will be baked project-dependently, i.e. you can use a plugin that has been built for a project A for a project B, but for all objects in project B that have not also been baked in project A, you will not get natural grasps.

<!--
### The Process of Baking behind the Scenes

In the absence of automatic baking servers and licensing services, there is still a manual step involved though the process itself is already highly automated and integrated to each game engine plugin. 

When a bake is requested on an external project, we are introducing the following pipeline: 

Enable "Save Debug Files" in the MyVirtualGrasp component. 

Run the project. OBJ files of each interactable object are exported into a [project_root]/Assets/vg_tmp folder, together with a couple of other files needed for baking or debugging

Stop the project. The files in that directory are zipped into a [project_name].zip in the project root folder

After doing this, disable "Save Debug Files" again.
-->



## Using CABVG - the VG_BakingClient 

You will be able to request a bake by connecting to Gleechi's CABVG server through a GUI interface that is part of the SDK. You can find it in the VirtualGrasp menu:

{% include image.html file="unity/unity_vg_baking_client.png" alt="VG Baking Client." caption="VG_BakingClient" %}

### Upload Input

To upload the files for a bake:

* First, create a package of the necessary inputs for the bake (this is equivalent to creating the [Debug Files](debug.files)).
* Insert the SitePath (provided to you with your license). The site path is the server address.
* Insert the ApiKey (provided to you with your license). The api key is an identifier to access the service.
* Enter your email address (to which you want to get notifications)
* Select the target platform
* Click "Upload"

Note that as soon as you close the window, your settings will be stored in a file called vg_cabvg_settings.json in your project folder, so you won't have to re-enter them all the time (since when you open the window, the settings will be loaded).

After clicking Upload, the server will receive the package and trigger a bake, and you should get a notification mail.

Now you have to wait (depending on the number of objects and their complexity)

### Download Output

You can either download the product of the bake, rename it and sort it in the Unity plugin folder yourself, or you can copy the download link, paste it in the DownloadURL field of the VG_BakingClient and click "Download." 

The VG_BakingClient will identify itself how to rename and where to place the file.

* An .so file (for Android/Quest) should become Plugins/Android/libvirtualgrasp-selection.so
* A .dll file (Windows) should become Plugins/x86_64/virtualgrasp-selection.dll

This should have finalized the process and you will be able to enjoy baked grasps of your interactable objects, without any involvement of other people's resources.

<!--
Known Issues

After creating the input package for the first time, and stopping Unity, the program may crash. The results are there though, so you can disable "Save Debug Files" again and continue with your regular work while waiting for the bake response.

In the console you can get errors that the mesh is not readable, this usually solves when enabling read/write in the import settings.   
-->