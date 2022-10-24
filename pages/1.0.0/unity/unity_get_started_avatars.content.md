### A First Look at the Hand Model

First, import a hand model into your scene, such as the provided GleechiRig in ThirdParty/VirtualGrasp/Resources/GleechiHands. 

Next, link it into its place under Sensors → Avatars → Skeletal Mesh, by dragging and dropping its SkinnedMeshRenderer (which you can find directly under GleechiRig in the Hierarchy) into this slot.

{% include image.html file="unity/unity_hand_model_0_11_1.png" alt="Unity hand model." caption="Hand model references need to be provided in Sensors → Avatars → Skeletal Mesh." %}

### Conditions for Avatars

**In Pro-versions of VG,** you can replace this model by any other skinned mesh renderer that you import into the scene, but there are certain conditions on which kind of skeletal meshes are supported. 

As a rule of thumb, the rigging / model hierarchy should be same as the model in the project:

* 1 avatar should include 2 hands (its SkeletalMesh structure), 
* 1 hand should include 5 fingers (no extra bones), and 
* 1 finger should include 3-4 bones (with or without fingertip). If a fingertip is missing, VirtualGrasp will estimate its position, but it is recommended, and also very easy in Unity to add missing fingertip bones manually.

<!--You can see that VG has successfully initialized the avatar when messages like these appear:
{% include image.html file="unity/unity_avatar_init_0_11_1.png" alt="Unity avatar init." caption="VirtualGrasp initialization message in the Unity console." %}
-->
