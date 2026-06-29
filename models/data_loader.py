import json
import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "database")

def load_classes():
    with open(os.path.join(BASE_PATH, "classes.json"), "r", encoding="utf-8") as f:
        return json.load(f)
    
    
def load_race():
    with open(os.path.join(BASE_PATH, "racas.json"), "r", encoding="utf-8") as f:
        return json.load(f)    