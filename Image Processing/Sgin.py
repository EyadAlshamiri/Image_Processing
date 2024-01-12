from typing import Optional, Tuple, Union
import customtkinter 
from tkinter import messagebox
from PIL import Image as Im
from InterFace import *

global Value 
Value = False 
User_Email = ""
Username = "" 
Password = "" 
conferm_password = "" 

class username:
   user_name = False 

def Sgin_IN(root):
   def Enter_SginUp (root) : 
      clear() 
      Sgin_Up(root)

   def Enter() :
      Username = user.get() 
      Password = password.get() 
      if Username == "" :
         messagebox.showerror("Error" , "please enter your username ")
      elif Password == "" : 
         messagebox.showerror("Error" , "please enter your Password ")
      else :
         username.user_name = True 
         Value = True
         clear()
         close()

   def clear():
      label.destroy()
      sign_label.destroy()
      user.destroy()
      user_frame.destroy()
      password.destroy()
      password_frame.destroy()
      sigin_Button.destroy()
      sign_up_Button.destroy()
      sign_up_label.destroy()
      show_password_check.destroy()
   
   def show_password() : 
      if show_password_check.get() == True : 
         password.configure(show="")
      else : 
         password.configure(show="*")
   image= customtkinter.CTkImage(dark_image=Im.open("image\\sgin1.png")
                                 , light_image=Im.open("image\\sgin1.png")
                                 , size=(404 , 351))

   label = customtkinter.CTkLabel(root , image = image  , text="")
   label.place(x = 10 ,y = 10 ) 
   
   sign_label = customtkinter.CTkLabel(root , text= "Sign in" , text_color="#57a1f8"  , font=("Microsoft YaHei UI light" , 40 , "bold"))
   sign_label.place(x = 550 , y = 20)

   user = customtkinter.CTkEntry(root, width= 250 , border_width=0 , fg_color="transparent" ,  placeholder_text= "Username", font=("Microsoft YaHei UI light" , 20))
   user.place(x = 500 ,y = 110 )

   user_frame = customtkinter.CTkFrame(root , width= 250 , height=2 , fg_color="cyan")
   user_frame.place(x = 500 , y = 140)

   password = customtkinter.CTkEntry(root, width= 250  , border_width= 0  , fg_color="transparent" , show = "*", placeholder_text= "Password", font=("Microsoft YaHei UI light" , 20))
   password.place(x = 500 ,y = 170 )

   password_frame = customtkinter.CTkFrame(root , width= 250 , height=2 , fg_color="cyan")
   password_frame.place(x = 500 , y = 200)

   sigin_Button = customtkinter.CTkButton(root , text= "Sign in" , text_color= "white" , border_width=0 , command=Enter)
   sigin_Button.place(x = 565 , y = 250)

   show_password_check = customtkinter.CTkCheckBox(root , command=show_password , text="Show password" , border_width=1)
   show_password_check.place(x = 500 , y = 210)

   sign_up_label = customtkinter.CTkLabel(root, text="Don't have an account?" , text_color="white" , font=("Microsoft YaHei UI light" , 17))
   sign_up_label.place(x=500,y= 310)

   sign_up_Button = customtkinter.CTkButton(root ,text="Sign up" , border_width= 0 , fg_color="transparent" , cursor="hand2" , width=2, text_color="#57a1f8" , command=lambda:Enter_SginUp(root))
   sign_up_Button.place(x=680,y=310)

def Sgin_Up(root):
   def Enter_SginIn (root) : 
      clear() 
      Sgin_IN(root)
   
   def Enter() :
      User_Email = user_Email.get()
      Username = user_up.get()
      Password = password_Up.get() 
      if Username == "" :
         messagebox.showerror("Error" , "please enter your username ")
      elif Password == "" : 
         messagebox.showerror("Error" , "please enter your Password ")
      elif User_Email == "" :
         messagebox.showerror("Error" , "please enter your Email ")
      elif Password != password_Up_chick.get() : 
         messagebox.showerror("Error" , "please make sure that the password matches ")
      else :
         username.user_name = True 
         clear()
         close()
   
   def clear():
      label2.destroy()
      sign_UP_label.destroy()
      user_up.destroy()
      user__Email_frame.destroy()
      user_Email.destroy()
      password_Up_chick.destroy()
      password_Up_ckick_frame.destroy()
      user__Up_frame.destroy()
      password_Up.destroy()
      password_Up_frame.destroy()
      sigin_Up_Button.destroy()
      sign_in_Button.destroy()
      sign_in_label.destroy()
      show_password_check.destroy () 
   
   def show_password() : 
      if show_password_check.get() == True : 
         password_Up.configure(show="")
         password_Up_chick.configure(show="")
      else : 
         password_Up.configure(show="*")
         password_Up_chick.configure(show="*")

   image= customtkinter.CTkImage(dark_image=Im.open("image\\sgin2.png")
                              , light_image=Im.open("image\\sgin2.png")
                              , size=(444 , 379))

   label2 = customtkinter.CTkLabel(root , image = image  , text="" )
   label2.place(x = 0 ,y = 0 ) 

   sign_UP_label = customtkinter.CTkLabel(root , text= "Sign up" , text_color="#57a1f8" , font=("Microsoft YaHei UI light" , 40 , "bold"))
   sign_UP_label.place(x = 550 , y = 0 )

   user_Email = customtkinter.CTkEntry(root , width= 250 , border_width=0 , fg_color="transparent" , placeholder_text= "@Email", font=("Microsoft YaHei UI light" , 20))
   user_Email.place(x = 500 ,y = 70 )

   user__Email_frame = customtkinter.CTkFrame(root , width= 250 , height=2 , fg_color="cyan")
   user__Email_frame.place(x = 500 , y = 100)

   user_up = customtkinter.CTkEntry(root , width= 250 , border_width=0 , fg_color="transparent", placeholder_text= "Username", font=("Microsoft YaHei UI light" , 20))
   user_up.place(x = 500 ,y = 120 )

   user__Up_frame = customtkinter.CTkFrame(root, width= 250 , height=2 , fg_color="cyan")
   user__Up_frame.place(x = 500 , y = 150)

   password_Up = customtkinter.CTkEntry(root , width= 250  , border_width=0 , fg_color="transparent" , show = "*", placeholder_text= "Password", font=("Microsoft YaHei UI light" , 20))
   password_Up.place(x = 500 ,y = 180)

   password_Up_frame = customtkinter.CTkFrame(root , width= 250 , height=2 , fg_color="cyan")
   password_Up_frame.place(x = 500 , y = 210)

   password_Up_chick = customtkinter.CTkEntry(root , width= 250 , border_width= 0  , fg_color="transparent" , show = "*", placeholder_text= "Confirm Password", font=("Microsoft YaHei UI light" , 20))
   password_Up_chick.place(x = 500 ,y = 240)

   password_Up_ckick_frame = customtkinter.CTkFrame(root , width= 250 , height=2 , fg_color="cyan")
   password_Up_ckick_frame.place(x = 500 , y = 270)

   sigin_Up_Button = customtkinter.CTkButton(root, text= "Sign in" , text_color= "white" , border_width=0 , command = Enter)
   sigin_Up_Button.place(x = 565 , y = 310)

   show_password_check = customtkinter.CTkCheckBox(root ,width=10,height=5, command=show_password , text="Show password" , border_width=1 )
   show_password_check.place(x = 500 , y = 280)

   sign_in_label = customtkinter.CTkLabel(root, text="I have an account?" , text_color="white"  , font=("Microsoft YaHei UI light" , 17))
   sign_in_label.place(x=500,y= 350)

   sign_in_Button = customtkinter.CTkButton(root,text="Sign up" , border_width= 0 , fg_color="transparent" , cursor="hand2", width=2, text_color="#57a1f8" , command=lambda:Enter_SginIn(root))
   sign_in_Button.place(x=660,y=350)


class Sgin_usee(customtkinter.CTkToplevel):
   def __init__(self):
      super().__init__()
      customtkinter.set_appearance_mode("dark")
      customtkinter.set_default_color_theme("dark-blue")
      self.geometry("800x400+30+30")
      self.title("Sgin")
      self.resizable(False,False)

def N():
   global app 
   app = Sgin_usee()
   Sgin_IN(app)

def close () :
   app.destroy()





