#!/usr/bin/env Rscript

library(tidyverse)

rules <- read_csv("rules.csv")
ticket_files <- c("your_ticket.csv", "nearby_tickets.csv")
# ticket with value 1 is your ticket
tickets <- map_dfr(ticket_files, read_csv, col_names = F) %>%
    rowid_to_column(var = "ticket")


validate_values <- function(val) {
    rules %>%
        rowwise() %>%
        mutate(valid = between(val, min1, max1) || between(val, min2, max2)) %>%
        ungroup() 
}

valid_value <- function(val) {
    total_valid <- validate_values(val) %>%
        summarise(sum(valid)) %>%
        pluck(1, 1)
    total_valid > 0
}

# Pt 1 solution
tickets %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%
    mutate(valid = map_lgl(value, valid_value)) %>%
    filter(!valid) %>%
    summarise(pt_1_answer = sum(value))

# Pt 2 solution

tickets %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%






valid_values <- function(vals) {
    is_valid  <- rep(FALSE, length(vals))
    for (i in seq_along(vals)) {
        for (r in seq(nrow(rules))){
            if (between(vals[i], rules[[r, 2]], rules[[r, 3]]) && between(vals[i], rules[[r, 4]], rules[[r, 5]])) {
                is_valid[i] = TRUE
                break
            }
        }
    }
    is_valid
}

vals_to_test <- tickets %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%
    pull(value)

valid_values(vals_to_test)
