from flask import Flask ,render_template,send_from_directory,request,redirect
import csv
app = Flask(__name__)

def write_to_database(data):
    with open('./database.txt',mode='a') as file:
        data_to_write = f' email : {data["email"]}  , message : {data["message"]} , subject : {data["subject"]}'
        file.write(data_to_write)
        file.write("\n")


def write_to_csv(data):
    with open('./database.csv',,newline="",mode='a') as file:
        # data_to_write = f'{data["email"]},{data["message"]},{data["subject"]}'
        csv_writer = csv.writer(file,delimiter="," ,quotechar="'",quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([data["email"],data["message"],data["subject"]])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong try again!'



@app.route('/')
@app.route('/index.html')
def my_home():

    return render_template('./index.html')
 


@app.route('/<page_name>')
def works(page_name):

    return render_template(page_name)



