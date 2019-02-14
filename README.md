# Web-based 3D printing for kids
a Web-based app that let's kids easily do 3D printing. The project is broken down into a number of pieces.


## blender
This part shows how blender can be spawned as a subprocess from a Python script and then have a python script executed
within the blender environment which can then combine different objects and export to an STL file format for slicing 
and printing.

## octo
This folder contains a script that has a collection of functions that can connect to the RESTful JSON web services and
can delete files, upload files, print files.


## preview
This folder contains a demo for a wolf shaped 3d object in the STL file wolf.stl that is rendered using the Three.js
library in the web-broswer with an interactive control that let's the user rotate and zoom in and out of the model.


