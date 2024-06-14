### English2Morse API Documentation

---

## 1. Introduction
- **Overview**
  - The English2Morse API allows users to translate text between English and Morse code.
  - Key features include text-to-Morse translation, Morse-to-text translation, and error handling for unsupported characters.
- **Use Cases**
  - Converting English messages to Morse code.
  - Decoding Morse code messages back.

## 2. Getting Started
- **Prerequisites**
  - Python programming language.
  - requests library for making HTTP requests.
- **Installation**
  - Install Python from the official Python website.
- **Authentication**
  - This API does not require authentication.

## 3. Endpoints
### Endpoint Summary
| Method | Endpoint                   | Description                          |
|--------|----------------------------|--------------------------------------|
| GET    | /api/translate/            | Translates between English and Morse code |

### Endpoint Details

#### GET /api/translate/
- **Description**: Translates between English and Morse code based on the provided parameters.
- **Parameters**:
  - **Query**:
    - `translate` (string, required) - The target translation language, either `english` or `morse`.
    - `text` (string, required) - The text to be translated.
  - Note: Both parameters are required.
- **Request Example**:
  - English to Morse:
    ```http
    GET /api/translate/?translate=morse&text=Example%20text
    ```
  - Morse to English:
    ```http
    GET /api/translate/?translate=english&text=.-..%20-%20..-%20.-..%20.--.%20.%20.%20-%20%-%20..-%20-%20.-%20.%20-%20.-..%20--.%20-..%20.-..%20-..
    ```
- **Response Example**:
  - English to Morse:
    ```json
    {
      "translate": "morse",
      "text": "Example text",
      "translation": ". -..- .- -- .--. .-.. .   - . -..- -"
    }
    ```
  - Morse to English:
    ```json
    {
      "translate": "english",
      "text": ". -..- .- -- .--. .-.. .   - . -..- -",
      "translation": "Example text"
    }
    ```
- **Errors**:
  - `400 Bad Request` - The request is invalid or missing required parameters.
    - Example response:
      ```json
      {
        "error": "Invalid request. Provide both 'translate' and 'text' parameters."
      }
      ```

## 4. Data Models
- **Translation Request Parameters**
  - `translate` (string) - The target translation language, either `english` or `morse`.
  - `text` (string) - The text to be translated.
- **Translation Response**
  - `translate` (string) - The target translation language, either `english` or `morse`.
  - `text` (string) - The original text to be translated.
  - `translation` (string) - The translated text.

## 5. Examples

### Python Example: English to Morse
```python
import requests

text = "Example text"
params = {
    "translate": "morse",
    "text": text
}

response = requests.get("http://127.0.0.1:8000/api/translate/", params=params)
print(response.json())
```

### Python Example: Morse to English
```python
import requests

morse_code = ". -..- .- -- .--. .-.. .   - . -..- -"
params = {
    "translate": "english",
    "text": morse_code
}

response = requests.get("http://127.0.0.1:8000/api/translate/", params=params)
print(response.json())
```

## 6. Error Handling
- **400 Bad Request**: The request was invalid or missing required parameters.
  - Ensure that both `translate` and `text` parameters are provided and valid.
  - Example response:
    ```json
    {
      "error": "Invalid request. Provide both 'translate' and 'text' parameters."
    }
    ```

## 7. FAQs and Troubleshooting
- **What should I do if I receive a 400 error?**
  - Verify that the request URL contains both `translate` and `text` query parameters.
  - Check that the `translate` parameter is either `english` or `morse`.
  - Ensure the `text` parameter is properly formatted.

## 8. Glossary
- **API**: Application Programming Interface.
- **Endpoint**: A specific function or operation exposed by the API.
- **Morse Code**: A method of encoding text characters using sequences of dots and dashes.

---
