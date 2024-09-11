#objective: develop a RESTful API using Python that implements all CRUD operations using HTTP methods

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 



#using fastapi to create a new app
app = FastAPI()

class User(BaseModel):
    id: int #uniqueidentifier
    name: str
    email: str

#Sample data, holds user objects
user_db: List[User] = [
   
    User(id=1, name= 'Jefferson', email= 'jeffersonphato@gmail.com'),
    User(id=2, name= 'John', email='john@gmail.com')
]

#GET endpoint to retrieve all users in list

@app.get('/users')
def get_users():
    
        return user_db
    



#GET endpoint to retrieve a specific user from a list
@app.get('/users/{user_id}') 
def get_user(user_id: int):
    for user in user_db:
        if user.id== user_id:
            return user
        
    raise HTTPException(status_code=404, detail='user not found')
        

#Post endpoint to add new user to users_db
@app.post('/users')
def create_user(new_user: User):
    user_db.append(new_user)
    return new_user
    
#put endpoint to update existing user
@app.put('/users/{user_id}',response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, existing_user in enumerate(user_db):
        if existing_user.id == user_id:
            # Update the user data
            user_db[index] = updated_user
            return {"user_id": user_id, **updated_user.model_dump()}
    raise HTTPException(status_code=404, detail="User not found")

#delete endppoint to delete data from user_db list using user_id

@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    for user in user_db:
        if user.id == user_id:
            user_db.remove(user)
            return {'message': 'user has been deleted'}
        
    raise HTTPException(status_code=404, detail='Specified id not found')
