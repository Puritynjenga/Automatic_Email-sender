#
# # ######################################
# import os
#
#
# """print the working directories"""
# def current_dir():
#  cwd = os.getcwd()
#  print(cwd)
#
#  def file_path(filename):
#   path = os.path.abspath(filename)
#   print(path)
# #
# current_dir()
# filename = "scripting.py"
# file_path = (filename)
# ################################
# """printing time"""
# import time
# epc = time.time()
# print(epc)
# localtime = time.localtime(epc)
# print(localtime)
# """printing a specific item"""
# print(localtime.tm_year)
# """printing then time in a more formatted way"""
# print(time.ctime(epc))
# #################################
"""automating emails"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "puritynjenga895@gmail.com"
receiver_email = "aloomanase@gmail.com"  # Replace with the recipient's email
password = "oysdhukijlmodozi"   # Replace with your app-specific password

#Create the email content
message = MIMEMultipart()
message["Friends to hold"] = sender_email
message["aloomanase@gmail.com"] = receiver_email
message["Subject"] = "PARTY INVITATION"

body = ("Please purpose to attend my birthday party on Saturday")
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Log in to the server
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    # Close the connection to the server
    server.quit()



###################################
# """creating files"""
# from os import path
# def createFile(dest):
#  if not(path.isfile(dest)):
#   f = open(dest,'w')
#   f.write("Welcome to python scripting")
#   f.close()
# dest =  "C:\\Users\\purit\\Desktop\\myfiles.py\\sample.txt"
# createFile(dest)
# print("File created. I am glad you are learning")
######################################
#Nested functions
# def func1(called_func):
#  print("This is the first function")
#  def nested_func1():
#    print("This is the nested function")
#    called_func()
#  return nested_func1
#
# """The @ or decorator allows outer_func to be called thru func1 thus calling all the funcs.now outer_func becomes the arg for func 1"""
# @func1
# def outer_func():
#  print("This is the outer func")
# outer_func()
############################
#Static and Classmethods
# class Demo:
#  @classmethod
#  def addOne(self,y):
#    return y + 1
#
#  @staticmethod
#  def addTwo(y):
#     return y + 2
#
# print(Demo.addOne(15))
# obj = Demo()
# print(obj.addTwo(15))
###############################
#Creating labels
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frame = Frame(root)
#
# labelText = StringVar()
# label = Label(frame,textvariable = labelText)
# labelText.set("This is a label")
#
# button = Button(frame,text = "Click Me")
# label.pack()
# button.pack()
# frame.pack()
# root.mainloop()
#########################################3

# import tkinter
# m = tkinter.Tk()
# '''
# widgets are added here
# '''
# m.mainloop()






