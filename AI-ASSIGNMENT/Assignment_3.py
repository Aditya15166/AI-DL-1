# Parsing Family Tree Using Knowledge Base

family_tree = {
    "Adam": {"children": ["Cain", "Abel"], "spouse": "Eve"},
    "Eve": {"children": ["Cain", "Abel"], "spouse": "Adam"},
    "Cain": {"children": [], "spouse": None},
    "Abel": {"children": [], "spouse": None}
}

def get_children(person):
    return family_tree.get(person, {}).get("children", [])

def get_spouse(person):
    return family_tree.get(person, {}).get("spouse", None)

print("Children of Adam:", get_children("Adam"))
print("Spouse of Eve:", get_spouse("Eve"))
