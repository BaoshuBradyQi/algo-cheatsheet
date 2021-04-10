#!/bin/bash

text_file="./readme.txt"
readme_file="./README.md"
markdown="md"
parse_dir() {

echo "## ${1%/*} " >> $readme_file
echo "<table>" >>$readme_file
for f in `ls ./$1`;
do 
	filename=`echo "$f" | cut -d'.' -f1`
	ext=`echo "$f" | cut -d'.' -f2`
	
	
	if [ "$ext" != "$markdown" ];
	then
		platform=`echo "$filename" | cut -d'_' -f1`
		title=`echo "$filename" | cut -d'_' -f2`
	
		echo "<tr><td>$platform</td><td>$title</td><td><a -href=\""$1$f"\">$ext</a></td></tr>"	>> $readme_file
	fi

done
echo "</table>" >> $readme_file
}


cat $text_file > $readme_file


for d in `ls -d -- */`;
do
	parse_dir "$d"
done
