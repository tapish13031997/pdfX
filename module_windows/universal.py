#file containing global variables
import commands
import os
def init():
  global data
  data={}
  global tree
  global filename #filename of pdf file containing patents
  filename="15"
  global current_dir 
  current_dir = os.getcwd() #In future use in-built python function which is platform independent.
  global pdf_folder  #name of folder containing pdf burst files
  pdf_folder="3"
  global tag_folder #name of folder containing tag-html file
  tag_folder="tag_folder"
  global workbook
  global worksheet
  global date_format
  global row #row counter
  global flag #Flag for process of extraction has started or not 
  flag=0

