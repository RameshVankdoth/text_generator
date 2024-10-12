# GenInsights

GenInsights is a web application that provides text summarization and text generation features using advanced natural language processing models. Built with Flask and leveraging the power of the Facebook BART model, GenInsights aims to help users quickly distill information and generate relevant content based on keywords.

## Features

- **Text Summarization**: Summarize long pieces of text into concise summaries.
- **Text Generation**: Generate content based on a given keyword.
- **User Authentication**: Simple login and registration functionalities.

## Technology Stack

- **Flask**: Web framework for Python.
- **TensorFlow**: Used for loading and running the BART model.
- **Transformers**: Hugging Face library for state-of-the-art NLP models.
- **HTML/CSS**: For front-end rendering.

## Installation

### Prerequisites

Make sure you have Python installed (version 3.6 or higher). It's also recommended to use a virtual environment.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/geninsights.git
   cd geninsights
   ```
Install the required packages:

```bash
pip install -r requirements.txt
```
Download the necessary models. The application uses pre-trained models from Hugging Face.

Run the application:

```bash
python app.py
```
Open your web browser and navigate to http://127.0.0.1:5000.

Usage
Summarization:

Navigate to the summarization page.
Input the text you want to summarize and submit the form.
The summary will be generated and displayed.
Text Generation:

Navigate to the text generation page.
Input a keyword related to the content you want to generate and submit the form.
Generated content will be displayed based on the keyword.
Authentication:

Use the login and registration pages to create and manage user accounts.
Configuration
Modify the app.py file to adjust logging levels, model configurations, or Flask settings as needed.

Logging
The application uses the logging library for tracking events and errors. Logs are displayed in the console by default.

Contributing
Contributions are welcome! Please create a pull request or open an issue for any suggestions or improvements.

Acknowledgments
Hugging Face for the Transformers library.
TensorFlow team for the deep learning framework.
Flask for the web framework.

Feel free to adjust any sections to better fit your application's specifics!
