#!/bin/sh

curl -s "http://www.zipcodestogo.com/Indiana/" | grep -o 46556 | uniq
curl -s "http://www.zipcodestogo.com/Indiana/" | grep -oP "466[0-9]{2}" | uniq
curl -s "http://www.zipcodestogo.com/Indiana/" | grep -oP "466[[:digit:]]{2}" | uniq

curl -sL "http://yld.me/aBG" | grep -oP "[[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}"
curl -sL "http://yld.me/aBG" | grep -oP "[[:alnum:]]+@[[:alnum:]]+\.[[:alnum:]]{3}" | sort | uniq
curl -sL "http://yld.me/aBG" | grep -oP "[A-Za-z ]+Prof[^<]+" | sort | uniq