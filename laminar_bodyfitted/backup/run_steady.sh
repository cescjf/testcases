#!/bin/bash
CURRENT_DIR=/home/lscheuch/jcangles/Simulations/matthew/sim_1
AEROF_EXEC=/home/lscheuch/codes/aero-f_build/bin/aerof.debug
SOWER_EXEC=/home/mzahr/frg_codes/sower/bin/sower.Linux
XP2EXO_EXEC=/home/pavery/bin/xp2exo
SDESIGN_EXEC=/home/lscheuch/codes/sdesign.d/Executables.d/sdesign.Linux.opt

cd $CURRENT_DIR

cd sdesign
/home/yc344/bin/sdesign.Linux.opt naca.sdesign
$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.der -bc -3 -ascii -out naca_sowered.der 
/home/mzahr/frg_codes/sower/bin/sower.Linux -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.vmo -bc -3 -ascii -out naca_sowered.vmo
cd ..

mpirun -n 12 $AEROF_EXEC naca.aerof.steady

cd results
$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.pres -output naca_steady_pressure
$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.sol -output naca_steady_sol
$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.disp -output naca_steady_disp
$XP2EXO_EXEC ../../mesh/naca.top naca_steady.exo naca_steady_pressure.xpost naca_steady_sol.xpost naca_steady_disp.xpost
cd ..

