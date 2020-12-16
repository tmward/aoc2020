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
validated_tickets <- tickets %>%
    pivot_longer(
        -ticket,
        names_to = "field",
        names_prefix = "X",
        names_transform = list(field = as.integer),
        values_to = "value"
    ) %>%
    mutate(valid = map_lgl(value, valid_value)) 

validated_tickets %>%
    filter(!valid) %>%
    summarise(pt_1_answer = sum(value))

# Pt 2 solution (W.I.P)
# First remove invalid tickets in the validated_tickets
valid_tickets <- validated_tickets %>%
    group_by(ticket) %>%
    filter(all(valid)) %>%
    ungroup() %>%
    select(-valid)

# remove field names that are impossible based off having a false value
# for a certain field
validated_fields <- valid_tickets %>%
    mutate(valid = map(value, validate_field)) %>%
    unnest(valid) %>%
    pivot_longer(!c(ticket, field, value), names_to = "field_name", values_to = "valid") %>%
    group_by(field, field_name) %>%
    # if a field name is invalid even once for a certain field then we
    # know that field name can't work for that field
    filter(all(valid)) %>%
    ungroup()

# Filtering out the impossible fieldnames for each field is not enough
# (of course not that would be too easy). However, once the impossible
# field names are out, there is *one* field that can only have *one*
# possible fieldname. (There are also 2 fields that can have 2
# fieldnames, 3 fields with 3 fieldnames, etc). So start by finding that
# one field and its fieldname, save it, then iterate 19 more times,
# first filtering out rows that have previously seen answers
answers <- vector(mode = "character", length = max(validated_fields$field))
for (i in seq_along(answers)) {
    field_and_name <- validated_fields %>%
        filter(!field_name %in% answers) %>%
        group_by(ticket, field) %>%
        # once all previously seen answers filtered out, there is
        # one field that can have only one valid field name so get that
        # name
        filter(n() == 1) %>%
        ungroup() %>%
        distinct(field, field_name)
    answers[field_and_name[["field"]]] <- field_and_name[["field_name"]]
}
# rename fields for columns now that we know the valid names
colnames(tickets) <- c("ticket", answers)
# Calculate the answer:
tickets %>%
    filter(ticket == 1) %>%
    select(ticket, starts_with("departure")) %>%
    pivot_longer(-ticket, names_to = "fieldname") %>%
    summarise(part_2_answer = reduce(value, `*`))
