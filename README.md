# AI-Agent-Project-by-Aman

Here’s a detailed explanation of each point included in README file for better understanding:

### Technologies Used:

#### **Programming Language: Python**
- Python was used as the primary language for both backend development and data processing in this project. It is a versatile language, known for its simplicity and efficiency, making it ideal for web development and API integration.

#### **Framework: Flask**
- Flask is a lightweight web framework for Python that was used to build the server-side of this web application. It enables easy handling of routes, HTTP requests, and serving dynamic content to users, while keeping the application minimal and flexible.

#### **API: Google Sheets API**
- Google Sheets API is used to connect and interact with data stored in Google Sheets. The API allows the app to fetch, update, and process spreadsheet data in real-time, providing a cloud-based solution for storing and accessing user data or additional resources.

#### **CSV: User-provided CSV file uploads**
- Users upload CSV (Comma-Separated Values) files through the web application interface. These files contain data which the app processes, such as extracting specific columns, performing analysis, and possibly generating new data based on the user's request.

#### **Spreadsheets: Google Sheets (Cloud-based storage)**
- Google Sheets was used as a cloud-based storage solution to manage and update data dynamically. By using Google Sheets, the app can interact with live documents, making it easy to store and retrieve data from any location without maintaining a physical database.

#### **Frontend: HTML, CSS, JavaScript**
- The frontend of the web application was built using HTML for structure, CSS for styling, and JavaScript for dynamic interactions and data handling. This allows users to interact with the application, upload files, and view processed results in a user-friendly interface.

#### **Backend: Flask (Python)**
- Flask serves as the backend framework, handling the logic for processing uploaded files, interacting with the Google Sheets API, and generating responses based on the user’s input. It is responsible for routing, data validation, and sending data to the frontend.

#### **Storage: Google Cloud**
- Google Cloud is used for secure and scalable cloud storage of data. It ensures that files, like the processed CSV files, are stored in a safe environment with easy access for download. This eliminates the need for local file storage and ensures the data is available across different devices and locations.

## Summary:

- **Project Name**: AI Agent Project (with Google Cloud Integration)
- **Description**: 
  - Developed an AI-based web application using Flask for file upload and data processing.
  - Implemented Google Cloud integration to fetch and manipulate data stored in Google Sheets.
  - Allowed users to upload CSV files, select columns, and process the data by simulating results using custom queries.
  - Provided options for downloading processed data in CSV format.
  - Employed Google Cloud for seamless cloud-based storage and access.
  - Utilized OpenAI models for data generation (note: this part was excluded from the project as per recent feedback).
  - Focused on efficient data handling, web framework design, and cloud service utilization.

Here is an example of how you can structure your `README.md` file for your project, incorporating the required sections:

---

# AI Agent Project

## Project Description
This web application allows users to upload CSV files, process and extract specific data, and integrate with Google Sheets for data storage and retrieval. The app uses Python's Flask framework for the backend and provides a dynamic interface with HTML, CSS, and JavaScript for the frontend. By leveraging the Google Sheets API, users can manage and update data in real time. Additionally, Google Cloud storage is used to securely store processed results for easy access and download.

---

## Setup Instructions
Follow these steps to set up and run the application locally:

### Prerequisites:
- Python (version 3.7 or higher)
- Google Cloud Account (for API access)
- Google Sheets API credentials
- Google Cloud Storage account (for storing files)

### Steps to Set Up:

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies:**
   Create a virtual environment and install the required Python libraries.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
  

3. **Set up Google API:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project and enable the Google Sheets API and Google Cloud Storage.
   - Download your credentials JSON file and save it in the project directory.
   
4. **Install Google API client:**
   You will need to install the required Google API client libraries:
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

5. **Set environment variables:**
   Set up your Google API credentials and other environment variables (you can create a `.env` file or use environment configuration).
   ```bash
   export GOOGLE_SHEET_ID="your_google_sheet_id"
   ```

---

## Usage Guide

### How to Use the Dashboard:

1. **Start the Flask app:**
   In the project directory, run:
   ```bash
   flask run
   ```
   This will start the Flask application on your local server (typically at `http://127.0.0.1:5000`).

2. **Upload a CSV file:**
   On the homepage, you can upload a CSV file containing data. The app will process this file and display the available columns.

3. **Select columns and set queries:**
   After uploading, choose the columns you want to extract and enter any custom search queries to process the data.

4. **View results:**
   After the data is processed, the results will be displayed in a table format, and you can also download the processed data as a CSV file.

5. **Connect to Google Sheets:**
   The app will use the Google Sheets API to fetch or update data in a Google Spreadsheet as needed.

---

## API Keys and Environment Variables

For the application to run, you need to configure the following API keys and environment variables:

1. **Google Sheets API Key:** 
   - To interact with Google Sheets, you need to configure the Google Sheets API and set the `GOOGLE_SHEET_ID`.

2. **Google Cloud API Key:**
   - Set up Google Cloud credentials for storage and specify your `GOOGLE_CLOUD_BUCKET` in your environment variables.

3. **Optional - OpenAI API Key (if using OpenAI for data generation):**
   - If you want to use OpenAI's GPT models for generating data or text, you will need an API key from OpenAI and set it in your environment as `OPENAI_API_KEY`.

Make sure to replace placeholder values with your actual keys.

---

## Optional Features
  
- **Download Processed Data:** 
  Users can download the processed data in CSV format after the system has completed processing the uploaded file.
  
- **Google Cloud Integration:** 
  The app allows you to store processed files in Google Cloud Storage for easier file management and secure access.

# What I have not uploaded in this repository:
I haven't mentioned Credentials.json file as it contains my private confidential keys and datas, for others who want to make the same project as mine then can have their own Credentials.json once they work on google cloud console.
