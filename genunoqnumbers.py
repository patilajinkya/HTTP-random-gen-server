import mysql.connector


def mysql_connection():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="new_password",
    database="random_numbers"
    )
    return mydb

def mysql_insert_random_generated_numbers(random_number):
    mydb = mysql_connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO numbers (num) VALUES (%s)"
    val = [random_number]
    mycursor.execute(sql, val)

    mydb.commit()
    return True





def mysql_get_listof_already_generated_numbers():

    mydb = mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM numbers")
    myresult = mycursor.fetchall()
    return myresult

mysql_insert_random_generated_numbers()

myresult = mysql_get_listof_already_generated_numbers()

