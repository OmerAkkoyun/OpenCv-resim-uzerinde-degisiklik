import cv2

img =cv2.imread("C:/Users/Omer/Desktop/omer.jpg",cv2.IMREAD_GRAYSCALE) #GR� YAPAN KOD
print(img) #buras� bize resim renkkoardinat�n� verecek

if img is None:
    print("Hata !Dosya Yolu Yanl�� Belirtilmi�..")
	print("Oops! File does not exist !.")
else:
    cv2.imshow("burasi_baslik_olacak",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
