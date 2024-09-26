# Technical Assessment Test

This repository contains the solutions to a series of programming tasks focused on Python and Django. Each task has been implemented with attention to correctness, efficiency, and code readability.

## Table of Contents

- [Tasks Completed](#tasks-completed)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Tasks Completed

1. **Web Scraper**: Scrapes the latest articles from CNN using BeautifulSoup and Requests.
2. **User Data Cleaning**: Reads a CSV of user data, removes duplicates, and filters invalid emails.
3. **Django Model Query**: Retrieves the top 5 customers based on spending in the last 6 months.
4. **Rate Limiter**: Implements a rate limiter to control request frequency per user.
5. **Data Aggregation**: Aggregates values from a list of dictionaries based on a key.
6. **Find Duplicate**: Identifies duplicate numbers in an array with O(1) extra space.

## Requirements

To run this project, you need to install the dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Karan7426/Technical-Assessment-Test.git
    cd Technical-Assessment-Test
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations for the Django app:

    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- For the web scraper, run:

    ```bash
    python scrape_cnn.py
    ```

- To clean user data, run:

    ```bash
    python clean_user_data.py
    ```

- Access the top customers by visiting:

    ```
    http://127.0.0.1:8000/orders/top-customers/
    ```

