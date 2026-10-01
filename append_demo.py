from flask import Flask, render_template, request, render_template_string
import os

app = Flask(__name__)

APPEND_FILE = 'append_demo.txt'

@app.route('/', methods=['GET'])
def append_demo():
    content = ''
    if os.path.exists(APPEND_FILE):
        with open(APPEND_FILE, 'r', encoding='utf-8') as f: #Flaggan 'r' (read) anger att filen ska läsas
            content = f.read()
    return render_template("guestbook.html", file_content=content)

@app.route('/append', methods=['POST'])
def append():
    line = "Namn: "
    line += request.form.get("namn")
    print("\n")
    line += "Email: "
    line += request.form.get("email")
    print("\n")
    line += "Hemsida: "
    line += request.form.get("hemsida")
    print("\n")
    line += "telefonnummer: "
    line += request.form.get("tel")
    print("\n")
    line += "kommentar: "
    line += request.form.get("kommentar")
    print("\n")
    #osv...
    print(line)
    if line:
        with open(APPEND_FILE, 'a', encoding='utf-8') as f: #Flaggan 'a' (append) anger att filen ska skrivas till i slutet
            f.write(str(line) + ';')
    # Läs tillbaka hela filen för att visa uppdaterat innehåll
    with open(APPEND_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    x = content.split(";")
    print ("hello world")
    return render_template("guestbook.html", file_content=x)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
