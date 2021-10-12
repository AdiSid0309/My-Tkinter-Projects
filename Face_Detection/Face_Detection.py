import cv2
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

#-------------------------------Main Frame Creation-------------------------

root = Tk()
root.geometry('500x550')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
root.title('Face Detection')
photo = PhotoImage(file="ui.png")
root.iconphoto(False, photo)
frame.config(background='black')
label = Label(frame, text="Face Detection", fg="white", bg='black', font=('Algerian 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="ai.png")
background_label = Label(frame, image=filename)
background_label.pack(side=TOP)

#-------------------------------Tools and About Menu-------------------------

def Contri():
   tkinter.messagebox.showinfo("Programmers", "\n1.Siddharth Soni\n2. Jatin Mishra \n3. Kunal Chahar \n")


def anotherWin():
   tkinter.messagebox.showinfo("About", 'Driver Cam version-Using ivCam\n Made Using\n-OpenCV\n-Tkinter\n-Python 3')



menu = Menu(root)
root.config(menu=menu)


subm1 = Menu(menu)
menu.add_cascade(label="About", menu=subm1)
subm1.add_command(label="Details", command=anotherWin)
subm1.add_command(label="Programmers", command=Contri)

#-------------------------------Main Functions For Buttons-------------------------

def exitt():
   exit()


def web():
   capture =cv2.VideoCapture(0,cv2.CAP_DSHOW)

   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame', frame)

      if cv2.waitKey(10) & 0xFF == ord('q'):
         break

   capture.release()
   cv2.destroyAllWindows()

def webdet():
   capture =cv2.VideoCapture(0, cv2.CAP_DSHOW)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)

       for (x, y, w, h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame, 'Face', (x+w, y+h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
           cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]

           eye_g = eye_glass.detectMultiScale(roi_gray)

           for (ex, ey, ew, eh) in eye_g:
              cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xff == ord('q'):
          break

   capture.release()
   cv2.destroyAllWindows()

def webdetRec():
   capture =cv2.VideoCapture(0, cv2.CAP_DSHOW)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID')
   op=cv2.VideoWriter('Sample1.mp4', fourcc, 9.0, (640, 480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)

       for (x, y, w, h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame, 'Face', (x+w, y+h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
           cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]

           eye_g = eye_glass.detectMultiScale(roi_gray)

           for (ex, ey, ew, eh) in eye_g:
              cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

       op.write(frame)
       cv2.imshow('frame',frame)

       if cv2.waitKey(1) & 0xff == ord('q'):
          break

   op.release()
   capture.release()
   cv2.destroyAllWindows()


#-------------------------------Placement Of Buttons-------------------------
photo0 = Image.open("op_cam.png")
photo0 = photo0.resize((70, 180), Image.ANTIALIAS)
photo0 = ImageTk.PhotoImage(photo0)

photo1 = Image.open("open.png")
photo1 = photo1.resize((100, 100), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(photo1)

photo2 = Image.open("rec.png")
photo2 = photo2.resize((100, 200), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(photo2)

photo = PhotoImage(file = "exit1.png")


but0 = Button(frame, padx=5, pady=5, bg='white', fg='black', relief=GROOVE, command=web, image=photo0, height=70, width=100)
but0.place(x=200,y=104)

but1 = Button(frame, padx=5, pady=5, bg='white', fg='black', relief=GROOVE, command=webdet, image=photo1, height=100, width=100)
but1.place(x=200, y=200)

but2 = Button(frame, padx=5, pady=5, bg='white', fg='black', relief=GROOVE, command=webdetRec, image=photo2, height=100, width=100)
but2.place(x=200, y=320)

but3 = Button(frame, padx=5, pady=5, bg='white', fg='black', relief=GROOVE, command=exitt, image=photo, height=70, width=180)
but3.place(x=160, y=440)


root.resizable(False, False)

root.mainloop()