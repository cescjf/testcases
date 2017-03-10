#!/usr/bin/python

import os as os
import sys

sys.path.append("../")

# os.system("rm -rf ./results/*")

from functionlib import extractLifts, doFD, writeCSVana
from functionlib2 import MainText, ReadInfo, ReadInputFiles

MainText("\nREADING INPUT-FILES")
machnums, angles, perturbvals, NUMMACH, NUMANGLES, NUMPERTURB = ReadInputFiles('scriptinput/')


for type in ['liftdrag', 'force']:
  MainText("STARTING CALCULATIONS")
  for index_mach in range(1,NUMMACH+1):
      for index_angle in range(1,NUMANGLES+1):
          csvfilename='results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+type+'.csv'                                ##############
          with open(csvfilename,'w') as resultfile:
              resultfile.write("absvar-value,dLx,dLy\n")
              print('\033[4mMACH: '+machnums[index_mach-1]+'   ANGLE: '+angles[index_angle-1]+'\033[00m')
              for index_perturb in range(1,NUMPERTURB+1):
                  simname = "sim_"+str(index_mach)+'_'+str(index_angle)+"_"+str(index_perturb)

                  absvar=float(perturbvals[index_perturb-1])

                  #reading the lift results for that simulations
                  Lx_plus, Ly_plus = extractLifts(simname+'/results/naca_plus_steady.'+type)                #############3
                  Lx_minus, Ly_minus = extractLifts(simname+'/results/naca_minus_steady.'+type)             #############

                  #calculating the finite difference
                  writeline=doFD(Lx_minus,Lx_plus,Ly_minus,Ly_plus,absvar)
                  print(simname+'/results/naca_plus_steady.'+type+'  -> '+csvfilename)                          #############
                  print(simname+'/results/naca_minus_steady.'+type+' -> '+csvfilename)                           ############

                  #writing the result
                  resultfile.write(writeline+"\n")


          anasimname="anasim_"+str(index_mach)+'_'+str(index_angle)
          #print('\033[4mMACH: '+machnums[index_mach-1]+'   ANGLE: '+angles[index_angle-1]+'\033[00m')
          for method in ['direct','adjoint']:
              csvfile='results/'+anasimname+'_'+method+'_'+type+'.csv'                                                      ##############

              #opeing the .csv file
              with open('results/'+anasimname+'_'+method+'_'+type+'.csv','w') as resultfile:                               ##############3
                  resultfile.write('ABSVAR,dLx,dLy\n')

                  fluidresultfile=anasimname+'/results/naca_'+method+'_sens.'+type                             ############
                  writeCSVana(fluidresultfile,csvfile)
              with open('results/'+anasimname+'_'+method+'_linearsolver_'+type+'.csv','w') as resultfile:                  ##############
                  resultfile.write('iteration,residual\n')
                  solverresultfile=anasimname+'/results/linearsolver_'+method+'.txt'                               ##############
                  with open(solverresultfile) as sfile:
                    sfile.readline()
                    for line in sfile:
                      resultfile.write(','.join(line.split()[0:2])+"\n")
  MainText("")
