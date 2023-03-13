import cv2
import numpy as np

# Membuat jendela tampilan untuk menampilkan hasil pemindaian
cv2.namedWindow("Color Scanner")

# Membuka kamera
cap = cv2.VideoCapture(0)

while True:
    # Membaca setiap frame dari kamera
    ret, frame = cap.read()
    
    # Mengubah frame menjadi nilai HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Menentukan rentang nilai Hue untuk setiap warna
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([5, 255, 255])
    lower_orange = np.array([6, 100, 100])
    upper_orange = np.array([20, 255, 255])
    lower_yellow = np.array([21, 100, 100])
    upper_yellow = np.array([35, 255, 255])
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([75, 255, 255])
    lower_blue = np.array([76, 100, 100])
    upper_blue = np.array([130, 255, 255])
    lower_violet = np.array([131, 100, 100])
    upper_violet = np.array([160, 255, 255])
    lower_pink = np.array([161, 100, 100])
    upper_pink = np.array([179, 255, 255])
    
    # Menerapkan filter warna untuk setiap warna
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_orange = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    mask_yellow = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    mask_violet = cv2.inRange(hsv_frame, lower_violet, upper_violet)
    mask_pink = cv2.inRange(hsv_frame, lower_pink, upper_pink)
    
    # Menggabungkan semua mask
    mask = mask_red + mask_orange + mask_yellow + mask_green + mask_blue + mask_violet + mask_pink
    
    # Menampilkan hasil pemindaian
    cv2.imshow("Color Scanner", mask)
    
    # Keluar dari loop jika tombol q ditekan
    if cv2.waitKey(1) == ord('q'):
        break

# Menutup jendela tampilan dan melepaskan kamera
cv2.destroyAllWindows()
cap.release()