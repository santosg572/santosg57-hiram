#!/bin/bash

dd=$(date +"Year: %y, Month: %m, Day: %d")
dd=$(date +"M%mD%dY%y")
echo $dd

if [ "$1" = "" ]; then
  echo
  echo "path del directorio para generar"
  echo
else
  if [ "$2" = "" ]; then
    echo
    echo "nombre del archivo para grabar"
    echo
  else
    echo "bien"
    echo $1 > $2"_"$dd".txt"
    filon=$2"_"$dd
    ls -1 $1/ >> ${filon}".txt"
  fi
fi

python creaHTML.py ${filon}

open ${filon}".html"
