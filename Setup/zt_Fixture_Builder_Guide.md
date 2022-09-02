# Fixture Builder Guide

zactrack uses `.ztft` filetype for it's native fixtre types.<br>
From zactrack `v3.19.3.0` [zactrack Client `v7.6.0`], it allows to import `GDTF` fixture types.<br>
zactrack can export to 2 different filetypes:
	* zactrack Native
	* zactrack Fixture Type

> **Note:**<br>
It is possible to access & create fixture types from the Android/Bluestacks app even if the server is not connected.<br>
For a full list of possibilities without the need of server, visit [here](zt_Serverless_Connection.md)

On Bluestacks, files are exported to:<br>
```
/storage/emulated/0/Zactrack/FixtureTypes
```

# Creating a Custom Fixture
Before we being building our custom fixture type, take a look at your fixture's DMX Data Sheet and pull apart the following information:
```
1. Name
2. Number of DMX Channels
3. DMX Channel Numbers, Physical Ranges(min. & max.):
	Pan
	Tilt
	Dimmer
	Zoom
	Focus
	Iris
```
To make it easier, [here](https://docs.google.com/spreadsheets/d/1BaPLQeKCo2O8mKZ4Hm6NT0wqThhCdQiBgi9dSIflqUc/edit?usp=sharing) is a google sheet that helps to summarize your information into the information that zactrack needs.

Enter the 