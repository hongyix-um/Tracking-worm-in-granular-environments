# Worm kinematic data extraction

https://github.com/user-attachments/assets/fc90da60-c96c-4162-989c-0670478d4b29

This sub-package reads the segmented video and use Python libraries to derive specific parameters of the worm's kinematics. From the segemented mask of each worm, we identify five nodes alongside its body, which can be used for subsequent analysis.

The main file to check and execute is "unitool.py".

As of now, the most useful output is "raw_data.csv", which contains the identified nodal position in unit of pixels for each frame. Although additional information is also written, but the corresponding functions are in a testing stage. For the research manuscript, we wrote separate MATLAB code to directly analyze worm kinematics based on the nodal positions of the worm.  

As a worm can exist in a complicated environment, the head/tail distinguishment can be challenging, and the result in "raw_data.csv" needs to be corrected. For each video segment, we can mannualy identify the worm's head node in the first frame, and use an proximity-based criterion to identify the head node in the subsequent frames. An example code in MATLAB is attached here, although it will require the video to be converted to images first. A intervals.csv file can also be created for a user to specify which frame intervals of interest should be corrected.  

