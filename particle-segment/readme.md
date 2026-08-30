# ML-based Worm Segmentation Toolbox

The main goal for this sub-package is to segment the particles in the video. This is mostly based on an existing package "bellybutton": https://pypi.org/project/bellybuttonseg/

The package is introduced in: Dillavou, S., Hanlan, J. M., Chieco, A. T., Xiao, H., Fulco, S., Turner, K. T., & Durian, D. J. (2024). Bellybutton: accessible and customizable deep-learning image segmentation. Scientific Reports, 14(1), 14281.

However, the original package has a potential memory leak, and the segmentation process will terminate if the entire computer's memory is occupied. A quick fix was then implemented in the uploaded "predict.py" here, which breaks the whole set of images into batches.

<img width="960" height="720" alt="310_binarized" src="https://github.com/user-attachments/assets/021765a5-3adf-4e45-93b2-6ffe9be5592b" />


