#!/bin/sh

# After looking at online solutions... realized the seat representations
# are just binary numbers.

echo "Part 1 solution:"
tr 'FBLR' '0101' < input.txt | sort -r | head -n1 | sed 's/.*/2i&p/' | dc

echo "Part 2 solution:"
tr 'FBLR' '0101' < input.txt | sed 's/.*/2i&p/' | dc | sort -h |
    awk 'NR == 1 {prev = $0 - 1} {if (prev != $0 - 1) {print $0 - 1; exit}; prev = $0}'
