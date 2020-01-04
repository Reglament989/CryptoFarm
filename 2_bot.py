import requests, os, re, json, hashlib, time, webbrowser, sys, urllib.request, random
import logging as log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telethon import sync, events
from virus_total_apis import PublicApi as VirusTotalPublicApi
from telethon import TelegramClient
from datetime import datetime
from config import client_2, file2_txt, file2_balance, file2_log
    
log.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
    filename= file2_log,
    level=log.INFO)

class RunChromeTests():

    __cicles = 0
    
    __sorry = 0

    __counter = 0

    def time(self, object):
        if object == 'standart':
            return random.randint(2,6)
        elif object == 'normal':
            return random.randint(450,900)
        elif object == 'medium':
            return random.randint(120,280)

    def testMethod(self,waitin,url_rec):
        caps = {'browserName': 'chrome'}
        driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub',
            desired_capabilities=caps)
        driver.maximize_window()
        driver.get(url_rec)
        time.sleep(waitin + 10)
        driver.close()
        driver.quit()

    def pluscounter(self, object=None, int=0):
        if object == 'counter':
            self.__class__.__counter += int
        elif object == 'cicles':
            self.__class__.__cicles += int
        elif object == 'sorry':
            self.__class__.__sorry += int
        else:
            self.__class__.__counter = 0
            self.__class__.__sorry = 0

    def checker(self, object):
        if object == 'counter':
            return self.__class__.__counter
        elif object == 'cicles':
            return str(self.__class__.__cicles)
        elif object == 'sorry':
            return self.__class__.__sorry
        else:
            pass

    def balance(self,  client, tegmo, console=False):
        client.send_message('LTC Click Bot', "/balance")
        time.sleep(RunChromeTests().time('standart'))
        balance = client.get_messages(tegmo, limit=1)[-1].message
        bwrite = str(balance) +" "+ str(datetime.today().strftime("Date:%y/%m/%d Time: %H:%M"))
        with open(filemom_balance, 'w') as f:
            f.write(bwrite + " + " + str(RunChromeTests().checker('cicles')))
        if console != False:
            print(bwrite)
        else:
            log.warning(bwrite)
            time.sleep(RunChromeTests().time('normal'))
            pass
        RunChromeTests().pluscounter() # RESET sorry/counter
        time.sleep(RunChromeTests().time('standart'))
        client.send_message('LTC Click Bot', "/menu")
        time.sleep(1)
        # client.send_message('LTC Click Bot', "/visit")
        # sys.exit()
        

def main(client, console=False):

    client.start()

    dlgs = client.get_dialogs()

    for dlg in dlgs:
        if dlg.title == 'LTC Click Bot':
            tegmo = dlg

    RunChromeTests().balance(client, tegmo, True)

    while True:
        msgs = client.get_messages(tegmo, limit=1)
        cr = RunChromeTests().pluscounter(object='counter', int=1)
        if RunChromeTests().checker('counter') > random.randint(15,28):
            RunChromeTests().balance(client, tegmo)
            continue

        for mes in msgs:
            if re.search(r'\bseconds to get your reward\b', mes.message):
                log.warning("Найдено reward")
                str_a = str(mes.message)
                zz = str_a.replace('You must stay on the site for', '')
                qq = zz.replace('seconds to get your reward.', '')
                waitin = int(qq)
                log.warning("Ждать придется: " + str(waitin))
                client.send_message('LTC Click Bot', "/visit")
                time.sleep(RunChromeTests().time('standart'))
                msgs2 = client.get_messages(tegmo, limit=1)
                for mes2 in msgs2:
                    button_data = mes2.reply_markup.rows[1].buttons[1].data
                    message_id = mes2.id

                    log.warning("Перехожу по ссылке")
                    
                    try:
                        url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                    except:
                        # client.send_message('LTC Click Bot', "/menu")
                        # time.sleep(2)
                        client.send_message('LTC Click Bot', "/visit")
                        time.sleep(RunChromeTests().time('standart'))
                        continue
                    try:
                        url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                        ch = RunChromeTests()
                        ch.testMethod()
                        time.sleep(RunChromeTests().time('standart'))
                        fp = urllib.request.urlopen(url_rec)
                        mybytes = fp.read()
                        mystr = mybytes.decode("utf8")
                        fp.close()
                    except:
                        mystr = ""
                    if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
                        from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                        resp = client(GetBotCallbackAnswerRequest(
                            'LTC Click Bot',
                            message_id,
                            data=button_data
                        ))
                        time.sleep(RunChromeTests().time('standart'))
                        log.error("КАПЧА!")
                        #os.system("pkill chromium")
                    else:
                        log.warning("Переход успешный!")
                        time.sleep(waitin)
                        #os.system("pkill chromium")
                        time.sleep(RunChromeTests().time('standart'))

            elif re.search(r'\bSorry\b', mes.message):
                client.send_message('LTC Click Bot', "/visit")
                log.error("Найдено Sorry")
                time.sleep(RunChromeTests().time('medium'))
                if RunChromeTests().checker('sorry') > 10:
                    RunChromeTests().balance(client, tegmo)
                    while_n = True
                    while while_n:
                        time.sleep(RunChromeTests().time('normal'))
                        check = client.get_messages(tegmo, limit=1)[-1].message
                        if re.search(r'\ba new site for you\b', check):
                            while_n = False
                        else:
                            pass     
                RunChromeTests().pluscounter(object='sorry', int=1)

            else:
                messages = client.get_messages('Litecoin_click_bot')
                try:
                    url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                except:
                    # client.send_message('LTC Click Bot', "/menu")
                    # time.sleep(2)
                    client.send_message('LTC Click Bot', "/visit")
                    time.sleep(RunChromeTests().time('standart'))
                    continue
                f = open("per10.txt")
                fd = f.read()
                if fd == url_rec:
                    log.warning("Найдено повторение переменной")
                    msgs2 = client.get_messages(tegmo, limit=1)
                    for mes2 in msgs2:
                        button_data = mes2.reply_markup.rows[1].buttons[1].data
                        message_id = mes2.id
                        from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                        resp = client(GetBotCallbackAnswerRequest(
                            tegmo,
                            message_id,
                            data=button_data
                        ))
                        time.sleep(random.randint(16,60))
                else:
                    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
                    params = {
                        'apikey': 'virus-total-api-key(past your)', 'url': url_rec}
                    response = requests.post(url, data=params)
                    my_file = open(filemom_txt, 'w')
                    my_file.write(url_rec)
                    log.warning("Новая запись в файле сдерана")
                    time.sleep(random.randint(16,60))
                    RunChromeTests().pluscounter(object='cicles', int=1)
                    log.warning("Пройдено циклов: " + RunChromeTests().checker('cicles'))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        param_name = sys.argv[1]
        if param_name == '--balance' or param_name == '-b':
            main(client_2, True)
        else:
            print("Invalid arg")
            sys.exit()
    else:
        main(client_2)