#!/bin/bash

function printSuccess() {
   RED='\033[1;31m'
   NC='\033[0m'
   printf "${RED}$1${NC}\n\n"
}

CURRENT_DIR=/home/lscheuch/jcangles/Simulations/matthew/sim_1
AEROF_EXEC=/home/lscheuch/codes/aero-f_build/bin/aerof.debug
SOWER_EXEC=/home/mzahr/frg_codes/sower/bin/sower.Linux
XP2EXO_EXEC=/home/pavery/bin/xp2exo
SDESIGN_EXEC=/home/lscheuch/codes/sdesign.d/Executables.d/sdesign.Linux.opt
#/home/yc344/bin/sdesign.Linux.opt

cd $CURRENT_DIR

cd sdesign
$SDESIGN_EXEC naca.sdesign
printSuccess "SDESIGN finished"

$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.der -bc -3 -ascii -out naca_sowered.der
printSuccess "SOWER finished"

$SOWER_EXEC -fluid -split -con ../../mesh/mesh_ref.con -mesh ../../mesh/mesh_ref.msh -result naca.vmo -bc -3 -ascii -out naca_sowered.vmo
printSuccess "SOWER on fluid finished"
cd ..

mpirun -n 12 $AEROF_EXEC naca.aerof.sens
printSuccess "AERO-F finished"

#mpirun -n 12 $AEROF_EXE naca.aerof.sens
