import pymysql
import credential
import foodspam_crypto as crypto

def user_signup(id,name,username,password,email,phone_no):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into user_master (user_id,name,user_name,password,email,phone_no) value (%s,%s,%s,%s,%s,%s)"
            # phone_no=int(phone_no)
            curr.execute(sql,(id,name,username,password,email,phone_no))
            conn.commit()
            return 1
    except Exception as e:
        print(e)        
        return 0
def user_login(username,password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select password from user_master where user_name=(%s)"
            curr.execute(sql,username)
            output=curr.fetchone()
            # print(output[0])
            # print(output[0]," hheehe ",password)
            # output = output[0].decode('utf-8')
            if(output):
                temp = output[0]
                temp = bytes(temp,encoding='utf-8')
                temp = crypto.decode(temp)
                if(password == temp):
                    return 1 #"correctPassword"
                else: return 0#"wrongPassword"    
            else:
                return -1 #"UsernameDosenotExit"    
    except Exception as e:
        print(e)       
        
def ngo_signup(ngo_id,ngo_name,username,password,email,phone_no):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into nog_master (ngo_id,ngo_name,username,password,email,phone_no) value (%s,%s,%s,%s,%s,%s)"
            # phone_no=int(phone_no)
            curr.execute(sql,(ngo_id,ngo_name,username,password,email,phone_no))
            conn.commit()
    except Exception as e:
        print(e)        

def ngo_login(username,password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select password from ngo_master where username=(%s)"
            curr.execute(sql,username)
            output=curr.fetchone()
            # print(output)
            if(output):
                if(password == output[0]):
                    return 1 #"correctPassword"
                else: return 0#"wrongPassword"    
            else:
                return -1 #"UsernameDosenotExit"    
    except Exception as e:
        print(e)       

def user_check(user_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select exists(select 1 from user_master where user_id=(%s))"
            curr.execute(sql,(user_id))
            output = curr.fetchone()
            return output[0]
    except Exception as e:
        print(e)   
# print(user_check("hhhdhhd"))