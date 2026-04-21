text = "hello@# world!! 123"

result = " "

for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch
print(result)