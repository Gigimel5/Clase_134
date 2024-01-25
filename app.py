from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtener el texto ingresado del requerimiento POST.
    input_text=request.json.get("text")
    
    if not input_text:
        # Respuesta para enviar si input_text está indefinido.
        response={"status":"error","message":"Ingresa un texto"}
        return jsonify(response)
    else:
        emotion,emoticon=predict(input_text)
        response={"status":"success","data":{"emotion":emotion,"emoticon":emoticon}}
        return jsonify(response)
        
        # Respuesta para enviar si input_text no está indefinido.
        
        # Enviar respuesta.         
        
       
app.run(debug=True)



    