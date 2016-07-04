#!/usr/bin/env bash
cat $1 | grep 'group 0' -A1 | grep -v 'group 0' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 1' -A1 | grep -v 'group 1' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 2' -A1 | grep -v 'group 2' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 3' -A1 | grep -v 'group 3' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 4' -A1 | grep -v 'group 4' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 5' -A1 | grep -v 'group 5' | awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
cat $1 | grep 'group 5' -A2 | grep -v 'group 5' |grep -v 'READ'| awk -F '=' '{print $4}' | awk -F ','  '{print $1}'
