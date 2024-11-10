from flask import Flask, request, render_template, send_file
import pandas as pd
from sheet import access_google_sheet, write_to_google_sheet  # Import both access and write functions

app = Flask(__name__)

# Global variables to store data between requests
uploaded_df = None
results_df = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_df
    file = request.files['file']
    if file.filename.endswith('.csv'):
        uploaded_df = pd.read_csv(file)
        columns = uploaded_df.columns.tolist()
        return render_template('select_column.html', columns=columns)
    else:
        return "Please upload a CSV file."

@app.route('/process', methods=['POST'])
def process():
    global uploaded_df, results_df
    main_column = request.form['main_column']
    custom_query = request.form['custom_query']

    # Access data from Google Sheets
    sheet_data = access_google_sheet()  # Fetch data from the Google Sheet

    # Filter the DataFrame based on the custom query in the selected column
    filtered_df = uploaded_df[uploaded_df[main_column].astype(str).str.contains(custom_query, case=False, na=False)]

    # Store all columns of rows that match the query
    results_df = filtered_df.copy()

    # Write the results to Google Sheets
    write_to_google_sheet(results_df)

    # Render the results with the filtered data
    return render_template('results.html', 
                           tables=[results_df.to_html(index=False)], 
                           titles=results_df.columns.values, 
                           sheet_data=sheet_data)

@app.route('/download')
def download():
    global results_df
    output_file = 'extracted_results.csv'
    results_df.to_csv(output_file, index=False)
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
