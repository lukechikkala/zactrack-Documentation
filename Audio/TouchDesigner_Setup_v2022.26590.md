# TouchDesigner Initial Setup for `v2022.26590`

In TouchDesigner `v2022.26590`, it is not possible to select a specific Network Adapter of your PC to choose to listen for PSN traffic in TouchDesigner.<br>
However, the developers of TouchDesigner have changed this in `v2022.28040`.<br>
If you are still using TouchDesigner `v2022.26590` or below, you will need to disable all network adaptors except the one you are expecting the PSN traffic from.

## On Windows
1. Open `Network Connections` by clicking on Start (Windows Icon) and type `View Network Connections`.
<p align="center">
    <img src="resources/View_Network_Connections.png" width=50% height=50%>
</p>

2. Select the network interface that is not expected to receive PSN traffic, right-click and choose `Disable`.<br>
Do this for all the network interfaces except for the one that is expected to receive PSN traffic.


# Resources

- [x] [TD Forum Post](resources/PSN_CHOP_Interface_dev_comment.png).
- [ ] [Link to Touch Designer Forum](https://forum.derivative.ca/t/posinet-chop-artnet-cant-receive-data-simultaneous/150683/9?u=lukechikkala)