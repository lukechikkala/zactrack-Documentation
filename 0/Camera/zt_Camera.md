# zacTrack :: Camera
**[zacTrack Documentation](../../README.md) `>` [zacTrack with Camera](zt_Camera.md)**

![Untitled](resources/Untitled.png)

![Picture1.png](resources/Picture1.png)

# Introduction

Stage Precision enables interaction between various control systems using several protocols allowing the user to build unique workflows.
The software requires both virtual and real world elements to create some form of interaction.

The virtual elements are a set of `Objects` that can be created and only exist inside the software.
These objects are then visualized (can be seen) in the *Viewport* pane of the software.

The real world elements are a set of input/output connections (`IO Connections`) that are added based on either by:

- Directly selecting the relevant hardware
- Selecting a protocol that the relevant hardware uses.

The first step is to add both the virtual elements and see how we can link them.
Then, we add the real world elements into our software and connect them with the existing virtual elements.

For the rest of the video I will switch the terminology for:

- Virtual elements as `Objects`
- Real world elements as `IO Connections`

**Note**:
Take note that Stage Precision is currently in a public beta phase so, expect a few reaffirmations and reasserts in the values that we change.
At the time of this video, the current zacTrack Software Version is: `<<< zacTrack Version >>>`
And Stage Precision's software version is: `<<< Stage Precision Version >>>`

## Adding and Connecting Objects

Add a **PTZ Camera** object in the *Objects pane*:
`Fixture → PTZ Camera`
This should now add a camera object also on the *Viewport* pane.

Add a **Tracker** object in the *Objects* pane:
`Tracked Objects → Tracker`
Again, a tracker object is now visible on the *Viewport* pane.

Let's try to move both the objects apart from each other so we can see them with better clarity.
Now let's set the PTZ Camera's control to this Tracker that we added.

The control of the PTZ Camera can either be:

- **Static**: Meaning we move it using the values or by mouse in the *Viewport* pane.
- **Target**: So we could assign it's control to another **Object**.
- **PanTilt**: `<<< Insight Needed >>>`

Let's set the Control of the camera to **Target**.
And now we have to set what's the target that we want it to follow.
This can be done under the **Target** settings.
And now as you see, the camera just follows where ever I move the tracker.

Now, we just need to connect the real world PTZ Camera & Tracker to our virtual objects which are working perfectly.

## Adding and Connecting IO Connections

Right-click in the *IO Connections* pane and let's add the PTZ Camera first.
`PTZ Camera → Panasonic PTZ`
The model of Panasonic camera we have here is: Panasonic AW-UE150KE.

The LAN Port on the back of the camera is connected to the same switch as the PC that's running Stage Precision software which is also the same switch from which we are receiving our 

### B-Roll Footage

1. Panasonic AW-UE150KE // Rear Panel
2. Panasonic AW-UE150KE // Connecting Cables
3. Panasonic AW-UE150KE // Model
4. Panasonic AW-UE150KE // Front
5. Camera Tracking
6. zacTrack Server
7. Room Setup

### Random Notes

The word “Mapping” in Stage Precision refers to < X >, which is different from Routing.

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

1. Ensure coordinates of both the software applications are same.
2. Start ambience recording on Mac
3. The video assumes that you already have a zactrack system up and running.
