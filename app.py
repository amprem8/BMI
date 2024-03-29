from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi*10000

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        interpretation = interpret_bmi(bmi)
        return render_template('result.html', bmi=bmi, interpretation=interpretation)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
