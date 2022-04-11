### Make an Object Interactable in a Few Seconds

To make a GameObject {% include tooltip.html tooltip="VGInteractable" text="interactable" %} you simply add a [VG_Articulation](unity_component_vgarticulation.0.11.1.html) component to it.

### Conditions for Interactable Objects

The following two conditions have to be met:

1. The {% include tooltip.html tooltip="GameObject" text="GameObject" %} must have a MeshRenderer component (representing the actual 3D shape data) assigned to it.
2. The source of that MeshRenderer must have the "Read/Write enabled" checkbox checked in the model inspector. You can either do that manually or use the "VirtualGrasp → Utilities → Make Interactables Readable" helper function after you have equipped your objects with VG_Articulations.

Only the MeshRenderer on that {% include tooltip.html tooltip="GameObject" text="GameObject" %} will be interactable, i.e. no MeshRenderers in the hierarchy below it.

The {% include tooltip.html tooltip="GameObject" text="GameObject" %} will be made {% include tooltip.html tooltip="VGInteractable" text="interactable" %} with the hands through VG's [object articulation](object_articulation.0.11.1.html) feature. 

However, if you also want to get natural grasps then a preprocessing step called [object baking](object_baking.0.11.1.html) is needed.

<!--
### Customizing Layers and Component Names

VirtualGrasp is using names to identify which objects are marked as {% include tooltip.html tooltip="VGInteractable" text="interactable" %}. You can customize component and layer names in MyVirtualGrasp → Object Identifiers. 
"VG_Articulation" is a default entry, but this method also allows you to quickly adjust your project if you already have a layer or a component that marks your {% include tooltip.html tooltip="VGInteractable" text="interactable" %} objects.

{% include image.html file="unity/unity_object_identifiers.png" alt="Unity Object Identifiers." caption="VG will use the Object Identifier list to browse components and layers for interactable objects."%}
-->
