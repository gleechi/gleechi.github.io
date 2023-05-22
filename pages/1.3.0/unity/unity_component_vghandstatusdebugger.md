---
title: VG_HandStatusDebugger Component
keywords: editor, script
sidebar: main_sidebar_1_3_0
permalink: unity_component_vghandstatusdebugger.1.3.0.html
folder: mydoc
---

## Description

The VG_HandStatusDebugger is a {% include tooltip.html tooltip="VGPublicScript" text="public script" %} that shows the current status of hands during runtime in the Editor. 

The VG_HandStatusDebugger provides a tutorial on some of the members of [VG_HandStatus](unity_component_vghandstatus.1.3.0.html) which are central to many of the API functions, such as [GetHands()](virtualgrasp_unityapi.1.3.0.html#gethands) or some [Events](virtualgrasp_unityapi.1.3.0.html#events).

As you can see in the example video, this is data such as the current avatar ID, the hand side, the wrist transform of that hand, the currently selected object, and the grab strength.

{% include singleton_script.html %}

```js
// ThirdParty/VirtualGrasp/Scripts/VG_HandStatusDebugger.cs

public class VG_HandStatusDebugger : MonoBehaviour
{
    [Tooltip("This list will be updated during runtime with the VG_HandStatus of all hands.")]
    public List<VG_HandStatus> m_hands = new List<VG_HandStatus>();

#if UNITY_EDITOR
    public void Update()
    {
        m_hands.Clear();
        foreach (VG_HandStatus hand in VG_Controller.GetHands())
            m_hands.Add(hand);
    }
#endif
}
````

{% include youtube.html id="8YOEeZmeil8" caption="The VG_HandStatusDebugger will continuously update the list of VG_HandStatus in the Inspector." %}

