import mysql.connector as mysql
import inotify.adapters
# import glob
import time
import requests

dbSettings = {
    "host": "IP",  # IP of your MySQL DB
    "user": "user",   # user Name
    "passwd": "password!5",  # password
    "database": "NameOfDB"  # Name Of Db
}

print("Started")


def startListener():
    i = inotify.adapters.Inotify()
    i.add_watch('/home/aidar/Desktop/Python_services')

    currentTime = time.time()

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        if (type_names == ['IN_CREATE']):
            if (time.time() - currentTime > 5):
                currentTime = time.time()
                clearTable("t_prikazy")
            # print(glob.glob("/home/aidar/Desktop/Python_services/*.jpg"))
            # print(counter)
            # print((path + "/" + filename))
            addNewEntry(path + "/" + filename)


def addNewEntry(new_path):
    # db = mysql.connect(
    #     host=dbSettings["host"],
    #     user=dbSettings["user"],
    #     passwd=dbSettings["passwd"],
    #     database=dbSettings["database"])
    # cursor = db.cursor()
    print("http://127.0.0.1:5000/prikazy src=" + new_path)
    response = requests.post('http://127.0.0.1:5000/prikazy', data={'src': new_path})
    print(response.content)
    # query = "INSERT INTO t_prikazy (src) VALUES (%s)"
    # values = (new_path,)

    # cursor.execute(query, values)
    # db.commit()
    # print(cursor.rowcount)
    # db.close()

def clearTable(tableName):
    db = mysql.connect(
        host=dbSettings["host"],
        user=dbSettings["user"],
        passwd=dbSettings["passwd"],
        database=dbSettings["database"])
    cursor = db.cursor()
    cursor.execute("DROP TABLE " + tableName)
    cursor.execute("CREATE TABLE t_prikazy( _created DATETIME, _updated DATETIME,_etag VARCHAR(40), id_img INTEGER NOT NULL AUTO_INCREMENT,src VARCHAR(255) NOT NULL,PRIMARY KEY(id_img))ENGINE=InnoDB CHARSET=UTF8MB4")
    print("Table cleared succesfully")
    db.close()


# addNewEntry(1, "23")
startListener()
