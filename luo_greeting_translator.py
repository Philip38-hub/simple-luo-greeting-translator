#dictionary function task
def converter(message):
    words = message.split(" ")
    translater = {
        "goodmorning" : "Oyawre",
        "goodevening" : "Oimore",
        "hello" : "amosi"
    }
    translated = ""
    for word in words:
        translated += translater.get(word, "!") + ""
    return translated


message = input("> ").lower()
print(converter(message))