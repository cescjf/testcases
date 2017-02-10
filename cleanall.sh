
CURRENTDIR=$(pwd)

echo $CURRENTDIR

find . -type d -name 'ALE_*' | while read line; do
  echo $line
  cd $line
  ./deletefolders.sh
  cd $CURRENTDIR
done

