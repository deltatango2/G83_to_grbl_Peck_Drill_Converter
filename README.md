# G83_to_grbl_Peck_Drill_Converter
Python script to convert G83 commands to grbl compatible instructions 

This is a script to convert G83 gcode instructions to Gcode compatible with the grbl machine controller.  I used this code
successfully with my X-Carve.

The code uses the Tkinter library to allow GUI selection of the input file.  If Tkinter isn't avaialble on your machine, simply hardcode the input file path into the variable, "file_path".

The output file will be named "file_path"_4grbl.nc


