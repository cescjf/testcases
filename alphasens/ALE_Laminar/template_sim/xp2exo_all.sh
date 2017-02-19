#!/bin/bash
XP2EXO_EXECUTABLE=/home/pavery/bin/xp2exo

$XP2EXO_EXECUTABLE ../mesh/naca.top \
                   ./results/exo/all_quantities.exo \
                   results/xpost/DensitySensitivity.xpost \
                   results/xpost/MachSensitivity.xpost \
                   results/xpost/PressureSensitivity.xpost \
                   results/xpost/TemperatureSensitivity.xpost \
                   results/xpost/TotalPressureSensitivity.xpost \
                   results/xpost/VelocityNormSensitivity.xpost \
                   results/xpost/VelocitySensitivity.xpost \
                   results/xpost/MeshdispSensitivity.xpost
