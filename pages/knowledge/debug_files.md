---
title: Debug Files
sidebar: main_sidebar
keywords: vg_tmp
permalink: debug_files.html
folder: knowledge
toc: true
---

{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG Debug Settings." caption="Debug Settings." %}

Enabling "Save Debug Files" and running the application will create a **vg_tmp** subdirectory in your project and save sources that are used for different purposes. The full debug files process is only in effect in development mode (i.e. using the Unity Editor), but not in builds.

{% include important.html content="Each creation of debug files is scene-dependent, meaning that it only relates to the **current** Unity scene. Thus, to complement debug files from multiple scenes, you have to run these scenes separately." %}

### Content

Whenever you start the scene, the following data will be saved in the "vg_tmp" folder (which will be created if it does not yet exist):
* One **.OBJ** file for each interactable object, i.e. raw 3D mesh data in uniform scale,
* One **.BIN** file for each avatar (containing one or a pair of hands of this avatar)

While you are running the scene, the following data will be saved in the "vg_tmp" folder:
* One **.LOG** file with VG log data (the same that also appears on the Console) for the scene that you are running.

Whenever you stop the scene, the following data will be saved:
* **.DB** & **.LAB** files carrying data created with [VirtualGrasp Studio](unity_component_vggraspstudio.html),
* One **.SCN** & **.SCN.OBJRIG** file for each scene, including scene configuration data. (See section [Debugging Interaction Issues](#debugging-interaction-issues) to learn about scene files)
* Finally, from all this content, one **.ZIP** file named "PROJECT_NAME".zip will be generated in your project folder.

{% include important.html content="Accordingly, it is recommended to delete the vg_tmp folder whenever you start with a new debug file creation process, since existing and potentially outdated data will not be deleted (only potentially overwritten)." %}

<!--
### Creating the Debug Files
If properly setup, you will see similar info as below in your console:

{% include image.html file="unity/unity_vg_debug_console.png" alt="VG Baking Debug Console." caption="Console Output after Saving Debug Files." %}
-->


### How To Use The Debug Files

#### Object Baking

The **.ZIP** file of all the content is the input that is needed for [Object Baking](grasp_baking.html#upload-input).

#### Grasp Editor

The **.OBJ** files of all the objects are used for the automatic generation of the [Grasp Studio](unity_component_vggraspstudio.html) scene.

### Debugging Interaction Issues

When you stop the scene, two scene configuration files for each Unity or Unreal scene will be saved: 
* .SCN: Is a [Protocol buffers](https://developers.google.com/protocol-buffers) representation of the current state of the scene including VG interaction setup and all interactable objects' status at the moment of saving. 
* .SCN.OBJRIG: Completely corresponds to .SCN file, but uses indentation to represent object hiearchy. 

These scene files reveals **how VG sees the status of your current scene** in your VR application. 
Because of this, they are very useful for you to debug any VG-related interaction issues that you experience. 

For example:
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.ObjectHierarchy}}">Object Hierarchy</a>: you thought you placed antenna as the child of radio, to see if it is really that way in VG, you can check the .scn file. 
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.SelectionWeight}}">Selection Weight</a>: you thought you have changed selection weight on antenna to 0, but it is actually not when check the .scn file. 
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.Affordance}}">Affordance</a>: you thought you have set radio to afford FINGER_PUSHABLE, but it is actually ONLY_GRASPABLE
* <a href="#" data-toggle="tooltip" data-original-title="{{site.data.glossary.GraspSynthesisMethod}}">Synthesis Method</a>: you thought you have decided to use STATIC_GRASP on antenna, but it is DYNAMIC_GRASP in reality.

{% include important.html content="Since .scn files are written at the moment when you stop playing the scene, the saved information reflects your scene configuration at that moment. 
So if you in runtime, for example, changed an object's joint type or selection weight, then stopped playing, the resulting .scn files will reflect the effective values after your runtime change." %}

Below shows an example of a .scn file representing a simple scene with just two objects - "radio" and "antenna". 
```
units_in_meters: 1
sensor_setup {
  wrist_pos_sensor: LEAP
  wrist_rot_sensor: LEAP
  finger_pose_sensor: LEAP
  finger_control_type: BY_SENSOR_FULL_DOFS
  sensor_origin_position {
    x: 13.0999994
    y: -19.6
    z: -3.7
  }
  sensor_origin_rotation {
    w: 1
  }
}
control_setup {
  gesture_duration: 0.1
  form_push_gesture: true
  mode_interpolation_duration {
    grasp: 0.2
    hold: 0.1
    release: 0.2
    empty: 0.1
  }
  grasp_selection_pos_thresh: 1
  grasp_selection_rot_thresh: 0.5
  grasp_selection_pos_weight: 0.5
  grasp_selection_rot_weight: 0.5
  push_angle_thresh: 2.61799383
}
avatar {
  scale: 1
  instance_id: 1
  avatar_hash: 1269503502
  hand_hash: 1949468064
  hand_hash: 3674342058
}
object {
  joint {
    id: 17908
    name: "radio"
    hash: 4092480540
    parent_id: 17888
    joint_type: floating
    joint_center {
      x: -2.13999987
      y: -0.807300091
      z: 1.40440011
    }
    axis {
      y: 1
    }
    position {
      x: -36.7001877
      y: 2.9882288
      z: 5.93024588
    }
    rotation {
      x: -0.498288751
      y: -0.498305738
      z: -0.501694202
      w: 0.501699686
    }
    push_axis {
      y: 1
    }
    grasp_constraint_axis {
      y: 1
    }
  }
  selection_weight: 1
  affordance: ONLY_GRASPABLE
  synthesis_method: DYNAMIC_GRASP
  physical: true
}
object {
  joint {
    id: 17958
    name: "antenna"
    hash: 1617809614
    parent_id: 17908
    joint_type: universal
    joint_center {
      z: -0.299999863
    }
    axis {
      z: 1
    }
    range_min: 0.52359879
    position {
      x: -29.2235985
      y: 8.81296
      z: 0.696459293
    }
    rotation {
      x: -0.49828881
      y: -0.498305798
      z: -0.501694262
      w: 0.501699746
    }
    user_specified_joint_center: true
    push_axis {
      z: 1
    }
    grasp_constraint_axis {
      z: 1
    }
  }
  selection_weight: 1
  affordance: ONLY_GRASPABLE
  synthesis_method: DYNAMIC_GRASP
}
```