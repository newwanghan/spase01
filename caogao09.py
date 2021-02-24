import time
import datetime


def second_timestamp():
    return str(
        int(time.mktime(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S"))))


def login():
    print('---------------------用户登陆---------------------')
    cont = 2
    li_user = []
    li_pw = []
    while True:
        user = input('请输入用户名：')
        user_pw = input('请输入密码：')
        with open('pw.txt') as f:
            for i in f.readlines():
                b = i.split('=')
                if 'username' == b[0].strip():
                    username = b[1].strip()
                elif 'passwd' == b[0].strip():
                    passwd = b[1].strip()
                elif b[0].strip().startswith('username') and len(b[0]) > 8:
                    li_user.append(b[1].strip())
                elif b[0].strip().startswith('passwd') and len(b[0]) > 6:
                    li_pw.append(b[1].strip())
            if cont > 0:
                if username == user and passwd == user_pw:
                    print('***登陆成功***')
                    break
                else:
                    if user not in li_user and user_pw in li_pw and user != username and user_pw == passwd:
                        print('用户名输入有误，您还有{0}次输入机会'.format(cont))
                        tmp_u = 'username' + second_timestamp() + '=' + user + '\n'
                        tmp_p = 'passwd' + second_timestamp() + '=' + user_pw + '\n'
                        with open('pw.txt', 'a+') as f1:
                            f1.write(tmp_u)
                            f1.write(tmp_p)
                        cont -= 1
                        continue
                    elif user == username and user_pw != passwd:
                        print('密码输入有误，您还有{0}次输入机会'.format(cont))
                        tmp_p = 'passwd' + second_timestamp() + '=' + user_pw + '\n'
                        with open('pw.txt', 'a+') as f1:
                            f1.write(tmp_p)
                        cont -= 1
                        continue
                    elif user not in li_user and user_pw not in li_pw and user != username and user_pw != passwd:
                        print('请输入正确的用户，您还有{0}次输入机会'.format(cont))
                        tmp_u = 'username' + second_timestamp() + '=' + user + '\n'
                        tmp_p = 'passwd' + second_timestamp() + '=' + user_pw + '\n'
                        with open('pw.txt', 'a+') as f1:
                            f1.write(tmp_u)
                            f1.write(tmp_p)
                        cont -= 1
                        continue
            else:
                print('用户已锁定')
                break


if __name__ == '__main__':
    login()
