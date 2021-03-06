
#!/usr/bin/python

import os as os

#The following lines reads integer key-value pairs from a text file
with open('info') as f:
    for line in f.readlines():
        exec(line.split()[0] + " = int(line.split()[1])")

#check if all neccessary information has been read from the info-file
if 'NUMANGLES' in locals() and 'NUMPERTURB' in locals() and 'NUMMACH' in locals() and 'NUMSHAPEVARS' in locals():
    print("info file is valid")
else:
    print("info file is invalid")
    exit()


# perturbvals=[]
# with open('scriptinput/perturbations') as f:
  # for line in f.readlines():
    # perturbvals.append(float(line))


for index_mach in range(1,NUMMACH+1):
    for index_angle in range(1,NUMANGLES+1):
        for index_shapevar in range(1,NUMSHAPEVARS+1):
            # resultfile = open('results/sim_'+str(index_mach)+'_'+str(index_angle)+'_'+str(index_shapevar)+'.csv','w')
            # resultfile.write("absvar-value,dLx,dLy\n")
            # for index_perturb in range(1,NUMPERTURB+1):
                # simname = "sim_"+str(index_mach)+'_'+str(index_angle)+'_'+str(index_shapevar)+"_"+str(index_perturb)
                # print(simname)
                # absvar=float(perturbvals[index_perturb-1])
                # # with open(simname+'/sdesign/naca_plus.sdesign') as f:
                    # # lines=f.readlines()
                    # # index1=lines.index('ABSVAR\n')
                    # # absvar=float(lines[index1+2].split()[1])

                # #reading the lift results for that simulations
                # with open(simname+'/results/naca_plus_steady.liftdrag') as f:
                    # s = f.readlines()
                    # lastrow = s[-1]
                    # split   = lastrow.split()
                    # Lx_plus=float(split[4])
                    # Ly_plus=float(split[5])
                # with open(simname+'/results/naca_minus_steady.liftdrag') as f:
                    # s = f.readlines()
                    # lastrow = s[-1]
                    # split   = lastrow.split()
                    # Lx_minus=float(split[4])
                    # Ly_minus=float(split[5])

                # #calculating the finite difference
                # dLx="{:.10e}".format((Lx_plus-Lx_minus)/(absvar*2  ))
                # dLy="{:.10e}".format((Ly_plus-Ly_minus)/(absvar*2  ))
                # absvar="{:.10e}".format(absvar)
                # writeline=",".join([absvar,dLx,dLy])

                # #writing the result
                # resultfile.write(writeline)
                # resultfile.write("\n")
            # resultfile.close()


# for index_mach in range(1,NUMMACH+1):
    # for index_angle in range(1,NUMANGLES+1):
        # simname="anasim_"+str(index_mach)+'_'+str(index_angle)
        # for method in ['direct','adjoint']:

            # #opeing the .csv file
            # resultfile = open('results/'+simname+'_'+method+'.csv','w')
            # resultfile.write('ABSVAR,dLx,dLy\n')

            # #open the liftdrag file and write the important parts to the csv file
            # with open(simname+'/results/naca_'+method+'_sens.liftdrag') as f:
                # f.readline()#throw away first line
                # for line in f:
                    # split1=line.split()
                    # var=split1[0]
                    # dLx=split1[5]
                    # dLy=split1[6]
                    # writeline=",".join([var,dLx,dLy])
                    # resultfile.write(writeline)
                    # resultfile.write("\n")
            # resultfile.close()
