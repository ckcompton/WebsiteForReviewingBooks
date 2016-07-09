__author__ = 'Cameron'


def get_authfirstname(cur):

    cur.execute('SELECT auth_firstname FROM author')
    return [sk for (sk,) in cur]





def login_check(cur,email, password, auth_e = None):
    cur.execute('''
        SELECT user_email,user_password
        FROM "user"
        WHERE user_email = %s AND user_password = %s
    ''', (email,password))


    for user_e, user_p in cur:
        auth_e.append({'user_e': user_e, 'user_p': user_p})
    return auth_e

def get_signup(cur, firstname, lastname, email, password, user_pic_url, user_url, date_joined, dob):

    cur.execute('''
      INSERT INTO "user"(user_firstname,user_lastname,user_email, user_password, user_id,user_pic_url, user_url,date_joined,dob)
      VALUES (%s,%s,%s,%s,DEFAULT,%s,%s,%s,%s)
    ''', (firstname, lastname, email, password,user_pic_url, user_url,date_joined,dob))

def get_credentials(cur,email):
    cur.execute('''
        SELECT user_id, user_email,user_firstname,user_lastname,user_url,user_pic_url,date_joined, dob
        FROM "user"
        WHERE user_email = %s
    ''', (email,))
    credentials = []

    for u_id, u_email, f_name, l_name, url, pic_url, join_date, birth in cur:
        credentials.append({'u_id': u_id, 'u_email': u_email, 'f_name': f_name, 'l_name': l_name, 'url': url, 'pic_url': pic_url, 'join_date': join_date, 'birth': birth })
    return credentials
'''
def get_user_id(cur):
    cur.execute('SELECT COUNT(user_id) FROM "user"')
    (count,) = cur.fetchone()
    return count
'''