from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy ()

import pypyodbc


Connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=tcp:l4osrvrdb.database.windows.net,1433;'
                              'Database=L4Odev;'
                              'Uid=l4o@l4osrvrdb;Pwd=Us3r_Lf01.01;'
                              'Encrypt=yes')
cursor = myConnection.cursor()
cursor.execute("Select * from Categorias")
myConnection.close()