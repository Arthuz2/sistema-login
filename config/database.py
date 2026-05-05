from os import path
import hashlib
import json

class Database:
  def __init__(self):
    self.dbPath: str = path.abspath('data/db.json')

    adminPasswordHash = self.hashPassword("1234")

    adminUser = {
      "id": 0,
      "username": "admin",
      "password": adminPasswordHash
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
      "password": self.hashPassword(password)
    }
    
    users.append(newUser)
    with open(self.dbPath, 'w') as db:
      json.dump({"users": users}, db)

  def isAdmin(self, username: str) -> bool:
    return username == "admin"

  def hashPassword(self, password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()