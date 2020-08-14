# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:19:23 2017

@author: Gabriel PC
"""

import qtpy.QtGui as gui
import qtpy.QtWidgets as wid
import sys
import numpy as np
import TrabajoHitoFina as t

def exist(ar,val): #Detect if X value already exist
    answer = False
    size = np.size(ar,0)
    for i in range(0,size):
        if ar[i][0] == val:
            answer = True
    return answer

def window():
    # Variables
    
    app 	= wid.QApplication(sys.argv)
    tabs	= wid.QTabWidget()
    
    # Create tabs
    tab1	= wid.QWidget()	
    tab2	= wid.QWidget()
    tab4	= wid.QWidget()
    
    tabs.resize(1200, 800)
    
    #Primera Tab
    tab_1 = wid.QVBoxLayout()
    licence = ( "Trabajo de Procesamiento de Imagenes" +
              " \n Reconocimiento Simple de notas"+
              "\n \n Alumnos: \n" +
              "Gabriel Ramirez Reategui \n" +
              "Carlos Guizado Diaz \n" 
              )
    text0 = wid.QLabel(licence)
    text0.setWordWrap(True)
    tab_1.addWidget(text0)
    tab1.setLayout(tab_1)
    
    
    #Segunda Tab
    tab_2	= wid.QGridLayout()
    #textbox
    lx = wid.QLabel()
    lx.setText("Nombre del archivo:")
    tb = wid.QLineEdit()
    tab_2.addWidget(tb,0,4)
    def run():
        #t.demo(lx.text)
        t.demo(tb.text())
        msg = wid.QMessageBox()
        msg.setIcon(wid.QMessageBox.Information)
        msg.setText("Proceso terminado! ")
        msg.setWindowTitle("Resultado")
        msg.exec_()
        pass
    
    
    pushButton1 = wid.QPushButton("Crear MIDI")
    pushButton1.clicked.connect(run)
    tab_2.addWidget(lx,0,3)
    tab_2.addWidget(pushButton1,4,5)
    
    
    
    tab2.setLayout(tab_2)
    
   
    
    
    #Cuarta Tab
    
    tab_4 = wid.QVBoxLayout()
    licence = ( "El sistema experto asi como el codigo del mismo se libera bajo la licencia de codigo Abierto para cualquier persona pueda leer, modificar y reutilizar el codigo" +
              " \n Este software fue desarrollado en conjunto por los alumnos de la universidad de ciencias aplicadas"+
              " para el curso de Procesamiento de Imagenes de la carrera de Ciencias de la Computacion" +
              "\n \n Alumnos: \n" +
              "Gabriel Ramirez Reategui \n" +
              "Carlos Guizado Diaz \n"
              )
    text1 = wid.QLabel(licence)
    text1.setWordWrap(True)
    tab_4.addWidget(text1)
    tab4.setLayout(tab_4)
    
    
    ## information
    l1 = wid.QLabel()
    l1.setText("Entrar a la tabla Programa, seleccionar sintomas y hacer clic en S.E para probar, no olvidar poner direccion")
    l1.setGeometry(200, 200, 600, 600)
    tab_1.addWidget(l1)
    tab1.setLayout(tab_1)   
    # Add tabs
    tabs.addTab(tab1,"Introduccion")
    tabs.addTab(tab2,"Programa")
    tabs.addTab(tab4,"licencia") 
    
    
 
    # Titulos e informacion
    tabs.setWindowTitle('Trabajo de Procesamiento de Imagenes: Reconocimiento de notas')
    tabs.show()
    sys.exit(app.exec_())

"""    
    data = []
    txt = ""
    app = wid.QApplication(sys.argv)
    w = wid.QWidget()
    w.setGeometry(200, 200, 600, 600)
    w.setWindowTitle("Trabajo de Inteligencia Artificial 2")
    # Labels and text

    #Message box
    

    # Title
    l = wid.QLabel(w)
    l.setText("Trabajo de Algebra Lineal!")
    l.move(170, 50)
    l.setFont(gui.QFont('SansSerif', 20))

    # information
    l1 = wid.QLabel(w)
    l1.setText("Agrega la cantidad de puntos hasta que desee generar el spline")
    l1.move(30, 100)

    # Textbox
    lx = wid.QLabel(w)
    lx.setText("Inserte valor en X: ")
    lx.move(10, 120)
    tx = wid.QLineEdit(w)
    tx.setGeometry(130, 115, 50, 20)

    ly = wid.QLabel(w)
    ly.setText("Inserte valor en Y: ")
    ly.move(10, 150)
    ty = wid.QLineEdit(w)
    ty.setGeometry(130, 145, 50, 20)


    # Functions to add
    def fill():
      
        pass
    labels =wid.QLabel(w)
    labels.setGeometry(30, 130, 600, 300)

        # Boton 1
    def clear():
        print("working")
        
    bta = []
    bta.append(wid.QPushButton(w))
    bta[0].setText("agregar valor!")
    bta[0].move(200, 140)
    bta[0].clicked.connect(fill)
    
    #btn 2
    bta.append(wid.QPushButton(w))
    bta[1].setText("Generar Spline!")
    bta[1].move(300, 140)

    bta.append(wid.QPushButton(w))
    bta[2].setText("Limpiar valores")
    bta[2].move(400, 140)
    bta[2].clicked.connect(clear)
    
    w.show()

"""
   

if __name__ == '__main__':
    window()