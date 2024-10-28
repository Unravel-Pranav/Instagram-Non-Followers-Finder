# Instagram Non-Followers Finder

This is a fun project that allows you to identify users on Instagram who you follow but who do not follow you back. It provides a simple and interactive interface built with Streamlit.😂

## Requirements

- Python 3.x
- Streamlit

## Getting Started

### Step 1: Download Your Instagram Data

1. Open the Instagram app or website.
2. Go to your profile and click on the **Settings** icon (gear).
3. Navigate to **Privacy and Security**.
4. Scroll down to the **Data Download** section and click on **Request Download**.
5. Select **JSON** format and choose the data you want to download. 
   - Make sure to select **Followers** and **Following** sections.
6. Instagram will prepare your data and send you a download link via email. Download the JSON files.

### Step 2: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/instagram-non-followers-finder.git
```
### Step 3: Install Dependencies
Navigate to the project directory:

```bash
cd instagram-non-followers-finder
```
### Install the required dependencies using pip:
```bash
pip install streamlit
```

### Step 4: Run the Application
Once the dependencies are installed, you can run the application using the following command:
```bash
streamlit run app.py
```

## Step 5: Upload Your Data

1. After running the application, open the provided URL in your browser.
2. Upload the JSON files you downloaded from Instagram:
   - Select the **Followers JSON** file.
   - Select the **Following JSON** file.
3. The application will process the files and display the results.

## Step 6: View Results

- You will see the total count of your followers, those you follow, and the users who do not follow you back.
- You can check the box to view the list of non-followers or download it as a text file.

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See the LICENSE file for more details.





