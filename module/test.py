import commands
import universal
def convert():
  if commands.getstatusoutput("pdf2txt.py -t html "+"-o "+universal.filename+".html "+universal.current_dir+"/"+universal.filename+"/"+universal.filename+".pdf")[0]==1:
    raise NameError("ERROR IN Commands.getstatusoutput for file "+universal.filename)
  if commands.getstatusoutput("pdf2txt.py -t tag "+"-o "+universal.filename+universal.filename+".html "+universal.current_dir+"/"+universal.filename+"/"+universal.filename+".pdf")[0]==1:
    raise NameError("ERROR IN Commands.getstatusoutput for file "+universal.filename+universal.filename)       
