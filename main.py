import uvicorn
from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}
    




 # mydb = mysql.connector.connect(
 #  host='db-c9sandbox-bob.cgjfhllahdce.eu-west-2.rds.amazonaws.com',
 #  user='admin',
 #  password='morri1359',
 #  database='db-c9sandbox-bob')
 
 
 # mycursor = mydb.cursor()
 #mycursor.execute("SHOW DATABASES")
 #mycursor.execute("USE db-c9sandbox-bob")

 # mycursor.execute("SHOW TABLES")

 # for x in mycursor:
 #    print(x)

 
 # base = declarative_base()

# General Config
 #   SECRET_KEY = environ.get('SECRET_KEY')
  #  FLASK_APP = environ.get('FLASK_APP')
  #  FLASK_ENV = environ.get('FLASK_ENV')
    
    


if __name__ == '__main__':
   uvicorn.run("main:app", port=8080, reload=True, access_log=False)
 
    