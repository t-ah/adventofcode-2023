#!/bin/bash

if [ "$1" == "" ]; then
    echo "use: ./setup.sh START_DAY [FINAL_DAY]"
    exit 1
elif [ "$2" == "" ]; then
    TO=$1
else
    TO=$2
fi
FROM=$1

for (( i=$FROM; i<=$TO; i++ ))
do
    mkdir -p "day${i}"
    cd "day${i}"
    cp "../template.py" "p1.py"
    # sed -e "s/PART/1/g" -i "" "p1.py"
    touch "p1-input.txt"
    touch "p1-test.txt"
done
