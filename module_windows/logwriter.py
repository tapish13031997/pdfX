def logwrite(log):
    log_file = open("log.txt","a")
    log_file.write(log+'\n')
    log_file.close()
