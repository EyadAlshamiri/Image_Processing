import cv2 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog 
import customtkinter
import os.path 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as Im
import random 
from Sgin import username

class spechile :
   def Show_Image(frame , path):
      
      img = cv2.imread(path)
      if img is None : 
         messagebox.showerror('error' , "pless select any image ")
      else :

         whidth_image = img.shape[1] 
         height_image = img.shape[0]
         
         if whidth_image <500 :
            new_value_width =500 - whidth_image
            new_width = whidth_image + new_value_width
         else : 
            new_value_width = whidth_image-500
            new_width = whidth_image-new_value_width

         if height_image < 500 : 
            new_value_height=500 - height_image
            new_height = height_image + new_value_height
         else : 
            new_value_height= height_image-500
            new_height = height_image-new_value_height

         new_imag = cv2.resize(img , (new_width ,new_height))

         cv2.imwrite("ImageNew.png", new_imag)

         image= customtkinter.CTkImage(dark_image=Im.open("ImageNew.png")
                                    , light_image=Im.open("ImageNew.png")
                                    ,size=(new_width,new_height))
               
         label = customtkinter.CTkLabel(frame , image = image  , text="" )
         label.place(x = 40 ,y = 30 ) 
      

   def imo2 (img ) :    # function to save the file in my combuter 
      file = filedialog.asksaveasfile(mode = 'w',filetypes=[('PNG Files')])
      if file : 
         filepath = os.path.abspath(file.name) # give the file bath and name path 
         cv2.imwrite(filepath,img)

   def Save_image(imag):
      if username.user_name == True :
         m2 = messagebox.askyesno("Save" ,"Do you wnt save image")
         if m2 == True: 
            img = cv2.imread(imag)
            spechile.imo2(img)

      else : m2 = messagebox.showerror("Error" ,"Please Log in")





''' class the function convert the Image'''
class convert_image :
   #function convert the img to Double precision 
   def Double_Precision( frame , path) :
      img = cv2.imread(path)
      if img is None :
         messagebox.showerror('error' , "pless select any image ")
      else :
         im_double = img.astype('float32')
         cv2.imwrite("ImageNew.png", im_double)
         spechile.Show_Image(frame ,"ImageNew.png")

   def Gray ( frame , path):
      img = cv2.imread(path)
      if img is None:
         messagebox.showerror('error' , "pless select any image ")
      else :
         gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         cv2.imwrite("ImageNew.png", gray)
         cv2.imwrite("save_image.png", gray)
         spechile.Show_Image(frame ,"ImageNew.png")
         



   # chang the color imag 
   def chang_color(frame ,  path , bright , cloudy , value ):
      img = cv2.imread(path)
      if img is None:
         messagebox.showerror('error' , "pless select any image ")
      else :
         if bright == 1 and cloudy == 0 :
            new =cv2.add(img,int(value)*(-1))
            cv2.imwrite("ImageNew.png", new)
            cv2.imwrite("save_image.png", new)
            spechile.Show_Image(frame ,"ImageNew.png")
         elif cloudy == 1 and bright == 0 :
            new =cv2.add(img,int(value))
            cv2.imwrite("ImageNew.png", new)
            cv2.imwrite("save_image.png", new)
            spechile.Show_Image(frame ,"ImageNew.png")
         else :
            messagebox.ERROR("Error" , "ples chek the mode : ")

   #function equalized
   def Equalized(frame , path):
      img = cv2.imread(cv2.samples.findFile(path))
      if img is None :
         print('The path is not corect ')
         exit(0)
      else :
         src = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         dst = cv2.equalizeHist(src)
         cv2.imwrite("ImageNew.png", dst)
         cv2.imwrite("save_image.png", dst)
         spechile.Show_Image(frame , "ImageNew.png" )

         m = messagebox.askyesno("show" , "Do you want Histogram")
         if m == True :
            histogram = np.histogram(src, bins=img.shape[1])[0]
            histogram2 = np.histogram(dst, bins=dst.shape[1])[0]
            # Plot the histogram.
            plt.figure()
            plt.bar(range(img.shape[1]), histogram)
            plt.xlabel("Pixel value")
            plt.ylabel("Number of pixels")
            plt.title("Histogram of the input image")
            plt.figure()
            plt.bar(range(dst.shape[1]), histogram2)
            plt.xlabel("Pixel value")
            plt.ylabel("Number of pixels")
            plt.title("Histogram of the equalize histograms")
            plt.show()


''' Class function the opration in Image'''
class Function :
   # function resize the image 
   def resize ( path , w , h) :
      img =cv2.imread(path) 
      if img is None:
         messagebox.showerror('error' , "pless select any image ")
      else :
         if w == 0 or h == 0:
               messagebox.showerror("Error" , 'Pless Enter width and heigth')
         else:
            new = cv2.resize(img , (w,h))
            cv2.imwrite("save_image.png", new)

   # function add point in image 
   def repxsels(frame , img , row,column,red,green,blue):
      if img is None:
         messagebox.showerror('error' , "pless select any image ")
      else :
         if int(row) > img.shape[0] or int(column) > img.shape[1] :
            messagebox.showerror("Error",'the point you selected is not in the image')
         else :
            if int(red) > 255 or int(green) > 255 or int(blue) > 255 :
               messagebox.showerror("Error",'Each color has values from 0 to 255 ')
            else:
               img[int(row),int(column)] = [int(blue),int(green),int(red)]
               cv2.imwrite("ImageNew.png", img)
               cv2.imwrite("save_image.png", img)
               spechile.Show_Image(frame , "ImageNew.png" )
               #spechile.Show_and_Save(img)

   # function merge oetuen 2 images 
   def to_merge(frame, path1 , path2 , value1 , value2 ,brightnes ):

      img1 = cv2.imread(path1)
      img2 = cv2.imread(path2)

      if img1 is None or img2 is None :
         messagebox.showerror('error' , "pless select any image ")
      else :
         if img1.shape != img2.shape :
            new_img1 = cv2.resize(img1,(500,500))
            new_img2 = cv2.resize(img2,(500,500))

         merge = cv2.addWeighted(new_img1,float(value1),new_img2,float(value2), int(brightnes))
         cv2.imwrite("ImageNew.png", merge)
         cv2.imwrite("save_image.png", merge)
         spechile.Show_Image(frame ,"ImageNew.png")

   # creat Border in the image 
   def border(w1, frame,combobox ,path, up,down,lift,right):
      img = cv2.imread(path)
      if img is None:
         messagebox.showerror('error' , "pless select any image ")
      else:
         if combobox == "REPLICATE" :
            replicate = cv2.copyMakeBorder(img,int(up),int(down),int(lift),int(right),cv2.BORDER_REPLICATE)
            cv2.imwrite("ImageNew.png", replicate)
            cv2.imwrite("save_image.png", replicate)
            spechile.Show_Image(frame ,"ImageNew.png")

         elif combobox == "REFLECT" :
            reflect = cv2.copyMakeBorder(img,int(up),int(down),int(lift),int(right),cv2.BORDER_REFLECT)
            cv2.imwrite("ImageNew.png", reflect)
            spechile.Show_Image(frame ,"ImageNew.png")

         elif combobox == "REFLECT_101" :
            reflect101 = cv2.copyMakeBorder(img,int(up),int(down),int(lift),int(right),cv2.BORDER_REFLECT_101)
            cv2.imwrite("ImageNew.png",reflect101)
            cv2.imwrite("save_image.png", reflect101)
            spechile.Show_Image(frame ,"ImageNew.png")

         elif combobox == "WRAP" :
            wrap = cv2.copyMakeBorder(img,int(up),int(down),int(lift),int(right),cv2.BORDER_WRAP)
            cv2.imwrite("ImageNew.png", wrap)
            cv2.imwrite("save_image.png", wrap)
            spechile.Show_Image(frame ,"ImageNew.png")

         elif combobox == "CONSTANT" :
            l5 = customtkinter.CTkLabel(w1,text="Red", font=('times gor roman',15))
            l5.place(x=50,y=160)
            l6 = customtkinter.CTkLabel(w1,text="Green",  font=('times gor roman',15))
            l6.place(x=300,y=160)
            l7 = customtkinter.CTkLabel(w1,text="Blue",  font=('times gor roman',15))
            l7.place(x=250,y=260)
            
            def show2(value):
               entry_red.delete(0,END)
               entry_red.insert(0,str(int(value)))

            red_sli= customtkinter.CTkSlider(w1, from_=0, to= 255 , width=150, command=show2)
            red_sli.place(x=10,y=200)

            entry_red = customtkinter.CTkEntry(w1 , width=60)
            entry_red.place(x =160 , y = 200)

            def show4(value):
               entry_green.delete(0,END)
               entry_green.insert(0,str(int(value)))

            green_sli= customtkinter.CTkSlider(w1, from_=0, to= 255, width=150 ,  command=show4)
            green_sli.place(x=270,y=200)

            entry_green = customtkinter.CTkEntry(w1 , width=60)
            entry_green.place(x =420 , y =200)
      
            def show5(value):
               entry_blue.delete(0,END)
               entry_blue.insert(0,str(int(value)))

            blue_sli= customtkinter.CTkSlider(w1, from_=0, to= 255, width=150,  command=show5)
            blue_sli.place(x=220,y=280)

            entry_blue = customtkinter.CTkEntry(w1 , width=60)
            entry_blue.place(x =380 , y = 280)


            buton_enter2 = customtkinter.CTkButton(w1,text = 'Enter',cursor='hand2', command=lambda:CONS(up,down,lift,right))
            buton_enter2.place(x=30 , y = 280)
            
            def CONS(Up , Down , Lift ,Right):
               constant= cv2.copyMakeBorder(img,int(Up),int(Down),int(Lift),int(Right),cv2.BORDER_CONSTANT,value=[int(entry_blue.get()),int(entry_green.get()),int(entry_red.get())])
               cv2.imwrite("ImageNew.png", constant)
               cv2.imwrite("save_image.png", constant)
               spechile.Show_Image(frame ,"ImageNew.png")

               entry_red.destroy()
               red_sli.destroy() 
               entry_green.destroy()
               green_sli.destroy()
               entry_blue.destroy()
               blue_sli.destroy()
               l5.destroy()
               l6.destroy()
               l7.destroy() 

               buton_enter2.destroy()

class Filters :
   def Mean_Filter(path):
      im= cv2.imread(path)
      cv2.imshow('image Before Linear ',im)
      mean_filter=cv2.blur(im,(4,4))
      spechile.Show_and_Save(mean_filter)


class Noise :
   def Salt_and_Pepper(frame , path , number) : 
      # ADD SALT AND PEPPER NOISE 
      def add_noise(img): 
         # Getting the dimensions of the image 
         row , col , colo = img.shape 
         # Randomly pick some pixels in the 
         # image for coloring them white 
         number_noise = number*1000000.0 
         number_noise = int(number_noise)
         number_of_pixels = random.randint(1000,number_noise) 
         for i in range(number_of_pixels): 
            # Pick a random y coordinate 
            y_coord=random.randint(0, row - 1) 
            # Pick a random x coordinate 
            x_coord=random.randint(0, col - 1) 
            # Color that pixel to white 
         img[y_coord][x_coord] = 255
         # Randomly pick some pixels in 
         # the image for coloring them black 
         # Pick a random number between 300 and 10000 
         number_of_pixels = random.randint(1000 , number_noise) 
         for i in range(number_of_pixels): 
            # Pick a random y coordinate 
            y_coord=random.randint(0, row - 1) 
            # Pick a random x coordinate 
            x_coord=random.randint(0, col - 1) 
            # Color that pixel to black 
            img[y_coord][x_coord] = 0
         return img 

      # salt-and-pepper noise can 
      # be applied only to grayscale images 
      # Reading the color image in grayscale image 
      img = cv2.imread(path) 
      #Storing the image 
      imnoise= add_noise(img)
      cv2.imwrite("ImageNew.png", imnoise)
      cv2.imwrite("save_image.png", imnoise)
      spechile.Show_Image(frame ,"ImageNew.png")

      
   def Gaussian(frame , path , number) : 
      image = cv2.imread(path)
      # Define the noise parameters
      mean = 0
      sigma = int(number*100.0)
      # Generate Gaussian noise
      noise = np.random.normal(mean, sigma, image.shape)
      # Add noise to the image
      noisy_image = image + noise
      # Normalize the image to range [0, 255]
      noisy_image = cv2.normalize(noisy_image, noisy_image, 0,255, cv2.NORM_MINMAX, dtype=-1)
      noisy_image = noisy_image.astype(np.uint8)
      # Display the original and noisy images
      cv2.imwrite("ImageNew.png", noisy_image)
      cv2.imwrite("save_image.png", noisy_image)
      spechile.Show_Image(frame ,"ImageNew.png")
      # Save noisy image
      #cv2.imwrite('noisy_img.jpg', noisy_img)
      # add gaussian noise to image <<<<<<<<<<<<<<<<GAUSION NOISE 

   def Periodic(frame , path , number):
      # Read the image
      image = cv2.imread(path)
      # Convert the image to grayscale
      grayscale_image =  image #cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      # Define the noise parameters
      amplitude = int((number*1000)/2)
      frequency = 0.1
      phase = 0
      # Generate periodic noise
      rows, cols , color = grayscale_image.shape
      noise = np.zeros((rows, cols), dtype=np.float32)
      for i in range(rows):
         for j in range(cols):
               noise[i, j ] = amplitude * np.sin(2.0 * np.pi * frequency* i + phase)
      noise = cv2.cvtColor(noise,cv2.COLOR_BGR2RGB)
      # Add periodic noise to the image
      noisy_image = grayscale_image + noise
      # Normalize the noisy image to range [0, 255]
      noisy_image = cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
      noisy_image = noisy_image.astype(np.uint8)
      # Display the original and noisy images
      cv2.imwrite("ImageNew.png", noisy_image)
      cv2.imwrite("save_image.png", noisy_image)
      spechile.Show_Image(frame ,"ImageNew.png")


   def shot_noise(frame , path , number):
      #add shot noise to an image using OpenC 
      image = cv2.imread(path)
      mean = 0
      sigma = int(number+300)
      shot_noise = np.random.poisson(mean, image.shape)
      
      noisy_image = image + shot_noise

      noisy_image = cv2.normalize(noisy_image, noisy_image, mean, sigma,cv2.NORM_MINMAX, dtype=-1)
      noisy_image = noisy_image.astype(np.uint8)
      cv2.imwrite("ImageNew.png", noisy_image)
      cv2.imwrite("save_image.png", noisy_image)
      spechile.Show_Image(frame ,"ImageNew.png")



class remove_noise:

   def Median_filter(frame , path , number) : 
      im= cv2.imread(path)
      # Apply median filter to remove salt and pepper noise
      number = int(number)
      if number%2 == 0 :
         number = number-1 
      denoised = cv2.medianBlur(im, number)
      cv2.imwrite("ImageNew.png", denoised)
      cv2.imwrite("save_image.png", denoised)
      spechile.Show_Image(frame ,"ImageNew.png")

   def Bilateral_Filter(frame , path , number) : 
      # Read the noisy image
      image = cv2.imread(path)
      # Convert the image to grayscale
      #grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      # Apply bilateral filtering
      number = int(number)
      filtered_image = cv2.bilateralFilter(image, number, 75, 75)
      # Display the original and denoised images
      cv2.imwrite("ImageNew.png", filtered_image)
      cv2.imwrite("save_image.png", filtered_image)
      spechile.Show_Image(frame ,"ImageNew.png")
      
   def Gussian_filter(frame , path , number) : 
      # way 2 Gaussian filtter
      # Load the noisy image
      noisy_image = cv2.imread(path)
      number = int(number)
      if number%2==0 : 
         number = number - 1 
      # Apply Gaussian filter to remove noise
      clean_image = cv2.GaussianBlur(noisy_image, (number, number), 0)
      # Display the cleaned image
      cv2.imwrite("ImageNew.png", clean_image)
      cv2.imwrite("save_image.png",clean_image)
      spechile.Show_Image(frame ,"ImageNew.png")

   
   def Non_Local(frame , path , number): 
      # way 3 
      # Read the noisy image
      image = cv2.imread(path)
      number = int(number)
      if number%2==0 : 
         number = number - 1 
      # Convert the image to grayscale
      #grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      # Apply non-local means denoising
      dst = cv2.fastNlMeansDenoisingColored(image, number,number,number,number)
      # Display the original and denoised images
      cv2.imwrite("ImageNew.png", dst)
      cv2.imwrite("save_image.png",dst)
      spechile.Show_Image(frame ,"ImageNew.png")

   def Average_Filter (frame , path ,number) : 
      # a way 4 by average filter 
      # Read the noisy image
      image = cv2.imread(path)
      # Apply average filter with window size 3x3
      number = int(number)
      filtered_image = cv2.blur(image, (number,number))
      # Display the original and filtered images
      cv2.imwrite("ImageNew.png", filtered_image)
      cv2.imwrite("save_image.png",filtered_image)
      spechile.Show_Image(frame ,"ImageNew.png")


class Edge_Detection :
         
   def  point_detection(frame , path ) :
      im= cv2.imread(path)
      #image point detection
      im_grey= im #cv.cvtColor(im,cv.COLOR_BGR2GRAY)
      mask=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
      #mask1=mask1/ np.sum(mask1)
      res_im=cv2.filter2D(im_grey,-1,mask)
      cv2.imwrite("ImageNew.png", res_im)
      cv2.imwrite("save_image.png",res_im)
      spechile.Show_Image(frame ,"ImageNew.png")

   def line_width(frame,path):
      im= cv2.imread(path)
      Mask_width=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
      res =cv2.filter2D(im,-1,Mask_width)
      cv2.imwrite("ImageNew.png", res)
      cv2.imwrite("save_image.png",res)
      spechile.Show_Image(frame ,"ImageNew.png")
   def line_height(frame,path):
      im= cv2.imread(path)
      Mask_width=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
      res =cv2.filter2D(im,-1,Mask_width)
      cv2.imwrite("ImageNew.png", res)
      cv2.imwrite("save_image.png",res)
      spechile.Show_Image(frame ,"ImageNew.png")

   def line_doubel_height(frame,path):
      im= cv2.imread(path)
      Mask_width=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
      res =cv2.filter2D(im,-1,Mask_width)
      cv2.imwrite("ImageNew.png", res)
      cv2.imwrite("save_image.png",res)
      spechile.Show_Image(frame ,"ImageNew.png")

   def line_width(frame,path):
      im= cv2.imread(path)
      Mask_width =np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
      res =cv2.filter2D(im,-1,Mask_width)
      cv2.imwrite("ImageNew.png", res)
      cv2.imwrite("save_image.png",res)
      spechile.Show_Image(frame ,"ImageNew.png")

   def lin_add(frame,path):
      im= cv2.imread(path)
      Mask_width=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
      Mask_height=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
      Mask_dobel_height=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
      Mask_width_and_height=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
      res_im_h=cv2.filter2D(im,-1,Mask_width)
      res_im_45=cv2.filter2D(im,-1,Mask_height)
      res_im_v=cv2.filter2D(im,-1,Mask_dobel_height)
      res_im_n45=cv2.filter2D(im,-1,Mask_width_and_height)
      res =cv2.add(res_im_h,res_im_v)
      cv2.imwrite("ImageNew.png", res)
      cv2.imwrite("save_image.png",res)
      spechile.Show_Image(frame ,"ImageNew.png")

   def horizontal_edge(frame, path) :
      im= cv2.imread(path)
      im_grey= im 
      # Sobel
      sobel_x = np.array([[-1, -2, -1],
      [ 0, 0, 0],
      [ 1, 2, 1]])
      # horizontal edge
      edge_x = cv2.filter2D(src=im_grey, ddepth=-1, kernel=sobel_x)
      edge_x[edge_x != 0] = 255
      cv2.imwrite("ImageNew.png", edge_x)
      cv2.imwrite("save_image.png",edge_x)
      spechile.Show_Image(frame ,"ImageNew.png")


   def vertical_edge(frame,path) : 
      im= cv2.imread(path)
      im_grey= im 
      # Sobel
      sobel_y = np.array([[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]])
      # vertical edge
      edge_y = cv2.filter2D(src=im_grey, ddepth=-1, kernel=sobel_y)
      edge_y[edge_y != 0] = 255
      cv2.imwrite("ImageNew.png", edge_y)
      cv2.imwrite("save_image.png",edge_y)
      spechile.Show_Image(frame ,"ImageNew.png")

   def combinte_x_y(frame,path) :
      #image edge detection
      im= cv2.imread(path)
      im_grey= im 
      # Sobel
      sobel_x = np.array([[-1, -2, -1],
      [ 0, 0, 0],
      [ 1, 2, 1]])
      sobel_y = np.array([[-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]])
      # horizontal edge
      edge_x = cv2.filter2D(src=im_grey, ddepth=-1, kernel=sobel_x)
      edge_x[edge_x != 0] = 255
      # vertical edge
      edge_y = cv2.filter2D(src=im_grey, ddepth=-1, kernel=sobel_y)
      edge_y[edge_y != 0] = 255
      # combinte the x and y edge
      add_edge = edge_x + edge_y
      cv2.imwrite("ImageNew.png", edge_y)
      cv2.imwrite("save_image.png",edge_y)
      spechile.Show_Image(frame ,"ImageNew.png")


class thresholding : 
   def thre_shold(frame , path , number) : 
      threshold_value= int(number)
      img = cv2.imread(path)
      _,binary_image=cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)
      cv2.imwrite("ImageNew.png", binary_image)
      cv2.imwrite("save_image.png",binary_image)
      spechile.Show_Image(frame ,"ImageNew.png")
