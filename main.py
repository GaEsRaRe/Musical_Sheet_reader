# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
import functions as f

import sys
sys.path.append('MIDI/src/midiutil')

from MidiFile3 import MIDIFile


tabla_sol = [77,76,74,72,71,69,67,65,64,62,60,59,57,55,53,52,50]
kernel = np.ones((2,2),np.uint8)
MyMIDI = MIDIFile(1)

def line_separator(img,color):
    sx,sy = np.size(img,0),np.size(img,1)
    c = 0
    ca =[]
    for i in range(0,sx):
        temp = False
        for j in range(0,sy):
            if(img[i][j] != color):
                temp = True
        if temp == True:
            c = c+1
        elif(c != 0):
            ca.append([c,i-c,i])
            c = 0
    return ca


def ar_line_separator(ar,color):
    ans = []
    for i in range(0,len(ar)):
        ans.append(line_separator(ar[i],255))
    return ans
    

def separator_blocks(img,cord):
    images = []
    for i in range(0,np.size(cord,0)):
        #For each one
        csize = cord[i][0] 
        sy = np.size(img,1)
        cstart = cord[i][1]
        temp = np.zeros([csize,sy],dtype=np.uint8)
        for n in range(0,csize):
            for m in range(0,sy):
                temp[n][m] = img[n + cstart][m]
        temp = agrandar(temp,30,30)
        images.append(temp)
    return images


def ar_separator_blocks(ar,cords):
    ans = []
    for i in range(0,len(ar)):
        ans.append(separator_blocks(ar[i],cords[i]))
    
    return ans
def EliminateLines(img):
    im = np.copy(img)
    sx = int(im.shape[0])
    sy = int(im.shape[1])
    #Another Tresshold
    for i in range(0,sx):
        for j in range(0,sy):
            if(im[i][j]>=210):
                im[i][j] = 255
            else:
                im[i][j] = 0
    im = ~im
    imgFinal = np.copy(im)
    (rows, cols) = im.shape
    estructura = np.array([[1], 
              [1],
             [1]])
    #Falta por convertir a manual
    imgFinal = cv2.erode(imgFinal, estructura, iterations = 1);
    imgFinal = cv2.dilate(imgFinal, estructura, iterations = 1);
    imgFinal = cv2.bitwise_not(imgFinal)
    return imgFinal




"""
test = f.loadimg("test.png")
f.show(test)
test = f.to_grey(test)
test = cv2.adaptiveThreshold(test,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
f.saveimg(test)
data = line_separator(test)
result = separator_blocks(test,data)
#mg(test)
"""
#Demo1
#Demo


def get_body(image):
    gray = cv2.medianBlur(image, 5)
    dst2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return dst2

def transpose_all(ar):
    for i in range(0,np.size(ar,0)):
        ar[i] = cv2.transpose(ar[i])
    
    return ar


def transponse_arr_all(ar):
    for i in range(0,len(ar)):
        ar[i]= transpose_all(ar[i])
    return ar



#test = f.tresshold(test,100)

#test = cv2.adaptiveThreshold(test,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)

"""
test = f.loadimg("test2.jpg")
test = f.to_grey(test)
f.saveimg(test,"imagen.png")
f.show(test)

clear = EliminateLines(test)
clear = f.tresshold(clear,50)
data = line_separator(test,255)

result_1 = separator_blocks(clear,data)
result_2 = transpose_all(result_1)
result_3 = ar_line_separator(result_2,255)
result_4 = ar_separator_blocks(result_2,result_3)
result_5 = transponse_arr_all(result_4)
"""


def agrandar(image,pixeles,n):
    sx,sy = np.size(image,0), np.size(image,1)
    img = np.ones([ sx+ pixeles + n,sy + pixeles + n],dtype = np.uint8) * 255
    for i in range(0,sx):
        for j in range(0,sy):
            img[i + 1][j + 1] = image[i][j]            
    return img
    

def show_circles(image):
    img = np.copy(image)
    img = f.tresshold(img,200)
    #img = cv2.resize(img,[np.size(img,0)*2,np.size(img,1)*2])
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1,param1=1,param2=7,minRadius=1,maxRadius=40)
    circles = np.uint8(np.around(circles))
    for i in circles[0,:]:   
       
       cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3,0)
    f.showc(cimg)
    pass
    

def delete_borders(image):
    data = line_separator(np.transpose(agrandar(image,2,2)),255)
    data = data[0]
    new_image = np.ones([np.size(image,0),data[0]],dtype = np.uint8) * 255
    for i in range(0,np.size(image,0)):
        for j in  range(0,data[0]):
            new_image[i][j] = image[i][j+data[1]]
    return new_image

def fcorchea(image):
    e = False
    total = 0
    image = agrandar(image,2,2)
    image = cv2.dilate(image,kernel)
    image = delete_borders(image)
    l1,l2,l3,l4 = 0,0,0,0
    sx, sy = np.size(image,0), np.size(image,1)
    for i in range(0,int(sx/2)):
        for j in range(0,int(sy/2)):
            if(image[i][j] < 10):
                l1 = l1 + 1
        for j in range(int(sy/2),sy):
            if(image[i][j] < 10):
                l2 = l2 + 1
    for i in range(int(sx/2),sx):
        for j in range(0,int(sy/2)):
            if(image[i][j] < 10):
                l3 = l3 + 1
                image[i][j] = 0
        for j in range(int(sy/2),sy):
            if(image[i][j] < 10):
                l4 = l4 + 1
    

    answe = [l1,l2,l3,l4]
    total = l1 + l2 + l3 + l4
    answe = np.sort(answe)
    sup = answe[3]
    inf = answe[0]
    if(answe[0] < 5):
        sup = answe[3]
        inf = answe[1]
        med = answe[2]
        val = sup/max(1,inf)
        if(val > 3):
            e = True
    elif((inf/sup)<1.3 and (inf/sup)>0.8):
        e = False
    if(answe[1] <5):
        e = False
    return e




def Erosion(im,pixel,mascara):
    val = False
    for i in range(0,1):
        for j in range(0,mascara.shape[0]):
            if im[pixel[0]+i][pixel[1]+j]==mascara[j]:
                val = True
            else:
                val = False
                break
        if(val == False):
            break
    if(val == False):
        im[pixel[0]][pixel[1]] = 255

def Dilatacion(im,pixel,mascara):
    for i in range(0,1):
        for j in range(0,mascara.shape[0]):
            im[pixel[0]+i][pixel[1]+j]=mascara[j]

def BorrarLineas(img, mascara):
    im = np.copy(img)
    sx = int(im.shape[0])
    sy = int(im.shape[1])
    for i in range(0,sx):
        for j in range(0,sy):
            if(im[i][j]>=210):
                im[i][j] = 255
            else:
                im[i][j] = 0
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            if(im[i][j]==0 and i+4<=im.shape[0] and j+4<=im.shape[1]):
                pixel = [i,j]
                Erosion(im,pixel,mascara)

    im2 = np.copy(im)
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            if(im2[i][j]==0 and i+4<=im.shape[0] and j+4<=im.shape[1]):
                pixel = [i,j]
                Dilatacion(im,pixel,mascara)
    return im

def eliminar_repetidas(arr):
    ans = np.copy(arr)
    to_delete = []
    rango = 3
    sz = np.size(arr,0)
    for i in range(sz):
        for n in range(i + 1,sz):
            a = abs(arr[i][0] - arr[n][0])
            b = abs(arr[i][1] - arr[n][1])
            if((a < rango) and (b < rango)):
                to_delete.append(n)
    to_delete = np.unique(to_delete)
    ans= np.delete(arr,to_delete,0)
    return ans

def templates(imag, templ, templPos, tipo):
    imagen_gray = f.to_grey(imag)
    w, h = templ.shape[::-1]
    res = cv2.matchTemplate(imagen_gray, templ ,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imag, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        temp = [pt[0],pt[1],tipo,w,h] #1 es cambiado por tipo
        templPos.append(temp)
    
    return imag, templPos

def ConseguirLineas(imag):
    masca = np.zeros([int(np.size(imag,1)/2)],dtype = np.uint8)
    #masca = np.array([(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)])
    imag = f.to_grey(imag)
    imag = BorrarLineas(imag,masca)
    f.saveimg(imag,"lineas.png")
    lineaPos = np.zeros([20])
    lineaCon = 0
    adi = 0
    LineasPos = []
    for i in range(0,imag.shape[0]):
        if(imag[i][100]+adi==0):
            lineaPos[lineaCon] = i
            lineaCon += 1
            adi=2
            LineasPos.append(i)
        else:
            adi=0
    
    lineaInicial = LineasPos[0]
    dist = LineasPos[1]-LineasPos[0]
    
    return lineaInicial, dist


def check_corchea(img,posx,dist):
    value = False
    sx = np.size(img,0)
    sy = int(dist)
    temp = np.ones([sx,sy],dtype = np.uint8)
    for i in range(0,sx):
        for j in range(0,sy):
            temp[i][j] = img[i][posx + j]
    temp = agrandar(temp,1,1)
    
    temp = delete_borders(temp)
    temp = np.transpose(delete_borders(np.transpose(temp)))
    value = fcorchea(temp)
    return value

def change_to_corc(arr,image,black):
    for i in range(0,np.size(arr,0)):
        if(check_corchea(image,arr[i][0],arr[i][3]*1.4)):
            arr[i][2] = 5
    pass

def decide_position(arr,lin,size):
    for i in range(0,np.size(arr,0)):
        temp = ((arr[i][1] - lin + 2))/size
        next_temp = ((arr[i][1]+arr[i][3] - lin))/size
        if(np.floor(next_temp) == np.ceil(temp)):#se le da un margen de error
            arr[i][4] = 2*(np.floor(temp)) + 1
        else:
            arr[i][4] = np.floor(temp)*2 + 2
    
    pass

def newNote(time, duration, pitch):
    track = 0
    MyMIDI.addTrackName(track,time,"Sample Track")
    MyMIDI.addTempo(track,time, 120)
    channel = 0
    volume = 100
    MyMIDI.addNote(track,channel,pitch,time,duration,volume)
    
def make_midi(arr):
    time = 0
    for i in range(1,np.size(arr,0)):
        tempo = float(arr[i][2]) / 10.0
        
        frecuencia = tabla_sol[arr[i][4]]
        newNote(time,tempo,frecuencia)
        time = time + tempo
    pass
    
def song(f_lista):
    tiempo = 0
    newNote(0,f_lista[0][1],f_lista[0][0])
    for i in range(1,len(f_lista)):
        
        newNote(tiempo,f_lista[i][1],f_lista[i][0])
        tiempo = tiempo + f_lista[i-1][1]
    pass

def get_dataset(imagen):
    linea, distancia = ConseguirLineas(imagen)
    negra = cv2.imread('templates/b1.png',0)
    blanca = cv2.imread('templates/w1.png',0)
    blanca2 = cv2.imread('templates/w2.png',0)
    sol = cv2.imread('templates/sol.png',0)
    fa = cv2.imread('templates/clavefa.jpg',0)
    redonda = cv2.imread('templates/r1.png',0)
    redonda2 = cv2.imread('templates/r2.png',0)
    tata = f.to_grey(imagen)
    tata = EliminateLines(tata)
    NegraPos = []
    BlancaPos = []
    RedondaPos = []
    SolPos = []
    FaPos = []
    
    imagen, NegraPos = templates(imagen, negra, NegraPos,10)
    imagen, BlancaPos = templates(imagen, blanca, BlancaPos,20)
    imagen, BlancaPos = templates(imagen, blanca2, BlancaPos,20)
    imagen, SolPos = templates(imagen, sol, SolPos,50)
    imagen, RedondaPos = templates(imagen, redonda, RedondaPos, 40)
    imagen, RedondaPos = templates(imagen, redonda2, RedondaPos, 40)
    imagen, FaPos = templates(imagen, fa, FaPos,60)
    
    NegraPos = eliminar_repetidas(NegraPos)
    change_to_corc(NegraPos,tata,negra)
    BlancaPos = eliminar_repetidas(BlancaPos)
    SolPos = eliminar_repetidas(SolPos)
    NegraPos = sorted(NegraPos,key=lambda order:order[0],reverse = False)
    if(np.size(SolPos,0) > 0):
        dataset = np.concatenate((SolPos,NegraPos),axis = 0)
    if(np.size(BlancaPos,0) > 0):
        dataset = np.concatenate((dataset, BlancaPos),axis=0)
    
    dataset = np.array(sorted(dataset,key=lambda order:order[0],reverse = False))
    decide_position(dataset,linea,distancia)
    return dataset



def demo():
    
    image = cv2.imread("maria.jpg")
    tata = f.to_grey(image)
    tata = EliminateLines(tata)
    f.saveimg(tata,"qw.png")
    
    
    image = f.to_grey(image)
    clear = EliminateLines(image)
    clear = f.tresshold(clear,50)
    data = line_separator(clear,255)
    result = separator_blocks(image,data)
    datasets = []
    for i in range(0,np.size(result,0)):
        result[i] = agrandar(result[i],15,15)
        datasets.append(get_dataset(result[i]))
        
    for i in range(1,np.size(datasets,0)):
        dataset = np.concatenate((datasets[i-1],datasets[i]),axis = 0)
    #dataset = get_dataset(result[1])
    make_midi(dataset)
    binfile = open("FINAL2.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
    
    cv2.imwrite('res2.png',image)

    pass

demo()