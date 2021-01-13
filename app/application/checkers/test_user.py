import unittest
from .user import register_params_check
#username 长度短
username1 = {'username': '', 'password': '', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#username 长度长
username2= {'username': '01234567891', 'password': '', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#username 类型不符
username3= {'username': 0, 'password': '', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}


#password 长度短
password1 = {'username': '012345', 'password': '012aA', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 长度长
password2 = {'username': '012345', 'password': '01234567891234567aA', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 缺小 小写字母，大写字母
password3 = {'username': '012345', 'password': '0123456789123456', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 缺小 大写字母
password4 = {'username': '012345', 'password': '012345678912345a', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 缺小 小写字母
password5 = {'username': '012345', 'password': '012345678912345A', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 包含其他字符
password6 = {'username': '012345', 'password': '0123456789123@aA', 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}
#password 类型不符
password7 = {'username': '012345', 'password': 0, 'nickname': '', 'document_number': '', 'mobile': '', 'email': ''}


#nickname 长度短
nickname1 = {'username': '012345', 'password': '01234567891234Aa', 'nickname': '0', 'document_number': '', 'mobile': '', 'email': ''}
#nickname 长度长
nickname2 = {'username': '012345', 'password': '01234567891234Aa', 'nickname': '012345678', 'document_number': '', 'mobile': '', 'email': ''}
#nickname 类型不符
nickname3 = {'username': '012345', 'password': '01234567891234Aa', 'nickname': 0, 'document_number': '', 'mobile': '', 'email': ''}


#document_number 长度短
document_number1 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '01234567890123456', 'mobile': '', 'email': ''}
#document_number 长度长
document_number2 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '0123456789012345679', 'mobile': '', 'email': ''}
#document_number 包含其他字符
document_number3 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '@12345678901234567', 'mobile': '', 'email': ''}
#document_number 日期不存在（12/32）
document_number4 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '000000194912320000', 'mobile': '', 'email': ''}
#document_number 日期不存在（1900/02/29）
document_number5 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '00000019002290000', 'mobile': '', 'email': ''}
#document_number 校验码不对
document_number6 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '110105194912310024', 'mobile': '', 'email': ''}
#document_number 类型不符
document_number7 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': 0, 'mobile': '', 'email': ''}

#mobile 是负数
mobile1 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': -13167352115, 'email': ''}
#mobile 是小数
mobile2 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115.1, 'email': ''}
#mobile 长度长
mobile3 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 131673521151, 'email': ''}
#mobile 长度短
mobile4 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 1316735211, 'email': ''}
#mobile 类型不符
mobile5 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': '', 'email': ''}



#email 没有@
email1 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'wujun'}
#email 有多个@
email2 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'wujun@@'}
#email 最前面有@
email3 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': '@wujun'}
#email 域内部分有其他字符
email4 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'wujun!@'}
#email 域内部分超过63位
email5 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': '01234567890123456789012345678901234567890123456789012345678901234@'}
#email 域名部分超过63位
email6 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': '0@01234567890123456789012345678901234567890123456789012345678901234'}
#email 连字符作为首字符
email7 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@_a'}
#email 连字符作为尾字符
email8 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@a_.'}
#email 顶级域名纯数字
email9 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@a.123'}
#email @后面就有.
email10 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@..'}
#email .和.之间什么都没有
email11 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@.com'}
#email 顶级域名没有
email12 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@a.'}
#email 类型不符
email13 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 0}


#全空
void1 = {}
#只有 username
void2 = {'username': '012345'}
#只有 username password
void3 = {'username': '012345','password': '01234Aa'}
#只有 username password nickname
void4 = {'username': '012345','password': '01234Aa','nickname': '01'}
#只有 username password nickname document_number
void5 = {'username': '012345','password': '01234Aa','nickname': '01','document_number': '11010519491231002X'}
#只有 username password nickname document_number mobile
void6 = {'username': '012345','password': '01234Aa','nickname': '01','document_number': '11010519491231002X','mobile': 13167352115}

#全是正确
ok = {'username': '012345','password': '01234Aa','nickname': '01','document_number': '11010519491231002X','mobile': 13167352115,'email':'wujun97@naver.com'}



#이건 두고 보자
#content27 = {'username': '012345', 'password': '01234Aa', 'nickname': '01', 'document_number': '11010519491231002X', 'mobile': 13167352115, 'email': 'a@..'}
class UserCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(register_params_check(username1), ("username", False))
        self.assertEqual(register_params_check(username2), ("username", False))
        self.assertEqual(register_params_check(username3), ("username", False))


        self.assertEqual(register_params_check(password1), ("password", False))
        self.assertEqual(register_params_check(password2), ("password", False))
        self.assertEqual(register_params_check(password3), ("password", False))
        self.assertEqual(register_params_check(password4), ("password", False))
        self.assertEqual(register_params_check(password5), ("password", False))
        self.assertEqual(register_params_check(password6), ("password", False))
        self.assertEqual(register_params_check(password7), ("password", False))


        self.assertEqual(register_params_check(nickname1), ("nickname", False))
        self.assertEqual(register_params_check(nickname2), ("nickname", False))
        self.assertEqual(register_params_check(nickname3), ("nickname", False))


        self.assertEqual(register_params_check(document_number1), ("document_number", False))
        self.assertEqual(register_params_check(document_number2), ("document_number", False))
        self.assertEqual(register_params_check(document_number3), ("document_number", False))
        self.assertEqual(register_params_check(document_number4), ("document_number", False))
        self.assertEqual(register_params_check(document_number5), ("document_number", False))
        self.assertEqual(register_params_check(document_number6), ("document_number", False))
        self.assertEqual(register_params_check(document_number7), ("document_number", False))


        self.assertEqual(register_params_check(mobile1), ("mobile", False))
        self.assertEqual(register_params_check(mobile2), ("mobile", False))
        self.assertEqual(register_params_check(mobile3), ("mobile", False))
        self.assertEqual(register_params_check(mobile4), ("mobile", False))
        self.assertEqual(register_params_check(mobile5), ("mobile", False))


        self.assertEqual(register_params_check(email1), ("email", False))
        self.assertEqual(register_params_check(email2), ("email", False))
        self.assertEqual(register_params_check(email3), ("email", False))
        self.assertEqual(register_params_check(email4), ("email", False))
        self.assertEqual(register_params_check(email5), ("email", False))
        self.assertEqual(register_params_check(email6), ("email", False))
        self.assertEqual(register_params_check(email7), ("email", False))
        self.assertEqual(register_params_check(email8), ("email", False))
        self.assertEqual(register_params_check(email9), ("email", False))
        self.assertEqual(register_params_check(email10), ("email", False))
        self.assertEqual(register_params_check(email11), ("email", False))
        self.assertEqual(register_params_check(email12), ("email", False))
        self.assertEqual(register_params_check(email13), ("email", False))


        self.assertEqual(register_params_check(None), ("username", False))
        self.assertEqual(register_params_check(void1), ("username", False))
        self.assertEqual(register_params_check(void2), ("password", False))
        self.assertEqual(register_params_check(void3), ("nickname", False))
        self.assertEqual(register_params_check(void4), ("document_number", False))
        self.assertEqual(register_params_check(void5), ("mobile", False))
        self.assertEqual(register_params_check(void6), ("email", False))


        self.assertEqual(register_params_check(ok), ("ok", True))





if __name__ == '__main__':
    unittest.main()
