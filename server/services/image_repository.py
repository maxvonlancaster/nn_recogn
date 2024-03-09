import pyodbc 

connection_string = 'DRIVER={SQL Server};SERVER=5CD116MK8R\LOCALDB#51BBDB89;DATABASE=images-app;Trusted_Connection=yes;'

def save_image(image, file_name):
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    SQLCommand = ("INSERT INTO Image(Image, FileName) VALUES(?,?)")
    Values = [image, file_name]
    cursor.execute(SQLCommand, Values)
    connection.commit()
    return 1

def get_images():
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    SQLCommand = ("SELECT * FROM Image")
    cursor.execute(SQLCommand)
    cursor.execute(SQLCommand)
    data = cursor.fetchone()[0]
    connection.commit()
    return data