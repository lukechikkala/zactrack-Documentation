# zacTrack :: Camera
**[zacTrack Documentation](../../README.md) `>` [zacTrack with Camera](zt_Camera.md)**

<p align="center">
  <img src="/0/Camera/resources/misc_files/Logo_ZT.png" width=25% height=25%>
</p>

<p align="center">
  <img src="/0/Camera/resources/misc_files/Logo_SP.png" width=25% height=25%>
</p>


```

:!:!:!:!:!: THIS DOCUMENTATION IS INCOMPLETE AND IS IN PROGRESS :!:!:!:!:!:

```



# Index

* [Setup](#setup)


# Setup



# Introduction

Stage Precision enables interaction between various control systems using several protocols allowing the user to build unique workflows.<br>
The software requires both virtual and real world elements to create some form of interaction.<br>

The virtual elements are a set of `Objects` that can be created and only exist inside the software.<br>
These objects are then visualized (can be seen) in the *Viewport* pane of the software.<br>

The real world elements are a set of input/output connections (`IO Connections`) that are added based on either by:

- Directly selecting the relevant hardware
- Selecting a protocol that the relevant hardware uses.<br>

The first step is to add both the virtual elements and see how we can link them.<br>
Then, we add the real world elements into our software and connect them with the existing virtual elements.<br>

The rest of the document will use the following terminology for respective meaning:

- **Virtual elements** as `Objects`
- **Real world elements** as `IO Connections`

**Note**:
Take note that Stage Precision is currently in a public beta phase so, expect a few reaffirmations and reasserts in the values that we change.<br>
Stage Precision's software version used for the purposes of this documentation is:<br>
`v0.8.135`
<!-- At the time of this video, the current zacTrack Software Version is: `<<< zacTrack Version >>>` -->

## Adding and Connecting Objects
In the *Objects* pane, add **PTZ Camera** object :<br>
`Fixture → PTZ Camera`
<p align="center">
    <img src="/0/Camera/resources/0_SP_Add_PTZ_Camera.png" width=50% height=50%>
</p>

This should now add a camera object also on the *Viewport* pane.<br>
<p align="center">
  <img src="/0/Camera/resources/1_SP_ViewPortPane_Camera.png" width=50% height=50%>
</p>

Add a **Tracker** object in the *Objects* pane:<br>
`Tracked Objects → Tracker`
<p align="center">
  <img src="/0/Camera/resources/2_SP_Add_Tracker.png" width=50% height=50%>
</p>

A tracker object is now visible on the *Viewport* pane.<br>
<p align="center">
  <img src="/0/Camera/resources/3_SP_ViewPortPane_Camera.png" width=50% height=50%>
</p>

Select the objects and move them apart from each other by a few meters so they're not at the origin.<br>
To do this, select `PTZ Camera` and use the **Inspector** pane's options to adjust the position.<br>
[Video here](resources/4_SP_Move_Objects.mp4)

The `PTZ Camera`'s Pan-Tilt can be controlled in one of three ways:
<p align="center">
  <img src="/0/Camera/resources/4_SP_Camera_Control_Options.png" width=50% height=50%>
</p>

```
Static  : Camera's Pan-Tilt is in a Static Position;
          Only Zoom & Focus can be adjusted.
Target  : Camera's Pan-Tilt is referenced by a Tracker object.
PanTilt : Camera's Pan-Tilt is controlled by adjusting values.
```

Set the `Controller` of the camera to **Target**.<br>
Now, the Target has to be defined, since larger projects could potentially have several `Tracker`s that could be used for tracking several Objects.<br>
<p align="center">
  <img src="/0/Camera/resources/5_SP_Camera_Target_Selection.png" width=50% height=50%>
</p>

Now, the `Camera`'s Pan-Tilt should immediately start to point on to the Tracker.
<p align="center">
  <img src="/0/Camera/resources/6_SP_Camera_Tracker_Connected.png" width=50% height=50%>
</p>


You could now select the `Tracker` in the *Objects* pane and move it by adjusting the **Position** values.<br>
This automatically also changes the Pan-Tilt values of the camera.

## Adding and Connecting IO Connections
In the *IO Connections* pane, add **Panasonic PTZ** camera:
`PTZ Camera → Panasonic PTZ`
<p align="center">
  <img src="/0/Camera/resources/7_SP_IO_Panasonic_Camera.png" width=50% height=50%>
</p>

Stage Precision, in the current version, only supports following Panasonic models:
```
Panasonic AW-HE120
Panasonic AW-UE70
Panasonic AW-UE100
Panasonic AW-UE140
Panasonic AW-UE150
```

Note: No information about Panasonic `UE-140` has been found so far.<br>
It could be `AW-HE140`.

This documentation was tested on Panasonic `AW-UE150KE` as well as `AW-HE130KE` ( not in the above list but it is a newer version of Panasonic `AW-HE120` )

The LAN Port on the back of the camera is connected to the same switch as the PC that's running Stage Precision software which is also the same switch from which we are receiving our 
<!-- 
### B-Roll Footage

1. Panasonic AW-UE150KE // Rear Panel
2. Panasonic AW-UE150KE // Connecting Cables
3. Panasonic AW-UE150KE // Model
4. Panasonic AW-UE150KE // Front
5. Camera Tracking
6. zacTrack Server
7. Room Setup

### Random Notes

The word “Mapping” in Stage Precision refers to < X >, which is different from Routing.<br>

### Steps

1. Adding Objects
PTZ Camera
Tracker
2. Connecting Objects
3. Testing Object connections
4. Adding IO Connections
5. Connecting Objects to IO Connections
6. Placing Objects in the same position as the real world objects
7. Adding Zoom element

### ToDo

1.  Office setup diagram
2. Network setup diagram
3. Network configuration diagram
4. Audio Recordinng

### Notes

1. Ensure coordinates of both the software applications are same.<br>
2. Start ambience recording on Mac
3. The video assumes that you already have a zactrack system up and running.<br> -->
