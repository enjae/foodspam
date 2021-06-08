from flask import Flask,render_template,redirect,session,request
import db as api
import foodspam_crypto as crypto
import generate as gen
import credential
app = Flask(__name__)
app.secret_key=credential.secret_key

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return render_template('home.html')
@app.route('/index')
def index():
    # if 'username' in session:
    return render_template('index.html')

@app.route('/user_login',methods=['POST','GET'])
def user_login():
    try:
        if 'username' in session:
            return render_template('index.html')
        if request.method=='POST':
            details = request.form
            # print(details)
            # print(details['password'])
            # password = crypto.encrypt(details['password'])
            # print(password,"     jhhhh")
            t = api.user_login(details['username'],details['password'])
            if(t==1):
                session['username']=details['username']
                return redirect('/index')
            if t==0:
                print("wrong password")
                return render_template('/user_templates/login.html')
            if t==-1:
                print("username dosenot exist")
                return render_template('/user_templates/login.html')    
        return render_template("/user_templates/login.html")
    except Exception as e:
        print(e)
        return render_template("/user_templates/login.html")
# gAAAAABgv0gTwO65hoBGIKQQUFRCKZXSAh8g3F6zyXmJ19nPNLskHvtEFHLEYD5s0hLdi65E6gTwZJm-SRWV-YyNQ2-j6nMdMw==
@app.route('/user_signup',methods=['POST','GET'])
def user_signup():
    try:
        if 'username' in session:
            return render_template('index.html')
        if request.method=='POST':
            details = request.form
            # print(details)
            id = gen.get_id()
            id = "User"+str(id)
            while(api.user_check(id)==1):
                id = gen.get_id()
                id = "User"+str(id) 
                print("hello") 
            password = crypto.encrypt(details['password'])
            password = str(password,'UTF-8')
            # print(password)
            t = api.user_signup(id,details['name'],details['username'],password,details['email'],details['phone_no'])
            if(t==1):
                # session['username']=details['username']
                return redirect('/user_login')
            if t==0:
                print("signup insertion error")
                return render_template('/user_templates/signup.html')   
        return render_template("/user_templates/signup.html")
    except Exception as e:
        print(e)
        return render_template("/user_templates/signup.html")

@app.route('/ngo_login')
def ngo_login():
    return render_template("//ngo_templates//ngo_login.html")

if __name__=='__main__':
    app.run(debug=True)