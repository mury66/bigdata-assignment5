\# BigData Assignment 5 - Complete Solution



\*\*Student:\*\* \[حط اسمك هنا]  

\*\*Course:\*\* BigData  

\*\*Instructor:\*\* Ahmed Salama  

\*\*Date:\*\* January 30, 2026



---



\## Tasks Completed ✅



\### Task 1: MySQL Database Setup

\- Created database: `bigdata\_db`

\- Created table: `users (id, name, age)`

\- Inserted 3 records



\*\*Commands:\*\*

```sql

CREATE DATABASE bigdata\_db;

USE bigdata\_db;

CREATE TABLE users(id INT PRIMARY KEY, name VARCHAR(50), age INT);

INSERT INTO users VALUES (1,'Ahmed',25), (2,'Sara',30), (3,'Omar',28);

```



---



\### Task 2: Sqoop Import (MySQL → HDFS)

\- Imported data from MySQL to HDFS using Sqoop

\- Used local mapreduce mode



\*\*Command:\*\*

```bash

sqoop import \\

&nbsp; -Dmapreduce.framework.name=local \\

&nbsp; --connect jdbc:mysql://mysql:3306/bigdata\_db \\

&nbsp; --username root \\

&nbsp; --password password \\

&nbsp; --table users \\

&nbsp; --target-dir /user/bigdata/users \\

&nbsp; --delete-target-dir \\

&nbsp; --fields-terminated-by ',' \\

&nbsp; -m 1

```



\*\*Result:\*\* 3 records imported successfully to HDFS



---



\### Task 3: HDFS Data Verification

\- Verified data exists in HDFS

\- Checked file contents



\*\*Commands:\*\*

```bash

hdfs dfs -ls /user/bigdata/users

hdfs dfs -cat /user/bigdata/users/part-m-00000

```



\*\*Output:\*\*

```

1,Ahmed,25

2,Sara,30

3,Omar,28

```



---



\### Task 4: Hive Data Analysis

\- Created external Hive table

\- Ran analytical queries



\*\*Commands:\*\*

```sql

CREATE DATABASE bigdata\_hive;

USE bigdata\_hive;



CREATE EXTERNAL TABLE users (

&nbsp;   id INT,

&nbsp;   name STRING,

&nbsp;   age INT

)

ROW FORMAT DELIMITED

FIELDS TERMINATED BY ','

LOCATION '/user/bigdata/users';



SELECT \* FROM users;

SELECT COUNT(\*) FROM users;

SELECT AVG(age) FROM users;

```



---



\### Task 5: Export to MySQL

\- Created new table in MySQL

\- Exported new data from HDFS to MySQL



\*\*Result:\*\* Successfully added new records to MySQL



---



\### Task 6: PySpark Data Processing

\- Read data from HDFS using PySpark

\- Performed data analysis

\- Created new records

\- Exported to HDFS



\*\*Script:\*\* `pyspark\_task6.py`



\*\*Operations:\*\*

\- Read users data from HDFS

\- Displayed statistics

\- Filtered data (age > 25)

\- Created 3 new records

\- Saved to HDFS



---



\### Task 7: GitHub Repository

\- All code and documentation uploaded to GitHub

\- Repository organized and documented



---



\## Technologies Used



\- \*\*MySQL 5.7\*\* - Relational Database

\- \*\*Hadoop 3.2.1\*\* - Distributed Storage (HDFS)

\- \*\*Sqoop 1.4.6\*\* - Data Transfer Tool

\- \*\*Hive 3.x\*\* - Data Warehousing

\- \*\*PySpark\*\* - Big Data Processing

\- \*\*Docker\*\* - Containerization



---



\## Setup Instructions



\### Prerequisites:

\- Docker installed

\- MySQL container running

\- Hadoop cluster running (namenode, datanode, resourcemanager)

\- Sqoop container running



\### Running the Assignment:



1\. \*\*Task 1:\*\* Run SQL commands in MySQL

2\. \*\*Task 2:\*\* Run Sqoop import command

3\. \*\*Task 3:\*\* Verify with HDFS commands

4\. \*\*Task 4:\*\* Run Hive queries

5\. \*\*Task 5:\*\* Export data to MySQL

6\. \*\*Task 6:\*\* Run PySpark script

7\. \*\*Task 7:\*\* Push to GitHub



---



\## Key Learnings



\- Data flow in Big Data ecosystem

\- ETL processes using Sqoop

\- HDFS storage and management

\- SQL-like queries on distributed data using Hive

\- Large-scale data processing with PySpark

\- Integration between different Big Data tools



---



\## Next Steps



\- Machine learning implementation إن شاء الله

\- Advanced analytics

\- Real-time data processing



---



\*\*Repository:\*\* \[Your GitHub Link Here]

