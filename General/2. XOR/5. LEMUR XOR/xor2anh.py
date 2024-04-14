import cv2

anh1 = cv2.imread('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
anh2 = cv2.imread('flag_7ae18c704272532658c10b5faad06d74.png')

anh3 = cv2.bitwise_xor(anh1, anh2)

cv2.imshow('gohome',anh3)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()