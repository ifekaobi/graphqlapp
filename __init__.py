from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)
@app.route('/base',methods=['GET','POST'])
def home():
    Name = "jeff"
    if request.method=='POST':
        return render_template('base.html')
    return render_template('base.html',Name=Name)
      


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)