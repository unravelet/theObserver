                   .:                     :,                                          
,:::::::: ::`      :::                   :::                                          
,:::::::: ::`      :::                   :::                                          
.,,:::,,, ::`.:,   ... .. .:,     .:. ..`... ..`   ..   .:,    .. ::  .::,     .:,`   
   ,::    :::::::  ::, :::::::  `:::::::.,:: :::  ::: .::::::  ::::: ::::::  .::::::  
   ,::    :::::::: ::, :::::::: ::::::::.,:: :::  ::: :::,:::, ::::: ::::::, :::::::: 
   ,::    :::  ::: ::, :::  :::`::.  :::.,::  ::,`::`:::   ::: :::  `::,`   :::   ::: 
   ,::    ::.  ::: ::, ::`  :::.::    ::.,::  :::::: ::::::::: ::`   :::::: ::::::::: 
   ,::    ::.  ::: ::, ::`  :::.::    ::.,::  .::::: ::::::::: ::`    ::::::::::::::: 
   ,::    ::.  ::: ::, ::`  ::: ::: `:::.,::   ::::  :::`  ,,, ::`  .::  :::.::.  ,,, 
   ,::    ::.  ::: ::, ::`  ::: ::::::::.,::   ::::   :::::::` ::`   ::::::: :::::::. 
   ,::    ::.  ::: ::, ::`  :::  :::::::`,::    ::.    :::::`  ::`   ::::::   :::::.  
                                ::,  ,::                               ``             
                                ::::::::                                              
                                 ::::::                                               
                                  `,,`


https://www.thingiverse.com/thing:3008549
USB camera mount for Raspberry Pi by costmo is licensed under the Creative Commons - Attribution license.
http://creativecommons.org/licenses/by/3.0/

# Summary

This is a way to use a USB port to mount a Raspberry Pi camera.

I have a bunch of Raspberry Pis and cameras, and finding a place to mount the camera is always a challenge. However, once the computer is setup, I never use the USB ports.

I use the linked "camera Bed mount" for my 3D printer, and it works well for that application. I use the linked "USB Cover" to cover empty USB openings and reduce the amount of dust that makes its way into the computer. I decided to cut the camera mount short and stick the USB cover on its end in OpenSCAD.

Now I have a solid camera mount that works any place I have a Raspberry Pi.

The idea is general in nature, but this specific mounting case will only work for a Raspberry Pi camera.

# Print Settings

Printer Brand: Prusa
Printer: Prusa Clone
Rafts: No
Supports: No
Resolution: 0.2
Infill: 40%

Notes: 
caseBack.stl, caseFront.stl and titlArm.stl are copied form the original camera mount files. USB_Camera_arm.stl is the remix. Print all 4 files for a complete unit.

# Post-Printing

The camera arm and mount are the best I've seen, however, the plastic pieces tend to flex over time and the camera does not easily stay in place. To remedy that issue, I put a small amount of poster tack where the tilt arm piece meets the camera mount and in the two spots where the tilt arm meets the case back piece.

# How I Designed This

I imported the two downloaded STL files into OpenSCAD, cut off the end of the mount arm, stuck the pieces together, then added a little material for strength, stability and ease of printing.