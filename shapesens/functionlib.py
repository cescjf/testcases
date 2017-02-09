

def extractLifts(filename):
    #reading the lift results for that simulations
    Lx=0
    Ly=0
    with open(filename) as f:
        s = f.readlines()
        lastrow = s[-1]
        split   = lastrow.split()
        Lx=float(split[4])
        Ly=float(split[5])
    return Lx, Ly





def doFD(Lx_minus,Lx_plus,Ly_minus,Ly_plus,absvar):
    dLx="{:.10e}".format((Lx_plus-Lx_minus)/(absvar*2  ))
    dLy="{:.10e}".format((Ly_plus-Ly_minus)/(absvar*2  ))
    absvar="{:.10e}".format(absvar)
    return ",".join([absvar,dLx,dLy])


def writeCSVana(fluidresultfile,csvfile):
    #opeing the .csv file
    resultfile = open(csvfile,'w')
    resultfile.write('ABSVAR,dLx,dLy\n')

    with open(fluidresultfile) as f:
        f.readline()#throw away first line
        for line in f:
            split1=line.split()
            var=split1[0]
            dLx=split1[5]
            dLy=split1[6]
            writeline=",".join([var,dLx,dLy])
            resultfile.write(writeline)
            resultfile.write("\n")
    resultfile.close()
    print(fluidresultfile+" -> "+csvfile)
    return 0
