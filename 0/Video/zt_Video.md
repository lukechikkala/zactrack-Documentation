# zactrack :: Video
**[zacTrack Documentation](../../README.md) `>` [zacTrack with Video](zt_Video.md)**

<!-------------------------------------------------------------------------------------->

# Index
* [Introduction](#introduction)
* [Goal](#goal)
* [Requirements](#requirements)
* [Software Versions](#software-versions)
* [zactrack PSN [PosiStageNet] Setup](#zactrack-psn-posistagenet-setup)
* [TouchDesigner Setup](#touchdesigner-setup)
	* [PSN Setup](#psn-setup)
	* [Video Setup](#video-setup)
	<!-- * [Connecting Audio & PSN](#connecting-audio--psn) -->

<!-------------------------------------------------------------------------------------->

# Introduction

TouchDesigner is a node-based software that allows for creating some interaction between several protocols.<br>
It is mainly used for visual interactions but in our case we are going to use it to get the XYZ data provided by zactrack over PSN to modify the position of some video elements.<br>

<!-------------------------------------------------------------------------------------->

# Goal
The idea is to project some text on the screen and move the text left/right/up/down based on zactrack's tracker position.

<!-------------------------------------------------------------------------------------->

# Requirements
1. zactrack System
2. PC or Mac running [TouchDesigner](https://derivative.ca/UserGuide/Install_TouchDesigner).

<!-------------------------------------------------------------------------------------->

# Software Versions
```
• zactrack      | v3.19.3.0
• TouchDesigner | v2022.28040
• Windows 10    | 21H1, Build: 19043.1889
• macOS         | <macos_version>
```

<!-------------------------------------------------------------------------------------->

# zactrack PSN [PosiStageNet] Setup
This documentation assumes the system is already calibrated.<br>
To know more about System Calibration, visit [here](../Setup/zt_Setup.md/#calibration).

1. Ensure atleast one Actor/Tracker is added.
2. Go to `Show Editor` → `Fixture Types`.
3. Click on green plus icon [**➕**].
4. Go to `Other Protocols` tab and select `PosiStageNet (PSN)`.
<p align="center">
	<img src="resources/7_zt_Add_PSN.png" width=50% height=50%>
</p>

5. Go to `Show Editor` → `Fixtures`.
6. Click on green plus icon [**➕**].
7. Click on `Fixture Type` and choose `PosiStageNet (PSN)`.
<p align="center">
	<img src="resources/8_zt_Add_PSN_Fixture.png" width=50% height=50%>
</p>

8. Perform a `Show Upload` by clicking on the alert icon on the top-right corner of the screen and choosing `Upload to Server`.
9. Go to `Live` → `Fixtures` → `PosiStageNet(PSN)`.
<p align="center">
	<img src="resources/9_zt_Assign_0.png" width=50% height=50%>
</p>

10. Uncheck `Console`, select `Assignment` and choose one of the Actors you added.
<p align="center">
	<img src="resources/10_zt_Assign_1.png" width=50% height=50%>
</p>

<!-------------------------------------------------------------------------------------->

# TouchDesigner Setup
1. Open TouchDesigner.<br>
It comes with some existing nodes, but we take a new file.
2. `File` → `New`<br>
The application will restart and we will have a new project.

<!-------------------------------------------------------------------------------------->

## PSN Setup
1. On this blank slate, we will now add a new operator (aka 'node') by:<br>
double-clicking on the empty grid area (we call this area as *Network Editor*)<br>
or<br>
hit `Tab` on the keyboard<br>
or<br>
right-click and and select `Add Operator`.<br>
Add a `PosiStageNet`
<p align="center">
	<img src="resources/6_PSN_CHOP.png" width=50% height=50%>
</p><br>
<p align="center">
	<img src="resources/Untitled.png" width=50% height=50%>
</p>

2. In the `Parameters` window of the `PosiStageNet`, select the `Local Address` to any of the IP Addresses that belong to the network interface that is receiving PSN traffic.<br>
It does not matter which IP Address (in case you have multiple IP Addresses assigned) as PSN is a multicast traffic.<br>
As long as you have the IP Address belonging to the interface is selected, it will work.
<p align="center">
	<img src="resources/PSN_Set_Interface.png" width=50% height=50%>
</p>

3. You should now immediately see the tracker information in the `PosiStageNet`.
<p align="center">
	<img src="resources/PSN_Incoming.gif" width=50% height=50%>
</p>

4. When there is only one tracker, you should see 9 channels as in the picture above.<br>
On the right half of the `PosiStageNet`, you will find the channel ID and on the left, the value of relevant channel.<br>
The channels are as below:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃          Channel         ┃ TouchDesigner ID  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Total Amount of Trackers ┃ total_trackers    ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's ID           ┃ tracker_0:id      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Status       ┃ tracker_0:tracked ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Position X   ┃ tracker_0:tx      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Position Y   ┃ tracker_0:ty      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Position Z   ┃ tracker_0:tz      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Rotation X   ┃ tracker_0:rx      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Rotation Y   ┃ tracker_0:ry      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ Tracker-1's Rotation Z   ┃ tracker_0:rz      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛
```
As new trackers are added, 8 additional channels per tracker will be shown in the `PosiStageNet`.

5. We are only interested in the the tracker's `X` & `Y` position; in the TouchDesigner's language,<br>
`tracker_0:tx`<br>
`tracker_0:ty`

<!-------------------------------------------------------------------------------------->

## Video Setup
1. We will now add a new `Top` operator called `Text`
<p align="center">
	<img src="resources/0_Text_CHOP.png" width=50% height=50%>
</p>

2. In the Properties window of the `Text` operator, under `Text` tab change the `Text` parameter to your desired text<br>
( that's a lot of texts ;) )
<p align="center">
	<img src="resources/0_Text_CHOP_Text.png" width=50% height=50%>
</p>

3. In the `Font` tab of the `Text` operator Properties window, we have 2 `Position` parameters.
<p align="center">
	<img src="resources/0_Text_CHOP_Pos.png" width=50% height=50%>
</p>

4. Adjusting these parameters we can find the border to which our text should reach.
<br>
In the example here, the limits are:<br>
X: -30 to 30<br>
Y: -100 to 100<br>
<p align="center">
	<img src="resources/0_Text_CHOP_Text_Limits.png" width=50% height=50%>
</p>

5. It is important to acknowledge these limits as the limits of `X` & `Y` from zactrack ( in theory, our stage ) will be different as they are real world values.

6. You will need to find the limits of the real world stage by placing the tracker at the extreme stage left, stage right, down stage and upstage locations.<br>
In general, we note the values of `X` when the tracker is placed at the extreme stage left and then at extreme stage right.<br>
And then we use the `Y` values as extreme downstage and upstage values.

7. As these real world limits are different from the `Text` operator's `Position` limits, we will need normalize them; We will do this with the help of `Math` `CHOP` operator.<br>

<p align="center">
	<img src="resources/Math_CHOP_Find.png" width=35% height=50%>&nbsp;&nbsp;&nbsp;&nbsp;
	<img src="resources/Math_CHOP.png" width=25% height=50%>
</p>

8. We now connect the `PosiStateNet`'s output to the `Math`.
<p align="center">
	<img src="resources/PSN_to_Math.gif" width=100%>
</p>

9. In the `Math`'s, `Parameters` window, click on `Range`.<br>
`From Range`, is for the input's values, for zactrack's PSN's range.<br>
`To Range` is for the output's values, for `Text` TOP's `Position` `X` range.

10. We repeat step-8 & step-9 also for `Position` `Y`.

<!-- 10. Place the Actor on the extreme left of your space/stage and take note of the `tracker_0:tx`'s value **from the `PosiStageNet`'s `CHOP`**.<br>
In our testing space the value of the tracker in the extreme left corner is roughly aroung `2.8`.
<p align="center">
	<img src="resources/PSN_Left.png">
</p>

5. Now, place the Actor on the extreme right of your space/stage and take note of the `tracker_0:tx`'s value, once again, **from the `PosiStageNet`'s `CHOP`**.<br>
In our testing space the value of the tracker in the extreme right corner is roughly aroung `0.2`.
<p align="center">
	<img src="resources/PSN_Right.png">
</p>

6. We now need to enter these values (`2.8` & `0.2`, in our test setup's case) in the `Math`'s `From Range` parameters.
<p align="center">
	<img src="resources/Math_CHOP_Range.png" width=50% height=50%>
</p>

7. You can now move the tracker from left to right and see that the `Math`'s `tracker_0:tx` value only go from 0 to 1.<br>
This is now ideal for influencing the `Pan` parameter of the `Audio Device Out`.

8. To do this, set the `Math` in `Viewer Active` state by clicking on the **➕** icon at the bottom-right.<br>
This allows us to interact wiht the channels directly.
<p align="center">
	<img src="resources/Math_CHOP_Viewer_Active.png" width=50% height=50%>
</p>

9. We should now be able to click and hold on the `tracker_0:tx` channel in `Math` and drag it (don't release the mouse yet) over `Audio Device Out`, wait till `Parameter` window switch to `Audio Device Out`'s parameters.<br>
Once the `Parameter` window is set to `Audio Device Out`, drop it on the `Pan` parameter and choose `Export CHOP Reference`.
<p align="center">
	<img src="resources/CHOP Reference.gif">
</p> -->

Now, as the Actor is moving across the stage, you can see the Text move based on the position of the Actor.