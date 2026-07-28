# 📰 GuardianHarvest

**GuardianHarvest** is a lightweight Python script designed to automatedly collect and archive articles from *The Guardian* using their official Open Platform API. 

**It fetches full article text from target categories (such as Technology), extracts key metadata, and automatically structures the raw text into timestamped local directories—providing a clean dataset for news archiving, media analysis, or NLP research.**

### ✨ Key Features
- ⚡ **Official API Ingestion:** Uses The Guardian's Open Platform API for fast, reliable data fetching.
- 📁 **Automated Timestamping:** Organizes output files into dedicated, date-and-time stamped folders to prevent data overwrites.
- 🎯 **Highly Customizable:** Easily change API parameters to target different sections (e.g., Politics, Environment, Science) or date ranges.
- 📊 **Research-Ready:** Outputs clean, plain-text files ready for text mining, sentiment analysis, or corpus building.

## About The Project

This Python script is designed to scrape articles from The Guardian's technology section using their API. It fetches article data, extracts the titles and content, and then saves each article's content to separate text files. The text files are organized in a folder named with the current date and time of the scraping. You can customize the script by changing the URL to target different sections or sources on The Guardian's website. This script is useful for collecting and archiving articles for research or analysis.

## Built With

 - Beautiful Soup

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/Article-Web-Scraping.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
   
  
## Usage and Configuration

### Guardian API Key

This project requires an API key from The Guardian to fetch article data. If you don't already have one, you can obtain an API key by following these steps:

1. Visit The Guardian Developer Portal: [The Guardian API Developer Portal](https://open-platform.theguardian.com/access/)

2. Sign up for an account or log in if you already have one.

3. Create a new application and obtain your API key.

### Configuration

Once you have obtained your API key, you need to configure the project to use it. Here's how to do it:

1. Open the Python script where you make the API request (the one with the URL to The Guardian's API).

2. Locate the `URL` variable that contains the API request URL.

3. In the URL, replace `YOUR_API_KEY` with the actual API key you obtained from The Guardian.


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

# 👩‍💻 Author

**Ishpreet Singh**

M.Tech
Indian Institute of Technology Bombay
Mail ID:
25m0326@iitb.ac.in




