#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

#for method in ['direct','adjoint']:
    #with file(fname+'/sdesign/naca_plus.sdesign') as f:
data = np.genfromtxt('./manual_sensitivities.csv', delimiter=',', skip_header=1,skip_footer=0, names=['stepsize', 'dLx', 'dLy'])

filestring_direct = './analytic_sensitivities_direct.csv'
data_direct = np.genfromtxt(filestring_direct, delimiter=',', skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])

filestring_adjoint = './analytic_sensitivities_adjoint.csv'
data_adjoint = np.genfromtxt(filestring_direct, delimiter=',', skip_header=1,skip_footer=0, names=['absvar', 'dLx', 'dLy'])

f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

ax1.semilogx(data['stepsize'], data['dLx'],'-o', color='r', label='numerical result')
ax1.semilogx(data['stepsize'], data['dLx']*0+data_direct["dLx"],'-', color='k', label='direct method')
ax1.semilogx(data['stepsize'], data['dLx']*0+data_adjoint["dLx"],'--', color='g', label='adjoint method')
ax1.set_xlabel("step-size")
ax1.set_ylabel("dLx")
ax1.set_title("Sensitivity Lx")

ax2.semilogx(data['stepsize'], data['dLy'],'-o', color='r', label='numerical result')
ax2.semilogx(data['stepsize'], data['dLy']*0+data_direct["dLy"],'-', color='k', label='direct method')
ax2.semilogx(data['stepsize'], data['dLy']*0+data_adjoint["dLy"],'--', color='g', label='adjoint method')
ax2.set_xlabel("step-size")
ax2.set_ylabel("dLx")
ax2.set_title("Sensitivity Ly")

box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.3,
                     box.width, box.height * 0.7])
box = ax2.get_position()
ax2.set_position([box.x0*1.1, box.y0 + box.height * 0.3,
                     box.width*1.1, box.height * 0.7])
# Put a legend below current axis
ax2.legend(loc='upper center', bbox_to_anchor=(-0.2, -0.20),
                  fancybox=True, shadow=True, ncol=5)



plt.savefig('./visualization.eps', format='eps', dpi=1000)
