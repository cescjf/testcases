#/usr/bin/bash!

#xargs essentially runs a command once for each of its instructions from standard input
find . -type d -name 'sim_*' | xargs rm -rf
find . -type d -name 'anasim_*' | xargs rm -rf

rm info
