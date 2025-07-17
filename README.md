# Budget Web App

## Project Overview
A simple web application built with Flask to help manage personal income and expenses. Users can add new expenses and incomes, view all transactions, and see a financial summary.

## Features
* Add new expenses with amount, category, description, and date.
* Add new incomes with amount, source (dropdown), description, and date.
* View all transactions (both expenses and incomes) in a single list.
* See a financial summary including total income, total expenses, and net balance.
* Data is stored in-memory for the current session (resets on server restart).

## Technologies Used
* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS

## Setup and Running the Application

### Prerequisites
* Python 3.7+ installed
* Git installed

### Installation Steps

1.  **Clone the repository (if you're not already in the project folder):**
    ```bash
    git clone [https://github.com/saivarun011/Budget_Web_App.git](https://github.com/saivarun011/Budget_Web_App.git)
    cd Budget_Web_App
    ```
    *(Note: Replace `saivarun011` with your actual GitHub username if different)*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install Flask
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

### Accessing the Application
Open your web browser and navigate to:
`http://127.0.0.1:5000`

## Project Structure
---

**Steps to update your `README.md`:**

1.  **Open your `README.md` file** in your text editor.
2.  **Locate the `## Project Structure` heading.**
3.  **Paste the code block above** (including the `Budget_Web_App/` line and all subsequent lines) directly below that heading.
4.  **Save the `README.md` file.**

After saving, remember to **add, commit, and push** this change to your GitHub repository so it updates online:

```bash
git add README.md
git commit -m "Update README: Add project structure section"
git push origin master # Or 'git push origin main' if your branch is main