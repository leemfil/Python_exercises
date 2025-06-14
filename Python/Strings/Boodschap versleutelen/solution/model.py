message = input().strip()
keyword = input().strip().lower()

message_lower = message.lower()
start = message_lower.find(keyword)

print(f"Het codewoord begint op positie {start}.")
print(message[start:])

masked = ""
for char in message:
    if char.isalpha():
        masked += "*"
    else:
        masked += char

print(f"De gemaskeerde boodschap is: {masked}")
