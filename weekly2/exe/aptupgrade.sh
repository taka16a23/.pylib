#!/bin/sh

python_path="/usr/bin/python"
weekly="/root/.pylib/weekly2/exe/aptupgrade.py"

[ -x $python_path ] || exit 0
[ -x $weekly ] || exit 0

xfce4-terminal --hold --command="$python_path $weekly"
exit 0
