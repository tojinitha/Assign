from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods =['POST'])
def predict():
     
    
    gender = request.values.get("Gender")
    if gender == "Male":
        gen = 1
    else:
        gen = 0  

    delay = float(request.values["DepartureDelay"])
   
    network = int(request.values["Network"])
    comfort = int(request.values["Comfort"])
    service = int(request.values["Service"])
    distance = int(request.values["Flight Distance"])
    age  = int(request.values["Age"])
    customertype = request.values["customertype"]
    if customertype == "Yes":
        customer = 1
    else:
        customer = 0    
    Time_convenient  = int(request.values["Time_Convenient"])
    Legroom  = int(request.values["Leg room"])
    Checkin_service  = int(request.values["Checkin service"])

    Gate_location  = int(request.values["Gate location"])
    
  
    output = model.predict([[gen,customer,age,distance,Time_convenient,Gate_location,Legroom,Checkin_service,delay,network,comfort,service]])
    output.item() 
    
    print (output)
    
    
    print (str(output[0]))
    if(str(output[0])) == "0":
        output = 'Not Satisfied'
    else:
        output = 'Satisfied'  
    return render_template('result.html',prediction_text ="Customer is  {}" .format(output))
    
     
if __name__ == '__main__':
    app.debug = True
    app.run()
   
