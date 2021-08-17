# First Udacity Project - PostgresSql.
# Introduction

Sparkify is a startup company where the data collected on songs and user activity are analyzed using there new music streaming app. This analyses will help in understanding the users interest towards the type of songs.

The aim of the project is to create a Database Schema and ETL pipeline so that the data is clean and available for the analysts.

# Project Description

In this project, a data model, i.e, the fact and dimension tables for a Star Schema are created in Postgres. An ETL pipeline in created in Python collect the data from data storage location, data wrangling is performed to collect the required data from the raw data in files and the data is cleaned and transformed into the tables.

# Schema for Song Play Analysis

## Fact Table

* songplays - contains the log data for all the songs played by users

## Dimension Tables

* users - details of the users

* songs - details regarding the songs in the app

* artists -details of the artists in the songs

* time  - processed data from the timestamps of records in songplays 

# Scripts

* sql_queries.py -all sql queries to drop existing table and create new tables in the sparkify database.

* create_tables.py -  drops and created sparkify database and calls create and drop queries from the sql_queries.

* etl.ipynb - read and processes a first file from song_data and log_data.

* etl.py - read and processes all the files from song_data and log_data and loads processed data into your tables.

* test.ipnb - displays the first few rows of each table to let you check your database

