with open("harry_potter_sample.txt", "r") as f:
    text = f.read()

new_text = ""
for i in range(len(text)-1):
    if text[i] == " " and text[i+1] == "\n" and text[i-1].islower() and text[i+2].islower():
        new_text += " "
    elif text[i] == "\n" and text[i-1] == " ":
        pass
    else:
        new_text += text[i]
new_text += text[-1]

with open("FIXED_harry_potter_page.txt", "w") as f:
    f.write(new_text)