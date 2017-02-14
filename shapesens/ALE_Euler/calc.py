#!/usr/bin/python

import os as os
import sys

sys.path.append("../")

from functionlib import extractLifts, doFD, writeCSVana
from functionlib2 import MainText, ReadInfo, ReadInputFiles


os.system("rm -rf ./results/*")

#The following lines reads integer key-value pairs from a text file
MainText('\nREADING INPUT-FILES')
machnums, angles, shapevars, perturbvals, NUMMACH, NUMANGLES, NUMSHAPEVARS, NUMPERTURB = ReadInputFiles('scriptinput/')



MainText('STARTING CALCULATIONS')
for index_mach in range(1,NUMMACH+1):
    for index_angle in range(1,NUMANGLES+1):
        for index_shapevar in range(1,NUMSHAPEVARS+1):
            csvfilename='results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+str(index_shapevar)+'.csv'
            print('\033[4mMACH: '+machnums[index_mach-1]+'   ANGLE: '+angles[index_angle-1]+'   SHAPEVAR: '+shapevars[index_shapevar-1]+'\033[00m')
            with open(csvfilename,'w') as resultfile:
                resultfile.write("absvar-value,dLx,dLy\n")
                for index_perturb in range(1,NUMPERTURB+1):
                    simname = "sim_"+str(index_mach)+'_'+str(index_angle)+'_'+str(index_shapevar)+"_"+str(index_perturb)
                    print(simname+'/results/naca_plus_steady.liftdrag  -> '+csvfilename)
                    print(simname+'/results/naca_minus_steady.liftdrag -> '+csvfilename)
                    absvar=float(perturbvals[index_perturb-1])

                    #reading the lift results for that simulations
                    Lx_plus, Ly_plus=extractLifts(simname+'/results/naca_plus_steady.liftdrag')
                    Lx_minus, Ly_minus=extractLifts(simname+'/results/naca_minus_steady.liftdrag')

                    #calculating the finite difference
                    writeline=doFD(Lx_minus,Lx_plus,Ly_minus,Ly_plus,absvar)
                    resultfile.write(writeline+"\n")
            #print('\n')


for index_mach in range(1,NUMMACH+1):
    for index_angle in range(1,NUMANGLES+1):
        simname="anasim_"+str(index_mach)+'_'+str(index_angle)
        for method in ['direct','adjoint']:
            fluidresultfile=simname+'/results/naca_'+method+'_sens.liftdrag'
            csvfile='results/'+simname+'_'+method+'.csv'
            writeCSVana(fluidresultfile,csvfile)
            
            temp=[]
            with open(simname+'/results/linearsolver_'+method+'.txt') as sfile:
                splittext=sfile.read().split('iterations')
                splittext=splittext[1:]
                for block in splittext:
                    finaltext=block.splitlines()[1:-1]
                    temp.append(finaltext)
            
            for index_shapevar in range(1,NUMSHAPEVARS+1):
                with open('results/'+simname+'_'+str(index_shapevar)+'_'+str(method)+'_linearsolver.csv','w') as csvresultfile:
                    csvresultfile.write('iteration,residual\n')
                    for line in temp[index_shapevar-1]:
                        csvresultfile.writelines(','.join(line.split()[0:2])+'\n')

                    

MainText('')
