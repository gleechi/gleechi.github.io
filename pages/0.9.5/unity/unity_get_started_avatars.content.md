### A First Look at the Hand Model

First, import a hand model into your scene, such as the provided OculusRig_3 in ThirdPart/VirtualGrasp/Resources. 

Next, link it into its place under Sensors → Avatars → Skeletal Mesh, by dragging and dropping Rhand.001 (which you can find directly under OculusRig_3 in the Hierarchy) into this slot.

{% include image.html file="unity/unity_hand_model.png" alt="Unity hand model." caption="Hand model references need to be provided in Sensors → Avatars → Skeletal Mesh." %}

### Conditions for Avatars

You can replace this model by any other skinned mesh renderer that you import into the scene, but there are certain conditions on which kind of skeletal meshes are supported. 

As a rule of thumb, the rigging / model hierarchy should be same as the model in the project:

* 1 avatar / skeletal mesh should include 2 hands, 
* 1 hand should include 5 fingers (no extra bones), and 
* 1 finger should include 3-4 bones (with or without fingertip). If a fingertip is missing, VirtualGrasp will estimate its position, but it is recommended, and also very easy in Unity to add missing fingertip bones manually.

You can see that VG has successfully initialized the avatar when messages like these appear:

{% include image.html file="unity/unity_avatar_init.png" alt="Unity avatar init." caption="VirtualGrasp initialization message in the Unity console." %}

{% include tip.html content="Enable \"Update When Offscreen\" for your models to always show the hands even if they are close to the camera." %}

{% if include.skip != "true" %}
{% include custom/series_acme_next.html %}
{% endif %}
