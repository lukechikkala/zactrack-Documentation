# Install Anaconda
> IMPORTANT NOTE:<br>
**This document is under development and is currently handled as research notes.**<br>
**Do not execute these commands to deploy these processes unless you are aware of them.**
___
___
___
___
___


## Quick Anaconda Steps
List all the python environments:
```python
conda env list
```
Create new anaconda environment(python version is found in TD):
```python
conda create -n TD_Onvif_LC python=3.9.5
```
Activate the environment
```python
conda activate TD_Onvif_LC
```
See list of installed packages
```python
conda list
```
Install onvif_zeep
```python
pip install onvif_zeep
```
Check whether onvif_zeep is installed using `conda list`.
Installing onvif_zeep will install following additional packages:
```
	# Name				Version		Build		Channel
	attrs				22.1.0		pypi_0		pypi
	cached-property		1.5.2		pypi_0		pypi
	charset-normalizer	2.1.1		pypi_0		pypi
	idna				3.3			pypi_0		pypi
	isodate				0.6.1		pypi_0		pypi
	lxml				4.9.1		pypi_0		pypi
	onvif-zeep			0.2.12		pypi_0		pypi
	platformdirs		2.5.2		pypi_0		pypi
	pytz				2022.2.1	pypi_0		pypi
	requests			2.28.1		pypi_0		pypi
	requests-file		1.5.1		pypi_0		pypi
	requests-toolbelt	0.9.1		pypi_0		pypi
	six					1.16.0		pypi_0		pypi
	urllib3				1.26.12		pypi_0		pypi
	zeep				4.1.0		pypi_0		pypi
```

# TouchDesigner Setup
1. Add `Execute DAT` and add the script from [`1_setup_python_variables.py`](./resources/1_setup_python_variables.py).
2. Change `username`'s value to the username on your PC.
3. Change `envrname`'s value to the name you assigned when creating your python environment.
4. Create a `Text DAT` and add the script from [`3_python_onvif.py`](./resources/3_python_onvif.py)

# TouchDesigner `Video Stream In` Setup
Default Address in TouchDesigner's `Video Stream In` TOP:
```
rtsp://127.0.0.1:554/tdvidstream
```
Address to access live stream as acquired from **Onvif Device Manager**: 
```
rtsp://192.168.1.100:554/live0&t=unicast&p=rtsp&ve=H264&w=1920&h=1080&ae=G711A&sr=8000
```
Since Bolin's camera requires login credentials to access the camera, insert `<username>` and `<password>` within the address itself:
```
rtsp://<username>:<password>@192.168.1.100:554/live0
```
For example:
```
rtsp://admin:BAMK@192.168.1.100:554/live0
```

## Bolin's Open Ports
```
   21  ftp         : listening
   23  telnet      : listening
   80  http        : listening
  554  rtsp        : listening
 2000  cisco-sccp  : listening
36666              : listening
36667              : listening
```
### Port 80 Errors
```
zeep.exceptions.Fault: Unknown fault occured
onvif.exceptions.ONVIFError: Unknown error: Unknown fault occured
```
### Port 554 Errors Summary
```
----------------------------------------------------------------------------------------------------------------------------------------------
	CODE
----------------------------------------------------------------------------------------------------------------------------------------------
http.client.RemoteDisconnected: Remote end closed connection without response
----------------------------------------------------------------------------------------------------------------------------------------------
	CODE
----------------------------------------------------------------------------------------------------------------------------------------------
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
onvif.exceptions.ONVIFError: Unknown error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

```
### Port 2000
Port 2000 seems to be responding to python onvif scripts.
```
My Camera's Hostname: Bolin 4K PTZ Cam 2
```

Stop
Left
Right
Up
Down
LeftUp
LeftDown
RightUp
RightDown