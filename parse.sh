if [ $# -ne 1 ]
then
	echo 'parse.sh: usage: sh parse.sh FILE'
	exit 1
fi

while read LINE
do
	KEY=$(echo $LINE | cut -d',' -f1)
	VAL=$(echo $LINE | cut -d',' -f2)
	if [ $VAL ]
	then
		echo -n "${KEY}=${VAL}&"
	fi
done <<< $(sed '1d' $1)
