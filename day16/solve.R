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

validate_field <- function(val) {
    validate_values(val) %>%
        select(field, valid) %>%
        mutate(field = str_replace(field, " ", "_")) %>%
        pivot_wider(names_from = field, values_from = valid)

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
    slice(168) %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%
    mutate(valid = map(value, validate_field)) %>%
    unnest(valid)
