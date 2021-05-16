import models
from models import Customer
from flask import Flask, request, session, redirect, url_for, render_template, flash,json,jsonify
import os
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def enter_ID():
    if request.method == 'POST':
         Galactic_ID = request.form['Galactic_ID']
         if Customer(Galactic_ID).find():
            return redirect(url_for('Customer_relationships',Galactic_ID=request.form.get('Galactic_ID')))
         else:
             return  "Wrong Galactic_ID"

     else:
         return render_template('Gal.html')

@app.route('/Customer_relationships/<Galactic_ID>')
def Customer_relationships(Galactic_ID):
    data = Customer(Galactic_ID).get_relationships():
    return render_template('rel.html',Galactic_ID=Galactic_ID,data =json.dumps(data))



if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.secret_key = os.urandom(24)
    app.run(host=host,port=port)