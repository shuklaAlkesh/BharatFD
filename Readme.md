# Django FAQ Management System

## Overview
Welcome to the **Django FAQ Management System**! This project is designed to help manage and display FAQs (Frequently Asked Questions) with multi-language support. It allows you to easily store questions and answers, translate them to different languages, and present them in a rich-text format using a WYSIWYG (What You See Is What You Get) editor. This system also comes with an intuitive admin interface and a REST API to interact with the data.

### What Does This Project Do?
1. It allows you to store FAQs with questions, answers, and language-specific translations.
2. The answers are formatted using the `django-ckeditor` rich-text editor, which makes it easy to create well-structured content.
3. It automatically translates FAQ content into multiple languages using the Google Translate API.
4. The system supports **Redis caching** to improve translation performance.
5. A clean and user-friendly **Django Admin Interface** is provided for managing FAQs.

## Key Features
- **Multilingual FAQs**: Easily manage FAQs in multiple languages.
- **Rich Text Answers**: Use the `django-ckeditor` editor to format answers with bold, italics, images, and more.
- **Dynamic Translations**: The system can automatically translate FAQ questions and answers into different languages like Hindi, Bengali, etc.
- **Caching for Performance**: Translations are cached in **Redis** to improve speed and avoid repetitive API calls.
- **REST API**: You can fetch FAQs in any language via simple API queries.
- **Django Admin Panel**: Manage FAQs and translations effortlessly using the built-in Django admin interface.

## Installation Guide

### Step 1: Clone the Repository
To get started, clone the project repository to your local machine:

```bash
git clone https://github.com/shuklaAlkesh/BharatFD
