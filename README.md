# SSAD Team 35

## Team Members

- Rohan Chacko
- AadilMehdi Sanchawala
- Priyank Modi
- Antony Martin

## Problem Statement:

- To detect and track objects in a 2D video using their corresponding 3D mesh models. To detect organs and operation instruments during surgery and keeping an inventory of the same.

## Directory Structure
```bash
.
├── data
│   ├── heart
│   │   ├── mesh
│   │   │   └── meshmodel
│   │   ├── templates
│   │   │   ├── heart_<templatenumber>
│   │   └── training_video
│   │       ├── heart_videonumber
│   └── syringe
│       ├── templates
│       │   ├── syringe_<templatenumber>
│       ├── training_video
│       │   ├── syringe_body_<videonumber>
│       ├── test_logging.mp4
│       └── test_video.mp4
├── document
│   ├── milestone.odt
│   ├── Presenation draft
│   ├── Product Design.pdf
│   ├── Project Synopsis.jpg
│   ├── R2 presentation
│   ├── ReleaseThemesInitiatives.xlsx
│   ├── Requirements.docx
│   ├── StatusTracker_1.xlsx
│   ├── Test_Planner_and_Tracker.xlsx
│   └── UML diagrams
│       ├── UMLDiagram1.jpeg
│       ├── UMLDiagram2.jpeg
│       ├── UMLDiagram3.jpeg
│       └── UMLDiagram4.jpeg
├── meeting_minutes
│   ├── Client
│   │   ├── 11_08.md
│   │   ├── 25_10.md
│   │   ├── 26_08.md
│   │   └── 29_09.md
│   ├── TA
│   │   ├── 07_08.md
│   │   └── 24_08.md
│   └── Team
│       ├── 01_10.md
│       ├── 11_09.md
│       ├── 19_08.md
│       ├── 19_09.md
│       ├── 02_11.md
│       └── 27_10.md
├── README.md
└── src
    ├── check.py
    ├── Config.py
    ├── detector.py
    ├── Item.py
    ├── main.py
    ├── requirements.txt
    ├── template_generator.py
    ├── tests
    │   ├── test_logging.py
    │   ├── test_template_generator.py
    │   ├── test_tracking.py
    │   ├── test_videostream_reception.py
    │   └── test_video_utilities.py
    ├── utilities.py
    ├── video_utils.py
    ├── video_writer.py
    └── window.py
```
### Modules

`main.py` - Main file which runs the whole software  
`Config.py` - Global constants declaration  
`Item.py` - Contains classes for all models  
`template_generator.py` - Generates edge templates based on video of edge template  
`detector.py` - Declares the detector class which contains the matching algorithm for the software  
`utilities.py` - Used for printing progress bars to provide a better UI  
`video_utils.py` - Contains functions to change the resolution of the video  
`video_writer.py` - Writes the output video  
`window.py` - Defines the specifications and design of the bounding box

## Install prerequisites

`pip3 install -r requirements.txt`

## Generating edge templates from mesh models

`python3 template_generator.py -tv <path-to-training-video> -a [rotation-angle-interval]`

## Run software

`python3 main.py <--templatedir> <path-to-template-directory> [--videofile] [path-to-video-file]`

## Testing the software

- Standard software tests can be run by executing the test programs in the `tests` directory
- All tests can be run by executing the `tox` command. `pip3 install tox` to install tox.

## Videos/Presentations
- First Release: https://www.youtube.com/watch?v=nXojR4SApy0
- First Release presentation: https://prezi.com/view/dBjzc3i97chm5FqSYNU0/
- Final Release: https://youtu.be/LgYexp6iawQ
- Final Release presentation: https://prezi.com/view/5tdPCb8dWDWIJCPCkz6q/
## Notes

- By default the software takes input from the web camera of the device. If a pre-recorded video needs to be used, videofile path has to be specified along with the --videofile (or -v) argument.

- Currently, data directory has only syringe and heart edge templates generated. Edge templates of other mesh models can be generated using the template_generator script with a provided video file of the projected 3D mesh model
