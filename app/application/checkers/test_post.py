import unittest
from .post import post_params_check
#title 长度短
title1 = {'title':'','content':'012345678912345'}
#title 长度长
title2 = {'title':'01234567890123456789012345678901234567890123456789012345678912345','content':'012345678912345'}
#title 类型不符
title3 = {'title':0,'content':'012345678912345'}


#content 长度短
content1 = {'title':'a','content':''}
#content 长度长
content2 = {'title':'a','content':'01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891234567'}
#content 类型不符
content3 = {'title':'a','content':0}


#全空
void1 = {}
#只有title
void2 = {'title':'a'}
#只有content
void3 = {'content':'012345678912345'}


#全是正确
ok = {'title':'a','content':'012345678912345'}


class PostCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(post_params_check(title1),("title",False))
        self.assertEqual(post_params_check(title2),("title",False))
        self.assertEqual(post_params_check(title3),("title",False))


        self.assertEqual(post_params_check(content1),("content",False))
        self.assertEqual(post_params_check(content2),("content",False))
        self.assertEqual(post_params_check(content3),("content",False))


        self.assertEqual(post_params_check(None),("title",False))
        self.assertEqual(post_params_check(void1),("title",False))
        self.assertEqual(post_params_check(void2),("content",False))
        self.assertEqual(post_params_check(void3),("title",False))



        self.assertEqual(post_params_check(ok),("ok",True))


if __name__ == '__main__':
    unittest.main()
