from flask import Flask, request, render_template_string, url_for
import json
import os

app = Flask(__name__)

# HTML form template
form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chi Epsilon Newsletter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}"> 
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto&display=swap">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/38d647a2f9.js" crossorigin="anonymous"></script>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <main class="centered-container">
        <div class="content">
            <h1>Subscribe To Our Newsletter!</h1>
            <h3>Stay updated on what Chi Epsilon is up to and find out ways you can get engaged as well.</h3>
            <form action="/submit" method="post">
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp" required="true">
                </div>
                <br>
                <button type="submit" class="btn btn-primary btn-round">Subscribe!</button>
            </form>
            
            <div class="social-media">
                <h3>Don't Forget To Follow Us On Social Media!</h3>
                <a href="https://www.instagram.com/ptkchiepsilon21/" class="fa-brands fa-instagram" aria-label="Instagram"></a>
                <a href="https://www.facebook.com/groups/352106216853" class="fa-brands fa-facebook-f" aria-label="Facebook"></a> 
            </div>
        </div>
    </main>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    file_path = 'emails.json'
    
    # Initialize emails list
    emails = []
    
    # Read the file
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                emails = json.load(f)
        except json.JSONDecodeError:
            # Handle case where JSON is invalid
            emails = []
        except Exception as e:
            return f"An error occurred while reading the file: {e}"
    
    # Check if the email is already subscribed
    if email not in emails:
        emails.append(email)
        try:
            with open(file_path, 'w') as f:
                json.dump(emails, f)
        except Exception as e:
            return f"An error occurred while writing to the file: {e}"
        return "Thank you for subscribing!"
    else:
        return "This email is already subscribed!"

if __name__ == '__main__':
    app.run(debug=True)
