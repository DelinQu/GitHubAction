import sys, getopt, os

asciiText = ""\
    "##   ##  #######    ###    ##     ######  ##   ##            #####   ##   ##  #######   #####   ##   ##  \n" \
    "##   ##  ##        ## ##   ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "#######  #####    ##   ##  ##       ##    #######           ##       #######  #####    ##       ####     \n" \
    "##   ##  ##       #######  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  #######  ##   ##  #######  ##    ##   ##            #####   ##   ##  #######   #####   ##   ##  \n"

if __name__ == "__main__":
    print(asciiText)
    print(os.environ["USERNAME"],os.environ["PASSWD"],os.environ["EMAIL"])
