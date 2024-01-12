from tkinter import * 
import numpy as np
import os.path # to Access in File system 
from tkinter import filedialog 
from tkinter import messagebox  
import cv2 
import  matplotlib.pyplot as mp 
import customtkinter
# Recall Files
from MODE import Mode
from project_6 import face
from project_5 import face_hand 
from InterFace import *
from Functions import *
from Sgin import *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

w1 =customtkinter.CTk() # windo                                        
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
w1.geometry('1250x600+30+30') # width and heigth window 
w1.title('PROGRAM') # chang name of window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
w1.resizable(False,False) # dont control the size of window  


# class creat fraem option 
class Frame_option : 
   chick = True 
   # variabel the entry
   path = StringVar()
   save = StringVar()
   opration = StringVar()
   new_img  = StringVar()
   new_image = StringVar()
   gray_img = ''

   def apaut_opject (frame) :      
      name_project = customtkinter.CTkLabel(frame, text="Image Processing Project" , text_color="black" ,font=("" , 40 , "bold"))
      name_project.place(x=20 ,y=50)

      name_project = customtkinter.CTkLabel(frame, text="Using Python " , text_color="black" ,font=("" , 40 , "bold"))
      name_project.place(x=120 ,y=120)

   # function open Image
   def imo1 (frame2 ) :    # function to open the file in my combuter to select the pictors 
      file = filedialog.askopenfile(mode = 'r',filetypes=[('imge Files',('*.png' ,'*.jpg' , '*.tif' , '*.mp4'))])
      if file : 
         filepath = os.path.abspath(file.name) # give the file bath and name path 
         Frame_option.path.set(filepath) #
         spechil_GUI.Path_Image = Frame_option.path.get()
         Clear_Image()
         spechile.Show_Image( frame2 , Frame_option.path.get() )

   ''' all opraition '''
   def chang (w1 , opration , path ):
      # print img array 
      if opration == 'array' :
         img = cv2.imread(path)
         if img is None:
            messagebox.showerror('error' , "pless select any image ")
         else :
            spechil_GUI.Scrollbar_txt(w1,img)
      
      # print shape the imeg 
      elif opration == 'shape' :
         img = cv2.imread(path)
         if img is None:
            messagebox.showerror('error' , "pless select any image ")
         else :
            spechil_GUI.Scrollbar_txt(w1,img.shape)

      # resize image 
      elif opration == 'resize':
         inter_face.Resize(w1,path)

      # 
      elif opration == 'Add points' :
         inter_face.pxels(w1 ,Imag_Frame,path)


      elif opration=="pxels valiue" :
         img = cv2.imread(path)
         if img is None : 
            messagebox.showerror('Error' , "plass select any image")
         else : 
            mp.imshow(img)
            mp.show() 
      elif opration == 'MakeBorder' :
         inter_face.MakeBorder1(w1,Imag_Frame,path)

      elif opration == "Merg" :
         inter_face.merge_interface(w1 , Imag_Frame,path)

      elif opration == "convert image":
         inter_face.interface_convert( w1, Imag_Frame  , path)
      elif opration == "Add Noise"  : 
         inter_face.interface_add_noise(w1 , Imag_Frame,path)
      elif opration == "Remove Noise" : 
         inter_face.interface_remove_noise(w1,Imag_Frame,path)
      elif opration == "Edge Detection" : 
         inter_face.interface_Edge_Detection(w1 , Imag_Frame , path)
      elif opration == "Thresholding" :
         inter_face.interface_thershol(w1,Imag_Frame,path)

   new_frame= customtkinter.CTkFrame(w1,width= 560, height= 230 , fg_color= "transparent" 
                                    , border_color="cyan" , border_width=2,corner_radius= 50  )
   new_frame2= customtkinter.CTkFrame(w1,width= 560, height= 330 , fg_color= "transparent" 
                                    , border_color="cyan" , border_width=2,corner_radius= 50  )
   def desplay_option(new_frame):

      Clear_Image()
      # --------Tools------
      
      new_frame.place (x=10 , y = 20)

      Frame_option.new_frame2.place (x=10 , y = 260)



      text = customtkinter.CTkLabel(new_frame,text='PROGRAM :Imge prossing [ Opencv ]',font=('times for roman',20)) # create text 
      text.place(x=110,y=10) # the text Aplace  
 
      en1_text = customtkinter.CTkLabel(new_frame,text="Image path : ", font=('times gor roman',15))
      en1_text.place(x= 10 , y= 50)
      en1 = customtkinter.CTkEntry(new_frame, font=('tines for roman',16),width=365, textvariable = Frame_option.path ) # create field for writing 
      en1.place(x=100,y=50) 
 
      btn1 = customtkinter.CTkButton(new_frame,text='+',cursor='hand2'  , width=10 , command=lambda:Frame_option.imo1(Imag_Frame))
      btn1.place(x = 445 , y = 51)
      en2_text =customtkinter.CTkLabel(new_frame,text="save Image: ", font=('times gor roman',15))
      en2_text.place(x= 10 , y=84)
      en2 = customtkinter.CTkEntry(new_frame, font=('tines for roman',16),width=365 , textvariable= Frame_option.save ) # create field for writing 
      en2.place(x=100,y=84) 

      #btn2 = Button(f1,text='+',cursor='hand2',command=lambda:imo2(new_img.get()))
      #btn2.place (x=445,y=85)

      en3_text = customtkinter.CTkLabel(new_frame,text="Opration     : ", font=('times gor roman',15))
      en3_text.place(x= 10 , y=117)
      OptionMenu_opration = customtkinter.CTkOptionMenu(new_frame ,width=365  
                                 , values=["array","shape","resize"
                                          , "Add points","pxels valiue"
                                          , "MakeBorder"
                                          ,"Merg" , "convert image"
                                          ,"Add Noise" , "Remove Noise"
                                          , "Edge Detection", "Thresholding"]
                                          ) # create field for writing 
      OptionMenu_opration.place(x=100,y=117) 

      en5 = customtkinter.CTkLabel(new_frame,text="Saving changes  : ", font=('times gor roman',15))
      en5.place(x= 270 , y=162)
      en5_but= customtkinter.CTkButton(new_frame,text = 'Save', command=lambda:Frame_option.chang ( Frame_option.new_frame2 , OptionMenu_opration.get(),Frame_option.path.get()))
      en5_but.place(x= 400, y=160)

      en7 = customtkinter.CTkLabel(new_frame,text="Exit program       : ", font=('times gor roman',15))
      en7.place(x= 10 , y=162)
      en7_but= customtkinter.CTkButton(new_frame,text = 'Exit  ' , cursor='hand2', command= w1.quit)
      en7_but.place(x= 100, y=160)

# function new image 

def information() : 
   messagebox.showinfo("information" , "the project was done by : \n Eyad Al-Shamiri \n Bandar Al-Fatesh \n Supervisor by: Eng.Amjad Al-Yousifi")

#---------Define------

def AI1():
   face.fa()

def AI2():
   face_hand.new()

image= customtkinter.CTkImage(dark_image=Im.open("image\\python.png")
                                 , light_image=Im.open("image\\python.png")
                                 ,size=(600,294))
               
label = customtkinter.CTkLabel(w1 , image = image  , text="")

image= customtkinter.CTkImage(dark_image=Im.open("image\\opencv2.png")
                                 , light_image=Im.open("image\\opencv2.png")
                                 ,size=(280,280))
            
label2 = customtkinter.CTkLabel(w1 , image = image  , text="")

label.place(x = 10 ,y = 10 )  
label2.place(x = 140 ,y = 280 )

global Imag_Frame 
Imag_Frame = customtkinter.CTkFrame(w1,width= 600, height= 550 , fg_color= "transparent" 
                                    , border_color="cyan" , border_width=2,corner_radius= 50  )
Imag_Frame.place (x=590 , y = 20)


Frame_Button = customtkinter.CTkFrame(w1,width= 500, height= 250 , fg_color= "transparent" 
                                    , border_color="cyan" , border_width=2,corner_radius= 50  )
Frame_Button.place (x=640 , y = 250)



aput = customtkinter.CTkLabel(w1,text="Image Processing Project"  ,font=("Microsoft YaHei UI light" , 43 , "bold"))
aput.place(x = 620 ,y = 50)

use = customtkinter.CTkLabel(w1,text="Using Python language" ,font=("Microsoft YaHei UI light" , 43 , "bold"))
use.place(x = 650 ,y = 130)

Bt_guest = customtkinter.CTkButton(Frame_Button , text= "Guest" , width= 200, height= 50, command=lambda:Enter_Guest(Frame_option.new_frame))
Bt_guest.place(x=40 , y = 40 )

Bt_information = customtkinter.CTkButton(Frame_Button , text= "Information" , width= 200, height= 50, command= information)
Bt_information.place(x=40 , y = 150 )

Bt_Sign_in = customtkinter.CTkButton(Frame_Button , text= "Sign in" , width= 200, height= 50, command= N)
Bt_Sign_in.place(x=260 , y = 40 )

Bt_Exit = customtkinter.CTkButton(Frame_Button , text= "Exit" , width= 200, height= 50, command= w1.quit)
Bt_Exit.place(x=260 , y = 150 )

def Clear_Image(): 
   label.destroy()
   label2.destroy()
   aput.destroy()
   use.destroy()
   Frame_Button.destroy()
   Bt_information.destroy()
   Bt_guest.destroy() 
   Bt_Exit.destroy() 
   Bt_Sign_in.destroy()

def Enter_Guest(w1):
   menu()
   Frame_option.desplay_option(w1)

# function menu 
def menu():
   menubar = Menu(w1 , fg= "gold")

   filemenu  = Menu(menubar , tearoff=0 )
   filemenu.add_command(label= "open Image" , command=lambda:Frame_option.imo1(Imag_Frame))
   filemenu.add_separator()
   filemenu.add_command(label="Save" , command=lambda:spechile.Save_image("ImageNew.png"))
   filemenu.add_separator()
   filemenu.add_command(label="Log in" , command=N)
   filemenu.add_separator()
   filemenu.add_command(label="Exit" , command= w1.quit)

   menubar.add_cascade(label="File", menu= filemenu)

   filemenu1  = Menu(menubar , tearoff=0 )
   filemenu1.add_command(label= "Darck Mode" , command=Mode.dark)
   filemenu1.add_command(label="White Mode" , command=Mode.white )
   
   menubar.add_cascade(label="Mode", menu= filemenu1)
   
   filemenu2 =Menu(menubar , tearoff=0)
   filemenu2.add_command(label= "AI" , command=AI1)
   filemenu2.add_command(label="AI2" , command=AI2 )
   
   menubar.add_cascade(label="program", menu= filemenu2)

   w1.config(menu=menubar )


w1.mainloop() # cod run TK() 
