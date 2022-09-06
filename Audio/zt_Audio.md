# zactrack :: Audio
**[zacTrack Documentation](../README.md) `>` [zacTrack with Audio](zt_Audio.md)**

# Index
* [Introduction](#introduction)
* [Software Versions](#software-versions)
* [Requirements](#requirements)
* [TouchDesigner Setup](#touchdesigner-setup)

# Introduction

TouchDesigner is a node-based software that allows for creating some interaction between several protocols. It is mainly used for visual interactions but in our case we are going to use it to get the XYZ data provided by zactrack over PSN to modify the PAN & Volume.

# Software Versions
```
• zactrack      | 'v3.19.3.0'
• TouchDesigner | 'v2022.26590'
• Windows 10    | '21H1, Build: 19043.1889'
• macOS         | <macos_version>
```

# Requirements
1. zactrack System
2. PC or Mac running [TouchDesigner](https://derivative.ca/UserGuide/Install_TouchDesigner).
3. Stereo System

# TouchDesigner Setup
If you are using a TouchDesigner `v2022.26590` or older, please follow the guide [here](TouchDesigner_Setup_v2022.26590.md) to do the initial setup.
3. Now, we open TouchDesigner
It comes with some existing nodes, but we take a new file.
4. `File` → `New`
The application will restart and we will have a new project.
5. We will first need to ensure that the Audio is being routed through TouchDesigner.
Usually, the Audio Routing in our PC is something like this:
<p align="center">
    <img src="resources/2_Audio_Routing_Default.png" width=50% height=50%>
</p><br>
We now need to route it via TouchDesigner and it would look something like this:<br>
<p align="center">
    <img src="resources/3_Audio_Routing_TD.png" width=50% height=50%>
</p>

6. To achieve this, we will now add a new operator (aka ‘node’) either by double-clicking or by hitting `Tab` on the keyboard or by right-clicking on the empty grid area (we call this area as Network Editor) and selecting `Add Operator`.
7. Head over to the `CHOP` tab and select `PosiStageNet`.
<p align="center">
    <img src="resources/0_Chop_PSN.png" width=50% height=50%>
</p><br>
It should look something like this:
<p align="center">
    <img src="resources/Untitled.png" width=50% height=50%>
</p>

8. Select the PosiStageNet node and in the `Properties` pane of the node, ensure you have the following options set.
<p align="center">
    <img src="resources/Untitled%201.png" width=50% height=50%>
</p>