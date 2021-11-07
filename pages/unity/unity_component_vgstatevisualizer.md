---
title: VG_StateVisualizer Component
keywords: editor, script, state-visualizer
sidebar: main_sidebar
permalink: unity_component_vgstatevisualizer.html
folder: mydoc
---

{% include image.html file="unity/unity_vg_statevisualizer_menu.png" alt="VG_StateVisualizer menu." caption="VG_StateVisualizer can be found in the VirtualGrasp/Components menu." %}

## Description

The VG_StateVisualizer is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that enables a Unity editor window in which you can read the current status of hands during runtime in the Editor. 

The VG_StateVisualizer.cs script itself provides a tutorial on some of the members of [VG_HandStatus](unity_component_vghandstatus.html) as well as some object-specific VG_Controller functions. 

As you can see in the example video, this is data such as the current avatar ID, the hand side, the currently selected object, the grab strength, or the {% include tooltip.html tooltip="JointState" text="state" %} of an articulated object (such as when grabbing the Antenna).

{% include editor_script.html %}

{% include youtube.html id="FQCzY6CdVRk" caption="Default VG_PostAnimator will modify the index finger bending." %}

```js
// ThirdParty/VirtualGrasp/Scripts/VG_StateVisualizer.cs

[...]

void OnGUI()
{
    if (!VG_Controller.IsEnabled())
    {
        GUILayout.Label("Play scene in order to visualize states.");
        return;
    }
    else
    {
        // Decide what to do based on the current hand status
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
        {
            GUILayout.Label("Avatar " + hand.m_avatarID + " " + hand.m_side + ": ", EditorStyles.boldLabel);
            GUILayout.Label(" Mode: " + hand.m_mode);
            GUILayout.Label(" Object: " + (hand.m_selectedObject == null ? "None" : hand.m_selectedObject.name));
            GUILayout.Label(" Grab: " + hand.m_grabStrength);
            if (hand.m_selectedObject != null) lastObj = hand.m_selectedObject;
            GUILayout.Label(" State: " + VG_Controller.GetObjectJointState(lastObj));
            GUILayout.Label("");
        }
    }
    this.Repaint();
}
````

