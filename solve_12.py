
from msilib.schema import File
from tkinter import *                                                   # Импортируем библиотеку, отвечающую за графику 
from tkinter import messagebox  
from tkinter import filedialog as fd                                                          
import math                                                                 
import random                                                               
import time                                                        

countOfPoints = 0                                                       # Глобальная переменная, отвечающая за количество точек (= прямоугольников)
arrPoints = [[0]*4]                                                     # Первый глобальный массив, где хранятся координаты в привычном виде
arrPoints2 = [[0]*4]                                                    # Второй глобальный массив, где координаты представлены в пикселях

arrRect1 = [0, 0, 0, 0]
arrRect2 = [0, 0, 0, 0]

posX = 0
posY = 0
countOfPoints0 = 0

arr = [0, 0]

def rgbtohex(r,g,b):                                                    # Функция перевода трёх параметров RGB в единый код цвета
    return f'#{r:02x}{g:02x}{b:02x}'


def createCoordAxes():                                                  # Функция, отвечающая за отрисовку координатной плоскости

    for i in range (0, 21):                                             # рисуем линии разметки 
        if(i != 10):                                                    
            coordPlane.create_line((60 + i*40), 0,                      # создаём горизонтальные линии разметки
            (60 + i*40), 840,                                     
            width=2, fill='#DBD7D2', dash=(10,1))

            coordPlane.create_line(40, (820 - i*40),                    # создаём вертикальные линии разметки    
            880, (820 - i*40),                                      
            width=2, fill='#DBD7D2', dash=(10,1))    

    coordPlane.create_line(40, 420, 880, 420, arrow=LAST,               # создаём ось x
    width=4, fill='#000000')              
    coordPlane.create_line(460, 840, 460, 0, arrow=LAST,                # создаём ось y
    width=4, fill='#000000')

    for i in range (0, 21):                                             # рисуем засечки на осях
        if(i != 10):
            coordPlane.create_line((60 + i*40), (420 - 5),              # горизонтальные засечки
            (60 + i*40), (420 + 5),                                     
            width=2, fill='#000000')

            coordPlane.create_line((460 - 5), (820 - i*40),             # вертикальные засечки  
            (460 + 5), (820 - i*40),                                      
            width=2, fill='#000000')                              

    x_text = Label(text = "x", background='#FAE7B5')                    # подписываем ось Х
    x_text.place(x = 830+1000, y = 425+80)
    y_text = Label(text = "y", background='#FAE7B5')                    # подписываем ось Y
    y_text.place(x = 425+1000, y = 80)
    zero_text = Label(text = "0", background='#FAE7B5')                 # и теперь подпишем 0
    zero_text.place(x = 422+1000, y = 80+422)

def understandOurWay():                                                 # Функция определения способа ввода (файл / мышь / клавиатура)
    inputMethod.place(x = 300, y = 200)             
    rad0.place(x = 300, y = 250)                                    
    rad1.place(x = 300, y = 290)
    rad2.place(x = 300, y = 330) 
    fb.place(x = 310, y = 380)

def fb_was_clicked():                                                   # Функция, отвечающая за осознание способа ввода, начинающая другие функции (в зависимости от выбора) 
    x = var.get()                                                       
    if(x == 1):
        inputMethod.place_forget()                                      
        rad0.place_forget()                                 
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()

        opFl1()
                                                                        
    if(x == 2):
        inputMethod.place_forget()                                     
        rad0.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()   

        tchCvs1()                                                                

    if(x == 3):
        inputMethod.place_forget()                                      
        rad0.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()  

        getCountOfPoints()                                             


def opFl1():                                                            # Функция ожидания получения пути к файлу
    b1.place(x = 200, y = 200)
 
    path = filePath()
    partpath = path[(len(path) - 4): len(path)]
    if(path != ''):
        if(partpath == '.txt'):
            b1.place_forget()
            opFl2(path)
        else:
            messagebox.showinfo("Troubles",                                      
            "Выбран не файл формата txt!")      

def filePath():                                                         # Функция получения пути к файлу на компьютере     
    file_name = fd.askopenfilename()
    return file_name

def opFl2(p):                                                           # Функция считывания данных с файла и их последующей обработки
    file = open(p, 'r')
    flag = True    

    s1 = file.readlines()

    for i in range (0, len(s1)):
        arrLine = s1[i].split(' ')
        if(i < len(s1) - 1):
            try:
                xxx = int(arrLine[0])
                yyy = int(arrLine[1])
                xxx2 = int(arrLine[2])
                yyy2 = arrLine[3]
                yyy2 = yyy2[0 : (len(arrLine[3])- 1)]
                yyy2 = int(yyy2)

                if(xxx != xxx2 and yyy != yyy2):
                    arrPoints.append([xxx, yyy, xxx2, yyy2])
                else:
                    messagebox.showinfo("Troubles",                                      
                    "В файле содержатся некорректные данные")
                    opFl1()

            except BaseException:
                messagebox.showinfo("Troubles",                                      
                    "В файле содержатся некорректные данные")
                opFl1()
        else:
            try:
                xxx = int(arrLine[0])
                yyy = int(arrLine[1])
                xxx2 = int(arrLine[2])
                yyy2 = int(arrLine[3])

                if(xxx != xxx2 and yyy != yyy2):
                    arrPoints.append([xxx, yyy, xxx2, yyy2])
                else:
                    messagebox.showinfo("Troubles",                                      
                    "В файле содержатся некорректные данные")
                    opFl1()

            except BaseException:
                messagebox.showinfo("Troubles",                                      
                    "В файле содержатся некорректные данные")
                opFl1()

    file.close()      
    print(arrPoints)  
    singleSegment()



def tchCvs1():                                                          # Получение количества прямоугольников
    getPointsNum.delete(0, END)
    getPointsNum.place(x = 80, y = 150)  
    startText.place(x = 110, y = 100)
    confirmBtnSP.place(x = 340, y = 144)

def confirmBtnSP_was_clicked():                                         # Приём количества точек и начало обработки
    str0 = getPointsNum.get()                                          
    if(str0.isdigit() == TRUE):                                         
        if(int(str0) > 0):                                              
            global countOfPoints 
            countOfPoints = int(str0) * 2   

            global countOfPoints0 
            countOfPoints0 = int(str0) * 2                            

            str1 = "Осталось ввести точек: " + str(countOfPoints)                    
            pointRemain.config(text = str1)                             
            pointRemain.place(x = 310, y = 600)

            startText.place_forget()                                    
            confirmBtnSP.place_forget()                                   
            getPointsNum.place_forget()                                 
                                                                        
            tchCvs2()                                                       
                                                          
        else:                                                           
            getPointsNum.delete(0, last=END)                            
            messagebox.showinfo("Troubles",                             
            "Введено не натуральное число!")     

    else:                                                               
        getPointsNum.delete(0, last=END)                                
        messagebox.showinfo("Troubles",                                
        "Введено не натуральное число!")        

def tchCvs2():                                                          # Считывание нажатий 
    coordPlane.bind("<Button-1>", print_event)     
    
    ed = 1
    for i in range(0, 21):                                              
        if(i != 10):
            x_num = Label(text = round(ed*(i - 10), 1),                
            background='#FAE7B5')                                       
            x_num.place(x = 1010 + i*40, y = 920)                      

            y_num = Label(text = round(ed*(i - 10), 1),                 
            background='#FAE7B5')            
            y_num.place(x = 968, y = 920-30-i*40)    

def print_event(event):                                                 # Что делаем при нажатии    
    
    global posX
    posX = event.x
    #print(posX)
    global posY
    posY = event.y
    #print(posY)

    global countOfPoints
    countOfPoints = countOfPoints - 1
    

    if(countOfPoints % 2 == 1):
        global arr
        arr[0] = posX
        arr[1] = posY
    elif(countOfPoints % 2 == 0 and countOfPoints < countOfPoints0 and countOfPoints >= 0):
        xxx = arr[0]
        yyy = arr[1]
        xxx2 = posX
        yyy2 = posY

        xxx = xxx - 60
        oxxx = xxx % 40
        if(oxxx >= 20):
            xxx = xxx - oxxx + 40
        else:
            xxx = xxx - oxxx
        xxx = xxx / 40 - 10
        xxx = int(xxx)

        xxx2 = xxx2 - 60
        oxxx = xxx2 % 40
        if(oxxx >= 20):
            xxx2 = xxx2 - oxxx + 40
        else:
            xxx2 = xxx2 - oxxx
        xxx2 = xxx2 / 40 - 10
        xxx2 = int(xxx2)

        yyy = yyy - 20
        oxxx = yyy % 40
        if(oxxx >= 20):
            yyy = yyy - oxxx + 40
        else:
            yyy = yyy - oxxx
        yyy = yyy / 40 - 10
        yyy = int(-yyy)

        yyy2 = yyy2 - 20
        oxxx = yyy2 % 40
        if(oxxx >= 20):
            yyy2 = yyy2 - oxxx + 40
        else:
            yyy2 = yyy2 - oxxx
        yyy2 = yyy2 / 40 - 10
        yyy2 = int(-yyy2)

        if(xxx != xxx2 and yyy != yyy2):
            arrPoints.append([xxx, yyy, xxx2, yyy2])
            print([xxx, yyy, xxx2, yyy2])
            drawTouch(1)
        else:
            messagebox.showinfo("Troubles",                                      
            "Это не прямоугольник")
            countOfPoints = countOfPoints + 2

        if(countOfPoints == 0):
            pointRemain.place_forget()
            coordPlane.unbind("<Button-1>")
            mainTask()
    
    str1 = "Осталось точек: " + str(countOfPoints)                     
    pointRemain.config(text = str1)  

def drawTouch(base):                                                    # Рисуем прямоугольники
    ggg = 30
    bbb = 60
    rrr = 240                              

    print("1111")
    x1 = arrPoints[len(arrPoints) - 1][0]
    y1 = arrPoints[len(arrPoints) - 1][1]
    x2 = arrPoints[len(arrPoints) - 1][2]
    y2 = arrPoints[len(arrPoints) - 1][3]

    print([x1, y1, x2, y2])

    x1 = (x1 / base)*40 + 460                                    
    y1 = 420 - (y1 / base)*40                                       
    x2 = (x2 / base)*40 + 460                                        
    y2 = 420 - (y2 / base)*40 

    print([x1, y1, x2, y2])

    arrPoints2.append([int(x1), int(y1),                           
    int(x2), int(y2)])

    if(ggg < 250 and bbb < 250):
        coordPlane.create_rectangle(x1, y1,                             
        x2, y2, width = 2, outline = rgbtohex(rrr, ggg, bbb))  
    else:
        coordPlane.create_rectangle(x1, y1,                             
        x2, y2, width = 2, outline = 'red')  
        
    ggg = ggg + 30
    bbb = bbb + 30
    rrr = rrr - 30



def getCountOfPoints():                                                 # Отрисовываем строку ввода количесва точек, надпись и кнопку. Ждём её нажатия
    getPointsNum.delete(0, END)
    getPointsNum.place(x = 80, y = 150)  
    startText.place(x = 110, y = 100)
    confirmBtn.place(x = 340, y = 144)

def confirmBtn_was_clicked():                                           # Функция после нажатия кнопки, сообщающая, что количество точек (прямоугольников получено)
    str0 = getPointsNum.get()                                           
    if(str0.isdigit() == TRUE):                                         
        if(int(str0) > 0):                                              
            global countOfPoints
            countOfPoints = int(str0) * 4                               

            str1 = "Осталось точек: " + str(countOfPoints)              
            pointRemain.config(text = str1)                             
            pointRemain.place(x = 110, y = 600)

            startText.place_forget()                                    
            confirmBtn.place_forget()                                   
            getPointsNum.place_forget()                                 
                                                                        
            getThePoints()                                              
                                                          
        else:                                                           
            getPointsNum.delete(0, last=END)                            
            messagebox.showinfo("Troubles",                             
            "Введено не натуральное число!")     

    else:                                                               
        getPointsNum.delete(0, last=END)                                
        messagebox.showinfo("Troubles",                                 
        "Введено не натуральное число!")        

def getThePoints():                                                     # Функция сбора значений точек    

    inputTextX1.place(x = 76, y = 270)                                  # Разместим 4 строки ввода   
    inputTextY1.place(x = 76, y = 350)
    inputTextX2.place(x = 76, y = 430)
    inputTextY2.place(x = 76, y = 510)

    getPointX1.place(x = 80, y = 300)                                   # Разместим 4 текста         
    getPointY1.place(x = 80, y = 380)                           
    getPointX2.place(x = 80, y = 460)    
    getPointY2.place(x = 80, y = 540) 

    confirmBtn2.place(x = 350, y = 405)                                 # И кнопку "Принять"   

    randButton.place(x = 150, y = 830)                                  # А также кнопку получения рандомных значений
    rad10.place(x = 250, y = 700)                                       # И выбор, в каком диапазоне числа рандомить (до 10, до 50, до 100)
    rad11.place(x = 250, y = 740)
    rad12.place(x = 250, y = 780) 
         
def confirmBtn2_was_clicked():                                          # Функция, исполняемая при нажатии кнопки, сообщающая о том, что точки введены
    cp = pointRemain.cget("text")                                       
    cp = cp[16:]                                                       
    cpp = int(cp)
    if(cpp > 0):                                                        
        xxx1 = getPointX1.get()                                         
        yyy1 = getPointY1.get()
        xxx2 = getPointX2.get()                                          
        yyy2 = getPointY2.get()
        
        if(is_digit(xxx1) and is_digit(yyy1) and                       
        is_digit(xxx2) and is_digit(yyy2)):                            
            if(int(xxx1) != int(xxx2) and int(yyy1) != int(yyy2)):      
                getPointX1.delete(0, last=END)                          
                getPointY1.delete(0, last=END)
                getPointX2.delete(0, last=END)                  
                getPointY2.delete(0, last=END)
                arrPoints.append( [int(xxx1), int(yyy1),               
                int(xxx2), int(yyy2)] )
                cpp = cpp - 4
                str1 = "Осталось точек: " + str(cpp)                     
                pointRemain.config(text = str1) 
                if(cpp == 0):                                           
                    finalPoint()                                        
            else:
                getPointX1.delete(0, last=END)                          
                getPointY1.delete(0, last=END)
                getPointX2.delete(0, last=END)                  
                getPointY2.delete(0, last=END)
                messagebox.showinfo("Troubles",                         
                "Это не прямоугольник!")    

        else:                                                           
            getPointX1.delete(0, last=END)                  
            getPointY1.delete(0, last=END)
            getPointX2.delete(0, last=END)                  
            getPointY2.delete(0, last=END)
            messagebox.showinfo("Troubles",                               
            "Введено не число!")    
    
def randButton_was_clicked():                                           # Функция, отвечающая за генерацию рандомных значений точек
    x = var1.get()                                                      
    if(x == 1):                                                         
        getPointX1.delete(0, last=END)                                  # на всякий случай очищаем строки ввода    
        getPointY1.delete(0, last=END)
        getPointX2.delete(0, last=END)                  
        getPointY2.delete(0, last=END)

        getPointX1.insert(0, str(random.randint(-10, 10)))              # и заполняем только что очищенные строки рандомными значениями из выбранного промежутка  
        getPointY1.insert(0, str(random.randint(-10, 10)))
        getPointX2.insert(0, str(random.randint(-10, 10)))                  
        getPointY2.insert(0, str(random.randint(-10, 10)))
    
    if(x == 2):                                                         
        getPointX1.delete(0, last=END)                                 
        getPointY1.delete(0, last=END)
        getPointX2.delete(0, last=END)                  
        getPointY2.delete(0, last=END)

        getPointX1.insert(0, str(random.randint(-50, 50)))                 
        getPointY1.insert(0, str(random.randint(-50, 50)))
        getPointX2.insert(0, str(random.randint(-50, 50)))                  
        getPointY2.insert(0, str(random.randint(-50, 50)))
    
    if(x == 3):                                                         
        getPointX1.delete(0, last=END)                                    
        getPointY1.delete(0, last=END)
        getPointX2.delete(0, last=END)                  
        getPointY2.delete(0, last=END)

        getPointX1.insert(0, str(random.randint(-100, 100)))                 
        getPointY1.insert(0, str(random.randint(-100, 100)))
        getPointX2.insert(0, str(random.randint(-100, 100)))                  
        getPointY2.insert(0, str(random.randint(-100, 100)))

def is_digit(t):                                                        # Функция, написанная, чтобы определить, получили мы число, приемлемое на плосоксти
    if(t.isdigit()):
        return True
    else:
        t1 = t[:1]
        if(t1 == '-'):
            t2 = t[1:]                                                  
            if t2.isdigit():
                return True
            else:
                try:
                    float(t2)
                    return True
                except ValueError:
                    return False
        else:
            t2 = t
            try:
                float(t2)
                return True
            except ValueError:
                return False
  
def finalPoint():                                                       # После ввода точек промежуточная функция
    getPointX1.place_forget()                                           
    getPointY1.place_forget()
    getPointX2.place_forget()                                           
    getPointY2.place_forget()
    pointRemain.place_forget()
    inputTextX1.place_forget()
    inputTextY1.place_forget()
    inputTextX2.place_forget()                                          
    inputTextY2.place_forget()
    confirmBtn2.place_forget()
    rad10.place_forget()
    rad11.place_forget()
    rad12.place_forget()
    randButton.place_forget()                                               
    singleSegment()

def singleSegment():                                                    # Функция определения единичного отрезка на плоскости
    arrPoints.pop(0)                                                    
    x1max = abs(arrPoints[0][0])                                        
    y1max = abs(arrPoints[0][1])
    x2max = abs(arrPoints[0][2])
    y2max = abs(arrPoints[0][3])

    arr1 = [x1max, y1max, x2max, y2max]                                 
    arr2 = [0, 0, 0, 0]                                                 

    for i in range (1, len(arrPoints)):                                 
        arr2 = [abs(arrPoints[i][0]), abs(arrPoints[i][1]),             
        abs(arrPoints[i][2]), abs(arrPoints[i][3])]                            

        arr1.sort()                                                     
        arr2.sort()                                                        

        if(arr1[3] < arr2[3]):                                         
            arr1[0] = arr2[0]                                           
            arr1[1] = arr2[1]   
            arr1[2] = arr2[2]
            arr1[3] = arr2[3]
                                                                            
    ed = math.ceil(arr1[3] / 10)                                                                       

    for i in range(0, 21):                                              
        if(i != 10):
            x_num = Label(text = round(ed*(i - 10), 1),                
            background='#FAE7B5')                                       
            x_num.place(x = 1010 + i*40, y = 920)                      

            y_num = Label(text = round(ed*(i - 10), 1),                 
            background='#FAE7B5')
            if(arr1[3] >= 10):
                otstup = 15
            if(arr1[3] >= 100):
                otstup = 25
            if(arr1[3] < 10):
                otstup = 5                   
            y_num.place(x = 968, y = 920-30-i*40)
    drawPoints(ed)

def drawPoints(base):                                                   # Рисуем прямоугольники
    ggg = 30
    bbb = 60
    rrr = 240
    for i in range(0, len(arrPoints)):                                  

        x1 = arrPoints[i][0]
        y1 = arrPoints[i][1]
        x2 = arrPoints[i][2]
        y2 = arrPoints[i][3]

        x1 = (x1 / base)*40 + 460                                    
        y1 = 420 - (y1 / base)*40                                       
        x2= (x2 / base)*40 + 460                                        
        y2 = 420 - (y2 / base)*40 

        arrPoints2.append([int(x1), int(y1),                           
        int(x2), int(y2)])

        if(ggg < 250 and bbb < 250):
            coordPlane.create_rectangle(x1, y1,                             
            x2, y2, width = 2, outline = rgbtohex(rrr, ggg, bbb))  
        else:
            coordPlane.create_rectangle(x1, y1,                             
            x2, y2, width = 2, outline = 'red')  
        
        ggg = ggg + 30
        bbb = bbb + 30
        rrr = rrr - 30

    mainTask()

def mainTask():                                                         # Перейдём к выполнению основного задания
    time.sleep(1)                                                                     
    arrPoints2.pop(0)                                                  

    MaX = 0                                                             
    arrMaX1 = [0, 0]                                                   
    arrMaX2 = [0, 0]

    for i in range (0, len(arrPoints2)):                                

        roadYStart = min(arrPoints2[i][1], arrPoints2[i][3])            
        roadYEnd = max(arrPoints2[i][1], arrPoints2[i][3])              # roadXStart, roadYStart - верхняя левая точка прямоугольника   
        roadXStart = min(arrPoints2[i][0], arrPoints2[i][2])            # roadXEnd, roadXStart - правая нижняя точка
        roadXEnd = max(arrPoints2[i][0], arrPoints2[i][2]) 

        for j in range(0, len(arrPoints2)):                            

            crossroad = False                                           # Пересечений нет
            crossroad2 = False                                          # Наложений нет

            if(i != j):                                                   

                YStart = min(arrPoints2[j][1], arrPoints2[j][3])        # Обозначим переменными значениями координат других прямоугольников, с которыми мы будем сравнивать
                YEnd = max(arrPoints2[j][1], arrPoints2[j][3])          # За XStart, XEnd, YStart, YEnd
                XStart = min(arrPoints2[j][0], arrPoints2[j][2])
                XEnd = max(arrPoints2[j][0], arrPoints2[j][2]) 

                print(roadXStart, roadYStart, roadXEnd, roadYEnd)         
                print(XStart, YStart, XEnd, YEnd)

                 
                if(roadXStart < XStart and roadXEnd > XEnd and roadYStart < YStart and roadYEnd > YEnd):          
                    crossroad = False
                    print("случай 5.1")
                elif(roadYStart > YStart and roadYEnd < XEnd and roadXStart > XStart and roadXEnd < XEnd):        
                    crossroad = False  
                    print("случай 5.2")
                elif(roadYStart > YEnd):                                                                          
                    crossroad = False
                    print("случай 5.3")
                elif(roadXEnd < XStart):                                                                          
                    crossroad = False
                    print("случай 5.4")
                elif(roadYEnd < YStart):                                                                             
                    crossroad = False
                    print("случай 5.5")
                elif(roadXStart > XEnd):                                                                          
                    crossroad = False
                    print("случай 5.6")
                else:       
                    crossroad = True                                    # Обработаны все возможные варианты "не пересечений" 2-х рассматриваемых прямоугольников, 
                                                                        # значит, они пересекаютcя

                count = 0                                               # отвечает за количество пересечений
                ss1 = [0, 0]                                            # координаты крайних точек линии, соединяющей места пересечений    
                ss2 = [0, 0]

                if(crossroad == True):                                  # Если пересечение есть,
                    if(roadXStart == XStart or roadXStart == XEnd or    # проверим на наложение
                    roadXEnd == XStart or roadXEnd == XEnd or
                    roadYStart == YStart or roadYStart == YEnd or 
                    roadYEnd == YStart or roadYEnd == YEnd):
                        crossroad = False                               # пересечения нет
                        crossroad2 = True                               # есть наложение


                    if(roadXStart < XStart and roadXEnd > XEnd and      # Пересечений может быть либо 4, либо 2
                    roadYStart > YStart and roadYEnd < YEnd):      
                        count = 4                                                     
                    elif(roadXStart > XStart and roadXEnd < XEnd and 
                    roadYStart < YStart and roadYEnd > YEnd):    
                        count = 6                                         
                    else:
                        count = 2                                       # не 4, значит 2

                if(count == 2 and crossroad == True):                   # Если пересечения 2, и нет наложения, то

                    if(roadXStart > XStart and roadYStart > YStart and roadXEnd > XEnd and roadYEnd > YEnd):      
                        ss1 = [roadXStart, YEnd]
                        ss2 = [XEnd, roadYStart]
                        print("случай 1.1")
                    elif(roadXStart < XStart and roadYStart > YStart and roadXEnd < XEnd and roadYEnd > YEnd):    
                        ss1 = [XStart, roadYStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 1.2")
                    elif(roadXStart < XStart and roadYStart < YStart and roadXEnd < XEnd and roadYEnd < YEnd):    
                        ss1 = [XStart, roadYEnd]
                        ss2 = [roadXEnd, YStart]
                        print("случай 1.3")
                    elif(roadXStart > XStart and roadYStart < YStart and roadXEnd > XEnd and roadYEnd < YEnd):   
                        ss1 = [XEnd, roadYEnd]
                        ss2 = [roadXStart, YStart]
                        print("случай 1.4")


                    elif(roadXStart > XStart and roadYStart < YStart and roadXEnd > XEnd and roadYEnd > YEnd):    
                        ss1 = [roadXStart, YStart]
                        ss2 = [roadXStart, YEnd]
                        print("случай 2.1")
                    elif(roadXStart < XStart and roadYStart > YStart and roadXEnd > XEnd and roadYEnd > YEnd):    
                        ss1 = [XStart, roadYStart]
                        ss2 = [XEnd, roadYStart]
                        print("случай 2.2")
                    elif(roadXStart < XStart and roadYStart < YStart and roadXEnd < XEnd and roadYEnd > YEnd):    
                        ss1 = [roadXEnd, YStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 2.3")
                    elif(roadXStart < XStart and roadYStart < YStart and roadXEnd > XEnd and roadYEnd < YEnd):    
                        ss1 = [XEnd, roadYEnd]
                        ss2 = [XStart, roadYEnd]
                        print("случай 2.4")


                    elif(roadXStart > XStart and roadYStart > YStart and roadXEnd > XEnd and roadYEnd < YEnd):    
                        ss1 = [XEnd, roadYStart]
                        ss2 = [XEnd, roadYEnd]
                        print("случай 3.1")
                    elif(roadXStart > XStart and roadYStart > YStart and roadXEnd < XEnd and roadYEnd > YEnd):    
                        ss1 = [roadXEnd, YEnd]
                        ss2 = [roadXStart, YEnd]
                        print("случай 3.2")
                    elif(roadXStart < XStart and roadYStart > YStart and roadXEnd < XEnd and roadYEnd < YEnd):    
                        ss1 = [XStart, roadYStart]
                        ss2 = [XStart, roadYEnd]
                        print("случай 3.3")
                    elif(roadXStart > XStart and roadYStart < YStart and roadXEnd < XEnd and roadYEnd < YEnd):    
                        ss1 = [roadXStart, YStart]
                        ss2 = [roadXEnd, YStart]
                        print("случай 3.4")
                    

                if(count == 4 and crossroad == True):            # Если пересечения 4 (1 сл.)                      
                    ss1 = [XStart, roadYStart]
                    ss2 = [XEnd, roadYEnd]
                    print("случай 4.1")    
                      
                if(count == 6 and crossroad == True):            # Если пересечения 4 (2 сл.)                      
                    ss1 = [roadXStart, YStart]
                    ss2 = [roadXEnd, YEnd]
                    print("случай 4.2")
            

                if(crossroad2 == True):                          # Если есть наложение, а не пересечение  

                    if(roadXStart == XEnd):
                        if(roadYStart <= YStart and roadYEnd >= YEnd):
                            ss1 = [XEnd, YStart]
                            ss2 = [XEnd, YEnd]
                            print("case 6.1.1")
                        else:
                            if(YStart < roadYStart):
                                ss1 = [XEnd, roadYStart]
                                print("case 6.2.1.1")
                            else:
                                ss1 = [XEnd, YStart]
                                print("case 6.2.1.2")

                            if(YEnd > roadYEnd):
                                ss2 = [XEnd, roadYEnd]
                                print("case 6.2.1.3")
                            else:
                                ss2 = [XEnd, YEnd]
                                print("case 6.2.1.4")
                    
                    if(roadXEnd == XStart):
                        if(roadYStart <= YStart and roadYEnd >= YEnd):
                            ss1 = [XStart, YStart]
                            ss2 = [XStart, YEnd]
                            print("case 6.1.2")
                        else:
                            if(YStart < roadYStart):
                                ss1 = [XStart, roadYStart]
                                print("case 6.2.2.1")
                            else:
                                ss1 = [XStart, YStart]
                                print("case 6.2.2.2")

                            if(YEnd > roadYEnd):
                                ss2 = [XStart, roadYEnd]
                                print("case 6.2.2.3")
                            else:
                                ss2 = [XStart, YEnd]
                                print("case 6.2.2.4")

                    if(roadYStart == YEnd):
                        if(roadXStart <= XStart and roadXEnd >= XEnd):
                            ss1 = [XStart, YEnd]
                            ss2 = [XEnd, YEnd]
                            print("case 6.1.3")
                        else:
                            if(XStart < roadXStart):
                                ss1 = [roadXStart, YEnd]
                                print("case 6.2.3.1")
                            else:
                                ss1 = [XStart, YEnd]
                                print("case 6.2.3.2")

                            if(XEnd > roadXEnd):
                                ss2 = [roadXEnd, YEnd]
                                print("case 6.2.3.3")
                            else:
                                ss2 = [XEnd, YEnd]
                                print("case 6.2.3.4")
                                
                    if(roadYEnd == YStart):
                        if(roadXStart <= XStart and roadXEnd >= XEnd):
                            ss1 = [XStart, YStart]
                            ss2 = [XEnd, YStart]
                            print("case 6.1.4")
                        else:
                            if(XStart < roadXStart):
                                ss1 = [roadXStart, YStart]
                                print("case 6.2.4.1")
                            else:
                                ss1 = [XStart, YStart]
                                print("case 6.2.4.2")

                            if(XEnd > roadXEnd):
                                ss2 = [roadXEnd, YStart]
                                print("case 6.2.4.3")
                            else:
                                ss2 = [XEnd, YStart]
                                print("case 6.2.4.4")

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

                    if(roadXStart == XStart):
                        if(YStart <= roadYStart and YEnd <= roadYEnd):
                            if(XEnd <= roadXEnd):
                                ss1 = [XStart, YEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.3.1.1")
                            else:
                                ss1 = [XStart, YEnd]
                                ss2 = [roadXEnd, roadYStart]
                                print("case 6.3.1.2")
                            
                        if(YStart > roadYStart and YEnd < roadYEnd):
                            if(XEnd < roadXEnd):
                                ss1 = [XStart, YStart]
                                ss2 = [XStart, YEnd]
                                print("case 6.3.2.1")
                            else:
                                ss1 = [XStart, YStart]
                                ss2 = [roadXEnd, YEnd]
                                print("case 6.3.2.2")

                        if(YStart > roadYStart and YEnd >= roadYEnd):
                            if(XEnd <= roadXEnd):
                                ss1 = [XStart, YStart]
                                ss2 = [XEnd, roadYEnd]
                                print("case 6.3.3.1")
                            else:
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [roadXEnd, YStart]
                                print("case 6.3.3.2")

                        if(YStart < roadYStart and YEnd > roadYEnd):
                            if(XEnd <= roadXEnd):
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.3.4.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYStart]
                                print("case 6.3.4.2")

                        if(YStart == roadYStart and YEnd == roadYEnd):
                            if(XEnd <= roadXEnd):
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.3.5.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYStart]
                                print("case 6.3.5.2")        
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

                    if(roadXEnd == XEnd):
                        if(YStart <= roadYStart and YEnd <= roadYEnd):
                            if(roadXStart <= XStart):
                                ss1 = [XStart, roadYStart]
                                ss2 = [roadXEnd, YEnd]
                                print("case 6.4.1.1")
                            else:
                                ss1 = [roadXStart, YEnd]
                                ss2 = [roadXEnd, roadYStart]
                                print("case 6.4.1.2")
                            
                        if(YStart > roadYStart and YEnd < roadYEnd):
                            if(roadXStart < XStart):
                                ss1 = [XEnd, YStart]
                                ss2 = [XEnd, YEnd]
                                print("case 6.4.2.1")
                            else:
                                ss1 = [XEnd, YEnd]
                                ss2 = [roadXStart, YStart]
                                print("case 6.4.2.2")

                        if(YStart > roadYStart and YEnd >= roadYEnd):
                            if(roadXStart <= XStart):
                                ss1 = [XStart, roadYEnd]
                                ss2 = [roadXEnd, YStart]
                                print("case 6.4.3.1")
                            else:
                                ss1 = [roadXStart, YStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.4.3.2")

                        if(YStart < roadYStart and YEnd > roadYEnd):
                            if(roadXStart <= XStart):
                                ss1 = [XStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.4.4.1")
                            else:
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.4.4.2")

                        if(YStart == roadYStart and YEnd == roadYEnd):
                            if(roadXStart <= XStart):
                                ss1 = [XStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.4.5.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.4.5.2")  

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

                    if(roadYStart == YStart):
                        if(XStart <= roadXStart and XEnd <= roadXEnd):
                            if(roadYEnd >= YEnd):
                                ss1 = [roadXStart, YEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.5.1.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [XEnd, roadYEnd]
                                print("case 6.5.1.2")

                        if(roadXStart < XStart and XEnd < roadXEnd):
                            if(roadYEnd > YEnd):
                                ss1 = [XStart, YStart]
                                ss2 = [XEnd, YStart]
                                print("case 6.5.2.1")
                            else:
                                ss1 = [XStart, YStart]
                                ss2 = [XEnd, roadYEnd]
                                print("case 6.5.2.2")

                        if(roadXStart <= XStart and XEnd > roadXEnd):
                            if(roadYEnd >= YEnd):
                                ss1 = [XStart, YStart]
                                ss2 = [roadXEnd, YEnd]
                                print("case 6.5.3.1")
                            else:
                                ss1 = [roadXEnd, roadYStart]
                                ss2 = [XStart, roadYEnd]
                                print("case 6.5.3.2")
                        
                        if(roadXStart > XStart and XEnd > roadXEnd):
                            if(roadYEnd >= YEnd):
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, YEnd]
                                print("case 6.5.4.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYStart]
                                print("case 6.5.4.2")
                        
                        if(roadXStart == XStart and roadXEnd == XEnd):
                            if(roadYEnd >= YEnd):
                                ss1 = [XStart, YStart]
                                ss2 = [XEnd, YEnd]
                                print("case 6.5.6.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.5.6.2")

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

                    if(roadYEnd == YEnd):    
                        if(XStart <= roadXStart and XEnd <= roadXEnd):
                            if(roadYStart <= YStart):
                                ss1 = [roadXStart, YStart]
                                ss2 = [XEnd, YEnd]
                                print("case 6.6.1.1")
                            else:
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.6.1.2")
                        
                        if(roadXStart < XStart and XEnd < roadXEnd):
                            if(roadYStart < YStart):
                                ss1 = [XStart, YEnd]
                                ss2 = [XEnd, YEnd]
                                print("case 6.6.2.1")
                            else:
                                ss1 = [XStart, YEnd]
                                ss2 = [XEnd, roadYStart]
                                print("case 6.6.2.2")

                        if(roadXStart <= XStart and XEnd > roadXEnd):
                            if(roadYStart <= YStart):
                                ss1 = [XStart, YEnd]
                                ss2 = [roadXEnd, YStart]
                                print("case 6.6.3.1")
                            else:
                                ss1 = [XStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.6.3.2")
                        
                        if(roadXStart > XStart and XEnd > roadXEnd):
                            if(roadYStart <= YStart):
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [roadXEnd, YStart]
                                print("case 6.6.4.1")
                            else:
                                ss1 = [roadXStart, roadYEnd]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.6.4.2")
                        
                        if(roadXStart == XStart and roadXEnd == XEnd):
                            if(roadYStart <= YStart):
                                ss1 = [roadXStart, YStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.6.5.1")
                            else:
                                ss1 = [roadXStart, roadYStart]
                                ss2 = [roadXEnd, roadYEnd]
                                print("case 6.6.5.2")


#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------                                              


                r = math.sqrt((ss2[0]-ss1[0])**2 + (ss2[1]-ss1[1])**2)  # расстояние между точками     

                if(r > MaX):                                            # Сравним его с максимумом  
                    MaX = r                                             # Если максимум вдруг меньше - перепишем все значения
                    arrMaX1 = ss1
                    arrMaX2 = ss2
                    arrRect1.pop(3)
                    arrRect1.pop(2)
                    arrRect1.pop(1)
                    arrRect1.pop(0)
                    arrRect1.append(roadXStart)
                    arrRect1.append(roadYStart)
                    arrRect1.append(roadXEnd)
                    arrRect1.append(roadYEnd)
                    arrRect2.pop(3)
                    arrRect2.pop(2)
                    arrRect2.pop(1)
                    arrRect2.pop(0)
                    arrRect2.append(XStart)
                    arrRect2.append(YStart)
                    arrRect2.append(XEnd)
                    arrRect2.append(YEnd)


    
    coordPlane.create_rectangle(arrRect1[0], arrRect1[1], arrRect1[2], arrRect1[3], outline='black', width= 3)
    coordPlane.create_rectangle(arrRect2[0], arrRect2[1], arrRect2[2], arrRect2[3], outline='black', width= 3)
    coordPlane.create_line(arrMaX1[0], arrMaX1[1], arrMaX2[0],         
        arrMaX2[1], fill='purple', width = 4)  

    zanovo.place(x = 300, y = 300)
    save.place(x = 300, y = 500)

def zanovo_was_clicked():                                               # Запускает всё заново
    coordPlane.delete("all")
    zanovo.place_forget()

    save.place_forget()

    global countOfPoints
    countOfPoints = 0      

    global arrPoints                                          
    arrPoints = [[0]*4]         

    global arrPoints2                                            
    arrPoints2 = [[0]*4]                                                    

    global arrRect1
    arrRect1 = [0, 0, 0, 0]

    global arrRect2
    arrRect2 = [0, 0, 0, 0]

    createCoordAxes()                                                       
    understandOurWay()                                                      

def save_was_clicked():
    t = time.localtime()
    ct = time.strftime("%d%m%Y_%H%M%S", t)
    strr = ct + ".txt"
    fd1 = fd.askdirectory()
    fd1 = fd1 + "/" + strr
    strr = fd1

    newf = open(strr, "w")
    for i in range (0, len(arrPoints)):
        strrr = ""
        strrr = str(arrPoints[i][0]) + " " + str(arrPoints[i][1]) + " "
        strrr = strrr + str(arrPoints[i][2]) + " " + str(arrPoints[i][3]) + "\n"

        newf.write(strrr)
    
    newf.close()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


window = Tk()                                                           # Создаём главное окно
window.title("Task 12")                                                 # Устанавливаем название окна

window.geometry("1920x1080")                                            # Задаём начальный размер окна  

coordPlane = Canvas(window, width=880, height=860, bg='#FAE7B5')        # Создаём плоскость для рисования прямоугольников
coordPlane.place(x = 960, y = 80)                                       

zanovo = Button(text = 'Заново', font='Arial 14',                        
width = 15, bg='#B2EC5D', command = zanovo_was_clicked)

b1 = Button(text="Открыть файл", font='Arial 14',                        
width = 20, bg='#C018FF', command=opFl1)

fb = Button(text = 'Применить', font='Arial 14',                        
width = 10, bg='#B2EC5D', command = fb_was_clicked)
confirmBtn = Button(text = 'Применить', font='Arial 14',                   
width = 20, bg='#C018FF', command  =confirmBtn_was_clicked)   
confirmBtnSP = Button(text = 'Применить', font='Arial 14',                   
width = 25, bg='#C018FF', command  =confirmBtnSP_was_clicked)             
confirmBtn2 = Button(text = 'Применить', font='Arial 14',               
width = 20, bg='#76EA9F', command = confirmBtn2_was_clicked)           
    
save = Button(text = 'Сохранить прямоугольники', font='Arial 14',                        
width = 25, bg='#B2EC5D', command = save_was_clicked)


randButton = Button(text = 'Использовать рандом', font='Arial 14',                
width = 30, bg='#7FFF00', command = randButton_was_clicked)

inputMethod = Label(text='Выберите способ ввода:', font='Arial 16')     

var = IntVar()                                                          
var.set(3)
rad0 = Radiobutton(window, text="Файлом", variable=var, 
font='Arial 14', value=1)                                                   
rad1 = Radiobutton(window, text="На плоскости", variable=var, 
font='Arial 14', value=2)
rad2 = Radiobutton(window, text="С клавиатуры", variable=var, 
font='Arial 14', value=3)                                               

startText = Label(text = "Введите количество прямоугольников",          
font='Arial 16')

getPointsNum = Entry(bg='white', font='Arial 16', width = 20)           
                                                        
getPointX1 = Entry(bg='white', font='Arial 16', width = 20)             
getPointY1 = Entry(bg='white', font='Arial 16', width = 20)               
getPointX2 = Entry(bg='white', font='Arial 16', width = 20)             
getPointY2 = Entry(bg='white', font='Arial 16', width = 20)               
                     
pointRemain = Label(text = "", font='Arial 14', fg='#1D4290')           

inputTextX1 = Label(text = "Введите X1 прямоугольника:",                
    font='Arial 14')
inputTextY1 = Label(text = "Введите Y1 прямоугольника:",                        
    font='Arial 14')
inputTextX2 = Label(text = "Введите X2 прямоугольника:",                     
    font='Arial 14')
inputTextY2 = Label(text = "Введите Y2 прямоугольника:",                        
    font='Arial 14')

var1 = IntVar()                                                         
var1.set(1)
rad10 = Radiobutton(window, text="Числа до 10", variable = var1, 
font='Arial 14', value=1)          
rad11 = Radiobutton(window, text="Числа до 50", variable = var1, 
font='Arial 14', value=2)
rad12 = Radiobutton(window, text="Числа до 100", variable = var1, 
font='Arial 14', value=3)                                               

createCoordAxes()                                                       # запускаем функцию по отрисовке координатной плоскости
understandOurWay()                                                      
window.mainloop()                                                       

                      




