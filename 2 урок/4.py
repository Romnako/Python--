text = "Мороз и солнце - день чудесный!"
print(text.split())
for st in text.split():
    print(text)

text = ("Мороз и солнце - день чудесный!").split()
length = len(text)
for i in range(length):
    print(str(i + 1), text[i])
print('------------------------->')
text = "Мороз и солнце - день чудесный!"
n = 10
for i in range(1, n):
    text = ":)" + text + "%"
print(text)