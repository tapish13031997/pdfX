import file1
import convert
import universal
import commands
import excelwriter
def run_command(string):
  if commands.getstatusoutput(string)[0]==1:
     raise NameError("ERROR IN Commands.getstatusoutput "+string)
universal.init()  #for initializing global variables 
universal.filename=str(input("Enter filename(without extension)\n"))
excelwriter.init()
run_command("mkdir "+universal.pdf_folder)
run_command("mkdir "+universal.tag_folder)
run_command("pdftk "+universal.filename+".pdf burst output "+universal.current_dir+"/"+universal.pdf_folder+"/%d.pdf")
i=1
temp=universal.filename #assigning filename to temp
while 1:    #loop for locating first patent file
  universal.filename=str(i);
  convert.convert() #for initializing conversion of files
  i+=1
  if file1.begin()!=-1:
    excelwriter.loop()
    break

fappend=open("log.txt",'a')   
fappend.write("\n********"+"\n"+temp+"\n*************\n")
fappend.close()
universal.flag=1 #Process of extraction will start    
while 1:
  universal.filename=str(i);
  convert.convert() #for initializing conversion of files
  if file1.begin()==-1:
    break
  excelwriter.loop()
  i+=1        
universal.workbook.close()  
run_command("rm -r "+universal.pdf_folder)
run_command("rm -r "+universal.tag_folder)
fappend=open("log.txt",'a')
fappend.write("********"+"\n"+temp+"\n*************\n")
fappend.close()

