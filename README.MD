# Open Terminal - Trading Application

A Flask-based web application for trading using the AngelOne Smart API.

## Features

- User Registration and Authentication
- AngelOne Smart API Integration
- Secure Session Management
- Protected Dashboard Access
- Two-Factor Authentication (2FA)

## Prerequisites

- Python 3.8+
- pip
- AngelOne Trading Account
- Google Authenticator

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd open-terminal-trading-app
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/MacOS
venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Required Credentials:
   - Client ID
   - API Key
   - Trading Password
   - Google Authenticator TOTP

2. Database: SQLite (auto-created)

## Running the Application

```bash
python app.py
```

Access at: `http://localhost:5000`

## Usage

1. Register:
   - Enter username
   - Provide AngelOne Client ID
   - Input API Key

2. Login:
   - Use Client ID
   - Enter trading password
   - Provide TOTP from Google Authenticator

## Project Structure

```
open-terminal-trading-app/
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── login.html
│   └── dashboard.html
│
├── app.py
├── routes.py
├── models.py
├── extensions.py
├── config.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Security Recommendations

- Never share API credentials
- Use HTTPS in production
- Secure Google Authenticator
- Regularly update passwords

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Create Pull Request

## License

This project is licensed under the GNU Affero General Public License (AGPL) version 3.0.

Key points:
- Network service usage requires complete source code disclosure
- Preserve all copyright notices
- Modifications must be released under AGPL
- Commercial use permitted with full source code sharing

Full license terms in LICENSE file.

## Disclaimer

This software is provided "as is" without warranty. Use at your own risk.
Not affiliated with AngelOne. Requires compliance with AngelOne's API Terms of Service.