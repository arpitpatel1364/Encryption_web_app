# 🚀 Django Encryption Web App

A hacker-themed Django web application that provides secure channel-based encryption and decryption services with a terminal-style interface.

## ✨ Features

- **🔐 User Authentication**: Secure signup, login, and logout system
- **🧩 Channel System**: Create and join private encrypted channels
- **🔄 3-Layer Encryption**: Custom character mapping + XOR + secret key generation
- **🛡️ Security**: Encrypted custom maps, CSRF protection, and access control
- **🎨 Hacker UI**: Terminal-style interface with Matrix background effects
- **🌙 Theme Toggle**: Switch between dark hacker theme and light mode
- **📱 Responsive**: Works on desktop, tablet, and mobile devices
- **💾 Message History**: Optional encrypted message storage (24hr auto-delete)

## 🛠️ Tech Stack

- **Backend**: Django 4.2+, Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with hacker theme
- **Database**: SQLite (default) / PostgreSQL (production)
- **Security**: Cryptography.fernet, Django signing
- **Icons**: Font Awesome 6

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd encryption_web
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Create .env file
   echo "DEBUG=True" > .env
   echo "SECRET_KEY=your-secret-key-here" >> .env
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your browser and go to `http://localhost:8000`
   - Sign up for a new account or login

## 📁 Project Structure

```
encryption_web/
├── encryption_app/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── channel_create.html
│   │   ├── channel_join.html
│   │   ├── encrypt.html
│   │   ├── decrypt.html
│   │   └── help.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── hacker.css
│   │   │   └── light-theme.css
│   │   └── js/
│   │       ├── theme-toggle.js
│   │       └── matrix.js
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── urls.py
├── encryption_web/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .env (create this)
└── README.md
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-very-secure-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Production Settings

For production deployment:

1. Set `DEBUG=False`
2. Configure secure `SECRET_KEY`
3. Set up proper database (PostgreSQL recommended)
4. Configure `ALLOWED_HOSTS`
5. Set up static file serving
6. Enable HTTPS
7. Configure proper logging

## 🎮 Usage Guide

### Creating a Channel

1. **Login** to your account
2. Go to **Dashboard**
3. Click **"Create Channel"**
4. Enter a unique channel name
5. **Copy the generated key** - share this with trusted users
6. Channel is ready for encryption/decryption

### Joining a Channel

1. **Login** to your account
2. Go to **Dashboard**
3. Click **"Join Channel"**
4. Enter the **channel key** provided by the channel creator
5. You're now a member and can encrypt/decrypt messages

### Encrypting Messages

1. **Select a channel** from your dashboard
2. Go to **"Encrypt"** page
3. Enter your message (supported characters: a-z, 0-9, space, punctuation)
4. Click **"Encrypt"** 
5. **Copy the secret key** - this is what you share with others
6. The secret key can only be decrypted by channel members

### Decrypting Messages

1. **Select the correct channel** (same channel used for encryption)
2. Go to **"Decrypt"** page
3. Paste the **secret key** you received
4. Click **"Decrypt"**
5. The original message will be revealed

## 🔐 Security Features

### Encryption Process

The app uses a 3-layer encryption system:

1. **Custom Character Mapping**: Text → Custom numeric codes
2. **XOR Transformation**: Custom codes → XOR with seeded random values
3. **Secret Key Generation**: Final encrypted numeric sequence

### Security Measures

- **Encrypted Custom Maps**: Channel maps are encrypted before database storage
- **Channel Isolation**: Each channel has unique encryption parameters
- **Access Control**: Only channel members can encrypt/decrypt
- **CSRF Protection**: All forms protected against cross-site request forgery
- **Secure Key Generation**: Uses `secrets.token_urlsafe()` for channel keys
- **Password Security**: Django's built-in password hashing

## 🎨 UI Features

### Hacker Theme (Default)
- **Terminal-style interface**
- **Matrix background animation**
- **Green monospace font (VT323)**
- **Glowing effects and animations**
- **Typing simulation effects**

### Light Theme
- **Clean, modern interface**
- **Professional color scheme**
- **Improved readability**
- **Accessible contrast ratios**

### Interactive Elements
- **Theme toggle button**
- **Copy-to-clipboard functionality**
- **Hover effects and transitions**
- **Responsive design**
- **Loading animations**

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows PEP 8 guidelines. Use flake8 for linting:

```bash
pip install flake8
flake8 .
```

### Database Migrations

When you modify models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files

In production, collect static files:

```bash
python manage.py collectstatic
```

## 🚀 Deployment

### Heroku Deployment

1. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables**:
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-production-secret-key
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

4. **Run migrations**:
   ```bash
   heroku run python manage.py migrate
   ```

### Docker Deployment

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 📊 API Documentation

### Models

#### Channel
- `name`: Unique channel identifier
- `key`: Secure channel access key
- `creator`: User who created the channel
- `encrypted_custom_map`: Encrypted character mapping

#### ChannelMembership
- `user`: User in the channel
- `channel`: Channel reference
- `joined_at`: Timestamp of joining

#### EncryptedMessage (Optional)
- `encrypted_data`: Encrypted message content
- `channel`: Channel where message was created
- `created_by`: User who created the message
- `timestamp`: Creation timestamp

### Views

#### Authentication Views
- `signup`: User registration
- `login`: User authentication
- `logout`: User session termination

#### Channel Views
- `dashboard`: List user channels
- `channel_create`: Create new channel
- `channel_join`: Join existing channel
- `encrypt`: Encrypt messages
- `decrypt`: Decrypt messages

## 🛡️ Security Best Practices

### For Developers

1. **Never commit secrets** to version control
2. **Use environment variables** for sensitive data
3. **Validate all user inputs**
4. **Implement proper error handling**
5. **Use HTTPS in production**
6. **Regular security audits**

### For Users

1. **Keep channel keys secure**
2. **Don't share keys over insecure channels**
3. **Use strong passwords**
4. **Log out from shared devices**
5. **Regularly update passwords**

## 🐛 Troubleshooting

### Common Issues

#### Database Errors
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
```

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput
```

#### ImportError
```bash
# Check virtual environment
pip list
pip install -r requirements.txt
```

### Debug Mode

Enable detailed error messages:

```python
# In settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests for new functionality**
5. **Run tests and ensure they pass**
6. **Submit a pull request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/encryption-web.git
cd encryption-web

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python manage.py test
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Support

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check this README for detailed instructions
- **Community**: Join our discussion forums

## 🔮 Future Enhancements

- **Multi-factor Authentication**
- **File Encryption Support**
- **Mobile App (React Native)**
- **API for Third-party Integration**
- **Advanced Key Management**
- **Audit Logging**
- **Real-time Chat Interface**

## 🙏 Acknowledgments

- **Django Community** for the excellent framework
- **Font Awesome** for the icons
- **Matrix Digital Rain** inspiration for the background effect
- **Security Best Practices** from OWASP guidelines

---

**Built by : Arpit Bhojani **

For more information, visit our or contact us at [bhojaniarpit1432@gmail.com] (7383181094).