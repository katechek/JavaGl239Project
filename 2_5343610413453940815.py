
from tkinter import *
from tkinter import messagebox
import math
import random
import time

countOfPoints = 0                                                       #глобальная переменная, отвечающая за количество точек (= прямоугольников)
arrPoints = [[0]*4]                                                     #глобальный массив, где координаты
arrPoints2 = [[0]*4]                                                    #глобальный массив, где координаты в пикселях

def createCoordAxes():

    for i in range (0, 21):
        if(i != 10):
            coordPlane.create_line((60 + i*40), 0,
            (60 + i*40), 840,                                     
            width=2, fill='#DBD7D2', dash=(10,1))

            coordPlane.create_line(40, (820 - i*40),
            880, (820 - i*40),                                      
            width=2, fill='#DBD7D2', dash=(10,1))    

    coordPlane.create_line(40, 420, 880, 420, arrow=LAST,
    width=4, fill='#000000')              
    coordPlane.create_line(460, 840, 460, 0, arrow=LAST,
    width=4, fill='#000000')

    for i in range (0, 21):
        if(i != 10):
            coordPlane.create_line((60 + i*40), (420 - 5),
            (60 + i*40), (420 + 5),                                     
            width=2, fill='#000000')

            coordPlane.create_line((460 - 5), (820 - i*40),
            (460 + 5), (820 - i*40),                                      
            width=2, fill='#000000')                              

    x_text = Label(text = "x", background='#FAE7B5')
    x_text.place(x = 830+1000, y = 425+80)
    y_text = Label(text = "y", background='#FAE7B5')
    y_text.place(x = 425+1000, y = 80)
    zero_text = Label(text = "0", background='#FAE7B5')
    zero_text.place(x = 422+1000, y = 80+422)



def understandOurWay():                                                 # ввод (файл, рисунок, клавиатура)
    inputMethod.place(x = 300, y = 200)             
    rad0.place(x = 300, y = 250)                                    
    rad1.place(x = 300, y = 290)
    rad2.place(x = 300, y = 330) 
    fb.place(x = 310, y = 380)

def fb_was_clicked():
    x = var.get()
    if(x == 1):
        inputMethod.place_forget()
        rad0.place_forget()                                 
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()


    if(x == 2):
        inputMethod.place_forget()
        rad0.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()   


    if(x == 3):
        inputMethod.place_forget()
        rad0.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        fb.place_forget()  

        getCountOfPoints()

def getCountOfPoints():
    getPointsNum.place(x = 80, y = 150)  
    startText.place(x = 110, y = 100)
    confirmBtn.place(x = 340, y = 144)

def confirmBtn_was_clicked():
    str0 = getPointsNum.get()
    if(str0.isdigit() == TRUE):
        if(int(str0) > 0):
            global countOfPoints
            countOfPoints = int(str0) * 4                               #количество точек в глобальную переменую

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

def getThePoints():

    inputTextX1.place(x = 76, y = 270)
    inputTextY1.place(x = 76, y = 350)
    inputTextX2.place(x = 76, y = 430)
    inputTextY2.place(x = 76, y = 510)

    getPointX1.place(x = 80, y = 300)
    getPointY1.place(x = 80, y = 380)                           
    getPointX2.place(x = 80, y = 460)    
    getPointY2.place(x = 80, y = 540) 

    confirmBtn2.place(x = 350, y = 405)

    randButton.place(x = 150, y = 830)
    rad10.place(x = 250, y = 700)
    rad11.place(x = 250, y = 740)
    rad12.place(x = 250, y = 780) 
         
def confirmBtn2_was_clicked():
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
    
def randButton_was_clicked():
    x = var1.get()
    if(x == 1):
        getPointX1.delete(0, last=END)
        getPointY1.delete(0, last=END)
        getPointX2.delete(0, last=END)                  
        getPointY2.delete(0, last=END)

        getPointX1.insert(0, str(random.randint(-10, 10)))
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

def is_digit(t):
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
  
def finalPoint():
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

def singleSegment():
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

def drawPoints(base):   
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

        coordPlane.create_rectangle(x1, y1,
         x2, y2, width = 2, outline = 'red')  
       
    mainTask()

def mainTask():
    time.sleep(1)
    arrPoints2.pop(0)

    MaX = 0
    arrMaX1 = [0, 0]
    arrMaX2 = [0, 0]

    for i in range (0, len(arrPoints2)):

        roadYStart = min(arrPoints2[i][1], arrPoints2[i][3])
        roadYEnd = max(arrPoints2[i][1], arrPoints2[i][3])
        roadXStart = min(arrPoints2[i][0], arrPoints2[i][2])
        roadXEnd = max(arrPoints2[i][0], arrPoints2[i][2]) 

        for j in range(0, len(arrPoints2)):

            crossroad = False
            crossroad2 = False

            if(i != j):

                YStart = min(arrPoints2[j][1], arrPoints2[j][3])
                YEnd = max(arrPoints2[j][1], arrPoints2[j][3])
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
                    crossroad = True


                count = 0
                ss1 = [0, 0]
                ss2 = [0, 0]

                if(crossroad == True):
                    if(roadXStart == XStart or roadXStart == XEnd or
                    roadXEnd == XStart or roadXEnd == XEnd or
                    roadYStart == YStart or roadYStart == YEnd or 
                    roadYEnd == YStart or roadYEnd == YEnd):
                        crossroad = False
                        crossroad2 = True


                    if(roadXStart < XStart and roadXEnd > XEnd and
                    roadYStart > YStart and roadYEnd < YEnd):      
                        count = 4
                    elif(roadXStart > XStart and roadXEnd < XEnd and 
                    roadYStart < YStart and roadYEnd > YEnd):    
                        count = 6
                    else:
                        count = 2

                if(count == 2 and crossroad == True):

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
                    

                if(count == 4 and crossroad == True):
                    ss1 = [XStart, roadYStart]
                    ss2 = [XEnd, roadYEnd]
                    print("случай 4.1")    
                      
                if(count == 6 and crossroad == True):
                    ss1 = [roadXStart, YStart]
                    ss2 = [roadXEnd, YEnd]
                    print("случай 4.2")
            



                if(crossroad2 == True):
                    if(roadXStart == XStart and roadYStart < YStart and roadYEnd > YEnd):
                        ss1 = [XStart, YStart]
                        ss2 = [XStart, YEnd]
                        print("случай 6.1.1")
                    elif(roadXStart == XEnd and roadYStart < YStart and roadYEnd > YEnd):
                        ss1 = [XEnd, YStart]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.1.2")
                    elif(roadXEnd == XStart and roadYStart < YStart and roadYEnd > YEnd):
                        ss1 = [XStart, YStart]
                        ss2 = [XStart, YEnd]
                        print("случай 6.1.3")
                    elif(roadXEnd == XEnd and roadYStart < YStart and roadYEnd > YEnd):
                        ss1 = [XEnd, YStart]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.1.4") 
                    elif(roadYStart == YStart and roadXStart < XStart and roadXEnd > XEnd):
                        ss1 = [XStart, YStart]
                        ss2 = [XEnd, YStart]
                        print("случай 6.1.5") 
                    elif(roadYStart == YEnd and roadXStart < XStart and roadXEnd > XEnd):
                        ss1 = [XStart, YEnd]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.1.6") 
                    elif(roadYEnd == YStart and roadXStart < XStart and roadXEnd > XEnd):
                        ss1 = [XStart, YStart]
                        ss2 = [XEnd, YStart]
                        print("случай 6.1.7") 
                    elif(roadYEnd == YEnd and roadXStart < XStart and roadXEnd > XEnd):
                        ss1 = [XStart, YEnd]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.1.8")


                    elif(roadXStart == XEnd and roadYStart >= YStart and roadYEnd <= YEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXStart, roadYEnd]
                        print("случай 6.2.1")
                    elif(roadXEnd == XStart and roadYStart >= YStart and roadYEnd <= YEnd):
                        ss1 = [roadXEnd, roadYStart]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.2.2")                                                       
                    elif(roadYStart == YEnd and roadXStart >= XStart and roadXEnd <= XEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, roadYStart]
                        print("случай 6.2.3") 
                    elif(roadYEnd == YStart and roadXStart >= XStart and roadXEnd <= XEnd):
                        ss1 = [roadXStart, roadYEnd]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.2.4") 


                    elif(roadXStart == XStart and roadYStart == YStart and roadXEnd == XEnd and roadYEnd == YEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.3.1") 
                    elif(roadXStart == XStart and roadXEnd == XEnd and roadYStart >= YStart and roadYEnd <= YEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.3.2") 
                    elif(roadYStart == YStart and roadYEnd == YEnd and roadXStart >= XStart and roadXEnd <= XEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.3.3")
                    elif(roadXStart == XStart and roadYStart == YStart and roadYEnd > YEnd and roadXEnd > XEnd):
                        ss1 = [roadXStart, YEnd]
                        ss2 = [XEnd, roadYStart]
                        print("случай 6.3.4") 
                    elif(roadYStart == YStart and roadXEnd == XEnd and roadXStart < XStart and roadYEnd > YEnd):
                        ss1 = [XStart, roadYStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 6.3.5")
                    elif(roadXEnd == XEnd and roadYEnd == YEnd and roadYStart < YStart and roadXStart < XStart):
                        ss1 = [XStart, roadYEnd]
                        ss2 = [roadXEnd, YStart]
                        print("случай 6.3.6") 
                    elif(roadXStart == XStart and roadYEnd == YEnd and roadXEnd > XEnd and roadYStart < YStart):
                        ss1 = [XStart, YStart]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.3.7")
                    

                    elif(roadXStart == XStart and roadYStart >= YStart and roadYEnd <= YEnd and roadXEnd > XEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [XEnd, roadYEnd]
                        print("случай 6.4.1") 
                    elif(roadYStart == YStart and roadXStart >= XStart and roadXEnd <= XEnd and roadYEnd > YEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 6.4.2")
                    elif(roadXEnd == XEnd and roadYStart >= YStart and roadYEnd <= YEnd and roadXStart <= XStart):
                        ss1 = [roadXEnd, roadYEnd]
                        ss2 = [XStart, roadYStart]
                        print("случай 6.4.3") 
                    elif(roadYEnd == YEnd and roadXStart >= XStart and roadXEnd <= XEnd and roadYStart <= YStart):
                        ss1 = [roadXEnd, roadYEnd]
                        ss2 = [roadXStart, YStart]
                        print("случай 6.4.4")



                    if(roadXStart == XEnd and roadYStart > YStart and roadYEnd > YEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [XEnd, YEnd]
                        print("случай 6.5.1") 
                    elif(roadXStart == XEnd and roadYStart < YStart and roadYEnd < YEnd):
                        ss1 = [roadXStart, YStart]
                        ss2 = [XEnd, roadYEnd]
                        print("случай 6.5.2")                                                                   
                    elif(roadXEnd == XStart and roadYStart > YStart and roadYEnd > YEnd):
                        ss1 = [XStart, roadYStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 6.5.3")
                    elif(roadXEnd == XEnd and roadYStart < YStart and roadYEnd < YEnd):
                        ss1 = [roadXEnd, YStart]
                        ss2 = [XStart, roadYEnd]
                        print("случай 6.5.4") 
                    elif(roadYStart == YStart and roadXStart > XStart and roadXEnd < XEnd):
                        ss1 = [roadXStart, roadYStart]
                        ss2 = [roadXEnd, roadYStart]
                        print("случай 6.5.5") 
                    elif(roadYStart == YEnd and roadXStart < XStart and roadXEnd < XEnd):
                        ss1 = [XStart, roadYStart]
                        ss2 = [roadXEnd, YEnd]
                        print("случай 6.5.6") 
                    elif(roadYEnd == YStart and roadXStart > XStart and roadXEnd > XEnd):
                        ss1 = [roadXStart, YStart]
                        ss2 = [XEnd, YStart]
                        print("случай 6.5.7") 
                    elif(roadYEnd == YStart and roadXStart < XStart and roadXEnd < XEnd):
                        ss1 = [XStart, YStart]
                        ss2 = [roadXEnd, roadYEnd]
                        print("случай 6.5.8")



                r = math.sqrt((ss2[0]-ss1[0])**2 + (ss2[1]-ss1[1])**2)
                if(r > MaX):
                    MaX = r
                    arrMaX1 = ss1
                    arrMaX2 = ss2
    
    coordPlane.create_line(arrMaX1[0], arrMaX1[1], arrMaX2[0],
    arrMaX2[1], fill='purple', width = 6)   
                


window = Tk()
window.title("Task 12")
window.geometry("1920x1080")

coordPlane = Canvas(window, width=880, height=860, bg='#FAE7B5')
coordPlane.place(x = 960, y = 80)
createCoordAxes()




inputMethod = Label(text='Выберите способ ввода:', font='Arial 16')

var = IntVar()
var.set(3)
rad0 = Radiobutton(window, text="Файлом", variable=var, 
font='Arial 14', value=1)                                                   
rad1 = Radiobutton(window, text="На плоскости", variable=var, 
font='Arial 14', value=2)
rad2 = Radiobutton(window, text="С клавиатуры", variable=var, 
font='Arial 14', value=3)

fb = Button(text = 'Применить', font='Arial 14',
    width = 10, bg='#B2EC5D', command = fb_was_clicked)

startText = Label(text = "Введите количество прямоугольников",
    font='Arial 16')
confirmBtn = Button(text = 'Применить', font='Arial 14',
    width = 20, bg='#C018FF', command  =confirmBtn_was_clicked)

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

confirmBtn2 = Button(text = 'Применить', font='Arial 14',
    width = 20, bg='#76EA9F', command = confirmBtn2_was_clicked)           
    
randButton = Button(text = 'Использовать рандом', font='Arial 14',
    width = 30, bg='#7FFF00', command = randButton_was_clicked)

var1 = IntVar()
var1.set(1)
rad10 = Radiobutton(window, text="Числа до 10", variable = var1, 
font='Arial 14', value=1)          
rad11 = Radiobutton(window, text="Числа до 50", variable = var1, 
font='Arial 14', value=2)
rad12 = Radiobutton(window, text="Числа до 100", variable = var1, 
font='Arial 14', value=3)


understandOurWay()

window.mainloop()