#!/bin/bash
FILE=$1
COMMAND=$2

if [ "$FILE" == "" ]
then
  echo "No file provided"
  exit 1
fi
if [ "$COMMAND" != "check" -a "$COMMAND" != "create" ]
then
  echo "no create or check command specified, assuming check"
  COMMAND=check
fi

if [ ! -f ${FILE} ]
then
  echo "no file found to checksum"
  exit 1
fi
SIZE=`du -Bg $FILE|sed 's/\(\d*\)G.*/\1/'`

if [ "$COMMAND" == "create" ]
then
  > ${FILE}.checksum
  for((i=1;i<=$SIZE;++i)) do
    dd bs=1M skip=$((1024*$i)) count=1 if=$FILE 2>/dev/null | sha512sum >> ${FILE}.checksum
  done
  echo "CHECKSUM CREATED"
  exit 0
elif [ -f ${FILE}.checksum -a "$COMMAND" == "check" ]
then
  for((i=1;i<=$SIZE;++i)) do
    CHECKSUM=`dd bs=1M skip=$((1024*$i)) count=1 if=$FILE 2>/dev/null | sha512sum |awk '{print $1}'`
    LINE=`grep -n $CHECKSUM ${FILE}.checksum|awk -F\: '{print $1}'`
    if [ "$LINE" != "$i" ]
    then
      echo "CHECKSUM FAILED"
      exit 1
    fi
  done
  echo "CHECKSUM SUCCEEDED"
  exit 0
elif [ ! -f ${FILE}.checksum -a "$COMMAND" == "check" ]
then
  echo "no checksum file found"
  exit 1
fi
