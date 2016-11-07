#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

for method in ['direct','adjoint']:
    #with file(fname+'/sdesign/naca_plus.sdesign') as f:
    data = np.genfromtxt('./manual_sensitivities.csv', delimiter=',', skip_header=1,skip_footer=0, names=['stepsize', 'dLx', 'dLy'])

    filestring = './analytic_sensitivities_'+method+'.csv'
    print filestring
    data_anaytic = np.genfromtxt(filestring, delimiter=',', skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])


    f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

    ax1.semilogx(data['stepsize'], data['dLx'],'-o', color='r', label='Sensitivity dLx')
    ax1.semilogx(data['stepsize'], data['dLx']*0+data_anaytic["dLx"],'--', color='k', label='analytic result')
    ax1.set_xlabel("step-size")
    ax1.set_ylabel("dLx")
    ax1.set_title("Sensitivity Lx")

    ax2.semilogx(data['stepsize'], data['dLy'],'-o', color='r', label='Sensitivity dLy')
    ax2.semilogx(data['stepsize'], data['dLy']*0+data_anaytic["dLy"],'--', color='k', label='analytic result')
    ax2.set_xlabel("step-size")
    ax2.set_ylabel("dLx")
    ax2.set_title("Sensitivity Ly")


    plt.savefig('./manual_sensitivities_'+method+'.eps', format='eps', dpi=1000)
