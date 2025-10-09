"""cv2 script to display image"""

import cv2

def display_image(image_path: str, window_name: str) -> None:
    """display image function"""
    
    image = cv2.imread(image_path)

    while True:
        cv2.imshow(window_name, image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.destroyAllWindows()
    