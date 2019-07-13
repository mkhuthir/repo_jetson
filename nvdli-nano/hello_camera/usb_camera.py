#!/usr/bin/python3

from jetcam.usb_camera import USBCamera

#TODO change capture_device if incorrect for your system
camera = USBCamera( width=224, 
                    height=224, 
                    capture_width=640, 
                    capture_height=480, 
                    capture_device=0)

image = camera.read()

print(image.shape)
print(camera.value.shape)
