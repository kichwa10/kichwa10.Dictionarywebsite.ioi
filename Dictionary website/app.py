from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dictionary/")
def dictionary_library():

    title = "Dictionary"
    text = "Choose a letter"
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return render_template("dictionary.html", title=title, text=text, list=list)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    title = "Dictionary"

    s = word.upper()
    f = open('words.txt')
    word_list = f.read().splitlines()
    count = 0
    real_word = s in word_list

    for w in word_list:
        if s == word[0:len(s)]:
            count += 1
    
    list = [word+"a",word+"b",word+"c",word+"d",word+"e",word+"f",word+"g",word+"h",
    word+"i",word+"j",word+"k",word+"l",word+"m",word+"n",word+"o",word+"p",word+"q",word+"r",word+"s",
    word+"t",word+"u",word+"v",word+"w",word+"x",word+"y",word+"z"]
    return render_template("plusdictionary.html", word=word, list=list, title = title, real_word= real_word, count=count)