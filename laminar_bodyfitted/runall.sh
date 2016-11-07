#/usr/bin/bash!

CURDIR=$(pwd)
echo $CURDIR

find . -type d -name 'sim_*' | while read line; do
#echo $line
    cd $line
    ls
    pwd
    qsub ./run_steady.sh  >& consoleout &
    cd $CURDIR
done

cd anasim
qsub ./run_sens.sh
