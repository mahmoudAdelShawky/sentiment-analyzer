from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Set up the sentiment analysis pipeline
sent_pipeline = pipeline("sentiment-analysis")

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None  # Initialize sentiment to None
    if request.method == 'POST':
        # Get the user input from the form
        text = request.form['text']
        
        # Analyze sentiment
        sentiment = sent_pipeline(text)[0]
    
    # Render the template and pass the sentiment result (if any)
    return render_template('index.html', sentiment=sentiment, pagetitle="home page", custom_css="main")

if __name__ == '__main__':
    app.run(debug=True)
