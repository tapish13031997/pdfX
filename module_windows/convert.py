import commands
import universal
import subprocess
import os
cmd = "C:\Python27\python.exe C:\Python27\Scripts\pdf2txt.py -t tag -Y exact -o "
def run_command(string):
  if commands.getstatusoutput(string)[0]==1:
     raise NameError("ERROR IN Commands.getstatusoutput "+string)
    
def convert():
  run = subprocess.Popen(cmd+universal.tag_folder+"/"+universal.filename+universal.filename+".html "+universal.pdf_folder+"/"+universal.filename+".pdf", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = run.communicate()
    #  run_command("pdf2txt.py -t html -Y exact "+"-o "+universal.filename+".html "+universal.current_dir+"/"+universal.year+"/"+universal.filename+".pdf")
  #run_command("pdf2txt.py -t tag -Y exact "+"-o "+universal.current_dir+"/"+universal.tag_folder+"/"+universal.filename+universal.filename+".html "+universal.current_dir +"/"+ universal.pdf_folder+"/"+universal.filename+".pdf")
def remove():
  #run_command("rm "+universal.current_dir+"/"+universal.tag_folder+"/"+universal.filename+universal.filename+".html")
  os.remove(universal.tag_folder+"/"+universal.filename+universal.filename+".html")
#universal.init();
#for i in range(8,622):
#  #print(i)
#  universal.filename=str(i);
#  convert() #for initializing conversion of files
    
