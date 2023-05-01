from flask import Flask, escape, render_template, request
from pydantic import BaseModel, validator, ValidationError

class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()

app = Flask(__name__)

#Flask Routing
#@app.route('/')
#def index():
#    return 'Hello World!'

#@app.route('/about')
#def about():
#    return '<h2>About this application...</h2>'

@app.route('/stocks/')
def stocks():
    return '<h2>Stock List...</h2>'

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'

#@app.route('/example', methods=['GET', 'POST'])
#def example():
#    return 'an example'

#----------------------------------------------------------------------------
#Template Engines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', company_name='TestDriven.io')
#    return render_template('about.html')

#----------------------------------------------------------------------------
#Forms

#@app.route('/add_stock')
#def add_stock():
#    return render_template('add_stock.html')


#@app.route('/add_stock', methods=['GET', 'POST'])
#def add_stock():
#    if request.method == 'POST':
#        # Print the form data to the console
#        for key, value in request.form.items():
#            print(f'{key}: {value}')
#
#    return render_template('add_stock.html')

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)
        except ValidationError as e:
            print(e)

        return render_template('add_stock.html')