#/usr/bin/bash!

perturbations=(0.01 0.001 0.0001 0.00001 0.000001 0.0000001 0.00000001)
index=1

cp -r template_ana anasim

for i in ${perturbations[@]}
do
  cp -r template_sim sim_$index
  
  sed -i "s/<perturb_abs1>/$i/g" ./sim_$index/sdesign/naca_plus.sdesign
  sed -i "s/<perturb_abs1>/$i/g" ./sim_$index/sdesign/naca_minus.sdesign
  sed -i "s/<index>/$index/g" ./sim_$index/run_steady.sh
  index=$(($index + 1))
  echo $i
done



