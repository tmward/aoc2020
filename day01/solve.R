#!/usr/bin/env Rscript
d <- read.table("input.txt")[, 1]

for (i in d) {
  complement <- 2020 - i
  if (complement %in% d && i != complement) {
    print(paste("Part 1 answer:", i * complement))
    break
  }
}

answered <- FALSE
for (i in d) {
  for (j in d) {
    complement <- 2020 - (i + j)
    if (complement %in% d && i * 3 != 2020) {
      print(paste("Part 2 answer:", i * j * complement))
      answered <- TRUE
      break
    }
  }
  if (answered) {
    break
  }
}
