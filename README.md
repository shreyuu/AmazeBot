# AmazeBot 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

AmazeBot is an AI-powered chatbot built with **Django (Backend)**, **React.js (Frontend)**, and **Tailwind CSS**. It leverages **Hugging Face's Blenderbot model** to provide intelligent and engaging conversations.

## **🔗 Live Demo**

🚀 [AmazeBot Live](https://your-live-demo-link.com) _(Not depolyed yet, Will update once deployed)_

## **📌 Features**

✅ AI-powered chatbot with **Hugging Face Blenderbot**  
✅ **Django REST Framework** API backend  
✅ **React.js + Tailwind CSS** frontend for a sleek UI  
✅ **Real-time conversation experience**  
✅ **CORS enabled for seamless frontend-backend communication**  
✅ **Future Enhancements**: WebSockets, Chat History, Authentication, and Speech-to-Text
✅ Rate limiting with **10 requests/second**
✅ Response caching for improved performance
✅ Error handling and retry logic

---

## **🛠 Tech Stack**

### **Backend (Django API):**

- Django
- Django REST Framework (DRF)
- Django Channels (for WebSockets in the future)
- PostgreSQL / MongoDB (for chat history)
- Request Throttling
- Response Caching
- Hugging Face API Integration

### **Frontend (React.js UI):**

- React.js
- Tailwind CSS
- Axios (for API calls)
- Vercel / Netlify (for deployment)

---

## **📂 Project Structure**

```plaintext
amazebot/
├── .env                # Environment variables
├── .github/           # GitHub Actions workflows
│   └── workflows/
│       ├── backend.yml
│       └── frontend.yml
├── backend/           # Django Backend
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot/           # Chatbot Django App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── throttling.py
│   ├── urls.py
│   └── views.py
├── frontend/          # React Frontend
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   ├── tailwind.config.js
│   └── postcss.config.js
├── README.md          # Project Documentation
├── requirements.txt   # Python dependencies
└── manage.py         # Django management script
```

---

## **🚀 Setup & Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/shreyuu/amazebot.git
cd amazebot
```

### **2️⃣ Backend (Django API) Setup**

First, ensure you have Python 3.8+ and pip installed.

**Install Required Packages:**

```plaintext
# requirements.txt
django>=4.2.0
djangorestframework>=3.14.0
django-cors-headers>=4.3.0
python-dotenv>=1.0.0
requests>=2.31.0
python-decouple>=3.8
whitenoise>=6.6.0
gunicorn>=21.2.0
```

#### For MacOS/Linux:

```bash
# Create and activate virtual environment
python3 -m venv amazebotenv
source amazebotenv/bin/activate

# Install dependencies and setup database
cd backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver  # Starts server at localhost:8000
```

#### For Windows:

```powershell
# Create and activate virtual environment
python -m venv amazebotenv
.\amazebotenv\Scripts\activate

# Install dependencies and setup database
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # Starts server at localhost:8000
```

#### **Environment Variables**

Backend environment variables (`backend/.env`):

```plaintext
HUGGINGFACE_API_KEY=your-huggingface-api-key
DEBUG=True
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
DATABASE_URL=sqlite:///db.sqlite3
DJANGO_SETTINGS_MODULE=backend.settings
```

Create a `.env` file in the frontend directory:

```plaintext
# filepath: frontend/.env
REACT_APP_API_URL=http://127.0.0.1:8000
```

### **3️⃣ Frontend (React) Setup**

#### For MacOS/Linux/Windows:

```bash
# Open a new terminal
cd frontend
npm install
npm start  # Starts React app at localhost:3000
```

#### **Frontend Configuration**

Update the API endpoint in `frontend/src/App.js`:

```javascript
// filepath: /Users/shreyuu/VS_Code_projects/learning/python/Django-learning-Dec2024/AmazeBot/frontend/src/App.js
const API_ENDPOINT =
  process.env.NODE_ENV === "production"
    ? "https://your-api-url.com/api/chat/"
    : "http://127.0.0.1:8000/api/chat/";

const res = await axios.post(API_ENDPOINT, {
  message: input,
});
```

### **4️⃣ Verify Setup**

1. Backend API should be running at: `http://127.0.0.1:8000/`
2. Frontend should be running at: `http://localhost:3000/`
3. Test the chatbot by sending a message through the UI

---

## **📡 Deployment**

### **🔹 Backend (Django API)**

1. Choose a platform:

   - **Render**: Follow [Django deployment guide](https://render.com/docs/deploy-django)
   - **Railway**: Use [Railway Django template](https://railway.app/new/template/django)
   - **Heroku**: Follow [Heroku Django guide](https://devcenter.heroku.com/articles/django-app-configuration)

2. Set environment variables in your deployment platform:

```plaintext
HUGGINGFACE_API_KEY=your-key
DEBUG=False
SECRET_KEY=your-production-key
ALLOWED_HOSTS=your-domain.com
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### **🔹 Frontend (React.js UI)**

1. Build the production version:

```bash
cd frontend
npm run build
```

2. Deploy to Vercel or Netlify:

   - **Vercel**: `vercel --prod`
   - **Netlify**: `netlify deploy --prod`

3. Set environment variables:

```plaintext
REACT_APP_API_URL=https://your-backend-domain.com
```

#### **Update API Endpoint for Production**

```javascript
const res = await axios.post("https://your-api-url.com/api/chat/", {
  message: input,
});
```

---

## **📌 Future Enhancements**

✅ WebSockets for real-time messaging  
✅ JWT-based Authentication for users  
✅ Chat history with database storage  
✅ Speech-to-text and text-to-speech integration

---

## **📄 License**

MIT License © 2025 [Shreyash Meshram](https://github.com/shreyuu/)

---

## **🤝 Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

1. **Fork the repo**
2. **Create a feature branch** (`git checkout -b feature-name`)
3. **Commit changes** (`git commit -m 'Added new feature'`)
4. **Push to GitHub** (`git push origin feature-name`)
5. **Create a Pull Request**

---

## **📞 Contact**

💼 **Shreyash Meshram**  
🔗 [LinkedIn](https://www.linkedin.com/in/shreyuu/)  
🐙 [GitHub](https://github.com/shreyuu/)  
📧 [Email](mailto:shreyashmeshram0031@gmail.com)

---

_Last updated: Feburary 2025_
