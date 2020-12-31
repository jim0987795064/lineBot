from transitions.extensions import GraphMachine

from utils import send_text_message

import urllib.request as req

#url="https://www.ptt.cc/bbs/movie/index.html"
import bs4
#titles=root.find_all("div",class_="title")

import datetime
import requests
location=0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)    
    #is going to

    def is_going_to_menu(self, event):
        print("start")
        return True


    def is_going_to_viewshow1(self, event):
        text = event.message.text
        if text.lower()=="1":
            print("is_going_to_viewshow1")
            return True
        else:
            return False

    def is_going_to_viewshow2(self, event):
        text = event.message.text
        if text.lower()=="2":
            print("is_going_to_viewshow2")
            return True
        else:
            return False

    def is_going_to_viewshow3(self, event):
        text = event.message.text
        if text.lower()=="3":
            print("is_going_to_viewshow3")
            return True
        else:
            return False

    def is_going_to_viewshow4(self, event):
        text = event.message.text
        if text.lower()=="4":
            print("is_going_to_viewshow4")
            return True
        else:
            return False

        
    def is_going_to_viewshow5(self, event):
        text = event.message.text
        if text.lower()=="5":
            print("is_going_to_viewshow5")
            return True
        else:
            return False

    def is_going_to_viewshow6(self, event):
        text = event.message.text
        if text.lower()=="6":
            print("is_going_to_viewshow6")
            return True
        else:
            return False

    def is_going_to_ptt(self, event):
        text = event.message.text
        if text.lower()=="search":
            print("is_going_to_ptt")
            return True
        else:
            return False


    def is_going_to_book(self, event):
        text = event.message.text
        if text.lower()=="book":
            print("is_going_to_book")
            return True
        else:
            return False
    #on enter 
    def on_enter_menu(self, event):
        print("menu_state")
        reply_token=event.reply_token
        send_text_message(reply_token, "查詢時刻表請輸入影城代號\n\n台北信義威秀影城:1\n台北京站威秀影城:2\n新竹大遠百威秀影城:3\n台南大遠百威秀影城:4\n台南南紡威秀影城:5\n台南FOCUS 威秀影城:6\n\n\n查詢影評請輸入:search")


    def on_enter_viewshow1(self, event):
        print("viewshow1_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=1"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break
        
    def on_enter_viewshow2(self, event):
        print("viewshow2_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=2"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break

    def on_enter_viewshow3(self, event):
        print("viewshow3_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=7"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break


    def on_enter_viewshow4(self, event):
        print("viewshow4_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=15"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break

    def on_enter_viewshow5(self, event):
        print("viewshow5_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=16"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break

    def on_enter_viewshow6(self, event):
        print("viewshow6_state")
        reply_token=event.reply_token
        url="https://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=22"
        request=req.Request(url,headers={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        names=root.find_all("article",class_="hidden article")
        for x in names: 
            send_text_message(reply_token, x.text+"\n\n請輸入book以進入訂票頁面")
            break

    def on_enter_book(self, event):
        print("book_state")
        reply_token=event.reply_token
        send_text_message(reply_token, "以下為訂票頁面，輸入任意鍵以繼續執行\nhttps://www.vscinemas.com.tw/vsweb/") 


    def on_enter_ptt(self, event):
        print("ptt_state")
        reply_token=event.reply_token
        t=""
        url="https://www.ptt.cc/bbs/movie/index.html"
        for i in range(3):
            request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
            with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
            root=bs4.BeautifulSoup(data,"html.parser")
            titles=root.find_all("div",class_="title")

            for title in titles:
                if title.a !=None:
                    for x in title.a.string:
                        if x=="R":
                            break
                        elif x=="雷":
                            t+=title.a.string+"\n"+"https://www.ptt.cc/"+title.a['href']+"\n"
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text,"html.parser")
            u = soup.select("div.btn-group.btn-group-paging a") #a標籤
            url = "https://www.ptt.cc"+ u[1]["href"]
        send_text_message(reply_token,t+"\n\n\n\n\n\n\n請輸入任意鍵以繼續執行")
        #send_text_message(reply_token,"請輸入任意鍵以繼續執行\n ")
"""
    def on_exit_viewshow(self):
        print("leaving viewshow")
        return True
    def on_exit_ptt(self):
        print("leaving ptt")
        return True
    def on_exit_book(self):
        print("leaving book")
        return True"""
