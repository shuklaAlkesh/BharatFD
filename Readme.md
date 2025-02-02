# FAQ Management System

## Overview
The `FAQ Management System` is designed to efficiently manage and display FAQs in a multi-language format. It uses advanced techniques such as caching, rich-text formatting, and automated translations, which allow for a seamless and scalable FAQ management experience. The system also includes a REST API for programmatically accessing the FAQs in various languages.

## Problem Statement
- **Challenge**: Managing FAQs with support for multiple languages, while ensuring scalability, performance, and ease of use.
- **Core Requirements**:
  - Efficiently store FAQs with questions and answers.
  - Provide multi-language support for FAQs.
  - Display answers using a rich-text format to allow rich formatting like bold, italic, images, etc.
  - Optimize performance with caching, specifically for translated FAQs, and allow for automatic translation.
  - Offer a simple, intuitive interface for managing FAQs.

## Approach & Solution

### 1. **Storing FAQs & Translations**:
   - The FAQ system stores both questions and answers in the database, with the ability to add multiple translations for each language.
   - The FAQ content is stored in the Django model with fields for `question`, `answer`, and `language`.
   - Translations are automatically fetched using the **Google Translate API** for different languages. This reduces the manual effort in translating content and increases productivity.

### 2. **Rich Text Formatting**:
   - Answers are formatted using the **django-ckeditor** editor, which allows the use of rich text features such as bold, italics, images, and links, ensuring that answers are presented in a clear, organized manner.
   - The editor is easy to use, and content can be styled without requiring knowledge of HTML.

### 3. **Caching with Redis**:
   - To improve performance, translations of FAQs are cached using **Redis**. This ensures that repeated translation requests for the same FAQ are faster, minimizing API calls to the Google Translate API.
   - Redis is used as an in-memory data store to cache the translation responses, which significantly reduces latency and optimizes response times.

### 4. **Django Admin Interface**:
   - The project includes the Django admin interface, which allows administrators to add, update, and manage FAQ questions and answers with ease. Admins can also update language translations for each FAQ entry directly from the admin panel.

### 5. **REST API for Multi-language Support**:
   - The system provides a simple and flexible REST API to fetch FAQs in multiple languages. By specifying the `lang` query parameter, users can get FAQs in different languages (e.g., English, Hindi, Bengali).
   - The API supports dynamic queries and provides a straightforward way to interact with FAQ data.

### 6. **Docker Support**:
   - To facilitate easy deployment, Docker support is included. The project provides a **Dockerfile** and **docker-compose.yml** configuration to easily containerize the Django application.
   - This ensures that the application can be run consistently across different environments (development, production, etc.) without worrying about dependency issues.

## Key Features
- **Multilingual FAQ Management**: Easily manage and display FAQs in multiple languages (e.g., English, Hindi, Bengali).
- **Rich Text Formatting**: Answer content is displayed using the **django-ckeditor** editor for easy formatting.
- **Caching for Performance**: Translations are cached using **Redis** to improve speed.
- **Automatic Translations**: FAQs are automatically translated using the **Google Translate API**.
- **REST API Access**: Easily fetch FAQs in any language via simple API queries.
- **Docker Support**: Simplifies deployment and containerization of the application.

## Installation & Setup Guide

### Step 1: Clone the Repository
Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/shuklaAlkesh/BharatFD
cd BharatFD
```
### Step 2: Install Dependencies
Create a virtual environment and install the required dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

### Step 3: Set up Redis
To enable caching with Redis, ensure that Redis is installed and running on your machine. If we are using Docker, the system will use Redis via a container.

```bash
docker-compose up
```

### Step 4: Run Migrations
Apply the migrations to set up the database:

```bash
python manage.py migrate
```

### Step 5:  Create Superuser
Create a superuser to access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
Run the Django development server to start the application:

```bash
python manage.py runserver
```
The application should now be running on http://127.0.0.1:8000/.

### Step 7: Access the Admin Panel
Open http://127.0.0.1:8000/admin/ in your browser and log in using the superuser credentials you created earlier.

### API Usage

## Fetching FAQs in Different Languages
The FAQ system provides an API endpoint to fetch FAQs in various languages. The language is determined by the lang query parameter.

Endpoint: `/api/faqs/ `

1. Fetch FAQs in English:
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=en
```

2. Fetch FAQs in Hindi:
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=hi
```
3. Fetch FAQs in Bengali:
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=bn
```

### Here We Can Creating a New FAQ using the POST request:
Endpoint: `/api/faqs/`

```base
{
  "question": "What is Django?",
  "answer": "Django is a high-level Python web framework.",
  "question_hi": "Django क्या है?",
  "answer_hi": "Django एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
}
```

## Admin Panel

The Django FAQ Management System includes an **Admin Panel** for easily managing FAQs through a user-friendly interface. Admins can add, edit, and delete FAQs, including the option to update translations for each FAQ entry directly from the panel.

### Accessing the Admin Panel
To access the admin panel, go to:
[http://localhost:8000/admin/](http://localhost:8000/admin/)

You will need to log in using the following credentials that I created for testing:
- **Username**: `asus`
- **Password**: `1234`
## Managing FAQs:
After logging in, you can add, edit, and delete FAQs, and use the `WYSIWYG` editor to format the answers with rich text, making them more engaging and informative.

### Registering the FAQ Model

For managing FAQs through the admin interface, the **FAQ** model needs to be registered in the Django admin. This allows you to view, add, update, and delete FAQs directly from the admin panel.

1. **Create the `FAQ` model in `models.py`**:
   - The FAQ model should include fields such as `question`, `answer`, and language-specific translations for each FAQ entry.

2. **Register the model in `admin.py`**:
   - To make the model accessible in the admin panel, register it using Django’s admin interface.

By registering the model, you can efficiently manage FAQs and their translations through the Django Admin Panel.


## Unit Tests & Code Quality

### Unit Tests
Unit tests ensure the FAQ system works correctly. We use **pytest** for testing:

- **Model Tests**: Check if FAQs and translations are created and retrieved correctly from the database.
- **API Tests**: Ensure that the API returns the correct FAQs based on the requested language and handles errors properly.

### Code Quality
We maintain high code quality by following best practices:

- **PEP8**: Standard guide for Python code formatting.
- **flake8**: Tool to check for PEP8 violations and common Python errors.
- **ES6**: JavaScript's modern standard for clean and efficient code.
- **ESLint**: Tool to enforce JavaScript style guidelines and detect issues.

By using **pytest**, **flake8**, and **ESLint**, we ensure the code is clean, readable, and reliable.


## Conclusion
This FAQ management system provides a flexible, efficient, and scalable way to manage and display frequently asked questions in multiple languages. In this implementation, support for three languages—**English**, **Hindi**, and **Bengali**—has been provided. With features like rich-text support, automatic translations, caching, and a REST API, this system can be easily integrated into a wide range of applications. Docker support ensures that deployment is seamless across environments.





