# 📘 Assignment: Python API Basics

## 🎯 Objective

Learn how to fetch data from a web API, parse JSON, and display useful information in a Python program. This assignment introduces the core idea that apps can request data from online services and work with it programmatically.

## 📝 Tasks

### 🛠️ Fetch JSON from a Public API

#### Description
Use Python's built-in `urllib` and `json` modules to request data from a simple public API and print the response.

#### Requirements
Completed program should:

- Request data from a public JSON API endpoint such as `https://jsonplaceholder.typicode.com/posts/1`
- Parse the response as JSON
- Print the returned data in a readable format
- Confirm the program works without installing extra libraries

### 🛠️ Extract Key Information

#### Description
Turn raw JSON into a friendly summary for the user.

#### Requirements
Completed program should:

- Read the JSON response and extract fields such as `userId`, `id`, `title`, and `body`
- Print a short summary like: `Post 1 by user 1: <title>`
- Display the message body in a clean, readable way
- Use functions to organize the code into reusable pieces

### 🛠️ Build a Small API Explorer

#### Description
Create a tiny program that lets a user choose a post ID and then fetches that post from the API.

#### Requirements
Completed program should:

- Prompt the user for a post ID
- Fetch the matching post from the API
- Display the post title and body
- Handle missing or invalid input gracefully
- Print a friendly message if the request fails

