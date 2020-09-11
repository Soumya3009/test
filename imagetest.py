#!/usr/bin/env python3
def main():
    infile=open("tree.jpg", "rb")
    outfile=open("out.jpg", "wb")
    while True:
        buf=infile.read(1024)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print("\nDone\n")
if  __name__=='__main__':main()

