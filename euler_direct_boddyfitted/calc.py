#!/usr/bin/python

import os as os

resultfile = open('manual_sensitivities.csv','w')
resultfile.write('stencilsize,dLx,dLy\n')

for fname in sorted(os.listdir('.')): #sorted is needed since the reults might be written out of order
    if fname[0:3]=='sim':
        with file(fname+'/sdesign/naca_plus.sdesign') as f:
            lines=f.readlines()
            index1=lines.index('ABSVAR\n')
            absvar=float(lines[index1+2].split()[1])
            print absvar
        with file(fname+'/results/naca_plus_steady.liftdrag') as f:
            s = f.readlines()
            lastrow = s[-1]
            split   = lastrow.split()
            Lx_plus=float(split[4])
            Ly_plus=float(split[5])
        with file(fname+'/results/naca_minus_steady.liftdrag') as f:
            s = f.readlines()
            lastrow = s[-1]
            split   = lastrow.split()
            Lx_minus=float(split[4])
            Ly_minus=float(split[5])
        dLx="{:.10e}".format((Lx_plus-Lx_minus)/(absvar*2  ))
        dLy="{:.10e}".format((Ly_plus-Ly_minus)/(absvar*2  ))
        absvar="{:.10e}".format(absvar)
        writeline=",".join([absvar,dLx,dLy])
        resultfile.write(writeline)
        resultfile.write("\n")
resultfile.close()


resultfile = open('analytic_sensitivities.csv','w')
resultfile.write('ABSVAR,dLx,dLy\n')

with file('./anasim/results/naca_sens.liftdrag') as f:
    f.readline()#throw away first line
    for line in f:
        split1=line.split()
        var=split1[0]
        dLx=split1[5]
        dLy=split1[6]
        writeline=",".join([var,dLx,dLy])
        resultfile.write(writeline)
        resultfile.write("\n")
