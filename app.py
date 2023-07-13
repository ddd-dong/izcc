from flask import *
from gridfs import *
from pymongo import *
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = str(hex(random.randint(0,18446744073709551616)))
app.config['SESSION_TYPE'] = 'filesystem'

url = "mongodb+srv://naup96321:aaa@naup.xsauomk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/class')
def class_intr():
    return render_template("class.html")

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/save_data", methods=["POST"])
def save_data():
    your_email = request.values["your_email"]
    your_name = request.values["your_name"]
    your_school = request.values["your_school"]
    your_phone = request.values["your_phone"]
    your_birthday = request.values["your_birthday"]
    your_identity_card_id = request.values["your_identity_card_id"]
    parent_name = request.values["parent_name"]
    parent_phone = request.values["parent_phone"]
    parent_identity_card_id = request.values["parent_identity_card_id"]
    parent_birthday=request.values["parent_birthday"]
    parent_relation = request.values["parent_relation"]
    diet = request.values["diet"]
    epilepsy = request.values["epilepsy"]
    cloth= request.values["cloth"]
    other_require = request.values["other_require"]
    other_speak=request.values["other_speak"]
    
    
    # os.makedirs(SAVE_DIRECTORY, exist_ok=True)

    # file_path = os.path.join(SAVE_DIRECTORY, pdf_file.filename)
    # pdf_file.save(file_path)
    data = {"your_email": your_email, 
            "your_name": your_name, 
            "your_school": your_school,
            "your_phone": your_phone,
            "your_birthday": your_birthday,
            "your_identity_card_id": your_identity_card_id,
            "parent_name": parent_name,
            "parent_phone": parent_phone,
            "parent_identity_card_id": parent_identity_card_id,
            "parent_birthday":parent_birthday,
            "parent_relation": parent_relation,
            "diet": diet,
            "epilepsy": epilepsy,
            "cloth":cloth,
            "other_require" :other_require,
            "other_speak":other_speak
    
            }
    client.save_summer_form.summer_form_data.insert_one(data)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port="8080",host='0.0.0.0',debug=True) #
