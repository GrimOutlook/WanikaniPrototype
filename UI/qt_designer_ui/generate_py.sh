#!/bin/bash
for i in *.ui; do
    pyuic5 -x "$i" > "$i".py
done
