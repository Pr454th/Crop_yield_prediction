# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:12:23 2023

@author: Arunagiri.S.S
"""

from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'C:/Users/Arunagiri.S.S/Desktop/Notes/sem 6/DA and CC lab/flask/model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
   a = request.form["rain"]
   b = request.form["pest"]
   c = request.form["temp"]
   Cassava        = [1,0,0,0,0,0,0,0]             
   Maize          = [0,1,0,0,0,0,0,0]                       
   Potatoes       = [0,0,1,0,0,0,0,0]                 
   Rice_paddy     = [0,0,0,1,0,0,0,0]               
   Sorghum        = [0,0,0,0,1,0,0,0]                     
   Soybeans       = [0,0,0,0,0,1,0,0]             
   Sweet_potatoes = [0,0,0,0,0,0,1,0]             
   Wheat          = [0,0,0,0,0,0,0,1] 
   inp=[int(a),int(b),int(c)]
   ar=[]
   ar.append(inp+Cassava)
   ar.append(inp+Maize)
   ar.append(inp+Potatoes)
   ar.append(inp+Rice_paddy)
   ar.append(inp+Sorghum)
   ar.append(inp+Soybeans)
   ar.append(inp+Sweet_potatoes)
   ar.append(inp+Wheat)
  
   target=ar
   output= model.predict(target)
   outputt1= str(output[0])
   outputt2= str(output[1])
   outputt3= str(output[2])
   outputt4= str(output[3])
   outputt5= str(output[4])
   outputt6= str(output[5])
   outputt7= str(output[6])
   outputt8= str(output[7])
   
   index=output.argmax()
   if(index==0):
    outputt= "Cassava is the recommended crop"
   elif(index==1):
    outputt= "Maize is the recommended crop"    
   elif(index==2):
    outputt= "Potatoes is the recommended crop"   
   elif(index==3):
    outputt= "Rice paddy is the recommended crop"  
   elif(index==4):
    outputt= "Sorghum is the recommended crop"  
   elif(index==5):
    outputt= "Soybeans is the recommended crop" 
   elif(index==6):
    outputt= "Sweet_potatoes is the recommended crop"  
   elif(index==7):
    outputt= "Wheat is the recommended crop" 
   print(output)  
        
   return render_template("result.html",aa=outputt1 ,bb=outputt2 ,cc=outputt3 ,dd=outputt4, ee=outputt5, ff=outputt6, gg=outputt7 ,hh=outputt8 ,z = outputt )

@app.route('/admin')#binds to an url
def admin():
    return "done"

if __name__ == '__main__' :
    app.run(debug= False,port=8080)