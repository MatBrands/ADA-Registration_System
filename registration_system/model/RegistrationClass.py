import os
import json

class Registration:
    def __init__(self, path: str = './controller/database.json') -> None:
        self.path = path
        if not os.path.exists(self.path):
            data = {}
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        
    def number_users(self) -> int:
        path = self.path
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return len(data)
        
    def create_user(self, **user_data: dict) -> bool:
        path = self.path
        
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if user_data['id'] in data:
            return False
        
        new_user = {
            user_data['id']: {
                'name': user_data['name'],
                'telephone': user_data['telephone'],
                'address': user_data['address'],
                'status': True
            }
        }
    
        data.update(new_user)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    
    def update_user(self, **user_data: dict) -> bool:
        path = self.path
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if user_data['id'] not in data:
            return False

        if not data[user_data['id']]['status']:
            return False
        
        user = {
            user_data['id']: { 
                'name': user_data['name'],
                'contact': user_data['contact'],
                'address': user_data['address'],
            }
        }
        
        data.update(user)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    def all_info_user(self) -> dict | bool:
        path = self.path
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        ative_users = { }
        for key, item in data.items():
            if item['status']:
                ative_users[key] = item
                
        if not len(ative_users):
            return False
                
        return ative_users
    
    