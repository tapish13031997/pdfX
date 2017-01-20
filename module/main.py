import file1
import convert
import universal
import commands
import excelwriter
def run_command(string):
  if commands.getstatusoutput(string)[0]==1:
     raise NameError("ERROR IN Commands.getstatusoutput "+string)
universal.init()  #for initializing global variables 
universal.filename=str(input("Enter filename(without extension)"))
excelwriter.init()
run_command("mkdir "+universal.pdf_folder)
run_command("mkdir "+universal.tag_folder)
run_command("pdftk "+universal.filename+".pdf burst output "+universal.current_dir+"/"+universal.pdf_folder+"/%d.pdf")
for i in range(8,500):
  print(i)
  universal.filename=str(i);
  convert.convert() #for initializing conversion of files
  file1.begin()
  excelwriter.loop()
universal.workbook.close()  
run_command("rm -r "+universal.pdf_folder)
run_command("rm -r "+universal.tag_folder)

