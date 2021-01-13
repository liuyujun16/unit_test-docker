import unittest
from .reply import reply_post_params_check
#content 长度短
content1 = {'content':'0','replyId':''}
#content 长度长
content2 = {'content':'01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891234567','replyId':0}
#content 类型不符
content3 = {'content':0,'replyId':1}


#replyId 为负数
replyId1 = {'content':'0123456789123456','replyId':-1}
#replyId 为小数
replyId2 = {'content':'0123456789123456','replyId':1.1}
#replyId 为类型不符
replyId3 = {'content':'0123456789123456','replyId':''}

#全空
void1 = {}
#只有content
void2 = {'content':'0123456789123456'}
#只有replyId
void3 = {'replyId':0}

#全是正确
ok = {'content':'0123456789123456','replyId':1}


class ReplyCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reply_post_params_check(content1), ("content", False))
        self.assertEqual(reply_post_params_check(content2), ("content", False))
        self.assertEqual(reply_post_params_check(content3), ("content", False))


        self.assertEqual(reply_post_params_check(replyId1), ("replyId", False))
        self.assertEqual(reply_post_params_check(replyId2), ("replyId", False))
        self.assertEqual(reply_post_params_check(replyId3), ("replyId", False))

        self.assertEqual(reply_post_params_check(None), ("content", False))
        self.assertEqual(reply_post_params_check(void1), ("content", False))
        self.assertEqual(reply_post_params_check(void2), ("ok", True))
        self.assertEqual(reply_post_params_check(void3), ("content", False))


        self.assertEqual(reply_post_params_check(ok), ("ok", True))



if __name__ == '__main__':
    unittest.main()
