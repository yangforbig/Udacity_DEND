# Project: Data Modeling with Postgres
This documentation is for the first project of Data Engineer Nanodegree.

### Introduction 
Sparkify would like to make use of user activity data on the app for analytics team to better understand what songs users are listening to. In this project, we create a Postgres database with star schema and also build the ETL pipline to consolidate the data from JSON files.



### Files
- [etl.py]() - Run the file will connect to the Sparkify database, extracts and processes the ***log_data*** and ***song_data***, and loads data into the fact and dimensional tables for a star schema. 
- [create_tables.py]() - Run the file will connect to the Sparkify database, and create five tables. It can also reset the tables before ETL.

    | Table | Type |Description|
    | ------ |----|------ |
    | Songplays | Fact| Records in log data associated with song plays|
    | Users | Dimension | Users in the app |
    | Songs| Dimension | Songs in music database |
    | Artists| Dimension | artists in music database  |
    | Time| Dimension | Timestamps of records in songplays|
    
- [sql_queries.py]() - Contains all the sql queries that will be called in create_tables.py.
- [etl.ipynb]() - Reads and processes a single file for testing in Udaicty work space environment
- [etl.ipynb]() - Reads and processes a single file for testing in local environment.
- [test.ipynb]() - Confirm all the files are running correctly and the records were inserted successfully. 
