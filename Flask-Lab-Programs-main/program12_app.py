from flask import Flask,render_template
import pickle
app=Flask(__name__)
@app.route('/')
def hello_world():
 return render_template("order.html")
if __name__=='_main_':
 app.run()
