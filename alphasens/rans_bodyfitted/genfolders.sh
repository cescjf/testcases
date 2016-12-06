#/usr/bin/bash!

echo "###########################################################"
echo "#  Automatic simulation folder creation                   #"
echo "###########################################################"
machnumbers=$(<scriptinput/machnumbers)
perturbations=$(<scriptinput/perturbations)
attackangles=$(<scriptinput/angles)
shapevars=$(<scriptinput/shapevariables)
echo "SHapevars: ${shapevars}"


sec_equations=$(<scriptinput/sec_equations)
sec_equations="$sec_equations"
echo $sec_equations


echo "MACHNUMBERS:   $machnumbers"
echo "ATTACKANGLES:  $attackangles"
echo "PERTURBATIONS: $perturbations"

echo ""
echo "STARTING FOLDER CREATION"
echo ""
index_mach=1
for curmach in ${machnumbers}
do
  index_angle=1
  for curangle in ${attackangles[@]}
  do
    cp -r template_ana anasim_${index_mach}_${index_angle}
    echo "anasim_${index_mach}_${index_angle}  MACH:${curmach}  ANGLE:${curangle}"

    ###########################################################################
    # SED commands for Sensitivity Analysis - files                           #
    ###########################################################################

    #puts the missing sections into the newly created aero-f input file
    #this replacements need to be done before any other
    for sec in sec_equations sec_meshmotion sec_space sec_surfaces sec_time_sens sec_bc; do
      python2.6 ./scriptinput/replacescript.py file=./anasim_${index_mach}_${index_angle}/naca_direct.aerof.sens key=${sec} text=./scriptinput/${sec}
      python2.6 ./scriptinput/replacescript.py file=./anasim_${index_mach}_${index_angle}/naca_adjoint.aerof.sens key=${sec} text=./scriptinput/${sec}
    done

    #the following comand executes pwd, thes replaces all "/" by "\/" and stores the result in PWD
    PWD=$(echo $(pwd) | sed -r 's/\//\\\//g')
    sed -i "s/<casepath>/$PWD/g" ./anasim_${index_mach}_$index_angle/run_sens.sh
    sed -i "s/<index_angle>/$index_angle/g" ./anasim_${index_mach}_${index_angle}/run_sens.sh
    sed -i "s/<index_mach>/$index_mach/g" ./anasim_${index_mach}_${index_angle}/run_sens.sh

    #replace angle of attach in anasim file
    sed -i "s/<alpha>/$curangle/g" ./anasim_${index_mach}_$index_angle/naca_direct.aerof.sens
    sed -i "s/<alpha>/$curangle/g" ./anasim_${index_mach}_$index_angle/naca_adjoint.aerof.sens

    #replace machnumber in anasim file
    sed -i "s/<machnumber>/$curmach/g" ./anasim_${index_mach}_$index_angle/naca_direct.aerof.sens
    sed -i "s/<machnumber>/$curmach/g" ./anasim_${index_mach}_$index_angle/naca_adjoint.aerof.sens



    ###########################################################################
    # SED commands for Steady Analysis - files                                #
    ###########################################################################
    index_perturb=1
    for i in ${perturbations[@]}
    do
      cp -r template_sim sim_${index_mach}_${index_angle}_${index_perturb}
      echo "sim_${index_mach}_${index_angle}  MACH:${curmach}  ANGLE:${curangle}  PERTURB:${i}"

      #replace the sections
      for sec in sec_equations sec_meshmotion sec_space sec_surfaces sec_time_steady sec_bc; do
        python2.6 ./scriptinput/replacescript.py file=./sim_${index_mach}_${index_angle}_${index_perturb}/naca_plus.aerof.steady key=${sec} text=./scriptinput/${sec}
        python2.6 ./scriptinput/replacescript.py file=./sim_${index_mach}_${index_angle}_${index_perturb}/naca_minus.aerof.steady key=${sec} text=./scriptinput/${sec}
      done

      #write siminfo file
      echo "machnumber: $curmach" >> sim_${index_mach}_${index_angle}_${index_perturb}/siminfo
      echo "perturb: $i" >> sim_${index_mach}_${index_angle}_${index_perturb}/siminfo
      echo "angle: $curangle" >> sim_${index_mach}_${index_angle}_${index_perturb}/siminfo

      #replace angle of attach
      plusangle=$(python -c "print $curangle+$i")
      minusangle=$(python -c "print $curangle-$i")
      sed -i "s/<alpha>/$plusangle/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/naca_plus.aerof.steady
      sed -i "s/<alpha>/$minusangle/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/naca_minus.aerof.steady

      #replace machnumber
      sed -i "s/<machnumber>/$curmach/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/naca_plus.aerof.steady
      sed -i "s/<machnumber>/$curmach/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/naca_minus.aerof.steady

      #replace simulation index and path in run-script
      sed -i "s/<index_mach>/$index_mach/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/run_steady.sh
      sed -i "s/<index_angle>/$index_angle/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/run_steady.sh
      sed -i "s/<index_perturb>/$index_perturb/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/run_steady.sh
      sed -i "s/<casepath>/$PWD/g" ./sim_${index_mach}_${index_angle}_${index_perturb}/run_steady.sh
      index_perturb=$(($index_perturb + 1))
      done

    index_angle=$(($index_angle + 1))
  done #done looping over angles


  index_mach=$(($index_mach + 1))
done #done looping over machnumbers
echo ""
echo "FINISHED FOLDER CREATION"

#writing some basic information to info file
#this information is later used by the pyhton scripts calc.py and plot.py
index_mach=$(($index_mach - 1))
index_angle=$(($index_angle - 1))
index_perturb=$(($index_perturb - 1))
echo "NUMMACH $index_mach" >> info
echo "NUMANGLES $index_angle" >> info
echo "NUMPERTURB $index_perturb" >> info
