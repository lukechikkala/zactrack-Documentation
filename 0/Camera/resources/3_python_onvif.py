# Author	: Luke Chikkala
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ Derivatives ]-----------------------------------------------------------------------------------------------------------------------------------
from onvif import ONVIFCamera
import os
from time import sleep
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ Camera Setup ]----------------------------------------------------------------------------------------------------------------------------------
IP_Address						= "192.168.1.100"
Port							= 2000
UserName						= "admin"
Password						= "BAMK"
Location						= "C:/Users/Chikkala/Documents/Software/onvif/python-onvif-zeep-zeep/python-onvif-zeep-zeep/wsdl"
LC_Cam							= ONVIFCamera(
												IP_Address,
												Port,
												UserName,
												Password,
												Location
											 )
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ PTZ Algorithm ]---------------------------------------------------------------------------------------------------------------------------------
XMAX							=  1
XMIN							= -1
YMAX							=  1
YMIN							= -1
moverequest						=  None
ptz								=  None
active							=  False

# ----------------------------------------------------------------------------------------------------------------------------------------------------
def do_move(ptz, request):
	# Start continuous move
	global active
	if active:
		ptz.Stop({'ProfileToken': request.ProfileToken})
	active						= True
	ptz.ContinuousMove(request)

def move_up(ptz, request):
	print ('moving up...')
	request.Velocity.PanTilt.x	= 0
	request.Velocity.PanTilt.y	= YMAX
	do_move(ptz, request)

def follow_zt(ptz, request):
	x_zt_raw = float(op('math1')['tracker_0:tx'])
#	x_zt = round(x_zt_raw, 1)
	x_zt = 1
	print ( "Attempting to follow zactrack..." )
	print ( "--------------------------------" )
	if x_zt > 0 and x_zt < 1:
		request.Velocity.PanTilt.x	= x_zt
		do_move(ptz, request)
		print(x_zt)
	else:
		print( "Tracker is not within the range" )
		print(x_zt)
		print ( "--------------------------------" )

def move_down(ptz, request):
	print ('moving down...')
	request.Velocity.PanTilt.x	= 0
	request.Velocity.PanTilt.y	= YMIN
	do_move(ptz, request)

def move_right(ptz, request):
	print ('moving right...')
	request.Velocity.PanTilt.x	= XMAX
	request.Velocity.PanTilt.y	= 0
	do_move(ptz, request)

def move_left(ptz, request):
	print ('moving left...')
	request.Velocity.PanTilt.x	= XMIN
	request.Velocity.PanTilt.y	= 0
	do_move(ptz, request)

def move_upleft(ptz, request):
	print ('move uing left...')
	request.Velocity.PanTilt.x	= XMIN
	request.Velocity.PanTilt.y	= YMAX
	do_move(ptz, request)

def move_upright(ptz, request):
	print ('move uing left...')
	request.Velocity.PanTilt.x	= XMAX
	request.Velocity.PanTilt.y	= YMAX
	do_move(ptz, request)

def move_downleft(ptz, request):
	print ('move dowing left...')
	request.Velocity.PanTilt.x	= XMIN
	request.Velocity.PanTilt.y	= YMIN
	do_move(ptz, request)

def move_downright(ptz, request):
	print ('move dowing left...')
	request.Velocity.PanTilt.x	= XMAX
	request.Velocity.PanTilt.y	= YMIN
	do_move(ptz, request)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ Device ]----------------------------------------------------------------------------------------------------------------------------------------
Device							= LC_Cam.devicemgmt.GetHostname()
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ PTZ ]-------------------------------------------------------------------------------------------------------------------------------------------
Media							= LC_Cam.create_media_service()
Media_Profile					= Media.GetProfiles()[0]
PTZ								= LC_Cam.create_ptz_service()
Request_LC						= PTZ.create_type('GetConfigurationOptions')
Request_LC.ConfigurationToken	= Media_Profile.PTZConfiguration.token
PTZ_Config_Options				= PTZ.GetConfigurationOptions(Request_LC)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ X ]-----------------------------------------------------------------------------------------------
X_Max							= PTZ_Config_Options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
X_Min							= PTZ_Config_Options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
# --[ Y ]-----------------------------------------------------------------------------------------------
Y_Max							= PTZ_Config_Options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
Y_Min							= PTZ_Config_Options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# --[ Movements ]-------------------------------------------------------------------------------------------------------------------------------------
MoveRequest						= PTZ.create_type('ContinuousMove')
MoveRequest.ProfileToken		= Media_Profile.token
if MoveRequest.Velocity is None:
	MoveRequest.Velocity = PTZ.GetStatus({'ProfileToken': Media_Profile.token}).Position
# ----------------------------------------------------------------------------------------------------------------------------------------------------

clear()

# --[ Final Commands ]--------------------------------------------------------------------------------------------------------------------------------
# move_up(PTZ, MoveRequest)
# move_down(PTZ, MoveRequest)
# move_right(PTZ, MoveRequest)
# move_left(PTZ, MoveRequest)
# move_upleft(PTZ, MoveRequest)
# move_upright(PTZ, MoveRequest)
# move_downleft(PTZ, MoveRequest)
# move_downright(PTZ, MoveRequest)
# ----------------------------------------------------------------------------------------------------------------------------------------------------
follow_zt(PTZ, MoveRequest)
# ----------------------------------------------------------------------------------------------------------------------------------------------------
