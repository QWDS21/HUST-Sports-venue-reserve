from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter.messagebox
import tkinter
import tkinter as tK
from dotenv import load_dotenv
import os
import time
from apscheduler.schedulers.background import BlockingScheduler

#-----------------------------------------------------------------------------------------------------------------------
#Xpath获取(此部分为AI生成)
GET_XPATH_SCRIPT ="""
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

#-----------------------------------------------------------------------------------------------------------------------
def code():
    try:
        window_main.destroy()
    except:
        pass
    #密码输入弹窗创建
    window_code = tK.Tk()
    window_code.title('验证码输入')
    window_code.geometry('300x85')
    #实时回显
    def display(*args):
        text = pwd_input.get()
        #修改文本
        result.configure(text=f'输入的验证码：{text}')
    #获取输入的密码
    def input():
        #声明全局变量PWD
        global PWD
        PWD = pwd_input.get()
        window_code.destroy()
    pwd_input = tK.StringVar()
    #监控pwd_input变化
    pwd_input.trace('w',display)
    label_1 = tK.Label(window_code, text='请在下方输入验证码',bg='red',width=20,height=1)
    label_1.pack()
    #输入框
    entry = tK.Entry(window_code,width=50,textvariable=pwd_input,show="*")
    entry.pack()
    #密码显示
    result = tK.Label(window_code,bg='red',width=100,height=1)
    result.pack()
    button = tK.Button(window_code,text='完成',command=input)
    button.pack()
    window_code.mainloop()
#程序开始。
def start():
    # 创建 Edge WebDriver 实例
    global browser
    browser = webdriver.Edge()
    browser.get('https://pass.hust.edu.cn/cas/login?service=https%3A%2F%2Fpecg.hust.edu.cn%2Fcggl%2Findex1')
    while True:
        # 加载文件
        load_dotenv('配置文件.env')
        # 智慧华中大登录
        input_name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="un"]')))
        input_name.send_keys(os.getenv('account'))
        input_password = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="pd"]')))
        input_password.send_keys(os.getenv('password'))
        code()
        input_code = browser.find_element(By.XPATH, '//*[@id="code"]')
        input_code.send_keys(PWD)
        #等待“登录”出现，防报错
        enter_HUST = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="index_login_btn"]')))
        enter_HUST.click()
        #防呆设计
        try:
            time.sleep(1)
            end = browser.find_element(By.ID,'errormsg')
            if end.text == '验证码错误':
                tkinter.messagebox.showerror('输入验证码错误','请输入正确的验证码，不要输错太多，会被封')
            else:
                break
        except:
            break

#-----------------------------------------------------------------------------------------------------------------------
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
    stadiumDictionaries = {'光谷体育馆羽毛球场': stadium_1,                  '光谷体育馆乒乓球场2': stadium_2,
                           '东区操场韵苑网球场2小时场': stadium_3,            '东区操场匹克球场': stadium_4,
                           '东区操场韵苑网球场1小时场': stadium_5,            '中心区操场沁苑网球场2小时场': stadium_6,
                           '中心区操场沙地网球场2小时场': stadium_7,           '中心区操场沙地网球场1小时场': stadium_8,
                           '中心区操场沁苑网球场1小时场': stadium_9,           '西区操场西边网球场2小时场': stadium_10,
                           '西区操场西边网球场1小时场': stadium_11,            '西边羽毛球馆': stadium_12,
                           '西边体育馆乒乓球2': stadium_13,                  '游泳馆游泳池': stadium_14,
                           '游泳馆羽毛球场': stadium_15, }
    stadium = stadiumDictionaries[name]
    stadium.click()

def FunctionSelect(name):
    match name:
        case '光谷体育馆羽毛球场':
            temp = T2()
            return temp
        case '光谷体育馆乒乓球场2':
            temp = T1()
            return temp
        case '东区操场韵苑网球场2小时场':
            temp = T4()
            return temp
        case '东区操场匹克球场':
            temp = T1()
            return temp
        case '东区操场韵苑网球场1小时场':
            temp = T1()
            return temp
        case '中心区操场沁苑网球场2小时场':
            temp = T4()
            return temp
        case '中心区操场沙地网球场2小时场':
            temp = T4()
            return temp
        case '中心区操场沙地网球场1小时场':
            temp = T1()
            return temp
        case '中心区操场沁苑网球场1小时场':
            temp = T1()
            return temp
        case '西区操场西边网球场2小时场':
            temp = T4()
            return temp
        case '西区操场西边网球场1小时场':
            temp = T1()
            return temp
        case '西边羽毛球馆':
            temp = T2()
            return temp
        case '西边体育馆乒乓球2':
            temp = T1()
            return temp
        case '游泳馆游泳池':  # 12
            temp = T3()
            return temp
        case '游泳馆羽毛球场':
            temp = T2()
            return temp
#-----------------------------------------------------------------------------------------------------------------------
#时间选择
def T1():#东区操场韵苑网球场1小时场,中心区操场沁苑网球场1小时场,中心区操场沙地网球场1小时场,西区操场西边网球场1小时场
    time_slots = (
        '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00',
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',
        '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00',
        '20:00-21:00','21:00-22:00')
    Ti = {slot: idx + 8 for idx, slot in enumerate(time_slots)}
    ti = None
    def starttime():
        nonlocal ti
        ti = Ti[lb.get(lb.curselection())]
        ti = str(ti) + ':00:00'
        window_start.destroy()
    # 开始时间屏幕创建
    window_start = tK.Tk()
    window_start.title('时间选择')
    window_start.geometry('300x300')
    # 列表
    lb = tK.Listbox(window_start, width=100, height=50)
    for slot in time_slots:
        lb.insert(tK.END, slot)
    button_start = tK.Button(window_start, text='开始时间确定',command=starttime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_start.mainloop()
    return ti

def T2():#羽毛球
    time_slots = (
        '08:00-10:00','10:00-12:00','12:00-14:00',
        '14:00-16:00','16:00-18:00','18:00-20:00',
        '20:00-22:00')
    # 字典映射(时间段转时间)2小时
    Ti = {slot: (2 * idx + 8) for idx, slot in enumerate(time_slots)}
    # 开始时间屏幕创建
    window_start = tK.Tk()
    window_start.title('开始时间')
    window_start.geometry('300x300')
    ti = None
    def StartTime():
        # 获取时间段
        nonlocal ti
        ti = Ti[lb.get(lb.curselection()[0])]
        ti = str(ti) + ':00:00'
        window_start.destroy()
    # 列表
    lb = tK.Listbox(window_start, width=100, height=50)
    for slot in time_slots:
        lb.insert(tK.END, slot)
    button_start = tK.Button(window_start, text='开始时间确定',command=StartTime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_start.mainloop()
    return ti

def T3():#游泳馆
    time_slots = (
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',
        '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00',
        '20:00-21:00')
    # 字典映射(时间段转时间)1小时
    Ti = {slot: idx + 12 for idx, slot in enumerate(time_slots)}
    # 开始时间屏幕创建
    window_start = tK.Tk()
    window_start.title('开始时间')
    window_start.geometry('300x300')
    ti = None
    def StartTime():
        # 获取时间段
        nonlocal ti
        ti = Ti[lb.get(lb.curselection()[0])]
        ti = str(ti) + ':00:00'
        window_start.destroy()
    # 列表
    lb = tK.Listbox(window_start, width=100, height=50)
    for slot in time_slots:
        lb.insert(tK.END, slot)
    button_start = tK.Button(window_start, text='开始时间确定',command=StartTime,width=20,height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_start.mainloop()
    return ti

def T4():#网球2小时场
    #总元组
    time_slots = ('08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00','12:00-13:00', '13:00-14:00',
                  '14:00-15:00', '15:00-16:00','16:00-18:00', '18:00-20:00','20:00-22:00')
    # 字典映射(时间段转时间)1小时
    time_slots_1 = (
        '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00',
        '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00',)
    Ti_1 = {slot_1: idx_1 + 8 for idx_1, slot_1 in enumerate(time_slots_1)}
    # 字典映射(时间段转时间)2小时
    time_slots_2 = ('16:00-18:00', '18:00-20:00', '20:00-22:00')
    Ti_2 = {slot_2: 2 * idx_2 + 16 for idx_2, slot_2 in enumerate(time_slots_2)}
    # 开始时间屏幕创建
    window_start = tK.Tk()
    window_start.title('开始时间')
    window_start.geometry('300x300')
    ti = None
    def StartTime():
        # 获取时间段
        nonlocal ti
        ti = lb.get(lb.curselection()[0])
        if ti in time_slots_1:
            time_start = str(Ti_1[ti])
            ti = str(time_start) + ':00:00'
        else:
            time_start = str(Ti_2[ti])
            ti = str(time_start) + ':00:00'

        window_start.destroy()
    # 列表
    lb = tK.Listbox(window_start, width=100, height=50)
    for slot in time_slots:
        lb.insert(tK.END, slot)
    button_start = tK.Button(window_start, text='开始时间确定', command=StartTime, width=20, height=2)
    button_start.pack(side='bottom')
    lb.pack(side='left', fill='y')
    window_start.mainloop()
    return ti
#-----------------------------------------------------------------------------------------------------------------------

#更换日期
def DayChoice(datetime):
    #今天
    if datetime ==1:
        pass
    #明天
    elif datetime ==2:
        nextDay = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", nextDay)
    #后天
    elif datetime ==3:
        nextDay = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", nextDay)
        afterDay = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
        browser.execute_script("arguments[0].click();", afterDay)
    else:
        print("时间选择出错")

# 更换时间
def timechoice(ti):
    CHOICE = browser.find_element(By.ID, 'starttime')
    select = Select(CHOICE)
    select.select_by_value(ti)

#订场函数
def scenes():
    states = browser.find_elements(By.CLASS_NAME, 'spacezt')
    ff = 0
    for idx, Sta in enumerate(states, 1):
        if Sta.text == '可预约':
            Xpath = browser.execute_script(GET_XPATH_SCRIPT, Sta)
            entry = browser.find_element(By.XPATH, Xpath)
            browser.execute_script("arguments[0].click();",entry)
            ff = 1
            #学生身份选择
            try:
                enter_3 = browser.find_element(By.ID,'partnerCardType1')
                browser.execute_script("arguments[0].click();", enter_3)
            except:
                pass
            #预约确定
            enter_4 = browser.find_element(By.XPATH,'//*[@id="command"]/div[3]/input[3]')
            browser.execute_script("arguments[0].click();", enter_4)
            try:
                decision = browser.find_element(By.XPATH,'//*[@id="dialog_1"]/div[2]/div/div/div[2]/div')
                browser.execute_script("arguments[0].click();", decision)
            except:
                pass
                tK.messagebox.showinfo('提示','预约成功，请付款')
        else:
            pass
    if ff == 0:
        tK.messagebox.showinfo('提示','该时段无场地')
        browser.quit()
        os._exit(0)

#-----------------------------------------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------------------
#体育馆名称输入
def namechoice():
    name = '光谷体育馆羽毛球场'
    def enter():
        nonlocal name
        name = lb.get(lb.curselection())
        window_name.destroy()
    slots = ('光谷体育馆羽毛球场', '光谷体育馆乒乓球场2', '东区操场韵苑网球场2小时场', '东区操场匹克球场',
             '东区操场韵苑网球场1小时场',
             '中心区操场沁苑网球场2小时场', '中心区操场沙地网球场2小时场', '中心区操场沙地网球场1小时场',
             '中心区操场沁苑网球场1小时场',
             '西区操场西边网球场2小时场', '西区操场西边网球场1小时场', '西边羽毛球馆', '西边体育馆乒乓球2',
             '游泳馆游泳池', '游泳馆羽毛球场')
    window_name = tK.Tk()
    window_name.geometry('300x300')
    button = tK.Button(window_name, text='确定', command=enter)
    button.pack()
    # 列表
    lb = tK.Listbox(window_name, width=100, height=5)
    for slot in slots:
        lb.insert(tK.END, slot)
    lb.pack(side='left', fill='y')
    window_name.mainloop()
    return name

#日期输入
def daychoice():
    daytime = 1
    def day1():
        nonlocal daytime
        daytime = 1
        window_day.destroy()
    def day2():
        nonlocal daytime
        daytime = 2
        window_day.destroy()
    def day3():
        nonlocal daytime
        daytime = 3
        window_day.destroy()

    window_day = tK.Tk()
    window_day.title('日期选择')
    window_day.geometry('300x300')
    button_now = tK.Button(window_day, text='今天', width=10, height=5, command=day1, bg='red', fg='white')
    button_now.pack()
    button_next = tK.Button(window_day, text='明天', width=10, height=5, command=day2, bg='red', fg='white')
    button_next.pack()
    button_after = tK.Button(window_day, text='后天', width=10, height=5, command=day3, bg='red', fg='white')
    button_after.pack()
    window_day.mainloop()
    return daytime

#-----------------------------------------------------------------------------------------------------------------------\
#定时运行类
class Schedule:
    def __init__(self):
        self.name = namechoice()
        self.day = daychoice()
        self.time = FunctionSelect(self.name)
        self.sched = BlockingScheduler()
        print(self.name)
        print(self.day)
        print(self.time)
        self.sched.add_job(
            func= lambda:self.stadiumChoice_and_reserve(),
            trigger='interval',
            seconds = 5,
        )
        self.sched.start()

    def stadiumChoice_and_reserve(self):
        try:
            print(f"正在为你选择场馆：{self.name}")
            stadiumChoice(self.name)
            print(f"正在选择时间：{self.time}")
            timechoice(self.time)
        except:
            pass
        try:
            print("正在检测可预约场地...")
            scenes()
        except Exception as e:
            print(e)
app = Schedule()