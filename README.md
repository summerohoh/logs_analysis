# Logs Analysis

----
## Overview
>a Python program reporting tool that prints out reports based on the data in the database. The program runs from the command line. It does not take any user input. Instead, it uses the psycopg2 module to connect to the database, SQL queries to analyze the log data, print out the answers to three questions.


## Set Up

#### 1. Install VirtualBox [here](https://www.virtualbox.org/wiki/Downloads

#### 2. Install Vagrant [here](https://www.vagrantup.com/downloads.html)

#### 3. Download the VM configuration.
* Download and unzip this [file](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

#### 4. Launch the Virtual Machine:
From your terminal, inside the vagrant subdirectory, run the command

    vagrant up

When finished, run

    vagrant ssh

to log in to the newly installed Linux VM

#### 5. Load the data

cd into the vagrant directory and use the command

    psql -d news -f newsdata.sql

#### 6. Run the program on terminal

    python3 logs_analysis.py

----
## Report

The reporting tool answers the following questions.

* **1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

* **2. Who are the most popular article authors of all time? **That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

* **3. On which days did more than 1% of requests lead to errors?**  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)


----
## Source
* Udacity - Full Stack Developer Nanodegree
