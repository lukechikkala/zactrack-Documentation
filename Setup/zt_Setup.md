# ZacTrack System Setup

Here goes the setup for setting up zactrack server, anchors, remote, etc.

# Index
* [Requirements](#requirements)
* [Network Setup](#network-setup)
* [Mounting](#mounting)
	* [Preperation](#preparation)
	* [Adding Anchors in ZacTrack App](#adding-anchors-in-zactrack-app)
* [Calibration](#calibration)

# Requirements
```
1 x ZacTrack SMART Server running v3.19.2.0
8 x Anchors
4 x Pucks
1 x Tracker [optionally more]

1 x 10-Port PoE Network Switch
1 x  4-Port Network Switch
1 x Wi-Fi Router (or) Access Point

8 x 15m Cat5 (or above) Ethernet Cables
7 x  5m Cat5 (or above) Ethernet Cables [optionally more]
1 x Andoid Tablet or PC with 'BlueStacks 5' installed; link to 'BlueStacks 5' below
```
[Download Bluestacks](https://www.bluestacks.com/)

# Network Setup
`<network_diagram>`<br>
Download the ZacTrack App from the ZacTrack Server.


# Mounting
## Preparation

> **Note**<br>
The **MOST** ideal way of calibrating the Anchors would be to have an empty space.<br>
Once the calibration is finished, the stage elements (like props, etc.) can be filled on the stage.

1. Place 4 Anchors at 1.5 ~ 2.0 meters, assymetrically.
2. Place 4 Anchors at 3.0 ~ 4.0 meters, assymetrically.
> **Note**<br>
The anchors cannot be farther than 30 meters between each other.

3. Ensure the Anchors placed at least 0.5 meters away from any reflective surfaces (like walls, etc.).<br>
`<image_of_anchor_and_wall>`

4. Ensure that the Anchors are placed only in landscape mode; either 0° or 180° flat.<br>
`<image_of_anchor_rotation>`

5. Ensure that the Anchors are not inclined down or up.
6. Ensure that all the Anchors have line-of-sight to the pucks (we will place them in the coming steps) or trackers.
7. Switch the Pucks ON (power button at the bottom) and ensure it's blinking blue.
8. Place the 4 Pucks on the stage (~3m apart from each other) in an approximate square/rectangle shape.<br>
They do not need to be in a perfect shape.
`<picture_of_puck_placement>`
9. Ensure that the axes (X, Y & Z axis) are properly aligned.
```
	Black   : Origin
	Red     : X-Axis [Along Stage Left]
	Green   : Y-Axis [Along Up Stage]
	Blue	: Custom []
```
10. Ensure the stage is empty.

## Adding Anchors in ZacTrack App
1. Open the ZacTrack app on the Android Tablet.
2. Tap on the `⋮` on the top-right corner, followed by `New Show` and chose Empty Show.
3. Go to `Show Editor` → `Points`.
4. Ensure all 8 Anchors are detectable here.<br>
`<picture_of_ofline_anchors_vs_online_anchors>`
5. Tap & hold on one of the Anchors and select `Auto Add All`<br>
`<picture_of_Auto_add_All>`
6. Perform a `Show Upload` by clicking on the alert icon on the top-right corner of the screen and choosing `Upload to Server`.<br>
`<picture_of_show_upload>`

# Calibration
1. Go to `Show Editor` → `Points`.
2. Tap on `System Calibration`
3. Select `Reinitialize System (Auto)` → `Next`.
4. ZacTrack App will now show the 8 anchors again; to emphasize the anchors it's calibrating.
5. Tap on `Next`.
6. Ensure `Advanced Mode` is set to `No` and that the `4/4 Trackers Online` is visible next to it.
7. Tap on `Next`; here it shows a short guide of Puck placements.
8. Proceed to the last step and it should now show the following screen<br>
`<picture_of_preparing_mesh_arrangement>`
`<picture_of_preparing_mesh_arrangement>`
`<picture_of_preparing_mesh_arrangement>`
`<picture_of_calibration_finished>`
9. Proceed to the next steps only if the Calibration Result is shown as **Good**.<br>
If not, move the pucks and ensure the line-of-sight is clear and try the calibration again.

10. There should not be more than 2 attempts.<br>
If the line-of-sight is extremely clear, the system directly skips the Calibration Progress.
11. Perform `Show Upload`.
