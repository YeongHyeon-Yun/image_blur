import cv2
import sys

import os

dir_path = "knowns"   # 모자이크할 이미지 폴더
save_path = "blur_done"  # 모자이크 처리된 이미지를 저장할 폴더를 만들어줘야한다

images_path = []
for (root, directories, files) in os.walk(dir_path):
    print('루트', root)
    for d in directories:
        d_path = os.path.join(root, d)
        print('디렉토리',d_path)

    for file in files:
        file_path = os.path.join(root, file)
        images_path.append(file_path)
        print('파일이름경로',file_path)
print(images_path)

for imagePath in images_path:
    file_name = imagePath.split('\\')[-1]
    
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=1,
        minSize=(30, 30)
    )

    print("[INFO] Found {0} Faces.".format(len(faces)))

    ksize = 70  # 모자이크 강도

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi = image[y:y+h, x:x+w] 
        roi = cv2.blur(roi, (ksize, ksize), cv2.BORDER_CONSTANT)
        image[y:y+h, x:x+w] = roi
        print("[INFO] Object found. Saving locally.")
        
        # 모자이크 처리된 얼굴만 저장
        # roi_color = image[y:y + h, x:x + w]
        # cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
        
    status = cv2.imwrite(save_path+"\\"+file_name, image)
    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)