#!/bin/sh

# After looking at online solutions... realized the seat representations
# are just binary numbers.

echo "Part 1 solution:"
tr 'FBLR' '0101' < input.txt | sort -r | head -n1 | sed 's/.*/2i&p/' | dc
