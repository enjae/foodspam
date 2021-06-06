import pymysql
import credential

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
            sql = "insert into user_master (id,name,username,password,email,phone_no) value (%s,%s,%s,%s,%s,%s)"
            # phone_no=int(phone_no)
            curr.execute(sql,(id,name,username,password,email,phone_no))
            conn.commit()
    except Exception as e:
        print(e)        

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
            sql = "select password from user_master where username=(%s)"
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
