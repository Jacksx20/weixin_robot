# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import receive
import time
import os
import requests


class Handle(object):

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "weixin"  #微信公众号后台token值

            list = [token, timestamp, nonce]
            list.sort()
            s = list[0] + list[1] + list[2]
            hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
            print( "handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return echostr
        except (Exception) as Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is:\n", webData)
            #打印消息体日志
            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName

                print('Reply message info:\n')
                print('toUser =', toUser)
                print('fromUser = ', fromUser)

                #判断消息是否为text类型
                if recMsg.MsgType == 'text':
                    print('收到文本消息:' + str(recMsg.Content))
                    content = "欢迎关注！" + str(recMsg.Content)
                    # r=requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+str(recMsg.Content)).text
                    # if str(r.json()['result'])=='0':
                    #     content=r.json()['content']
                    # else:
                    #     content = "欢迎关注！" + str(recMsg.Content)
                    # print('回复消息 = ', content)
                    return self.render.reply_text(toUser, fromUser, int(time.time()), content)
                #判断消息是否为image类型
                if recMsg.MsgType == 'image':
                    print('收到图片消息！')
                    mediaId = recMsg.MediaId
                    print('媒体id:' + mediaId)
                    return self.render.reply_image(toUser, fromUser,int(time.time()),  mediaId)
            else:
                print("不支持的消息类型：",recMsg.MsgType)
                return "success"
        except (Exception) as Argment:
            return Argment
