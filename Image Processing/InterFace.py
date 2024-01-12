import customtkinter
from tkinter import *
from tkinter import filedialog ,messagebox
import os.path
import cv2
import numpy as np
from PIL import Image as Im

# import the pyhton file 
from Functions import *



class spechil_GUI :
   count=0
   Path_Image = ""
   Image_Save = ""

   def imo1 (entry) :    # function to open the file in my combuter to select the pictors 
      file = filedialog.askopenfile(mode = 'r',filetypes=[('imge Files',('*.png' ,'*.jpg' , '*.tif' , '*.mp4'))])
      if file : 
         filepath = os.path.abspath(file.name) # give the file bath and name path 
         entry.insert(0,filepath) #
         

   def imo2 (img , en2) :    # function to save the file in my combuter 
      file = filedialog.asksaveasfile(mode = 'w',filetypes=[('PNG Files')])
      if file : 
         filepath = os.path.abspath(file.name) # give the file bath and name path 
         cv2.imwrite(filepath,img)
         en2.insert(0,filepath)

   def Scrollbar_txt(w1,img):
      def cle_scr() :
         txt.destroy()
         ctk_textbox_scrollbar.destroy()
         b.destroy()

      txt = customtkinter.CTkTextbox(w1,width=200 , activate_scrollbars=False)
      txt.insert("0.0",img)
      txt.place(x=200 , y = 10)

      ctk_textbox_scrollbar = customtkinter.CTkScrollbar(w1, command= txt.yview)
      ctk_textbox_scrollbar.place(x=400 , y = 10 )
      txt.configure(yscrollcommand=ctk_textbox_scrollbar.set)

      b= customtkinter.CTkButton( w1 , text= "x" , width=10 , command= cle_scr)
      b.place(x= 380 , y=10)

      messagebox.showinfo('opration' , 'Opration accomplished successfully ')


class inter_face :

   # inter face the resize opration 
   def Resize(w1,path) :

      def back():
         la1.destroy()
         en1.destroy()
         la2.destroy()
         en2.destroy()
         bu.destroy()
         back_button.destroy()

      la1 = customtkinter.CTkLabel(w1 , text=" width image :" )
      la1.place(x=50 , y=10)
      en1 = customtkinter.CTkEntry(w1,width= 100 )
      en1.place(x=150,y=10)

      la2 = customtkinter.CTkLabel(w1 , text="height image :" )
      la2.place(x=270 , y=10)
      en2 = customtkinter.CTkEntry(w1,width= 100 )
      en2.place(x=400 , y=10)

      bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:Function.resize( path,int(en1.get()), int(en2.get())))
      bu.place(x=100 , y=60)
      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=60)

      


   # inter face the opration merg 
   def merge_interface(w1 , frame , path1):
      def back ():
         path_lable.destroy()
         path_entry.destroy()
         value1_lable.destroy()
         value2_lable.destroy()
         entr_button.destroy()
         back_button.destroy()
         brightne_lable.destroy()
         path_button.destroy()

         entry_slider1.destroy() 
         entry_slider2.destroy() 
         entry_slider3.destroy() 
         value1_sli.destroy() 
         value2_sli.destroy()
         value3_sli.destroy() 


      def Enter():
         value1 = float(entry_slider1.get()) 
         value2 =float(entry_slider2.get()) 
         if value1+value2 > 1.0 :
            value1 = 0.5 
            value2 = 0.5
         Function.to_merge( frame,path1,path_entry.get() , value1,value2,int(entry_slider3.get()))

      path_lable = customtkinter.CTkLabel(w1,text="Image path : ", font=('times gor roman',15))
      path_lable.place(x=20,y=10)
      path_entry = customtkinter.CTkEntry(w1, font=('tines for roman',16),width=365 , ) # create field for writing 
      path_entry.place(x=120,y=10) 

      path_button = customtkinter.CTkButton(w1,text='+',cursor='hand2', width=10,command=lambda:spechil_GUI.imo1(path_entry))
      path_button.place (x=465,y=11)

      value1_lable = customtkinter.CTkLabel(w1,text="Value Image1", font=('times gor roman',15))
      value1_lable.place(x=70,y=60)
      value2_lable = customtkinter.CTkLabel(w1,text="Value Image2", font=('times gor roman',15))
      value2_lable.place(x=290,y=60)
      brightne_lable = customtkinter.CTkLabel(w1,text="Brightnes", font=('times gor roman',15))
      brightne_lable.place(x=200,y=150)

      def show(value):
         entry_slider1.delete(0,END)
         entry_slider1.insert(0,str(float(value)))

      value1_sli= customtkinter.CTkSlider(w1, from_=0.0, to= 1  , width= 150, command=show)
      value1_sli.place(x=20,y=100)

      entry_slider1 = customtkinter.CTkEntry(w1 , width=60)
      entry_slider1.place(x =180 , y = 100)

      def show2(value):
         entry_slider2.delete(0,END)
         entry_slider2.insert(0,str(float(value)))

      value2_sli= customtkinter.CTkSlider(w1, from_=0.0, to= 1 , width=150, command=show2)
      value2_sli.place(x=270,y=100)

      entry_slider2 = customtkinter.CTkEntry(w1 , width=60)
      entry_slider2.place(x =420 , y = 100)

      def show3(value):
         entry_slider3.delete(0,END)
         entry_slider3.insert(0,str(int(value)))

      value3_sli= customtkinter.CTkSlider(w1, from_=-100, to= 100, width=150 ,  command=show3)
      value3_sli.place(x=170,y=200)

      entry_slider3 = customtkinter.CTkEntry(w1 , width=60)
      entry_slider3.place(x =320 , y = 200)

      entr_button= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2' , command= Enter )
      entr_button.place(x=100 , y=250)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=250)

      
   def pxels(w1,frame,path):

      img =cv2.imread(path)
      
      number_row = img.shape[0] 
      number_col = img.shape[1] 
      def back ():
         l1.destroy()
         l2.destroy()
         l3.destroy()
         l4.destroy()
         l5.destroy()
         bu1.destroy()
         bu2.destroy()

         row_sli.destroy()
         entry_row.destroy()
         col_sli.destroy()
         entry_col.destroy()
         red_sli.destroy()
         entry_green.destroy()
         entry_red.destroy()
         green_sli.destroy()
         blue_sli.destroy()
         entry_blue.destroy() 

      l1 = customtkinter.CTkLabel(w1,text="Row", font=('times gor roman',15))
      l1.place(x=80,y=10)
      l2 = customtkinter.CTkLabel(w1,text="Column", font=('times gor roman',15))
      l2.place(x=350,y=10)
      l3 = customtkinter.CTkLabel(w1,text="Red", font=('times gor roman',15))
      l3.place(x=80,y=100)
      l4 = customtkinter.CTkLabel(w1,text="Green", font=('times gor roman',15))
      l4.place(x=350,y=100)
      l5 = customtkinter.CTkLabel(w1,text="Blue",  font=('times gor roman',15))
      l5.place(x=250,y=200)

      def show(value):
         entry_row.delete(0,END)
         entry_row.insert(0,str(int(value)))

      row_sli= customtkinter.CTkSlider(w1, from_=0, to= number_row  , width= 150, command=show)
      row_sli.place(x=20,y=50)

      entry_row = customtkinter.CTkEntry(w1 , width=60)
      entry_row.place(x =180 , y = 50)

      def show2(value):
         entry_col.delete(0,END)
         entry_col.insert(0,str(int(value)))

      col_sli= customtkinter.CTkSlider(w1, from_=0, to= number_col , width=150, command=show2)
      col_sli.place(x=270,y=50)

      entry_col = customtkinter.CTkEntry(w1 , width=60)
      entry_col.place(x =420 , y = 50)

      def show3(value):
         entry_red.delete(0,END)
         entry_red.insert(0,str(int(value)))

      red_sli= customtkinter.CTkSlider(w1, from_=0, to= 255, width=150 ,  command=show3)
      red_sli.place(x=20,y=140)

      entry_red = customtkinter.CTkEntry(w1 , width=60)
      entry_red.place(x =180 , y = 140)


      def show4(value):
         entry_green.delete(0,END)
         entry_green.insert(0,str(int(value)))

      green_sli= customtkinter.CTkSlider(w1, from_=0, to= 255, width=150 ,  command=show4)
      green_sli.place(x=270,y=140)

      entry_green = customtkinter.CTkEntry(w1 , width=60)
      entry_green.place(x =420 , y = 140)

      
      def show5(value):
         entry_blue.delete(0,END)
         entry_blue.insert(0,str(int(value)))

      blue_sli= customtkinter.CTkSlider(w1, from_=0, to= 255, width=150,  command=show5)
      blue_sli.place(x=220,y=240)

      entry_blue = customtkinter.CTkEntry(w1 , width=60)
      entry_blue.place(x =380 , y = 240)


      bu1= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2'
                                 , command=lambda:Function.repxsels(frame , img,int(entry_row.get()),int(entry_col.get()),int(entry_red.get()),int(entry_green.get()),int(entry_blue.get())))
      bu1.place(x=140 , y=290)
      bu2= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2',command=back)
      bu2.place(x=300 , y=290)

   # inter face the color imag 
   def Color(w1, frame ,path):

      def back():
         entry_slider.destroy()
         slider.destroy()
         chek_but1.destroy()
         chek_but2.destroy()
         bu.destroy()
         back_button.destroy()
         
      def show(value):
         entry_slider.delete(0,END)
         entry_slider.insert(0,str(int(value)))

      slider = customtkinter.CTkSlider(w1, from_=1, to=500 , command=show)
      slider.place(x=20, y = 60)

      entry_slider = customtkinter.CTkEntry(w1 , width=60)
      entry_slider.place(x =230 , y = 50)

      chek_but1 =customtkinter.CTkCheckBox(w1 , text="Bright")
      chek_but1.place(x =300 , y = 50 )

      chek_but2 =customtkinter.CTkCheckBox(w1 , text="Cloudy")
      chek_but2.place(x =400 , y = 50 )

      bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:convert_image.chang_color( frame ,path , chek_but1.get(), chek_but2.get(), slider.get()))
      bu.place(x=100 , y=100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)

   # function inter face the make border 
   def MakeBorder1 ( w1, frame,path):

      def back():
         l1.destroy()
         l2.destroy()
         l3.destroy()
         l4.destroy()
         Up.destroy()
         Down.destroy()
         Left.destroy()
         Right.destroy()
         buton_enter.destroy()
         back_button.destroy()
         l1_1.destroy()
         combobox.destroy()

      l1_1 = customtkinter.CTkLabel(w1,text="MakeBorder", font=('times gor roman',15))
      l1_1.place(x=20,y=10)

      combobox = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['REPLICATE','REFLECT','REFLECT_101','WRAP', 'CONSTANT']) 
      combobox.place(x=100,y=10) 

      l1 = customtkinter.CTkLabel(w1,text="Up", font=('times gor roman',15))
      l1.place(x=50,y=50)
      l2 = customtkinter.CTkLabel(w1,text="Down",  font=('times gor roman',15))
      l2.place(x=150,y=50)
      l3 = customtkinter.CTkLabel(w1,text="Lift",  font=('times gor roman',15))
      l3.place(x=350,y=50)
      l4 =customtkinter.CTkLabel(w1,text="Right",  font=('times gor roman',15))
      l4.place(x=450,y=50)

      Up = customtkinter.CTkEntry(w1,width= 50 )
      Up.place(x=50,y=80)
      Down = customtkinter.CTkEntry(w1,width= 50 )
      Down.place(x=150,y=80)
      Left = customtkinter.CTkEntry(w1,width= 50 )
      Left.place(x=350,y=80)
      Right = customtkinter.CTkEntry(w1,width= 50 )
      Right.place(x=450,y=80)

      buton_enter = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:Function.border(w1, frame,combobox.get(),path,Up.get(),Down.get(),Left.get() , Right.get()))
      buton_enter.place(x=130 , y = 130)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=130)


   # inter face the function convert image 
   def interface_convert (w1 , fream, path):
      def back():
         l1_1.destroy()
         combobox.destroy()
         buton_enter.destroy()
         back_button.destroy()
         

      l1_1 = customtkinter.CTkLabel(w1,text="Convert to :", font=('times gor roman',15))
      l1_1.place(x=30,y=10)

      combobox = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['Double Precision','Gray','chang color' , 'Equalized']) 
      combobox.place(x=130,y=10)

      buton_enter = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose(fream , combobox.get(),path))
      buton_enter.place(x=100 , y = 100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)

      def chose ( fream , combo , path):
         if combo == 'Double Precision' :
            convert_image.Double_Precision(fream ,path )
         elif combo == 'Gray' :
            convert_image.Gray(fream , path)
         elif combo == 'chang color' :
            inter_face.Color(w1 , fream,path)
         elif combo == 'Equalized':
            convert_image.Equalized(fream,path)
         

   def interface_add_noise(w1 , frame , path):
      def interface_salt():   
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(float(value)))

         slider = customtkinter.CTkSlider(w1, from_=0.1, to=1.0 , command=show)
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="Noise Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:Noise.Salt_and_Pepper( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_Gaussin():   
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(float(value)))

         slider = customtkinter.CTkSlider(w1, from_=0.1, to=1.0 , command=show)
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="Noise Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:Noise.Gaussian( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 


      def interface_periodic():   
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(float(value)))

         slider = customtkinter.CTkSlider(w1, from_=0.1, to=1.0 , command=show)
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="Noise Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:Noise.Periodic( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_shot_noise():   
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=1, to=2700 , command=show)
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="Noise Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:Noise.shot_noise( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 




      ######### Min interface Noise ##############
      def back():
         l1_1.destroy()
         combobox.destroy()
         buton_enter.destroy()
         back_button.destroy()

      l1_1 = customtkinter.CTkLabel(w1,text="Type Noise:", font=('times gor roman',15))
      l1_1.place(x=30,y=10)

      combobox = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['SALT AND PEPPER','GAUSSIaN','PREIODIC' , "SHOT"]) 
      combobox.place(x=130,y=10)

      buton_enter = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose(combobox.get()))
      buton_enter.place(x=100 , y = 100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)

      def chose ( combo ):
         if combo == 'SALT AND PEPPER' :
            interface_salt()
         elif combo == 'GAUSSIaN' :
            interface_Gaussin()
         elif combo == 'PREIODIC':
            interface_periodic()
         elif combo == "SHOT" :
            interface_shot_noise()
         

   def interface_remove_noise(w1 , frame , path):

      def imterface_median_filter():   
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=1, to=50 , command=show )
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="filter Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:remove_noise.Median_filter( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_Bilateral_Filter():
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=1, to=10 , command=show )
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="filter Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:remove_noise.Bilateral_Filter( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_gussian_filter():
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=0, to=30 , command=show )
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="filter Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:remove_noise.Gussian_filter( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_Non_local_filter():
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=0, to=100 , command=show )
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="filter Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:remove_noise.Non_Local( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 

      def interface_Average_Filter():
         def back():
            entry_slider.destroy()
            slider.destroy()
            bu.destroy()
            back_button.destroy()
            label.destroy() 
            
         def show(value):
            entry_slider.delete(0,END)
            entry_slider.insert(0,str(int(value)))

         slider = customtkinter.CTkSlider(w1, from_=0, to=100 , command=show )
         slider.place(x=130, y = 60)

         entry_slider = customtkinter.CTkEntry(w1 , width=60)
         entry_slider.place(x =330 , y = 50)

         label = customtkinter.CTkLabel(w1 , text="filter Value :")
         label.place(x = 20 , y =60 )

         bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:remove_noise.Average_Filter( frame ,path , slider.get()))
         bu.place(x=100 , y=100)

         back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button.place(x=400 , y=100) 


      def back():
         l1_1.destroy()
         combobox.destroy()
         buton_enter.destroy()
         back_button.destroy()

      l1_1 = customtkinter.CTkLabel(w1,text="Type Filter:", font=('times gor roman',15))
      l1_1.place(x=30,y=10)

      combobox = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['Median Filter','Bilateral_Filter','Gussian_Filter' 
                                                                     , "Non-Local" , "Average Filter" ]) 
      combobox.place(x=130,y=10)

      buton_enter = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose(combobox.get()))
      buton_enter.place(x=100 , y = 100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)

      def chose ( combo ):
         if combo == 'Median Filter' :
            imterface_median_filter()
         elif combo == "Bilateral_Filter" :
            interface_Bilateral_Filter()
         elif combo == 'Gussian_Filter':
            interface_gussian_filter()
         elif combo == "Non-Local" : 
            interface_Non_local_filter()
         elif combo == "Average Filter" : 
            interface_Average_Filter()


   def interface_Edge_Detection (w1,frame , path) : 
      
   
      def Line_Detection(w1,frame,path):
            
         def back():
            l1_11.destroy()
            combobox1.destroy()
            buton_enter1.destroy()
            back_button1.destroy()
         l1_11 = customtkinter.CTkLabel(w1,text="Line Detection:", font=('times gor roman',15))
         l1_11.place(x=30,y=60)

         combobox1 = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['Line Width','Line Height','Line Height2' 
                                                                        , "Line Height and Width" , "All of the above" ]) 
         combobox1.place(x=150,y=60)

         buton_enter1 = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose_lin(combobox1.get()))
         buton_enter1.place(x=100 , y = 100)

         back_button1= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button1.place(x=400 , y=100)

         def chose_lin ( combo ):
            if combo == 'Line Width' :
               Edge_Detection.point_detection(frame , path)
            elif combo == 'Line Height' :
               Edge_Detection.line_height(frame,path)
            elif combo == 'Line Height2' :
               Edge_Detection.line_doubel_height(frame,path)
            elif combo == "Line Height and Width" : 
               Edge_Detection.line_doubel_height(frame,path)
            elif combo == "All of the above" :
               Edge_Detection.lin_add(frame , path)

      def type_Detection(w1,frame,path):
            
         def back():
            l1_11.destroy()
            combobox1.destroy()
            buton_enter1.destroy()
            back_button1.destroy()
         l1_11 = customtkinter.CTkLabel(w1,text="type Detection:", font=('times gor roman',15))
         l1_11.place(x=30,y=60)

         combobox1 = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['horizontal edge',"vertical edge",'combinte x and y']) 
         combobox1.place(x=150,y=60)

         buton_enter1 = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose_lin(combobox1.get()))
         buton_enter1.place(x=100 , y = 100)

         back_button1= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
         back_button1.place(x=400 , y=100)

         def chose_lin ( combo ):
            if combo == 'horizontal edge':
               Edge_Detection.horizontal_edge(frame , path)
            elif combo == "vertical edge":
               Edge_Detection.vertical_edge(frame,path)
            elif combo == 'combinte x and y':
               Edge_Detection.combinte_x_y(frame,path)

      def back():
         l1_1.destroy()
         combobox.destroy()
         buton_enter.destroy()
         back_button.destroy()

      l1_1 = customtkinter.CTkLabel(w1,text="Edge Detection:", font=('times gor roman',15))
      l1_1.place(x=30,y=10)

      combobox = customtkinter.CTkOptionMenu(w1 ,width=290 , values=['Point Detecation',"Line Detecation" , "an other type"]) 
      combobox.place(x=150,y=10)

      buton_enter = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:chose(combobox.get()))
      buton_enter.place(x=100 , y = 100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)

      def chose ( combo ):
         if combo == 'Point Detecation' :
            Edge_Detection.point_detection(frame , path)
         elif combo == "Line Detecation" :
            Line_Detection(w1,frame,path)
         elif combo == "an other type" : 
            type_Detection (w1 , frame  ,path)

   def interface_thershol(w1, frame ,path):

      def back():
         entry_slider.destroy()
         slider.destroy()
         bu.destroy()
         back_button.destroy()
         lab.destroy()
         
      def show(value):
         entry_slider.delete(0,END)
         entry_slider.insert(0,str(int(value)))

      lab = customtkinter.CTkLabel(w1 , text= "Threshold value ")
      lab.place(x = 200 ,y = 20)
      slider = customtkinter.CTkSlider(w1, from_=1, to=255 , command=show)
      slider.place(x=170, y = 60)

      entry_slider = customtkinter.CTkEntry(w1 , width=60)
      entry_slider.place(x =380 , y = 50)

      bu= customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command= lambda:thresholding.thre_shold(frame,path, entry_slider.get()))
      bu.place(x=100 , y=100)

      back_button= customtkinter.CTkButton(w1,text = 'Back',cursor='hand2' , command= back )
      back_button.place(x=400 , y=100)
