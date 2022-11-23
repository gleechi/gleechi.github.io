### A First Look at the Hand Model

First, import a hand model into your scene, such as the provided GleechiRig in ThirdParty/VirtualGrasp/Resources/GleechiHands. 

Next, link it into its place under Avatars → Skeletal Mesh, by dragging and dropping its SkinnedMeshRenderer (which you can find directly under GleechiRig in the Hierarchy) into this slot.

{% include image.html file="unity/unity_hand_model_1_0_0.png" alt="Unity hand model." caption="Hand model references need to be provided in Avatars → Skeletal Mesh.<br>Note that \"Replay\" only appears in Pro-versions of VG." %}

### Customized Avatars and Hand Models

**In Pro-versions of VG,** you can replace this model by any other skinned mesh renderer that you import into the scene.

In this case, you need to potentially create and configure a new VG_HandProfile for your model, and link it into its place under Avatars → HandProfile. 
In addition, there are certain conditions on which kind of skeletal meshes are supported. 

We recommend you to include both left and right hands in one avatar model like in Gleechi's avatar model. But if you do have two separate models for left and right hands, you can set it up following [separate hand models](avatars.1.0.0.html#separate-hand-models). 

More about the use of custom hand models and configuring them is described in [Avatars](avatars.1.0.0.html).


<!--You can see that VG has successfully initialized the avatar when messages like these appear:
{% include image.html file="unity/unity_avatar_init_0_11_1.png" alt="Unity avatar init." caption="VirtualGrasp initialization message in the Unity console." %}
-->
