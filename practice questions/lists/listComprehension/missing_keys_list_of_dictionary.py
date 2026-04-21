data = [{"id":1},{},{"id":2}]
result = [item.get("id") for item in data]
print(result)
