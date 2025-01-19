# Open Terminal - Trading Application

A Flask-based web application for trading using the AngelOne Smart API.

## Features

- User Registration and Authentication
- AngelOne Smart API Integration
- Secure Session Management
- Protected Dashboard Access
- Responsive UI using Tailwind CSS

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- AngelOne Trading Account
- Google Authenticator (for 2FA)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd basic-flask-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Make sure you have your AngelOne credentials ready:
   - Client ID
   - API Key
   - Trading Password (PIN)
   - Google Authenticator set up for TOTP

2. The application uses SQLite as the database, which will be created automatically when you run the app.

## Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Register:
   - Navigate to the registration page
   - Enter your username
   - Enter your AngelOne Client ID
   - Enter your API Key

2. Login:
   - Use your Client ID
   - Enter your trading password (PIN)
   - Enter the current TOTP code from Google Authenticator

## Project Structure

```
basic-flask-app/
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── about.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
├── app.py
├── config.py
├── extensions.py
├── models.py
├── routes.py
├── requirements.txt
└── README.md
```

## Security Notes

- Never share your API keys or credentials
- Always use HTTPS in production
- Keep your Google Authenticator secure
- Regularly update your passwords

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details