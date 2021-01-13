# -*- coding: utf-8 -*-

def post_params_check(content):

    try:
        title_result = check_title(content.get('title'))
        if title_result == 1:
            pass
        else:
            return "title", False
    except:
        return "title", False
    content_result = check_content(content.get('content'))
    if content_result == 1:
        pass
    else:
        return "content",False

    return "ok", True


def check_title(title):
    if type(title) == str:
        pass
    else:
        return 0
    if len(title) >= 1 and len(title) <= 64:
        print('title length is correct')
        return 1
    else:
        print('title length is not correct')
        return 0


def check_content(content):
    if type(content) == str:
        pass
    else:
        return 0
    if len(content) >= 15 and len(content) <= 256:
        print('content length is correct')
        return 1
    else:
        print('content length is not correct')
        return 0


