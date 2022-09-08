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


