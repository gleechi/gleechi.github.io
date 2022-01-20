---
title: Debug Files
sidebar: main_sidebar_0_9_6
keywords: vg_tmp
permalink: debug_files.0.9.6.html
folder: knowledge
toc: true
---

{% include image.html file="unity/unity_vg_debug_settings.png" alt="VG Debug Settings." caption="\"Save Debug Files\" must be enabled Debug Settings to prepare the files." %}

## Creating Debug Files

Enable the **“Save Debug Files”** in your VG_MainScript when you want to create debug files.

Running the application in the Editor will create a *vg_tmp* subdirectory in your project’s Asset folder and export files (see [Debug Files Content](#debug-files-content) below) when you play your scene. It will then also create a .zip file from the vg_tmp folder in your project’s root folder.

The full debug files process is only in effect in development mode (i.e. using the Unity Editor), but not in builds.

{% include important.html content="Each creation of debug files is scene-dependent, meaning that it only relates to the **current** Unity scene. Thus, to complement debug files from multiple scenes, you have to run these scenes separately with \"Save Debug Files\" enabled." %}

**“Save Debug (Edit)"** will simulate a launch of the VG plugin from the Unity Editor, thus without launching the scene. This option is provided for convenience, but  objects that are not in your scene yet (such as those you spawn in runtime, or those you add by loading another scene during runtime), will not be included for baking.

{% include important.html content="It is recommended to delete the vg_tmp folder whenever you start with a new debug file creation process, since existing and potentially outdated data will not be deleted (only potentially overwritten)." %}<br>

{% include image.html file="knowledge/baking_pipeline.png" alt="Baking Pipeline." caption="Debug Files." %}

## Debug Files Content

* One *.obj* file for each interactable object in the scene, i.e. raw 3D mesh data in uniform scale, will be created when you start the scene.
* One *.bin* file for each avatar (containing one or a pair of hands of this avatar), will be created when you start the scene.
* One *.log* file with VG log data (the same that also appears on the Console) for the scene that you are running, will be filled while you are running the scene.
* One *.db* file carrying data filled with [VG_GraspStudio](unity_component_vggraspstudio.0.9.6.html) or [VG_BakingClient](unity_component_vgbakingclient.0.9.6.html).
* One *.scn* and one *.scn.objrig* file for each scene, including scene configuration data (see section [Debugging Interaction Issues](#debugging-interaction-issues) to learn about these {% include tooltip.html tooltip="VGSceneFiles" text="VG scene files" %}).

## Naming of the .zip and .db Files

By default, the .zip and .db files are given the name [applicationId]-[applicationVersion] (which are extracted from your Unity project's build settings).

You can customize the name by modifying the VG_VirtualGraspDBFile that you can find in the VirtualGrasp/Resource folder.

{% include image.html file="unity/unity_vg_virtualgraspdbfile.png" alt="VG_VirtualGraspDBFile" caption="Scriptable resource VG_VirtualGraspDBFile allows you to customize the name of your .db and .zip file." %}

## How To Use The Debug Files

### Object Baking

The *.zip* file of all the content is the input that is needed for [object baking](object_baking.0.9.6.html#upload-input).

### Grasp Editing

The *.obj* files of all the objects are used for the automatic generation of the [grasp studio](unity_component_vggraspstudio.0.9.6.html) scene.

### Debugging Interaction Issues

When you stop the scene, two scene configuration files for each Unity or Unreal scene will be saved: 
* *.scn*: Is a JSON representation of the current state of the scene including VG interaction setup and all interactable objects' status at the moment of saving. 
* *.scn.objrig* completely corresponds to the *.scn* file, but uses indentation to represent object hiearchy. 

These scene files reveals *how VG sees the status of your current scene* in your VR application. 
Because of this, they are very useful for you to debug any VG-related interaction issues that you experience. 
For example:

* {% include tooltip.html tooltip="ObjectHierarchy" text="object hierarchy" %}: you thought you placed antenna as the child of radio. To see if it is really that way in VG, you can check the *.scn* file. 
* {% include tooltip.html tooltip="SelectionWeight" text="selection weight" %}: you thought you have changed the selection weight on the antenna to 0, but it is actually not when checking the *.scn* file. 
* {% include tooltip.html tooltip="Affordance" text="affordance" %}: you thought you have set the radio to be pushable (FINGER_PUSHABLE), but it is actually only graspable (ONLY_GRASPABLE).
* {% include tooltip.html tooltip="GraspSynthesisMethod" text="synthesis method" %}: you thought you have decided to use static grasps (STATIC_GRASP) on the antenna, but it is using dynamic grasps (DYNAMIC_GRASP) in reality.

{% include callout.html content="Since .scn files are written at the moment when you stop playing the scene, the saved information reflects your scene configuration at that moment. 
So if you in runtime, for example, changed an object's joint type or selection weight, then the resulting .scn files will reflect the effective values after your runtime changes." %}


<div class="panel-group" id="accordion1">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapseOne1">.scn file example:</a>
            </h4>
        </div>
        <div id="collapseOne1" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">  
            Example of an .scn file representing a simple scene with just two objects - "radio" and "antenna".<br><br>
{% highlight java %}
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
    range_min: -0.52359879
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
{% endhighlight %}

            </div>
        </div>
    </div>
</div>

