#!/usr/bin/python3

import os as os
#import matplotlib.pyplot as plt
#import numpy as np
import sys
import time

sys.path.append("../")
from functionlib  import extractLifts, doFD, writeCSVana, extractFinalValue
from functionlib2 import MainText, ReadInfo, ReadInputFiles
from plotlib      import plotLifts, plotIterations, getCSVdata, setup_plots, save_plot


import matplotlib.pyplot as plt



def getLabel(dir,type):
    path=os.path.dirname(os.path.abspath(__file__))
    if path.find('alphasens')!=-1:
        svar='\\alpha'
    elif path.find('machsens')!=-1:
        svar='Ma_{\inf}'
    else:
        svar="s_{i}"

    if type=='liftdrag':
        q="L"
    else:
        q="F"

    label=r'$\frac{\partial '+q+'_'+dir+'}{\partial '+svar+'}$'
    # label=r"$"+label+"$"
    return label


os.system("rm -rf ./results/Ma*/*")

MainText("\nREADING INPUT-FILES")
machvalues, anglevalues, perturbvals, NUMMACH, NUMANGLES, NUMPERTURB = ReadInputFiles('scriptinput/')



f, axes = plt.subplots(2,2)
f.subplots_adjust(hspace=0.5)
f.subplots_adjust(wspace=0.5)
plotfile='./results/compare/Errors_over_angle.png'
print('\033[92m'+plotfile+'\033[00m')
method='direct'
itype=0
for type,denote in zip(['force','liftdrag'],['F','L']):
    for idir,dir in enumerate(['x','y']):
        for index_mach in range(1,NUMMACH+1):
            simvals=[]
            anavals=[]
            for index_angle in range(1,NUMANGLES+1):
                infile_ana='./results/anasim_'+str(index_mach)+'_'+str(index_angle)+'_'+method+'_'+type+'.csv'
                infile_sim='./results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+type+'.csv'
                print(infile_ana)
                qana=extractFinalValue(infile_ana,'dL'+dir)
                qsim=extractFinalValue(infile_sim,'dL'+dir)
                simvals.append(qsim)
                anavals.append(qana)
            err_ana=[abs((a-s)/s)*100 for a,s in zip(anavals,simvals)]
            axes[itype][idir].plot(anglevalues,err_ana,'o--',label='Ma: '+str(machvalues[index_mach-1]))
            axes[itype][idir].set_xlabel("angle [degree]")
            axes[itype][idir].set_ylabel('Error [%]')
            axes[itype][idir].set_title('Error d'+denote+'_'+dir+' over angle')
    itype=itype+1
axes[1][1].legend(loc='upper right', bbox_to_anchor=(1, -0.10),fancybox=True, shadow=True, ncol=8)
f.savefig(plotfile,format='png')


f, axes = plt.subplots(2,2)
f.subplots_adjust(hspace=0.5)
f.subplots_adjust(wspace=0.5)
f.set_size_inches(8,6)
plotfile='./results/compare/Errors_over_Mach.png'
print('\033[92m'+plotfile+'\033[00m')
method='direct'
itype=0
for type,denote in zip(['force','liftdrag'],['F','L']):
    for idir,dir in enumerate(['x','y']):
        for index_angle in range(1,NUMANGLES+1):
            simvals=[]
            anavals=[]
            for index_mach in range(1,NUMMACH+1):
                infile_ana='./results/anasim_'+str(index_mach)+'_'+str(index_angle)+'_'+method+'_'+type+'.csv'
                infile_sim='./results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+type+'.csv'
                print(infile_ana)
                qana=extractFinalValue(infile_ana,'dL'+dir)
                qsim=extractFinalValue(infile_sim,'dL'+dir)
                simvals.append(qsim)
                anavals.append(qana)
            err_ana=[abs((a-s)/s)*100 for a,s in zip(anavals,simvals)]
            axes[itype][idir].plot(machvalues,err_ana,'o--',label='Ma: '+str(anglevalues[index_angle-1]))
            axes[itype][idir].set_xlabel("Ma")
            axes[itype][idir].set_ylabel('Error [%]')
            axes[itype][idir].set_title('Error d'+denote+'_'+dir+' over Ma')
    itype=itype+1
axes[1][1].legend(loc='upper right', bbox_to_anchor=(1, -0.10),fancybox=True, shadow=True, ncol=8)
f.savefig(plotfile,format='png')





MainText("\nSTART PlOTTING")
for type in ['liftdrag', 'force']:
    for index_mach in range(1,NUMMACH+1):
        for index_angle in range(1,NUMANGLES+1):
            plotfile='./results/Ma'+str(machvalues[index_mach-1])+'/'+type+'_angle'+str(anglevalues[index_angle-1])+".png"
            print("Writing file"+plotfile)

            #check if an appropriate outputfolder exist; if not, create it
            if  not os.path.exists("./results/Ma"+str(machvalues[index_mach-1])):
              os.makedirs("./results/Ma"+str(machvalues[index_mach-1]))


            #create filenames of analytic simulations resuts from the manual on
            filedirect           = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_direct_'+type+'.csv'
            fileadjoint          = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_adjoint_'+type+'.csv'
            filedirect_linsolve  = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_direct_linearsolver.csv'
            fileadjoint_linsolve = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_adjoint_linearsolver.csv'
            file_sim='./results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+type+'.csv'

            data_sim, data_direct, data_adjoint, data_direct_linsolve,data_adjoint_linsolve=getCSVdata(
                    file_sim,filedirect,fileadjoint,filedirect_linsolve,fileadjoint_linsolve)


            #Initializing the plot
            plottitle=os.getcwd().split('/')[-1]+'  angle='+str(anglevalues[index_angle-1])+\
                      ' mach='+str(machvalues[index_mach-1])+' '+time.strftime('%d/%m/%Y')
            f, multiaxes = setup_plots(plottitle,17,6)


            ################################################
            # Plots for Lx sensitivity                     #
            ################################################
            axes     =multiaxes[0]
            xdata    =data_sim['stepsize']
            ydata_num=data_sim['dLx']
            ydata_direct =data_sim['dLx']*0+data_direct["dLx"]
            ydata_adjoint=data_sim['dLx']*0+data_adjoint["dLx"]
            # label=r"$\frac{\partial L_x}{\partial \alpha}$"
            label=getLabel('x',type)
            plotLifts(axes,xdata,ydata_num,ydata_direct,ydata_adjoint,label)


            ################################################
            # Plots for Ly sensitivity                     #
            ################################################
            axes     =multiaxes[1]
            xdata    =data_sim['stepsize']
            ydata_num=data_sim['dLy']
            ydata_direct =data_sim['dLy']*0+data_direct["dLy"]
            ydata_adjoint=data_sim['dLy']*0+data_adjoint["dLy"]
            # label=r"$\frac{\partial L_y}{\partial \alpha}$"
            label=getLabel('y',type)
            plotLifts(axes,xdata,ydata_num,ydata_direct,ydata_adjoint,label)


            # axes.legend(loc='lower center',mode="expand", borderaxespad=0., 
                         # bbox_to_anchor=(0.,-0.13, 1.,-0.13),
                        # fancybox=True, shadow=True, ncol=5)


            ################################################
            # Plots for linear solver                      #
            ################################################
            axes=multiaxes[2]
            iter_direct =data_direct_linsolve ['iteration']
            iter_adjoint=data_adjoint_linsolve['iteration']
            res_direct  =data_direct_linsolve ['residual']
            res_adjoint =data_adjoint_linsolve['residual']

            plotIterations(axes,iter_direct,res_direct,iter_adjoint,res_adjoint)


            # axes.legend(loc='upper center', bbox_to_anchor=(1, -0.20),
                                    # fancybox=True, shadow=True, ncol=5)

            save_plot(plotfile)
MainText("")
