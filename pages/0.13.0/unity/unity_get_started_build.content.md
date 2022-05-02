### Building an APK for Android

For Android, VirtualGrasp only supports 64 bit. 

You therefore have to ensure that you use **IL2CPP** as Scripting Backend and **ARM64** as Target Architecture in your Build Settings, see image below:

{% include image.html file="unity/unity_build_settings.png" alt="VG Build Settings" caption="Ensure that build settings are configured for 64 bit on Android." %}