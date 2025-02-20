# ReversePrint

### GUI library: [imgui](https://pyimgui.readthedocs.io/en/latest/)

This began as an experiment to play around with images in python,
load and display them on the fly in as low-level as possible.

Now that's achieved, I am focusing on creating an auto-masking/color isolation technique
which can cleanly separate an 'additive print' artwork into its original parts.
Examples: Japanese woodblock prints, screen prints.

Check out the algo in the code, it is 'decent' so far but has some fragmentation.
At some point I may write up a proper explanation.
I can't for the life of me pick a good name.


## Features:

### filesystem:
- file browsing window
- image preview/selection window

### 2D graphics manipulation:
- combine .png images with/without transparency
- Creating color masks from images
- Colorpicker over images
- Feature Detection for training, etc. (OpenCV Sift)

### 3D graphics:
- generate .obj files from 2D Feature sets (*very* experimental)