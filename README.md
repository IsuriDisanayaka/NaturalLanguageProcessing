# NaturalLanguageProcessing
This is a Flask-based web application for text classification. The application uses a pre-trained Random Forest model to classify text as either a disaster or not a disaster.
![image](https://github.com/IsuriDisanayaka/NaturalLanguageProcessing/assets/73772718/0a446bed-2074-4a33-9a30-9e0a12e3ab81)

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.11
- Flask (You can install it using `pip install flask`)
- Other required Python packages (See [requirements.txt](requirements.txt))

### Installation

1. Clone this repository:

   ```bash
   git clone git@github.com:IsuriDisanayaka/NaturalLanguageProcessing.git
2. Navigate to the project directory:

3. cd NaturalLanguageProcessing
    
4. Install the required Python packages:  
  pip install -r requirements.txt

5. Running the Application
To run the Flask application locally, use the following command:
   python app.py
*The application will be accessible at http://localhost:5000 in your web browser.

###Usage
Enter text in the text area on the web page.
Click the "Predict" button.

The application will classify the text as either a "Disaster" or "Not a Disaster" and display the result.

###Files in the Repository*
app.py: The Flask web application.
random_forest_model.pkl: The trained Random Forest model.
tfidf_vectorizer.pkl: The TF-IDF vectorizer.
templates/: Contains the HTML template files.

#Contributing*

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and commit them to your branch.
Push your branch to your fork.
Submit a pull request to the main repository.
Please ensure that your code follows the project's coding standards and includes appropriate documentation.

License
This project is licensed under the MIT License.




