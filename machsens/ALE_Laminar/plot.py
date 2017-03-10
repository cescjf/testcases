#!/usr/bin/python3

import os as os
#import matplotlib.pyplot as plt
#import numpy as np
import sys
import time

sys.path.append("../")
from functionlib  import extractLifts, doFD, writeCSVana
from functionlib2 import MainText, ReadInfo, ReadInputFiles
from plotlib      import plotLifts, plotIterations, getCSVdata, setup_plots, save_plot


os.system("rm -rf ./results/Ma*/*")

MainText("\nREADING INPUT-FILES")
machvalues, anglevalues, perturbvals, NUMMACH, NUMANGLES, NUMPERTURB = ReadInputFiles('scriptinput/')

MainText("\nSTART PlOTTING")
for index_mach in range(1,NUMMACH+1):
    for index_angle in range(1,NUMANGLES+1):
        plotfile='./results/Ma'+str(machvalues[index_mach-1])+'/angle'+str(anglevalues[index_angle-1])+".png"
        print("Writing file"+plotfile)

        #check if an appropriate outputfolder exist; if not, create it
        if  not os.path.exists("./results/Ma"+str(machvalues[index_mach-1])):
          os.makedirs("./results/Ma"+str(machvalues[index_mach-1]))


        #create filenames of analytic simulations resuts from the manual on
        filedirect           = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_direct.csv'
        fileadjoint          = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_adjoint.csv'
        filedirect_linsolve  = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_direct_linearsolver.csv'
        fileadjoint_linsolve = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_adjoint_linearsolver.csv'
        file_sim='./results/sim_'+str(index_mach)+'_'+str(index_angle)+'.csv'

        data_sim, data_direct, data_adjoint, data_direct_linsolve,data_adjoint_linsolve=getCSVdata(
                file_sim,filedirect,fileadjoint,filedirect_linsolve,fileadjoint_linsolve)


        #Initializing the plot
        plottitle=os.getcwd().split('/')[-1]+"  angle="+str(anglevalues[index_angle-1])+\
                  " mach="+str(machvalues[index_mach-1])+" "+time.strftime("%d/%m/%Y")
        f, multiaxes = setup_plots(plottitle,17,6)


        ################################################
        # Plots for Lx sensitivity                     #
        ################################################
        axes     =multiaxes[0]
        xdata    =data_sim['stepsize']
        ydata_num=data_sim['dLx']
        ydata_direct =data_sim['dLx']*0+data_direct["dLx"]
        ydata_adjoint=data_sim['dLx']*0+data_adjoint["dLx"]
        label=r"$\frac{\partial L_x}{\partial \alpha}$"
        plotLifts(axes,xdata,ydata_num,ydata_direct,ydata_adjoint,label)


        ################################################
        # Plots for Ly sensitivity                     #
        ################################################
        axes     =multiaxes[1]
        xdata    =data_sim['stepsize']
        ydata_num=data_sim['dLy']
        ydata_direct =data_sim['dLy']*0+data_direct["dLy"]
        ydata_adjoint=data_sim['dLy']*0+data_adjoint["dLy"]
        label=r"$\frac{\partial L_y}{\partial \alpha}$"
        plotLifts(axes,xdata,ydata_num,ydata_direct,ydata_adjoint,label)


        ################################################
        # Plots for linear solver                      #
        ################################################
        axes=multiaxes[2]
        iter_direct =data_direct_linsolve ['iteration']
        iter_adjoint=data_adjoint_linsolve['iteration']
        res_direct  =data_direct_linsolve ['residual']
        res_adjoint =data_adjoint_linsolve['residual']

        plotIterations(axes,iter_direct,res_direct,iter_adjoint,res_adjoint)


        multiaxes[0].legend(loc='upper center', bbox_to_anchor=(1, -0.20),
                                fancybox=True, shadow=True, ncol=5)

        save_plot(plotfile)
        
MainText("")
