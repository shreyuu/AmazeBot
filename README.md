# **AmazeBot**

AmazeBot is an AI-powered chatbot built with **Django (Backend)**, **React.js (Frontend)**, and **Tailwind CSS**. It leverages **OpenAI's GPT model** to provide intelligent and engaging conversations.

## **🔗 Live Demo**

🚀 [AmazeBot Live](https://your-live-demo-link.com) *(Not depolyed yet, Will update once deployed)*

## **📌 Features**

✅ AI-powered chatbot with **OpenAI GPT**  
✅ **Django REST Framework** API backend  
✅ **React.js + Tailwind CSS** frontend for a sleek UI  
✅ **Real-time conversation experience**  
✅ **CORS enabled for seamless frontend-backend communication**  
✅ **Future Enhancements**: WebSockets, Chat History, Authentication, and Speech-to-Text  

---

## **🛠 Tech Stack**

### **Backend (Django API):**

- Django
- Django REST Framework (DRF)
- Django Channels (for WebSockets in the future)
- OpenAI API (GPT-powered responses)
- PostgreSQL / MongoDB (for chat history)

### **Frontend (React.js UI):**

- React.js
- Tailwind CSS
- Axios (for API calls)
- Vercel / Netlify (for deployment)

---

## **📂 Project Structure**

```
amazebot/
│── backend/      # Django Backend
│── frontend/     # React Frontend
│── README.md     # Project Documentation
│── .gitignore    # Ignored files
│── requirements.txt  # Python dependencies
│── package.json  # Node.js dependencies
```

---

## **🚀 Setup & Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/shreyuu/amazebot.git
cd amazebot
```

### **2️⃣ Backend (Django API) Setup**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### **Environment Variables (`backend/.env`)**

```plaintext
OPENAI_API_KEY=your-openai-api-key
DEBUG=True
```

---

### **3️⃣ Frontend (React) Setup**

```bash
cd frontend
npm install
npm start  # Runs on localhost:3000
```

#### **Update API Endpoint in `frontend/src/components/Chatbot.js`**

```javascript
const res = await axios.post("http://127.0.0.1:8000/api/chat/", { message: input });
```

---

## **📡 Deployment**

### **🔹 Backend (Django API)**

- Use **Render, Heroku, or Railway** to deploy Django.

### **🔹 Frontend (React.js UI)**

- Use **Vercel or Netlify** for React deployment.

#### **Update API Endpoint for Production**

```javascript
const res = await axios.post("https://your-api-url.com/api/chat/", { message: input });
```

---

## **📌 Future Enhancements**

✅ WebSockets for real-time messaging  
✅ JWT-based Authentication for users  
✅ Chat history with database storage  
✅ Speech-to-text and text-to-speech integration  

---

## **📄 License**

MIT License © 2025 Shreyash Meshram  

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
📧 Email: <your-email@example.com>  

**Give this repo a ⭐ if you like it!** 🚀

# **AmazeBot**

AmazeBot is an AI-powered chatbot built with **Django (Backend)**, **React.js (Frontend)**, and **Tailwind CSS**. It leverages **OpenAI's GPT model** to provide intelligent and engaging conversations.

## **🔗 Live Demo**

🚀 [AmazeBot Live](https://your-live-demo-link.com) *(Update once deployed)*

## **📌 Features**

✅ AI-powered chatbot with **OpenAI GPT**  
✅ **Django REST Framework** API backend  
✅ **React.js + Tailwind CSS** frontend for a sleek UI  
✅ **Real-time conversation experience**  
✅ **CORS enabled for seamless frontend-backend communication**  
✅ **Future Enhancements**: WebSockets, Chat History, Authentication, and Speech-to-Text  

---

## **🛠 Tech Stack**

### **Backend (Django API):**

- Django
- Django REST Framework (DRF)
- Django Channels (for WebSockets in the future)
- OpenAI API (GPT-powered responses)
- PostgreSQL / MongoDB (for chat history)

### **Frontend (React.js UI):**

- React.js
- Tailwind CSS
- Axios (for API calls)
- Vercel / Netlify (for deployment)

---

## **📂 Project Structure**

```
amazebot/
│── backend/      # Django Backend
│── frontend/     # React Frontend
│── README.md     # Project Documentation
│── .gitignore    # Ignored files
│── requirements.txt  # Python dependencies
│── package.json  # Node.js dependencies
```

---

## **🚀 Setup & Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/shreyuu/amazebot.git
cd amazebot
```

### **2️⃣ Backend (Django API) Setup**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### **Environment Variables (`backend/.env`)**

```plaintext
OPENAI_API_KEY=your-openai-api-key
DEBUG=True
```

---

### **3️⃣ Frontend (React) Setup**

```bash
cd frontend
npm install
npm start  # Runs on localhost:3000
```

#### **Update API Endpoint in `frontend/src/components/Chatbot.js`**

```javascript
const res = await axios.post("http://127.0.0.1:8000/api/chat/", { message: input });
```

---

## **📡 Deployment**

### **🔹 Backend (Django API)**

- Use **Render, Heroku, or Railway** to deploy Django.

### **🔹 Frontend (React.js UI)**

- Use **Vercel or Netlify** for React deployment.

#### **Update API Endpoint for Production**

```javascript
const res = await axios.post("https://your-api-url.com/api/chat/", { message: input });
```

---

## **📌 Future Enhancements**

✅ WebSockets for real-time messaging  
✅ JWT-based Authentication for users  
✅ Chat history with database storage  
✅ Speech-to-text and text-to-speech integration  

---

## **📄 License**

MIT License © 2025 Shreyash Meshram  

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
📧 Email: <your-email@example.com>  

**Give this repo a ⭐ if you like it!** 🚀****
