---
title: Release Notes
#tags: [getting_started]
keywords: release notes #, announcements, what's new, new features
#last_updated: July 16, 2016
#summary: "Version 6.0 of the Documentation theme for Jekyll, released July 4, 2016, implements relative links so you can view the files offline or on any server without configuring urls and baseurls. Additionally, you can store pages in subdirectories. Templates for alerts and images are available."
sidebar: unity_sdk_sidebar
permalink: release_notes_050.html
folder: mydoc
---

## V0.5 (2021-03-24)

### Scripts/Tutorials
* PicoHand ExternalController added to support PicoSDK controllers
* VG_ChangeObjectJoint renamed to VG_JointChanger
* Improvements on VG_GraspHypothesizer, VG_Recorder, VG_JointChanger scripts
* Some small fixes and optimizations in VG_PostAnimator, VG_ButtonTester, VG_Snapper scripts

### Components
* VG AutoSetup also includes hand offset
* VG_Articulation API Un/Lock() functions added (to un/lock the articulation)
* Another ChangeObjectJoint() API function added that takes a VG_Articulation as input. This allows re-assigning VG_Articulations during runtime.

### Other
* Update to most recent VirtualGrasp library (0.2.9-cabvg)
* Update to CABVG 1.1.3 BakingClient
* Assured to work up to Unity version 2020.3.1f
* Objects registered with VG_Controller.RegisterObjectAtRuntime() will now also get fallback grasps if not baked
* New menu entry “Create VG Scene” to recreate a scene from exported data (in vg_tmp)
* New menu entry “Make Interactables Readable” to make all sources of objects in the scene readable
* Internal access to an articulation will relate to the first active VG_Articulation. This allows re-assigning VG_Articulations during runtime.
* .scn file will only be saved when save debug file option is enabled

