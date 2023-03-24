import cv2

ksize = 70              # 블러 처리에 사용할 커널 크기
win_title = 'mosaic'    # 창 제목
img = cv2.imread('ori\ymh5.jpg')    # 이미지 읽기
img = cv2.resize(img, (600, 800))
while True:
    x,y,w,h = cv2.selectROI(win_title, img, False) # 관심영역 선택
    if w > 0 and h > 0:         # 폭과 높이가 음수이면 드래그 방향이 옳음 
        roi = img[y:y+h, x:x+w]   # 관심영역 지정
        roi = cv2.blur(roi, (ksize, ksize), cv2.BORDER_CONSTANT) # 블러(모자이크) 처리
        img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
        cv2.imshow(win_title, img)
        cv2.imwrite('blur2/ymh5.jpg', img)
    else:
        break
cv2.destroyAllWindows()