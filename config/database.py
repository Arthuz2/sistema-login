from os import path
import json

class Database:
  def __init__(self, dbPath: str):
    self.dbPath: str = path.abspath(dbPath)

    adminUser = {
      "id": 0,
      "username": "admin",
      "password": "1234"
    }

    if not path.exists(self.dbPath):
      with open(self.dbPath, 'w') as db:
        json.dump({"users": [adminUser]}, db)

  def getUsers(self):
    with open(self.dbPath, 'r') as db:
      return json.load(db)["users"]

  def addUser(self, username: str, password: str)-> None:
    users = self.getUsers()
    newUser = {
      "id": len(users),
      "username": username,
      "password": password
    }
    
    users.append(newUser)
    with open(self.dbPath, 'w') as db:
      json.dump({"users": users}, db)

  def isAdmin(self, username: str) -> bool:
    return username == "admin"