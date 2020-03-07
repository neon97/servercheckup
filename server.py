import psycopg2
from flask import Flask
from flask import jsonify
import json
import pandas as pd

app = Flask(__name__)


fire = "select * from emp"



def emp():
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "9159",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "manager")

        # cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        # print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        # cursor.execute("select * from emp;")
        # record = cursor.fetchall()
        record = pd.read_sql(fire,connection)
        #print("You are connected to - ", record,"\n")
        #print(type(record))

        return record

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                # cursor.close()
                connection.close()
                # print("PostgreSQL connection is closed")



@app.route('/emp')
def home():
    return (
        {
            "sales":"true",
            "aiima":"true"
        }
    )
    # data = emp()
    # print(data)
    # return json.dumps(data)
    # return jsonify("hello")
    #return json.dumps(data.to_dict(orient='records'))
    # return jsonify(data.to_dict(orient='records'))
    #return 'Hello Flask'

#home()
# app.run(debug=True)