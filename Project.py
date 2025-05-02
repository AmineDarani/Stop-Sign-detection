import cv2
import numpy as np

def convert_to_sow(image):
###Convert RGB image to Saturation-Hue-Brightness (S-H-W*) space.
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    return hsv_image



def extract_red_regions(hsv_image):
###Extract red regions based on S-H-W* color space. 
    lower_red = np.array([0, 70, 50])
    upper_red = np.array([15, 255, 255])
    lower_red2 = np.array([165, 70, 50])
    upper_red2 = np.array([185, 255, 255])
    mask1 = cv2.inRange(hsv_image, lower_red, upper_red)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask

def detect_stop_sign(image, mask):
### Detect and extract the stop sign using contour detection.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    stop_sign_images = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        if len(approx) == 8 and cv2.isContourConvex(approx):  # Check if the contour has 8 sides and is convex (octagon)
            x, y, w, h = cv2.boundingRect(approx)
            stop_sign_image = image[y:y+h, x:x+w]
            stop_sign_images.append(stop_sign_image)
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
    return stop_sign_images, image

def main(image_path):
### Main function to process the image.
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    hsv_image = convert_to_sow(image)
    mask = extract_red_regions(hsv_image)


    stop_sign_images, result_image = detect_stop_sign(image, mask)
    result_image =cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

    if stop_sign_images:
        for i, stop_sign_image in enumerate(stop_sign_images):
            stop_sign_image = cv2.cvtColor(stop_sign_image, cv2.COLOR_RGB2BGR)

    else:
        print("No stop sign detected.")
    cv2.imshow('Tested Image with all contours detected', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Replace 'path_to_image.jpg' with your image file path
main('pic1.png')
main('pic2.png')
main('pic3.png')
