#!/usr/bin/python3

import os as os
import matplotlib.pyplot as plt
import numpy as np

machvalues=[]
with open('scriptinput/machnumbers') as f:
  for line in f.readlines():
    machvalues.append(float(line))

anglevalues=[]
with open('scriptinput/angles') as f:
  for line in f.readlines():
    anglevalues.append(float(line))

#The following lines reads integer key-value pairs from a text file
with open('info') as f:
  for line in f.readlines():
    exec(line.split()[0] + " = int(line.split()[1])")

#check if all neccessary information has been read from the info-file
if 'NUMANGLES' in locals() and 'NUMPERTURB' in locals():
  print('\x1b[0;37;42m' + 'Info-file is valid!' + '\x1b[0m')#green
  #print('\x1b[0;37;44m' + 'Info-file is valid!' + '\x1b[0m')#blue
  #print('\x1b[0;37;41m' + 'Info-file is valid!' + '\x1b[0m')#red
else:
  print('\x1b[0;37;42m' + 'Info-file is invalid!' + '\x1b[0m')
  exit()

for index_mach in range(1,NUMMACH+1):
    for index_angle in range(1,NUMANGLES+1):

      data_sim = np.genfromtxt('./results/sim_'+str(index_mach)+'_'+str(index_angle)+'.csv', delimiter=',', skip_header=1,skip_footer=0, names=['stepsize', 'dLx', 'dLy'])

      #create filenames of analytic simulations resuts from the manual on
      filedirect = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_direct.csv'
      fileadjoint = 'anasim_'+str(index_mach)+'_'+str(index_angle)+'_adjoint.csv'
      data_direct  = np.genfromtxt('./results/'+filedirect,  delimiter=',',max_rows=1, skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])
      data_adjoint = np.genfromtxt('./results/'+fileadjoint, delimiter=',',max_rows=1, skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])

      #check if an appropriate outputfolder exist; if not, create it
      if  not os.path.exists("./results/Ma"+str(machvalues[index_mach-1])):
          os.makedirs("./results/Ma"+str(machvalues[index_mach-1]))
      #create the name of the output file
      epsfile='./results/Ma'+str(machvalues[index_mach-1])+'/angle'+str(anglevalues[index_angle-1])+".png"
      print("Writing file"+epsfile)

      f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)
      plt.suptitle("RANS-bodyfitted  angle="+str(anglevalues[index_angle-1]))

      ################################################
      # Plots for Lx sensitivity                     #
      ################################################
      ax1.semilogx(data_sim['stepsize'], data_sim['dLx'],'-o', color='r', label='numerical result')
      ax1.semilogx(data_sim['stepsize'], data_sim['dLx']*0+data_direct["dLx"],'-', color='k', label='direct method')
      ax1.semilogx(data_sim['stepsize'], data_sim['dLx']*0+data_adjoint["dLx"],'--', color='g', label='adjoint method')
      ax1.set_xlabel("step-size")
      ax1.set_ylabel("dLx")
      ax1.set_title("Sensitivity Lx")

      ################################################
      # Plots for Ly sensitivity                     #
      ################################################
      ax2.semilogx(data_sim['stepsize'], data_sim['dLy'],'-o', color='r', label='numerical result')
      ax2.semilogx(data_sim['stepsize'], data_sim['dLy']*0+data_direct["dLy"],'-', color='k', label='direct method')
      ax2.semilogx(data_sim['stepsize'], data_sim['dLy']*0+data_adjoint["dLy"],'--', color='g', label='adjoint method')
      ax2.set_xlabel("step-size")
      ax2.set_ylabel("dLx")
      ax2.set_title("Sensitivity Ly")

      ################################################
      # Shift plots and add legends                  #
      ################################################
      box = ax1.get_position()
      ax1.set_position([box.x0, box.y0 + box.height * 0.3,
                           box.width, box.height * 0.7])
      box = ax2.get_position()
      ax2.set_position([box.x0*1.1, box.y0 + box.height * 0.3,
                           box.width*1.1, box.height * 0.7])
      # Put a legend below current axis
      ax2.legend(loc='upper center', bbox_to_anchor=(-0.2, -0.20),
                        fancybox=True, shadow=True, ncol=5)

      plt.savefig(epsfile, format='png', dpi=600)
      plt.close()






# for csvfile in sorted(os.listdir('results')): #sorted is needed since the reults might be written out of order
    # if csvfile[0:3]=='sim':

      # data_sim = np.genfromtxt('./results/'+csvfile, delimiter=',', skip_header=1,skip_footer=0, names=['stepsize', 'dLx', 'dLy'])
      # firstnum=csvfile.split('_')[1]
      # print(firstnum)

      # #create filenames of analytic simulations resuts from the manual on
      # filedirect = 'anasim_'+firstnum+'_direct.csv'
      # fileadjoint = 'anasim_'+firstnum+'_adjoint.csv'
      # data_direct  = np.genfromtxt('./results/'+filedirect,  delimiter=',', skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])
      # data_adjoint = np.genfromtxt('./results/'+fileadjoint, delimiter=',', skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])

      # #create the name of the output file
      # epsfile    =csvfile.replace("sim","comparison").replace(".csv",".eps")

      # f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

      # ################################################
      # # Plots for Lx sensitivity                     #
      # ################################################
      # ax1.semilogx(data_sim['stepsize'], data_sim['dLx'],'-o', color='r', label='numerical result')
      # ax1.semilogx(data_sim['stepsize'], data_sim['dLx']*0+data_direct["dLx"][0],'-', color='k', label='direct method')
      # ax1.semilogx(data_sim['stepsize'], data_sim['dLx']*0+data_adjoint["dLx"][0],'--', color='g', label='adjoint method')
      # ax1.set_xlabel("step-size")
      # ax1.set_ylabel("dLx")
      # ax1.set_title("Sensitivity Lx")

      # ################################################
      # # Plots for Ly sensitivity                     #
      # ################################################
      # print(data_sim['stepsize'])
      # print("\n")
      # ax2.semilogx(data_sim['stepsize'], data_sim['dLy'],'-o', color='r', label='numerical result')
      # ax2.semilogx(data_sim['stepsize'], data_sim['dLy']*0+data_direct["dLy"][0],'-', color='k', label='direct method')
      # ax2.semilogx(data_sim['stepsize'], data_sim['dLy']*0+data_adjoint["dLy"][0],'--', color='g', label='adjoint method')
      # ax2.set_xlabel("step-size")
      # ax2.set_ylabel("dLx")
      # ax2.set_title("Sensitivity Ly")

      # ################################################
      # # Shift plots and add legends                  #
      # ################################################
      # box = ax1.get_position()
      # ax1.set_position([box.x0, box.y0 + box.height * 0.3,
                           # box.width, box.height * 0.7])
      # box = ax2.get_position()
      # ax2.set_position([box.x0*1.1, box.y0 + box.height * 0.3,
                           # box.width*1.1, box.height * 0.7])
      # # Put a legend below current axis
      # ax2.legend(loc='upper center', bbox_to_anchor=(-0.2, -0.20),
                        # fancybox=True, shadow=True, ncol=5)

      # plt.savefig(epsfile, format='eps', dpi=1000)
