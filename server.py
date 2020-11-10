from flask import Flask,Response,request
from bson.objectid import ObjectId
from flasgger import Swagger 
import pymongo
import json
import pytest

app = Flask(__name__)
app.config.from_object("configuration.TestingConfig")

Swagger(app) 


print(' * Database: ' +  app.config['DB_NAME'])
print(' * Running on: ' + app.config['RUNNING_ON'])
print(app.config)



#Try/except for connection

##################################
#DELETE
@app.route("/users/<id>",methods=["DELETE"])
def delete_user(id):



    """delete users
    ---
    parameters:
        - name: user
        -  in: query
        -  type: string  
        -  required: true
    
    responses:
            200:
                description: The output values
    """
    try:
        dbResponse= db.users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps(
            {"message": "user deleted","id":f"{id}"}),
            status=200,
            mimetype="application/json")
        
        return Response(response=json.dumps(
            {"message": "user not found","id":f"{id}"}),
            status=200,
            mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps(
            {"message": "sorry canot delete user"}),
            status=500,
            mimetype="application/json")

##################################
#UPDATE
@app.route("/users/<id>", methods=["PATCH"])

def update_user(id):

    """update users
    ---
    parameters:
        - name: user
          in: query
          type: string  
          required: true
    
    responses:
            200:
                description: The output values
    """
    try:
        dbResponse = db.users.update_one({"_id":ObjectId(id)}, {"$set":{"name":request.form["name"]}}
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user update"}),
                status=200,
                mimetype="application/json")
        return Response(
                response=json.dumps(
                    {"message": "nothing to update"}),
                status=200,
                mimetype="application/json")


    except Exception as ex:
        print(ex)
        return Response( 
            response = json.dumps({'message':'Cannot update'}), 
            status = 500, 
            mimetype= "application/json")

##################################
#GET
@app.route("/users", methods=["GET"])

def get_users():

    """get users
    ---
    parameters:
        - name: user
          in: query
          type: string  
          required: true
    
    responses:
            200:
                description: The output values
    """
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response( 
            response = json.dumps(data), 
            status = 500, 
            mimetype= "application/json" ) 

    except Exception as ex:
        print(ex)
        return Response( 
            response = json.dumps({'message':'cannot get users'}), 
            status = 500, 
            mimetype= "application/json")
            
########################
#POST
@app.route("/users", methods =["POST"])

def create_user():

    """Post users
    ---
    parameters:
        - name: user
        -  in: query
        -  type: string  
        -  required: true
    
    responses:
            200:
                description: The output values
    """

    try:
        user = {"name": request.form["name"], 
                "lastname": request.form['lastname'] }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attrib in dir(dbResponse):
        #     print(attrib)
        return Response(
            
            response = json.dumps({'message':'user created', 'id':f"{dbResponse.inserted_id}"}), 
            status = 200, 
            mimetype= "application/json")

    except Exception as ex:
        print(ex)
#########################
if __name__ == '__main__':
    app.run(port=80, debug=True)