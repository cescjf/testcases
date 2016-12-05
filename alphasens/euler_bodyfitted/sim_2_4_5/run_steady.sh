#!/bin/bash

#PBS -N sim_2_4_<index_shapevar>_5_euler_bodyfitted
#PBS -M lscheuch@stanford.edu
#PBS -l nodes=1:ppn=12
#PBS -l walltime=48:00:00

CURRENT_DIR='/home/lscheuch/project/testcases_alphasensitivity/euler_bodyfitted/sim_2_4_5'

function printSuccess() {
   RED='\033[1;31m'
   NC='\033[0m'
   printf "${RED}$1${NC}\n\n"
}

module load openmpi/openmpi161_intel13

AEROF_EXEC=/home/lscheuch/codes/aero-f_build/bin/aerof.opt
SOWER_EXEC=/home/mzahr/frg_codes/sower/bin/sower.Linux
XP2EXO_EXEC=/home/pavery/bin/xp2exo
SDESIGN_EXEC=/home/lscheuch/codes/sdesign.d/Executables.d/sdesign.Linux.opt

cd $CURRENT_DIR

cd sdesign
$SDESIGN_EXEC naca_plus.sdesign
$SDESIGN_EXEC naca_minus.sdesign
printSuccess SDESIGN_ended

$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_plus.der -bc -3 -ascii -out naca_plus_sowered.der
$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_plus.vmo -bc -3 -ascii -out naca_plus_sowered.vmo
$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_minus.der -bc -3 -ascii -out naca_minus_sowered.der
$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_minus.vmo -bc -3 -ascii -out naca_minus_sowered.vmo
printSuccess PREPROCESSED_MESH
cd ..

mpirun -n 12 $AEROF_EXEC naca_plus.aerof.steady
mpirun -n 12 $AEROF_EXEC naca_minus.aerof.steady
printSuccess AEROF_ENDED

#cd results
#$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.pres -output naca_steady_pressure
#$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.sol -output naca_steady_sol
#$SOWER_EXEC -fluid -merge -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca_steady.disp -output naca_steady_disp
#$XP2EXO_EXEC ../../mesh/naca.top naca_steady.exo naca_steady_pressure.xpost naca_steady_sol.xpost naca_steady_disp.xpost
#printSuccess POSTPROCESSING_ENDED
#cd ..

