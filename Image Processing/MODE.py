import customtkinter
class Mode :
   def dark():
      customtkinter.set_appearance_mode("dark")
      customtkinter.set_default_color_theme("dark-blue")

   def white ():
      customtkinter.set_appearance_mode("System")
      customtkinter.set_default_color_theme("blue")