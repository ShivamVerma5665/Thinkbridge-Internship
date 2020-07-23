from flask import Flask, redirect, url_for, request, render_template, flash
from form import CurrencyForm
from currency_to_words import curConvert_English, curConvert_Hindi, curConvert_Marathi
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['POST', 'GET'])
def calc():
    form = CurrencyForm()
    try:
        if request.method == "POST" and form.validate():
            currency_inp = str(form.curInput.data)
            num,frac= map(int, currency_inp.split('.'))
            language = form.lang.data
            if language == 'hindi':
                result = (currency_inp + ' - ' + str(curConvert_Hindi(num)) + ' ' + str(frac) +"/100")
                return render_template("homepage.html", form = form, result = result)
            elif language == 'marathi':
                result = (currency_inp + ' - ' + str(curConvert_Marathi(num)) + ' ' + str(frac) +"/100") 
                return render_template("homepage.html", form = form, result = result)  
            else:   
                result = (currency_inp + ' - ' + str(curConvert_English(num)) + ' ' + str(frac) +"/100")
                return render_template("homepage.html", form = form, result = result)
        else:
            flash("All fields are required*")
            return render_template("homepage.html", form=form)
    except Exception as e:
        return(str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)   