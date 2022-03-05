#!/bin/bash

touch about.HTM contact.HTM footer.HTM header.HTM index.HTM

for file in *.HTM; do
	name=$(basename "$file" .HTM)
	mv "$file" "$name.html"
done