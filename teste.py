
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

image = cv2.imread('images/dog.jpg')
bbox, label, conf = cv.detect_common_objects(image)
print(bbox, label, conf)
out = draw_bbox(image, bbox, label, conf)

cv2.imshow("object_detection", out)
cv2.waitKey()
cv2.imwrite("images/dog_out.jpg", out)

cv2.destroyAllWindows()