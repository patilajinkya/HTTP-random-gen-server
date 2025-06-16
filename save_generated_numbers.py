import mysql.connector
from dotenv import load_dotenv
import os

#Mysql Connection logic, picking up the environment variables from .env file using load_dotenv
def mysql_connection():
    load_dotenv()
    mydb = mysql.connector.connect(
    host=os.getenv("HOSTNAME"),
    user=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
    )
    return mydb

#Logic to insert generated random number to mysql db to make it persistent.
def mysql_insert_random_generated_numbers(rand_number):
    table = "numbers"
    mydb = mysql_connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO " + table + " (num) VALUES (%s)"
    val = [rand_number]
    mycursor.execute(sql, val)
    mydb.commit()
    return True

#Logic to get the list of the stored random numbers iun previous runs.
#This code runs first to make sure that, web app has list of already generated numbers.
#As the results are returned in tuple format added a logic to extract the number form the tuple.
def mysql_get_listof_already_generated_numbers():
    table = "numbers"
    mydb = mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall() # Storing results to process them later to convert in list format.
    numbers = []  # Create an empty list.
    for item in myresult:
        numbers.append(item[0])  # Extract the number from the tuple and add to the list.
    return numbers


