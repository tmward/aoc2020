#!/usr/bin/env Rscript
suppressPackageStartupMessages(library(tidyverse))

# Prep/process the input file into nice columns
dat <- "input.txt" %>%
    read_delim(
        delim = " ",
        col_names = c("min_max", "letter", "pass"),
        col_types = "ccc"
    ) %>%
    separate("min_max", c("min_n", "max_n"), sep = "-", convert = TRUE) %>%
    mutate(letter = str_remove(letter, ":.*$")) %>%
    rowwise()

print("Part 1 solution:")
dat %>%
    filter(between(str_count(pass, letter), min_n, max_n)) %>%
    nrow()

print("Part 2 solution:")
dat %>%
    # TRUE is 1, FALSE is 0; Only want one TRUE so sum of two
    # conditionals needs to be 1
    filter(
        1 == sum(
            letter == str_sub(pass, min_n, min_n),
            letter == str_sub(pass, max_n, max_n)
        )
    ) %>%
    nrow()
