from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '35739719Abc'
app.config['MYSQL_DB'] = 'ADC'

 
mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def Index():
	return render_template("index.html")


@app.route("/Register", methods=["GET", "POST"])
def Register():
    if request.method == 'POST':
        content = request.form
        name = content['Name']
        email = content['Email']
        phone = content['Phone']
        country = content['Country']
        occupation = content['Occupation']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Contact(Name, Email, Phone, Country, Occupation) VALUES(%s, %s, %s, %s, %s)", [name, email, phone, country, occupation])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("Success"))
    return render_template("register.html")    


@app.route("/Success", methods=["GET", "POST"])
def Success(): 
    return render_template('success.html')
  


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404






if __name__ == '__main__':
	app.run(debug=True)

