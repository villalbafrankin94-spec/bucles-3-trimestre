
texto = "copilot"
alternado = ""
for i, c in enumerate(texto):
    alternado += c.upper() if i % 2 == 0 else c.lower()
print(alternado)
