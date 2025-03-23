import json
from dataclasses import dataclass
from pymongo import MongoClient
from datetime import datetime

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float  

def parse_roles(data):
    roles = []
    if data.get('is_user_admin'):
        roles.append('admin')
    if data.get('is_user_manager'):
        roles.append('manager')
    if data.get('is_user_tester'):
        roles.append('tester')
    return roles

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['crudify']
    collection = db['users']
    
    with open('server/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    users_list = data.get("users", data)

    for item in users_list:
        created_at_str = item.get('created_at')
        if created_at_str:
           
            dt = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ")
            created_ts = dt.timestamp()
        else:
            created_ts = datetime.utcnow().timestamp()
            
        user = User(
            username=item.get('user'),
            password=item.get('password'),
            roles=parse_roles(item),
            preferences=UserPreferences(timezone=item.get('user_timezone')),
            active=item.get('is_user_active', True),
            created_ts=created_ts
        )
        resultado = collection.insert_one({
            'username': user.username,
            'password': user.password,
            'roles': user.roles,
            'preferences': user.preferences.__dict__,
            'active': user.active,
            'created_ts': user.created_ts
        })
        print(f"Usuário {user.username} inserido com _id: {resultado.inserted_id}")

if __name__ == '__main__':
    main()
