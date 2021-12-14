# sparkify_nosql_populate

## Summary
This script creates and then populates 3 tables in an Apache Cassandra database.
As part of the data insertion, three queries are called against the new tables.
Follow the CLI instructions to view the results.

## Installation

1. Clone repo
2. Install all requirements in requirements.txt
3. Ensure you have localhost access to a cassandra node

## Running the code
All queries can be found in cql_queries.

1. Execute create_csv_data.py to generate the final CSV export
2. Execute create_tables.py to build the three tables for querying
3. Execute etl.py to insert the data and view the results of the validation queries.
