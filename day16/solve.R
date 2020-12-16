#!/usr/bin/env Rscript

library(tidyverse)

rules <- read_csv("rules.csv")
ticket_files <- c("your_ticket.csv", "nearby_tickets.csv")
# ticket with value 1 is your ticket
tickets <- map_dfr(ticket_files, read_csv, col_names = F) %>%
    rowid_to_column(var = "ticket")


# returns tibble of rule, valid checking val if valid for each rule
validate_values <- function(val) {
    rules %>%
        rowwise() %>%
        mutate(valid = between(val, min1, max1) || between(val, min2, max2)) %>%
        ungroup() 
}


# formats validate_values() tibble wide to one row in size to make unnesting easy
validate_field <- function(val) {
    validate_values(val) %>%
        select(field, valid) %>%
        mutate(field = str_replace(field, " ", "_")) %>%
        pivot_wider(names_from = field, values_from = valid)

}

# checks to see if val works for any of the rules (pt 1 solution requirement)
valid_value <- function(val) {
    validate_values(val) %>%
        summarise(any(valid)) %>%
        pluck(1, 1)
}

# Pt 1 solution
tickets %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%
    mutate(valid = map_lgl(value, valid_value)) %>%
    filter(!valid) %>%
    summarise(pt_1_answer = sum(value))

# Pt 2 solution (W.I.P)
tickets %>%
    slice(145) %>%
    pivot_longer(-ticket, names_to = "field", values_to = "value") %>%
    mutate(valid = map(value, validate_field)) %>%
    unnest(valid) %>%
    pivot_longer(!c(ticket, field, value), names_to = "field_name", values_to = "valid") %>%
    group_by(ticket, value) %>%
    summarise(every_valid = any(valid)) %>%
    ungroup() %>%
    filter(!every_valid) %>%
    summarise(pt_1_solution = sum(value))
