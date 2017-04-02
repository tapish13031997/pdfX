import main
import universal
universal.init()
#year=input("year\n")
#s=main.run_command("ls "+str(year),1).split("\n")
#fappend.close() 
#for x in s:
#  universal.filename=x
#  main.run_command("mv "+str(year)+"/"+str(x)+" "+universal.current_dir)
#  main.initial()
#  main.run_command("mv "+universal.current_dir+"/"+str(x)+" "+str(year))

#fappend=open("log.txt",'a')   
#fappend.write("\n********"+"\n"+str(year)+"\n*************\n\n\n")
#fappend.close()   
#i=input("Filename\n")
i=1
while i<=1:
  universal.filename=str(i)
  universal.logfile=str(i)
  main.initial()
  i+=1
