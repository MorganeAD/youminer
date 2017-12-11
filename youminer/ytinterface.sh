#!/bin/sh


if [ -z $1 ] 
then
	echo "needs parameter"
	exit 1
fi
if [ -z $2 ] 
then
	echo "needs parameter"
	exit 1
fi

. youminer/apikey.sh

mkdir -p tmp
case $1 in 
"v")
	REQ=$(sh youminer/parse.sh youminer/cfg.csv)
	>&2 echo "https://www.googleapis.com/youtube/v3/search?q=${2}&${REQ}key=${APIKEY}"
	curl -s -o answer.json "https://www.googleapis.com/youtube/v3/search?q=${2}&${REQ}key=${APIKEY}"
	;;
"a")
	curl -s -o answer.json "https://www.googleapis.com/youtube/v3/channels?id=${2}&part=statistics,snippet&key=${APIKEY}";
	;;
"*")
	echo "parameter not defined"
	exit 1
esac
