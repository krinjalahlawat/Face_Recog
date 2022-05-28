import mysql.connector

def insertData(data):
    rowId = 0

    
    conn = mysql.connector.connect(user ='root', password='Admit@1234',host='localhost',database='criminal',port=3306)
    mycursor = conn.cursor()
    print("database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
             data["Nationality"], data["Religion"], data["Crimes Done"])

    try:
        mycursor.execute(query)
        mycursor.fetchall()
        conn.commit()
        conn.close()
        
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")