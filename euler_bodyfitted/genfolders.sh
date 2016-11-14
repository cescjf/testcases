#/usr/bin/bash!

perturbations=$(<scriptinput/perturbations)
attackangles=$(<scriptinput/angles)
index_angle=1


for curangle in ${attackangles[@]}
do
  cp -r template_ana anasim_$index_angle

  #the following comand executes pwd, thes replaces all "/" by "\/" and stores the result in PWD
  PWD=$(echo $(pwd) | sed -r 's/\//\\\//g')
  sed -i "s/<casepath>/$PWD/g" ./anasim_$index_angle/run_sens.sh
  sed -i "s/<index_angle>/$index_angle/g" ./anasim_${index_angle}/run_sens.sh

  #replace angle of attach
  sed -i "s/<alpha>/$curangle/g" ./anasim_$index_angle/naca_direct.aerof.sens
  sed -i "s/<alpha>/$curangle/g" ./anasim_$index_angle/naca_adjoint.aerof.sens

  index_perturb=1
  for i in ${perturbations[@]}
  do
    cp -r template_sim sim_${index_angle}_${index_perturb}

    #write siminfo file
    echo "perturb: $i" >> sim_${index_angle}_${index_perturb}/siminfo
    echo "angle: $curangle" >> sim_${index_angle}_${index_perturb}/siminfo

    #replace perturbation magnitude in SDESIGN file
    sed -i "s/<perturb_abs1>/$i/g" ./sim_${index_angle}_${index_perturb}/sdesign/naca_plus.sdesign
    sed -i "s/<perturb_abs1>/$i/g" ./sim_${index_angle}_${index_perturb}/sdesign/naca_minus.sdesign

    #replace angle of attach
    sed -i "s/<alpha>/$curangle/g" ./sim_${index_angle}_${index_perturb}/naca_plus.aerof.steady
    sed -i "s/<alpha>/$curangle/g" ./sim_${index_angle}_${index_perturb}/naca_minus.aerof.steady

    #replace simulation index and path in run-script
    sed -i "s/<index_angle>/$index_angle/g" ./sim_${index_angle}_${index_perturb}/run_steady.sh
    sed -i "s/<index_perturb>/$index_perturb/g" ./sim_${index_angle}_${index_perturb}/run_steady.sh
    sed -i "s/<casepath>/$PWD/g" ./sim_${index_angle}_${index_perturb}/run_steady.sh
    index_perturb=$(($index_perturb + 1))
    echo $i
  done
  index_angle=$(($index_angle + 1))
done

#writing some basic information to info file
#this information is later used by the pyhton scripts calc.py and plot.py
index_angle=$(($index_angle - 1))
index_perturb=$(($index_perturb - 1))
echo "NUMANGLES $index_angle" >> info
echo "NUMPERTURB $index_perturb" >> info

