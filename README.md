# Tracking-worm-in-granular-environments
A package for analyzing a moving slender object in a quasi-2D granular environment. 

More specifically, we include four sets of code that could be executed according to the sequence below:

(1) A Python-based, neural-network based method to segment a worm from 2D images or videos. Example training images and a video are included along with the source code.

(2) A set of Python code to utilize segmented worm images to extract positional information of the worm as a function of time.

(3) A python-based code, utilizing an existing package (Bellybutton) to segment the particles in the same set of images. A region of interest can be set according to the identified worm position, so that only particles near the worm will be tracked.

(4) Example analysis code to utilize the above information. The code pieces can be used to further develop analysis such as worm speed vs. nearby particle density.
