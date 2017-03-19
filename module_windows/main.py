import file1
import convert
import universal
import commands
import excelwriter
import logwriter
import sys
import os
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader

def burstpdf(): 
  infile = PdfFileReader(open(universal.filename+".pdf", 'rb'))
  no_of_pages = infile.getNumPages()
  for i in xrange(infile.getNumPages()):
      p = infile.getPage(i)
      outfile = PdfFileWriter()
      outfile.addPage(p)
      with open(universal.pdf_folder+'/%d.pdf' % i, 'wb') as f:
          outfile.write(f)
  return no_of_pages

def run_command(string):
  if commands.getstatusoutput(string)[0]==1:
     raise NameError("ERROR IN Commands.getstatusoutput "+string)
      
universal.init()  #for initializing global variables 
universal.filename=str(input("Enter filename(without extension)\n"))
temp = universal.filename
logwriter.logwrite("\n********"+"\n"+universal.filename+"\n*************\n");
no_of_pages=0
try:
  excelwriter.init()
except:
  logwriter.logwrite("ERROR : Unable to create a xlsx file for %s" % universal.filename)
  sys.exit()
try:
  #run_command("mkdir "+universal.pdf_folder)
  os.mkdir(universal.pdf_folder)
  #print("good")
except:
  logwriter.logwrite("ERROR : Unable to create pdf_folder for %s" % universal.filename)
  sys.exit()
try:
  #run_command("mkdir "+universal.tag_folder)
  os.mkdir(universal.tag_folder)
  #print("good")
except:
  logwriter.logwrite("ERROR : Unable create tag_folder for %s" % universal.filename)
  sys.exit()
try:
  #run_command("pdftk "+universal.filename+".pdf burst output "+universal.current_dir+"/"+universal.pdf_folder+"/%d.pdf")
  no_of_pages=burstpdf()
  #print("good")
except:
  logwriter.logwrite("ERROR : Unable to burst %s" % universal.filename)
  sys.exit()
  
i=0
while i<no_of_pages:    #loop for locating first patent file
  universal.filename=str(i);
  try:
    convert.convert() #for initializing conversion of files
  except:
    logwriter.logwrite("ERROR : Unable to convert %s.pdf into .html file" % universal.filename)
    continue
  if file1.begin()!=-1:
    excelwriter.loop()
    break;
  i=i+1

universal.flag=1 #Process of extraction will start

while i<no_of_pages:
  universal.filename=str(i);
  try:
    convert.convert() #for initializing conversion of files
  except:
    logwriter.logwrite("ERROR : Unable to convert %s.pdf into .html file" % universal.filename)
    continue
  if file1.begin()==-1:
    break
  excelwriter.loop()
  i=i+1        
universal.workbook.close()  
try:
  #run_command("rm -r "+universal.pdf_folder)
  shutil.rmtree(universal.pdf_folder)
except:
  logwriter.logwrite("ERROR : Unable to delete pdf_folder %s" % temp)
try:
  #run_command("rm -r "+universal.tag_folder)
  shutil.rmtree(universal.tag_folder)
except:
  logwriter.logwrite("ERROR : Unable to delete tag_folder %s" % temp)
logwriter.logwrite("\n********"+"\n"+temp+"\n*************\n");
