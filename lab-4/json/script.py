import json

# Открытие JSON-файла
with open("sample_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Вывод количества элементов
print(f"Total Count: {data['totalCount']}")

# Вывод всех интерфейсов
for interface in data["imdata"]:
    attributes = interface["l1PhysIf"]["attributes"]
    print(f"Interface ID: {attributes['id']}, Status: {attributes['switchingSt']}")
