#!/bin/sh
. youminer/apikey.sh

REQ=$(sh youminer/parse.sh youminer/cfg.csv)
mkdir -p pages

curl -s -o answer.json "https://www.googleapis.com/youtube/v3/search?q=${1}&${REQ}key=${APIKEY}"
