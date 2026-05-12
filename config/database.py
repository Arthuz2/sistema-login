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
        json.dump({"users": [adminUser], "tasks": []}, db)

  def _readDb(self) -> dict:
    with open(self.dbPath, 'r') as db:
      data = json.load(db)
    if "tasks" not in data:
      data["tasks"] = []
    return data

  def _writeDb(self, data: dict) -> None:
    with open(self.dbPath, 'w') as db:
      json.dump(data, db)

  def getUsers(self):
    return self._readDb()["users"]

  def getUserByUsername(self, username: str):
    for user in self.getUsers():
      if user["username"] == username:
        return user
    return {}

  def addUser(self, username: str, password: str) -> None:
    data = self._readDb()
    nextId = max((u["id"] for u in data["users"]), default=-1) + 1
    data["users"].append({
      "id": nextId,
      "username": username,
      "password": self.hashPassword(password)
    })
    self._writeDb(data)

  def deleteUser(self, userId: int) -> None:
    data = self._readDb()
    data["users"] = [u for u in data["users"] if u["id"] != userId]
    data["tasks"] = [t for t in data["tasks"] if t["userId"] != userId]
    self._writeDb(data)

  def isAdmin(self, username: str) -> bool:
    return username == "admin"

  def getTasks(self):
    return self._readDb()["tasks"]

  def getTasksByUser(self, userId: int):
    return [t for t in self.getTasks() if t["userId"] == userId]

  def addTask(self, title: str, description: str, userId: int) -> None:
    data = self._readDb()
    nextId = max((t["id"] for t in data["tasks"]), default=-1) + 1
    data["tasks"].append({
      "id": nextId,
      "title": title,
      "description": description,
      "userId": userId,
      "done": False
    })
    self._writeDb(data)

  def updateTask(self, taskId: int, title: str, description: str) -> None:
    data = self._readDb()
    for task in data["tasks"]:
      if task["id"] == taskId:
        task["title"] = title
        task["description"] = description
        break
    self._writeDb(data)

  def toggleTask(self, taskId: int) -> None:
    data = self._readDb()
    for task in data["tasks"]:
      if task["id"] == taskId:
        task["done"] = not task.get("done", False)
        break
    self._writeDb(data)

  def deleteTask(self, taskId: int) -> None:
    data = self._readDb()
    data["tasks"] = [t for t in data["tasks"] if t["id"] != taskId]
    self._writeDb(data)

  def hashPassword(self, password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()