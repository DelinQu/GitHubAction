
import sys, getopt

asciiText = ""\
    "##   ##  #######    ###    ##     ######  ##   ##            #####   ##   ##  #######   #####   ##   ##  \n" \
    "##   ##  ##        ## ##   ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "#######  #####    ##   ##  ##       ##    #######           ##       #######  #####    ##       ####     \n" \
    "##   ##  ##       #######  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  #######  ##   ##  #######  ##    ##   ##            #####   ##   ##  #######   #####   ##   ##  \n"

def getArg(argv):
   username = ''
   passwd = ''
   email = ''

   try:
       opts, args = getopt.getopt(argv,"hu:p:e:")
   except getopt.GetoptError:
      print('main.py -u <username> -p <passwd> -e <email>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('main.py -u <username> -p <passwd> -e <email>')
         sys.exit()
      elif opt == "-u":
         username = arg
      elif opt == "-p":
         passwd = arg
      elif opt == "-e":
         email = arg
   return username,passwd,email

if __name__ == "__main__":
    print(asciiText)
    print(getArg(sys.argv[1:]))
