#!/usr/bin/env python3
f1=open("stud.txt", "w")
f1.write("arun,10-20-30-40\n")
f1.write("varun,11-21-31-41\n")
f1.write("hari,12-22-32-42\n")
f1.write("arun,100-200-300-400\n")
f1.close()

f1=open("stud.txt", "r")
f2=open("out.csv", "w")

f2.write("name,total\n")

for elem in f1:
        name, *mlst = elem.rstrip("\n").replace(",", "-").split("-")
        mlst = [int(e) for e in mlst]
        print(mlst)
        print(name, sum(mlst))
        f2.write("%s,%s" %(name, sum(mlst)))
f1.close()
f2.close()


