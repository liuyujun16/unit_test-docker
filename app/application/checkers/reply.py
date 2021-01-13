# -*- coding: utf-8 -*-

def reply_post_params_check(content):
    try:
        reply_content_result = check_reply_content(content.get('content'))
        if reply_content_result == 1:
            pass
        else:
            return "content", False
    except:
        return "content", False


    if content.get('replyId') == None:
        pass
    else:
        replyId_result = check_replyId(content.get('replyId'))
        print(replyId_result)
        if replyId_result == 1:
            pass
        else:
            return "replyId", False


    return "ok", True


def check_reply_content(reply_content):
    if type(reply_content) == str:
        pass
    else:
        return 0
    if len(reply_content) >= 15 and len(reply_content) <= 256:
        print('titles reply correct')
        return 1
    else:
        print('titles reply correct')
        return 0

def check_replyId(replyId):
    if type(replyId) == int:
        pass
    else:
        print('id is not a number')
        return 0
    if replyId < 0:
        print('id is minus')
        return 0
    print('this is right id')
    return 1

