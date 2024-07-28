from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
import cv2
import numpy as np
from PIL import Image,ImageTk


#global degisken
video = ""

#tkinter
window = Tk()
window.title("MAMA MİKTARI SORGULAMA")
window.config(bg="#4c4c4c")
window.geometry("1300x700")
window.resizable(FALSE,FALSE)

app = Frame(window)



#video secme
tb = Entry(window, width=80)
def openVideo():
    tb.delete(0, END)
    global video
    filterex = (
        ('Video Dosyası', '*.MP4'),
        ('Tüm Dosyalar', '*.*')
    )
    userfile = fd.askopenfile(title="Video Seç", filetypes=filterex)
    tb.insert(0, userfile.name)
    video = userfile.name
    print(video)
    video = cv2.VideoCapture(video)
    # videonun sürekli döndürülmesi için while
    while 1:

        # video değişkenini okutmak için videoGoruntu değişkeni içinde read komutu ile sisteme okutuyoruz
        ret, videoGoruntu = video.read()
        # ilk parametre çerçeve ismi , ikinci parametre video değil videoGoruntu çünkü  videoGoruntu değişkenine videoyu okuttuk

        hsv_frame = cv2.cvtColor(videoGoruntu, cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv_frame, (80, 50, 50), (100, 255, 255))
        blue = cv2.bitwise_and(videoGoruntu, videoGoruntu, mask=blue_mask)

        #red_mask1 = cv2.inRange(hsv_frame, (0, 50, 50), (10, 255, 255))
        #red_mask2 = cv2.inRange(hsv_frame, (170, 50, 50), (180, 255, 255))
        #red_mask = cv2.bitwise_or(red_mask1, red_mask2)
        red_mask = cv2.inRange(hsv_frame, (160, 100, 100), (179, 255, 255))
        red = cv2.bitwise_and(videoGoruntu,videoGoruntu, red_mask)

        green_mask = cv2.inRange(hsv_frame, (40, 50, 50), (70, 255, 255))
        green = cv2.bitwise_and(videoGoruntu, videoGoruntu, green_mask)



        # Mavi, kırmızı, sarı ve yeşil renkleri içeren piksel sayılarını hesaplıyoruz
        blue_pixels = cv2.countNonZero(blue_mask)
        red_pixels = cv2.countNonZero(red_mask)
        green_pixels = cv2.countNonZero(green_mask)




        blue = "Mavi Alan Mevcut "
        red = "Kirmizi Alan Mevcut "
        green = "Yesil Alan Mecvut: "




        # color ="Undefined"
        mama_miktari = "Undefined"

        if blue_pixels == 0 and red_pixels == 0 and green_pixels == 0 :
            mama_miktari = "Mama Yeteri Kadar Dolu.."
            durum = Label(window, text="MAMA DURUMU:"+"   "+mama_miktari, fg= "black" , bg="#4c4c4c",font="Times 15 bold")
            durum.place(x=70, y=210)

            cv2.putText(videoGoruntu, mama_miktari, (20, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)


        elif  green_pixels > 0 and blue_pixels == 0 and red_pixels == 0  :
            color = green
            mama_miktari = "Mama Orani: %50 "
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(videoGoruntu, color, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(videoGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        elif blue_pixels > 0 and green_pixels > 0 and red_pixels == 0 :
            color = blue
            mama_miktari = "Mama Orani: %25"
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(videoGoruntu, color , (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(videoGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        elif blue_pixels > 0 and green_pixels > 0 and red_pixels > 0 :
            color = red
            mama_miktari = "Lutfen Mama Doldurunuz.."
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",   font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(videoGoruntu, color, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(videoGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)



       # elif blue_pixels > 0 and green_pixels > 0 and red_pixels > 0 and yellow_pixels > 0:
        #    color = red
         #   mama_miktari = "Lutfen Mama Doldurunuz.."
          #  durum = Label(window, text=mama_miktari)
           # durum.place(x=70, y=210)
            #cv2.putText(videoGoruntu, color , (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            #cv2.putText(videoGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


        cv2.imshow("Video-mama-sorgulama", videoGoruntu)
        key = cv2.waitKey(34)
        if key == 27:
            break
    video.release()
    cv2.destroyAllWindows()


videoButton = Button(window, text="Videodan Mama Miktarı Sorgula ", bg="gray", fg="black", width=28, height=4, command=openVideo)
videoButton.place(x=70, y=100)



#webcam
def webcam():
    cap = cv2.VideoCapture(0)

    while True:
        ret, camGoruntu = cap.read()

        hsv_frame = cv2.cvtColor(camGoruntu, cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv_frame, (80, 50, 50), (100, 255, 255))
        blue = cv2.bitwise_and(videoGoruntu, videoGoruntu, mask=blue_mask)

        # red_mask1 = cv2.inRange(hsv_frame, (0, 50, 50), (10, 255, 255))
        # red_mask2 = cv2.inRange(hsv_frame, (170, 50, 50), (180, 255, 255))
        # red_mask = cv2.bitwise_or(red_mask1, red_mask2)
        red_mask = cv2.inRange(hsv_frame, (160, 100, 100), (179, 255, 255))
        red = cv2.bitwise_and(videoGoruntu, videoGoruntu, red_mask)

        green_mask = cv2.inRange(hsv_frame, (40, 50, 50), (70, 255, 255))
        green = cv2.bitwise_and(videoGoruntu, videoGoruntu, green_mask)



        # Mavi, kırmızı, sarı ve yeşil renkleri içeren piksel sayılarını hesaplıyoruz
        blue_pixels = cv2.countNonZero(blue_mask)
        red_pixels = cv2.countNonZero(red_mask)
        green_pixels = cv2.countNonZero(green_mask)


        #blue = "Mavi: " + str(blue_pixels)
        #red = "Kırmızı: " + str(red_pixels)
        #green = "Yeşil: " + str(green_pixels)


        blue = "Mavi Alan Mevcut "
        red = "Kirmizi Alan Mevcut "
        green = "Yesil Alan Mecvut: "


        #color ="Undefined"
        mama_miktari = "Undefined"

        if blue_pixels == 0 and red_pixels ==0 and green_pixels == 0 :

            mama_miktari = "Mama Yeteri Kadar Dolu.."
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",
                          font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(camGoruntu, mama_miktari, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        elif blue_pixels ==0 and red_pixels ==0 and green_pixels > 0 :
            color = green
            mama_miktari = "Mama Orani: %50 "
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",
                          font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(camGoruntu, color , (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(camGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        elif  blue_pixels > 0 and green_pixels > 0 and red_pixels == 0 :
            color = blue
            mama_miktari = "Mama Orani: %25"
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",
                          font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(camGoruntu, color , (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(camGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        elif blue_pixels > 0 and green_pixels > 0 and red_pixels > 0 :
            color = red
            mama_miktari = "Mama Orani: %25'in altında. Lütfen Mama Doldurunuz."
            durum = Label(window, text="MAMA DURUMU:" + "   " + mama_miktari, fg="black", bg="#4c4c4c",
                          font="Times 15 bold")
            durum.place(x=70, y=210)
            cv2.putText(camGoruntu, color, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(camGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        #elif blue_pixels > 0 and green_pixels > 0 and red_pixels > 0 and yellow_pixels > 0:
         #   color = yellow
          #  mama_miktari = "Lutfen Mama Doldurunuz.."
           # cv2.putText(camGoruntu, color, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(camGoruntu, mama_miktari, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("webcam-mama-sorgulama", camGoruntu)
        key = cv2.waitKey(1)
        if key == 27:
            break

webcamButton = Button(window, text="Webcamden Mama Miktarı Sorgula ", bg="gray", fg="black", width=28, height=4, command=webcam)
webcamButton.place(x=70, y=400)

window.mainloop()




