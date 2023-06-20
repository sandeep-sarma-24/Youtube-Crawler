from flask import Flask, render_template, request
from scraper import scrape_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    limit = int(request.form.get('limit'))  # Get the limit from the form
    proxies_to_use = int(request.form.get('proxies'))  # Get the number of proxies to use
    search_query = request.form.get('query')  # Get the search query
    data = scrape_data(limit, proxies_to_use, search_query)  # Pass the variables to the scrape function
    return render_template('results.html', results=data)

if __name__ == "__main__":
    app.run(debug=True)
