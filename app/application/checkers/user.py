# -*- coding: utf-8 -*-
import datetime
import re
def register_params_check(content):
    try:
        result_id = check_id(content.get('username'))
        if result_id == 1:
            pass
        else:
            return "username", False
    except:
        return "username", False

    result_password = check_password(content.get('password'))
    if result_password == 1:
        pass
    else:
        return "password", False
    result_nickname = check_nickname(content.get('nickname'))
    if result_nickname == 1:
        pass
    else:
        return "nickname", False
    result_citizen = check_citizen(content.get('document_number'))
    if result_citizen == 1:
        pass
    else:
        return "document_number", False
    result_mobile = check_phonenumber(content.get('mobile'))
    if result_mobile == 1:
        pass
    else:
        return "mobile", False
    result_email = check_email(content.get('email'))
    if result_email == 1:
        pass
    else:
        return "email", False

    return "ok", True




def check_citizen(citizen):
    if type(citizen) == str:
        pass
    else:
        return 0
    w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1]
    check = ['1','0','X','9','8','7','6','5','4','3','2']
    a = []
    sum = 0
    c_len = len(citizen)
    if(c_len != 18):
        print('length of citizen id is not correct')
        return 0
    if citizen[0:16].isdigit():
        pass
    else:
        print('citizen_num is not a number')
        return 0

    year = int(citizen[6:10])
    month = int(citizen[10:12])
    day = int(citizen[12:14])
    print(year,month,day)
    try:
        datetime.date(year,month,day)
    except:
        print('invalid date')
        return 0
    for element in citizen[0:17]:
        a.append(int(element))
    for idx in range(len(a)):
        sum += a[idx]*w[idx]
    index = sum % 11
    if citizen[17] == check[index]:
        print('this is right citizen id')
        return 1
    else:
        print('the last check-num is not correct')
        return 0
def check_password(password):
    if type(password) == str:
        pass
    else:
        return 0
    upper = 0
    lower = 0
    digit = 0
    if len(password) >= 6 and len(password) <= 18:
        pass
    else:
        print('lenth of password is incorrect')
        return 0
    for element in password:
        if element.isalpha():
            if element.isupper():
                upper = 1
            else:
                lower = 1
        elif element.isdigit():
            digit = 1
        else:
            print('there is anoter character in password')
            return 0
    if upper == 1 and lower == 1 and digit ==1:
        print('this is right password')
        return 1
    else:
        print('there is lack of upper or lower or number in password')
        return 0
def check_phonenumber(phone_number):

    if type(phone_number) == int and phone_number >= 0:
        pass
    else:
        print('this is minus or float')
        return 0
    if len(str(phone_number)) == 11:
        print('this is right phone number')
        return 1
    else:
        print('this is wrong phone number')
        return 0


def check_nickname(nickname):
    if type(nickname) == str:
        pass
    else:
        return 0
    if len(nickname) >= 2 and len(nickname) <= 8:
        print('nickname length is correct')
        return 1
    else:
        print('length of nickname is not correct')
        return 0

def check_id(Id):
    if type(Id) == str:
        pass
    else:
        return 0
    if len(Id) >= 6 and len(Id) <= 10:
        print('length of id is correct')
        return 1
    else:
        print('length of id is incorrect')
        return 0

def check_email(email_address):
    if type(email_address) == str:
        pass
    else:
        return 0
    # check '@'
    at_count = 0
    dot_count = 0
    dot1 = 0
    dot2 = 0
    dot = []
    e_len = len(email_address)
    find_at = email_address.find('@')
    find_last_dot = email_address.rfind('.')
    front_ok = 0
    back_ok = 0
    #전체적으로 들어갈수있는지 필터
    for element in email_address:
        if element == '@':
            at_count = at_count + 1
        if element.isalpha() or element.isdigit() or element == '@' or element == '.' or element == '_':
            pass
        else:
            print('there is another character ')
            return 0
    if at_count != 1:
        print('there is more than one @')
        return 0
    if find_at > 63 or e_len-find_at-1>63:
        print('length is over 63')
        return 0


    #앞엔은 숫자랑 영어만
    for element in email_address[0:find_at]:
        if element == '.' or element == '_':
            print('there is a . or _ in front of email')
            return 0
    if find_at == 0:
        print('@가 처음에 나와용')
        return 0
    if email_address[find_at+1] == '.':
        print('@와 . 사이에 뭐가 있어야지')
        return 0

    #뒤에는 . 이있어야해해
    for element in email_address[find_at+1:e_len]:
        if element == '.':
            dot_count = dot_count + 1
    if dot_count < 1:
        print('there is no .')
        return 0


    for idx in range(e_len-1):
        if email_address[idx] == '_':
            if email_address[idx-1] == '.' or email_address[idx+1] == '.':
                print('there is a _ front and back of .')
                return 0

    for a in re.finditer('\.',email_address):
        dot.append(a.start())

    print(dot)
    for idx in range(len(dot)-1):
        if dot[idx+1] - dot[idx] > 1:
            pass
        else:
            print('사이사이에 뭐가 있어야지')
            return 0
    if email_address[e_len-1] == '_' or email_address[find_at+1] == '_':
        print('there is _ the front and back')
        return 0


    if email_address[find_last_dot+1:e_len].isdigit() or email_address[find_last_dot+1:e_len]=='':
        print('last email part is pure number')
        return 0

    if e_len-find_at-1-dot_count < dot_count:
        print('뒤쪽이 틀려')
        return 0

    print('this is right email')
    return 1

check_email('wujun97@a.123')