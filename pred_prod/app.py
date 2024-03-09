from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/product_list', methods=['POST'])
def product_list():
    product_name = request.form['product_name']
    product_address = request.form['product_address']
    product_price = request.form['product_price']
    product_description = request.form['product_description']

    # Здесь вы можете сохранить данные в базу данных или выполнить другие действия

    return render_template('product_list.html', product_name=product_name, product_address=product_address, product_price=product_price, product_description=product_description)

# ... (ваш существующий код)

@app.route('/pay')
def pay():
    # Здесь вы можете добавить код для обработки страницы оплаты
    return render_template('pay.html')

# ... (ваш существующий код)

if __name__ == '__main__':
    app.run(debug=True)

