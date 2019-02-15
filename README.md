# Web-based 3D printing for kids
A Web-based app that let's kids easily do 3D printing. This project is made up of a number of different parts:






## blender
The combine.py script will spawn a subprocess with blender that will combine three different STL files by importing
them and then exporting all the combined objects into one final STL file. This is how the head, body and legs of a 
chosen model will be combined into one. To run the script create the path /opt/kids3d/ and copy all files in the
assets folder into that path. Below is a screenshot of a STL file created using this code.

![merged model](https://user-images.githubusercontent.com/3801994/52886447-59e37100-3185-11e9-9a29-ffdea69378ae.png)

## octo
This folder contains a script that has a collection of functions that can connect to the RESTful JSON web services and
can delete files, upload files, print files. Below is a photo of a model printed using this code.
![printed model](https://user-images.githubusercontent.com/3801994/52886296-ef323580-3184-11e9-90d9-ae85d9a63b76.png)


## preview
This folder contains the html and javascript code to that will render the dog_wing_octo.stl file which is a 3D model 
of a creature with a dogs head, wings and octopus legs. The file is rendered using the Three.js
library in the web-broswer with an interactive control that let's the user rotate and zoom in and out of the model. A 
[live demo](https://marwano.github.io/3d/) is available.



