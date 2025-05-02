# Stop-Sign-detection
This project is a simple stop sign detection system using OpenCV and Python. The algorithm attempts to detect red octagons in images, which is a charactaristic of a stop sign.


# Requirements
    Python 3.x
    OpenCV (cv2)
    NumPy

# Install requirements with:

    pip install opencv-python numpy

# How to use

    Place your images in the same directory as the script
    Update the main() function calls at the bottom of the script with your image filenames
    Run the script in terminal: python project.py



The script will Display the original image with detected stop signs outlined


# How It Works

    Color Space Conversion: Converts RGB image to HSV for better color segmentation

    Red Region Detection: Uses two HSV ranges to capture different shades of red

    Noise Reduction: Applies median blur and morphological closing to clean up the mask

    Shape Detection: Finds contours and looks for octagonal shapes (8-sided convex polygons)

    Result Visualization: Draws green contours around detected stop signs


The script includes example calls for pic1.png, pic2.png, and pic3.png. Replace these with your own image filenames.
Output


Press any key to close the display windows.
