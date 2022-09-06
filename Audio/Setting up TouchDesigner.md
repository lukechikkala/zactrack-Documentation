# Install Anaconda

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
1. Add `Execute DAT` and edit the script.
2. Change `username`'s value to the username on your PC.
3. Change `envrname`'s value to the name you assigned when creating your python environment.

> Execute DAT's Script
```python
# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

import sys
import os

def onStart():
	username = 'Chikkala'
	envrname = 'TD_Onvif_LC'
	os.environ['PATH'] += os.pathsep + f'C:\\Users\\{username}\\anaconda3\\envs\\{envrname}\\DLLs'
	os.environ['PATH'] += os.pathsep + f'C:\\Users\\{username}\\anaconda3\\envs\\{envrname}\\Library\\bin'

	sys.path = [f'C:\\Users\\{username}\\anaconda3\\envs\\{envrname}\\Lib\\site-packages'] + sys.path
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return
```

