from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter.messagebox
import tkinter
import tkinter as tK
from dotenv import load_dotenv
import time
import os

#Xpath获取(此部分为AI生成)
GET_XPATH_SCRIPT = """
function getXPath(element) {
    if (element.id !== '') return '//*[@id=\"'+element.id+'\"]';
    if (element === document.body) return '/html/body';

    let ix = 0;
    const siblings = element.parentNode.childNodes;

    for (let i = 0; i < siblings.length; i++) {
        const sibling = siblings[i];
        if (sibling === element) 
            return getXPath(element.parentNode) + '/' + element.tagName + '[' + (ix+1) + ']';
        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) 
            ix++;
    }
}
return getXPath(arguments[0]);
"""
#密码获取
def password():
    try:
        window_main.destroy()
    except:
        pass
    window_code = tK.Tk()
    window_code.title('验证码输入')
    window_code.geometry('300x85')
    #实时回显
    def display(*args):
        text = Input.get()
        result.configure(text=f'输入的验证码：{text}')
    #获取输入的密码
    def input():
        global PWD
        PWD = Input.get()
        window_code.destroy()
    Input = tK.StringVar()
    Input.trace('w',display)
    label_1 = tK.Label(window_code, text='请在下方输入验证码',bg='red',width=20,height=1)
    label_1.pack()
    #输入框
    entry = tK.Entry(window_code,width=50,textvariable=Input,show="*")
    entry.pack()
    #密码显示
    result = tK.Label(window_code,bg='red',width=100,height=1)
    result.pack()
    button = tK.Button(window_code,text='完成',command=input)
    button.pack()
    window_code.mainloop()

def start():
    # 创建 Edge WebDriver 实例
    global browser
    browser = webdriver.Edge()
    browser.get('https://pass.hust.edu.cn/cas/login?service=https%3A%2F%2Fpecg.hust.edu.cn%2Fcggl%2Findex1')
    while True:
        # 加载文件
        load_dotenv('配置文件.env')
        # 智慧华中大登录browser.find_element(By.XPATH, '//*[@id="pd"]')
        input_name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="un"]')))
        input_name.send_keys(os.getenv('account'))
        input_password = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="pd"]')))
        input_password.send_keys(os.getenv('password'))
        password()
        input_code = browser.find_element(By.XPATH, '//*[@id="code"]')
        input_code.send_keys(PWD)
        enter_HUST = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="index_login_btn"]')))
        enter_HUST.click()
        try:
            time.sleep(1)
            end = browser.find_element(By.ID,'errormsg')
            print(end.text)
            if end.text == '验证码错误':
                tkinter.messagebox.showerror('输入验证码错误','请输入正确的验证码，不要输错太多，会被封')
            else:
                break
        except:
            break
    # 更换回体育馆界面
    current_windows = browser.window_handles
    browser.switch_to.window(current_windows[-1])
    nameChoice()
#体育馆选项
def nameChoice():
    window_3 = tK.Tk()
    window_3.geometry('300x300')
    def enter():
        name = lb.get(lb.curselection())
        window_3.destroy()
        stadiumChoice(name)
    var = tkinter.StringVar()
    var.set(('光谷体育馆羽毛球场','光谷体育馆乒乓球场2','东区操场韵苑网球场2小时场','东区操场匹克球场','东区操场韵苑网球场1小时场',
             '中心区操场沁苑网球场2小时场','中心区操场沙地网球场2小时场','中心区操场沙地网球场1小时场','中心区操场沁苑网球场1小时场',
             '西区操场西边网球场2小时场','西区操场西边网球场1小时场','西边羽毛球馆','西边体育馆乒乓球2','游泳馆游泳池','游泳馆羽毛球场'))
    button = tK.Button(window_3,text='确定',command=enter)
    button.pack()
    # 列表
    lb = tK.Listbox(window_3, width=100, height=5, listvariable=var)
    lb.pack(side='left', fill='y')

#体育馆选择
def stadiumChoice(name):
    #各体育馆的Xpath
    stadium_1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[1]/div[1]/div[2]/span/a')#光谷体育馆羽毛球场
    stadium_2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/div[1]/div[2]/span/a')#光谷体育馆乒乓球场2
    stadium_3 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[3]/div[1]/div/span/a')#东区操场韵苑网球场2小时场
    stadium_4 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[4]/div[1]/div/span/a')#东区操场匹克球场
    stadium_5 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[5]/div[1]/div/span/a')#东区操场韵苑网球场1小时场
    stadium_6 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[6]/div[1]/div[2]/span/a')#中心区操场沁苑网球场2小时场
    stadium_7 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[7]/div[1]/div[2]/span/a')#中心区操场沙地网球场2小时场
    stadium_8 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[8]/div[1]/div[2]/span/a')#中心区操场沙地网球场1小时场
    stadium_9 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[9]/div[1]/div[2]/span/a')#中心区操场沁苑网球场1小时场
    stadium_10 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[10]/div[1]/div/span/a')#西区操场西边网球场2小时场
    stadium_11 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[11]/div[1]/div/span/a')#西区操场西边网球场1小时场
    stadium_12 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[12]/div[1]/div[2]/span/a')#西边羽毛球馆
    stadium_13 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[13]/div[1]/div[2]/span/a')#西边体育馆乒乓球2
    stadium_14 = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[14]/div[1]/div[3]/span/a')#游泳馆游泳池
    stadium_15 =browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[15]/div[1]/div[3]/span/a')#游泳馆羽毛球场
    match name:
        case '光谷体育馆羽毛球场':
            stadium_1.click()
            T2()
        case '光谷体育馆乒乓球场2':
            stadium_2.click()
            T1()
        case '东区操场韵苑网球场2小时场':
            stadium_3.click()
            T4()
        case '东区操场匹克球场':
            stadium_4.click()
            T1()
        case '东区操场韵苑网球场1小时场':
            stadium_5.click()
            T1()
        case '中心区操场沁苑网球场2小时场':
            stadium_6.click()
            T4()
        case '中心区操场沙地网球场2小时场':
            stadium_7.click()
            T4()
        case '中心区操场沙地网球场1小时场':
            stadium_8.click()
            T1()
        case '中心区操场沁苑网球场1小时场':
            stadium_9.click()
            T1()
        case '西区操场西边网球场2小时场':
            stadium_10.click()
            T4()
        case '西区操场西边网球场1小时场':
            stadium_11.click()
            T1()
        case '西边羽毛球馆':
            stadium_12.click()
            T2()
        case '西边体育馆乒乓球2':
            stadium_13.click()
            T1()
        case '游泳馆游泳池':#12
            stadium_14.click()
            T3()
        case '游泳馆羽毛球场':
            stadium_15.click()
            T2()

#时间选择
def T1():#东区操场韵苑网球场1小时场,中心区操场沁苑网球场1小时场,中心区操场沙地网球场1小时场,西区操场西边网球场1小时场
    daychoice()
    time_slots = (
        '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00',
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',
        '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00',
        '20:00-21:00','21:00-22:00')
    # 字典映射(时间段转时间)1小时
    Ti = {slot: idx + 8 for idx, slot in enumerate(time_slots)}
    # 开始时间屏幕创建
    window_5 = tK.Tk()
    window_5.title('开始时间')
    window_5.geometry('300x300')
    var = tkinter.StringVar()
    var.set(('08:00-09:00', '09:00-10:00', '10:00-11:00','11:00-12:00','12:00-13:00','13:00-14:00','14:00-15:00',
             '15:00-16:00','16:00-17:00','17:00-18:00','18:00-19:00','19:00-20:00','20:00-21:00','21:00-22:00'))

    def StartTime():
        # 获取时间段
        start_slot = lb.get(lb.curselection()[0])
        time_start = str(Ti[start_slot])
        window_5.destroy()
        # 结束时间屏幕创建
        window_6 = tK.Tk()
        window_6.title('结束时间')
        window_6.geometry('300x300')
        def EndTime():
            end_slot = l.get(l.curselection()[0])
            time_end = str(Ti[end_slot])
            window_6.destroy()
            # 分情况讨论
            if time_start == '8' and time_end == '9':
                timechoice('08:00:00')
                timechoice('09:00:00')
            elif time_start == '8' and int(time_end) >= 9:
                timechoice('08:00:00')
                timechoice('09:00:00')
                i = 10
                while int(i) <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
            elif time_start == '9':
                timechoice('09:00:00')
                i = 10
                while int(i) <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
            else:
                i = int(time_start)
                while i <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i+= 1
        # 列表
        l = tK.Listbox(window_6, width=100, height=50)
        l = tK.Listbox(window_6, width=100, height=50)
        for slot in time_slots:
            l.insert(tK.END, slot)
        button_end = tK.Button(window_6, text='结束时间确定', command=EndTime,width=20,height=2)
        button_end.pack(side='bottom')
        l.pack(side='left',fill='y')
        window_6.mainloop()
    # 列表
    lb = tK.Listbox(window_5, width=100, height=50, listvariable=var)
    button_start = tK.Button(window_5, text='开始时间确定',command=StartTime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_5.mainloop()

def T2():#羽毛球
    daychoice()
    time_slots = (
        '08:00-10:00','10:00-12:00','12:00-14:00',
        '14:00-16:00','16:00-18:00','18:00-20:00',
        '20:00-22:00')
    #字典映射(时间段转时间)2小时
    Ti = {slot: (2*idx + 8) for idx, slot in enumerate(time_slots)}
    # 开始时间屏幕创建
    window_5 = tK.Tk()
    window_5.title('开始时间')
    window_5.geometry('300x300')
    # 开始时间屏幕列表创建
    var = tkinter.StringVar()
    var.set(('08:00-10:00','10:00-12:00','12:00-14:00','14:00-16:00',
             '16:00-18:00','18:00-20:00','20:00-22:00'))

    def StartTime():
        # 获取时间段
        start_slot = lb.get(lb.curselection()[0])
        time_start = str(Ti[start_slot])
        window_5.destroy()
        # 结束时间屏幕创建
        window_6 = tK.Tk()
        window_6.title('结束时间')
        window_6.geometry('300x300')
        def EndTime():
            end_slot = l.get(l.curselection()[0])
            time_end = str(Ti[end_slot])
            window_6.destroy()
            # 分情况讨论
            if time_start == '8' and int(time_end) ==8:
                timechoice('08:00:00')
            elif time_start == '8' and int(time_end) >= 8:
                timechoice('08:00:00')
                i = 10
                while int(i) <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 2
            else:
                i = int(time_start)
                while i <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i+= 2
        # 列表
        l = tK.Listbox(window_6, width=100, height=50)
        l = tK.Listbox(window_6, width=100, height=50)
        for slot in time_slots:
            l.insert(tK.END, slot)
        button_end = tK.Button(window_6, text='结束时间确定', command=EndTime,width=20,height=2)
        button_end.pack(side='bottom')
        l.pack(side='left',fill='y')
        window_6.mainloop()
    # 列表
    lb = tK.Listbox(window_5, width=100, height=50, listvariable=var)
    button_start = tK.Button(window_5, text='开始时间确定',command=StartTime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_5.mainloop()

def T3():#游泳馆
    daychoice()
    time_slots = (
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',
        '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00',
        '20:00-21:00')
    # 字典映射(时间段转时间)1小时
    Ti = {slot: idx + 8 for idx, slot in enumerate(time_slots)}
    # 开始时间屏幕创建
    window_5 = tK.Tk()
    window_5.title('开始时间')
    window_5.geometry('300x300')
    # 开始时间屏幕列表创建
    var = tkinter.StringVar()
    var.set(('12:00-13:00','13:00-14:00','14:00-15:00','15:00-16:00',
             '16:00-17:00','17:00-18:00','18:00-19:00','19:00-20:00','20:00-21:00'))

    def StartTime():
        # 获取时间段
        start_slot = lb.get(lb.curselection()[0])
        time_start = str(Ti[start_slot])
        window_5.destroy()
        # 结束时间屏幕创建
        window_6 = tK.Tk()
        window_6.title('结束时间')
        window_6.geometry('300x300')
        def EndTime():
            end_slot = l.get(l.curselection()[0])
            time_end = str(Ti[end_slot])
            window_6.destroy()
            # 分情况讨论
            if time_start == '8' and time_end == '9':
                timechoice('08:00:00')
                timechoice('09:00:00')
            elif time_start == '8' and int(time_end) >= 9:
                timechoice('08:00:00')
                timechoice('09:00:00')
                i = 10
                while int(i) <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
            elif time_start == '9':
                timechoice('09:00:00')
                i = 10
                while int(i) <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
            else:
                i = int(time_start)
                while i <= int(time_end):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i+= 1
        # 列表
        l = tK.Listbox(window_6, width=100, height=50)
        l = tK.Listbox(window_6, width=100, height=50)
        for slot in time_slots:
            l.insert(tK.END, slot)
        button_end = tK.Button(window_6, text='结束时间确定', command=EndTime,width=20,height=2)
        button_end.pack(side='bottom')
        l.pack(side='left',fill='y')
        window_6.mainloop()
    # 列表
    lb = tK.Listbox(window_5, width=100, height=50, listvariable=var)
    button_start = tK.Button(window_5, text='开始时间确定',command=StartTime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_5.mainloop()

def T4():
    daychoice()
    #总元组
    time_slots = ('08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00','12:00-13:00', '13:00-14:00',
                  '14:00-15:00', '15:00-16:00','16:00-18:00', '18:00-20:00','20:00-22:00')
    # 字典映射(时间段转时间)1小时
    time_slots_1 = (
        '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00',
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',)
    Ti_1 = {slot_1: idx_1 + 8 for idx_1, slot_1 in enumerate(time_slots_1)}
    # 字典映射(时间段转时间)2小时
    time_slots_2 = ('16:00-18:00', '18:00-20:00','20:00-22:00')
    Ti_2 ={slot_2: 2*idx_2 + 16 for idx_2, slot_2 in enumerate(time_slots_2)}
    # 开始时间屏幕创建
    window_5 = tK.Tk()
    window_5.title('开始时间')
    window_5.geometry('300x300')
    # 开始时间屏幕列表创建
    var = tkinter.StringVar()
    var.set(time_slots)
    def StartTime():
        # 获取时间段
        start_slot = lb.get(lb.curselection()[0])
        if start_slot in time_slots_1:
            time_start = str(Ti_1[start_slot])
        else:
            time_start = str(Ti_2[start_slot])
        # 结束时间屏幕创建
        window_5.destroy()
        window_6 = tK.Tk()
        window_6.title('结束时间')
        window_6.geometry('300x300')

        def EndTime():
            end_slot = l.get(l.curselection()[0])
            #选择相应的映射字典
            if end_slot in time_slots_1:
                time_end = str(Ti_1[end_slot])
            else:
                time_end = str(Ti_2[end_slot])
            window_6.destroy()
            # 分情况讨论
            if time_start == '8' and time_end == '9':
                timechoice('08:00:00')
                timechoice('09:00:00')

            elif time_start == '8' and int(time_end) >= 9:
                timechoice('08:00:00')
                timechoice('09:00:00')
                i = 10
                while int(i) <= min(int(time_end), 16):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
                if int(time_end) >= 16:
                    i = 16
                    while i <= int(time_end):
                        InputTime = str(i) + ':00:00'
                        timechoice(InputTime)
                        i += 2

            elif time_start == '9':
                timechoice('09:00:00')
                i = 10
                while int(i) <= min(int(time_end), 16):
                    InputTime = str(i) + ':00:00'
                    timechoice(InputTime)
                    i += 1
                if int(time_end) >= 16:
                    i = 16
                    while i <= int(time_end):
                        InputTime = str(i) + ':00:00'
                        timechoice(InputTime)
                        i += 2

            else:
                i = int(time_start)
                if i <= 15 and int(time_end) <= 15:
                    while i <= int(time_end):
                        InputTime = str(i) + ':00:00'
                        timechoice(InputTime)
                        i += 1
                elif int(time_end) <=15 and int(time_start) >= 16:
                    i = int(time_start)
                    while i <= 16:
                        InputTime = str(i) + ':00:00'
                        timechoice(InputTime)
                        i += 1
                    k =16
                    while k <= int(time_end):
                        InputTime = str(k) + ':00:00'
                        timechoice(InputTime)
                        k += 2
                else:
                    i = int(time_start)
                    while i <= int(time_end):
                        InputTime = str(i) + ':00:00'
                        timechoice(InputTime)
                        i += 2

        # 列表
        l = tK.Listbox(window_6, width=100, height=50)
        for slot in time_slots:
            l.insert(tK.END, slot)
        button_end = tK.Button(window_6, text='结束时间确定', command=EndTime, width=20, height=2)
        button_end.pack(side='bottom')
        l.pack(side='left', fill='y')
        window_6.mainloop()

    # 列表
    lb = tK.Listbox(window_5, width=100, height=50, listvariable=var)
    button_start = tK.Button(window_5, text='开始时间确定', command=StartTime, width=20, height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_5.mainloop()

#更换日期
def daychoice():
    #今天
    def day1():
        pass
        window_day.destroy()
    #明天
    def day2():
        nextDay = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", nextDay)
        window_day.destroy()
    #后天
    def day3():
        nextDay = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", nextDay)
        afterDay = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", afterDay)
        window_day.destroy()
    window_day = tK.Tk()
    window_day.title('日期选择')
    window_day.geometry('300x300')
    button_now = tK.Button(window_day, text='今天',width=10,height=5,command=day1,bg='red',fg='white')
    button_now.pack()
    button_next = tK.Button(window_day, text='明天',width=10,height=5,command=day2,bg='red',fg='white')
    button_next.pack()
    button_after = tK.Button(window_day, text='后天',width=10,height=5,command=day3,bg='red',fg='white')
    button_after.pack()
    window_day.mainloop()

#获取可定的场
EN_list = []
# 更换时间
def timechoice(ti):
    CHOICE = browser.find_element(By.ID, 'starttime')
    select = Select(CHOICE)
    select.select_by_value(ti)
    #查看场地状态
    states = browser.find_elements(By.CLASS_NAME, 'spacezt')
    for idx, Sta in enumerate(states, 1):
        # 获取XPath
        xpath = browser.execute_script(GET_XPATH_SCRIPT, Sta)
        if Sta.text == '可预约':
            EN_list.append((Sta, ti, idx, xpath))
        else:
            EN_list.append((0, ti, idx, xpath))
#订场函数
def scenes(list):
    information_list = []
    #场地状态屏幕创建
    window_state = tK.Tk()
    window_state.title('场地状态')
    window_state.geometry('300x300')
    for item in list:
        if item[0] == 0:
            i=f'在{item[1]}的第{item[2]}场地无法预约'
            information_list.append(i)
        else:
            i = f'在{item[1]}的第{item[2]}场地可预约'
            information_list.append(i)
    def choice():#(Sta,ti,idx,xpath)
        #获取索引
        scene_slot = {slot:idx for idx, slot in enumerate(information_list)}
        scene = l.get(l.curselection()[0])
        locations = int(scene_slot[scene])
        if '无法预约' in scene:
            tK.messagebox.showerror('错误', '请预约可预约的场地')
        else:
            #xpath与time获取
            location = list[locations][3]
            when = list[locations][1]
            CHOICE = browser.find_element(By.ID, 'starttime')
            select = Select(CHOICE)
            select.select_by_value(when)
            entry = browser.find_element(By.XPATH,location)
            browser.execute_script("arguments[0].click();",entry)
            #学生身份选择
            enter_3 = browser.find_element(By.ID,'partnerCardType1')
            browser.execute_script("arguments[0].click();", enter_3)
            judge = tK.messagebox.askyesno('提示','是否确认预定该场地')
            if judge:
                #预约确定
                enter_4 = browser.find_element(By.XPATH,'//*[@id="command"]/div[3]/input[3]')
                browser.execute_script("arguments[0].click();", enter_4)
                tK.messagebox.showinfo('提示','预约成功，请付款')
            else:
                pass
    l = tK.Listbox(window_state, width=100, height=50)
    for j in information_list:
        l.insert(tK.END, j)
    button_end = tK.Button(window_state, text='预约场地确定', command=choice, width=20, height=2)
    button_end.pack(side='bottom')
    l.pack(side='left', fill='y')
    window_state.mainloop()

#程序入口
window_main = tK.Tk()
window_main.title('HUST抢场神器')
window_main.geometry('500x500')
l_1 = tK.Label(window_main,text='这是HUST的订场小程序，请点击下方的按钮开始订场，订场时间为8点到22点',bg='green',fg='white',width=100,height=10)
l_1.pack()
b = tK.Button(window_main,text='开始订场',width=20,height=5,command=start,bg='red')
b.place(x=170,y=250)
l_2 = tK.Label(window_main,text='本程序仅供交流学习使用，切勿用于非法用途',width=100,height=10)
l_2.pack(side='bottom')
window_main.mainloop()
scenes(EN_list)


