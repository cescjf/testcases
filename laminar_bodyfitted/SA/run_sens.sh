#!/bin/bash
CURRENT_DIR="/home/jcangles/Simulations/matthew/SA"

cd $CURRENT_DIR

cd sdesign
/home/yc344/bin/sdesign.Linux.opt naca.sdesign
/home/mzahr/frg_codes/sower/bin/sower.Linux -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.der -bc -3 -ascii -out naca_sowered.der 
/home/mzahr/frg_codes/sower/bin/sower.Linux -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.vmo -bc -3 -ascii -out naca_sowered.vmo
cd ..

mpirun -n 12 /home/jcangles/Codes/Fluid.merge/bin/aerof.opt naca.aerof.steady
mpirun -n 12 /home/jcangles/Codes/Fluid.merge/bin/aerof.opt naca.aerof.sens 
