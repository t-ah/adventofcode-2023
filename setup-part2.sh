#!/bin/bash

if [ "$1" == "" ] || [ "$1" == "--h" ]; then
    echo "use: ./setup-part2.sh DAY [--copy] (DAY=day number, --copy: copy test and input from part 1)"
    exit 1
fi

cd "day$1"
if [ "$2" == "--copy" ]; then
    cp "p1-input.txt" "p2-input.txt"
    cp "p1-test.txt" "p2-test.txt"
else
    touch "p2-input.txt"
    touch "p2-test.txt"
fi
cp "p1.py" "p2.py"
sed -e "s/p1-/p2-/g" -i "" "p2.py"
