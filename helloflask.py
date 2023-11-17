#helloworld

from flask import Flask
from flask import render_template
import csv
import json

apphello = Flask(__name__)

@apphello.route("/")
def hello_world():
    return render_template('welcome.html')

@apphello.route("/alpro/")
def helloalpro():
    return "<h2>Agoritma Pemrograman</h2>"

@apphello.route('/initempl/')
@apphello.route('/initempl/<name>')
def templaterun(name=None):
    return render_template('templ.html', name=name)

@apphello.route('/cv')
def cv():
    return render_template('cvmeri.html')

@apphello.route('/portofolio')
def port():
    return render_template('porto.html')

@apphello.route('/fibonacci', methods=['GET', 'POST'])
def fibo():
    if request.method == 'POST':
        # Ambil nilai input dari formulir
        length = int(request.form['length'])
        # Hitung deret Fibonacci
        fibonacci_sequence = generate_fibonacci(length)
        return render_template('fibo.html', length=length, sequence=fibonacci_sequence)
    return render_template('fiboInput.html')

def generate_fibonacci(length):
    # Fungsi untuk menghasilkan deret Fibonacci
    sequence = [1, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


@apphello.route('/csv_to_json')
def csv_to_json():
    csv_data = []
    with open('data_titanic.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_data.append(row)
    return json.dumps(csv_data)

from flask import request

@apphello.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        submitted_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'age': request.form['age']
            # tambahkan field lainnya sesuai kebutuhan
        }
        return render_template('submitted.html', data=submitted_data)
    return render_template('form.html')

@apphello.route('/biodata')
def bio():
    return render_template('biodata.html')

@apphello.route('/kalkulator')
def kalku():
    return render_template('kalkulator.html')

@apphello.route('/reverse')
def reverse():
    return render_template('reverse.html')
