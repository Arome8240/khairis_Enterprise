from flask import Flask, request,redirect, url_for,g, render_template
import sqlite3

app= Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="SKJF KDKLJK DJJJE KJDJ"

def connect_db():
    sql= sqlite3.connect(r"C:\Users\YAKSON HDJ\Desktop\khairis_Enterprise\data.db")
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g,"sqlite3"):
        g.sqlite_db = connect_db()
        return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g,"sqlite_db"):
        g.sqlite_db.close()

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=='GET':
        return render_template('contact.html')
    else:
        fullname = request.form['fullname']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        address = request.form['address']
       
        db = get_db()
        db.execute('insert into signup(fullname,email,phonenumber,address) values(?,?,?,?)', [fullname,email,phonenumber,address])
        db.commit()
        return redirect(url_for('contact'))


@app.route('/', methods=['POST','GET'])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        return redirect(url_for('theform'))



@app.route('/theform', methods=["POST", "GET"])
def theform():
    if request.method=='GET':
        return render_template('theform.html')
    else:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
       
        db = get_db()
        db.execute('insert into contact(name,email,message) values(?,?,?)', [name,email,message])
        db.commit()
        return redirect(url_for('theform'))



if __name__=="__main__":
    app.run()