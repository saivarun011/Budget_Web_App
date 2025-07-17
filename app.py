from flask import Flask, render_template, request, redirect, url_for
import datetime # To get the current date

app = Flask(__name__)

# --- Flask Configuration ---
# Secret key is needed for session management and form security
app.config['SECRET_KEY'] = 'your_super_secret_key_here' # **CHANGE THIS IN PRODUCTION**

# --- GLOBAL VARIABLES FOR TEMPORARY DATA STORAGE ---
expenses = []
# Structure for each expense: {'id': 1, 'amount': 50.0, 'category': 'Food', 'description': 'Lunch', 'date': '2023-10-27', 'type': 'expense'}
next_id = 1

incomes = []
# Structure for each income: {'id': 1, 'amount': 1000.0, 'source': 'Salary', 'description': 'Monthly Paycheck', 'date': '2023-10-27', 'type': 'income'}
next_income_id = 1
# ----------------------------------------------------

@app.route('/')
def home():
    # Render the index.html template and pass the expenses list to it
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        global next_id # Indicate we are modifying the global next_id
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = request.form['date'] # Get date from form

        # If no date provided, use today's date
        if not date:
            date = datetime.date.today().strftime('%Y-%m-%d')

        new_expense = {
            'id': next_id,
            'amount': amount,
            'category': category,
            'description': description,
            'date': date,
            'type': 'expense'
        }
        expenses.append(new_expense)
        next_id += 1 # Increment for the next expense

        return redirect(url_for('home')) # Redirect back to home after adding
    
    # For GET request, simply render the add_expense form
    return render_template('add_expense.html')

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        global next_income_id # Indicate we are modifying the global next_income_id
        amount = float(request.form['amount'])
        source = request.form['source']
        description = request.form.get('description', '') # Optional field
        date = request.form['date']

        if not date:
            date = datetime.date.today().strftime('%Y-%m-%d')

        new_income = {
            'id': next_income_id,
            'amount': amount,
            'source': source,
            'description': description,
            'date': date,
            'type': 'income' # Add a type for transactions page
        }
        incomes.append(new_income)
        next_income_id += 1

        return redirect(url_for('home')) # Redirect back to home or transactions
    
    # For GET request, simply render the add_income form
    return render_template('add_income.html')

@app.route('/transactions')
def view_transactions():
    all_transactions = []
    # Ensure 'type' is added to expenses when combining
    for exp in expenses:
        all_transactions.append({**exp, 'type': 'expense'}) 
    for inc in incomes:
        all_transactions.append({**inc, 'type': 'income'})

    # Sort transactions by date (most recent first)
    all_transactions.sort(key=lambda x: x['date'], reverse=True)

    return render_template('transactions.html', transactions=all_transactions)

@app.route('/summary')
def summary():
    total_income = sum(item['amount'] for item in incomes)
    total_expenses = sum(item['amount'] for item in expenses)
    net_balance = total_income - total_expenses

    return render_template('summary.html',
                           total_income=total_income,
                           total_expenses=total_expenses,
                           net_balance=net_balance)


if __name__ == '__main__':
    app.run(debug=True)