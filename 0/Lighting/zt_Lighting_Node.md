# Control using Network Node
**[zacTrack Documentation](../../README.md) `>` [zacTrack with Lighting](zt_Lighting.md) `>` [Control Using Node](Node_resources.md)**

In this setup, we will be using the node in sACN mode.<br>
This documentation assumes the system is already calibrated.<br>
To know more about System Calibration, visit [here](../Setup/zt_Setup.md/#calibration).

# Index
* [Setup](#setup)
* [Add Fixtures to zactrack](#add-fixtures-to-zactrack)
* [Teach zactrack placement of fixtures in real world](#teach-zactrack-placement-of-fixtures-in-real-world)
* [Add Actors](#add-actors)
* [Start Tracking](#start-tracking)

# Setup

![zactrack and Node.png](Node_resources/zactrack_Node.png)

# Add Fixtures to zactrack

1. Click on the `⋮` on the top-right corner, followed by `New Show` and chose Empty Show.
2. Follow the [zacTrack System Setup](../Setup/zt_Setup.md) notes to setup the system.
3. Go to `Show Editor` → `Fixture Types` and click on the green **➕ icon.**
4. Here, zacTrack shows a list of built-in Fixtures.<br>
Choose one from here or create a new custom fixture type by following the [Fixture Builder guide](../Setup/zt_Fixture_Builder_Guide.md).
5. Perform a `Show Upload` by clicking on the alert icon on the top-right corner of the screen and choosing `Upload to Server`.
6. Then, head over to `Show Editor` → `Fixtures` and add the fixture you added into the show by clicking on the green plus icon [**➕**].<br>
<p align="center">
    <img src="Node_resources/Fixtures.png" width=50% height=50%>
</p>

7. Click on `Fixture Type` and choose the fixture you added.
8. Set `Out Universe` to `OUT 1` and click on `OK`.
9. Perform `Show Upload`.
10. In `Show Editor` → `Fixtures`, select the target icon (under `CP/AF` column) next to fixture to check whether the fixture itself is controllable from zactrack.
11. This will popup a window showing the basic fixture controls like `Dimmer`, `Iris`, `Focus`, `Zoom`, `Pan` & `Tilt`, where it allows you to manually control the fixture for testing purposes.<br>
To check the fixture, ensure `Highlight Base Channels` is enabled.

# Teach zactrack placement of fixtures in real world

1. Once the fixture control is working manually, close the popup and head over to `Show Editor` → `Fixtures` and click on `Alignment Wizard`.
2. Select fixtures that we are you want to align and press `Next`.<br>
<p align="center">
    <img src="Node_resources/Untitled.png" width=50%>
</p>

3. Ensure Use `Console for Centering` and `Advanced Mode` are both set to `no` and click `Next`.<br>
<p align="center">
    <img src="Node_resources/Untitled%201.png" width=50%>
</p>

4. Ensure `Highlight` is toggled on.<br>
<p align="center">
    <img src="Node_resources/Fixture_Alignment.png" width=50%>
</p>

5. Set `Dimmer` to `255` and use the Track Pad to point the fixture at Black Puck.<br>
It doesn’t have to be in the center but as long as the beam is fairly falling on the black puck, it will be fine.<br>
See below pictures for reference.<br>
<p align="center">
    <img src="Node_resources/Fixture_Alignment_Puck__Fixture.jpeg" width=42% height=42%>
    <img src="Node_resources/Fixture_Alignment_Puck__Fixture_2.jpeg" width=35% height=35%>
</p>

6. We then click on `Next` to continue to do the same for Red, Green & Blue pucks.
7. At the end, zactrack will now start the refinement process trying to find the center of the beam.<br>
   This will help zactrack to figure out where the fixture is in the 3D space.<br>
   During the Refinement Process, it is also possible to adjust the `Resolution`, the default for which is `8 Ticks`.<br>
   The lower the ticks, the more time it takes to Refine but gives a much more precise location of the fixture in the 3D space.<br>
   <p align="center">
       <img src="Node_resources/Untitled%202.png" width=50% height=50%>
    </p>
8. Once the Refinement Process is finished, you would see a screen like this:<br>
<p align="center">
    <img src="Node_resources/Untitled%203.png" width=50% height=50%>
</p>

9. Perform `Show Upload`.

# Add Actors

1. We now need to add the Trackers by going to `Show Editor` → `Actor`.
2. Dismount one of the Trackers from the Charging Station and it will show up in the `Actor` window.<br>
This might take a second or two.
3. Once the Tracker shows up, press and hold on the shown Tracker and select `Auto Add`.<br>
<p align="center">
    <img src="Node_resources/Adding_Actor.png" width=75% height=50%>
</p>

4. The name of the `Tracker xxxxxx` now changes to `Actor 01`.
5. Perform `Show Upload`.

# Start Tracking
1. Go to `Live`, select your Fixture, disable `Console` next to `Assignment` option and set `Assignment` to `Actor 01 (1)`.
2. To switch on the Dimmer, set the `Base Channel Values` from `Console` to `Highlight`.