import psutil
from flask import Flask, render_template

app = Flask(__name__)
# path of application where it is goig to run "/" says home path

@app.route("/")
#creating a function to route if the user come at this home path 
def index():
    cpu_percent = psutil.cpu_percent()  # holds the cpu utilization value in variable cpu percent 
    mem_percent = psutil.virtual_memory().percent # we gonna getr memory usage in form percent as . percent is mentioned
    Message = None
    # we gonna create a condition like if memory/cpu is high, message that scaleup memory and cpu 
    if mem_percent>80 or cpu_percent>80:
        Message= "High CPU or Memory Percentage detected, Please scale up"
    return render_template("index.html",cpu_metric=cpu_percent,mem_metric=mem_percent,message=Message)
    
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')