SME Financial Health Assessment Tool

HCL × GUVI Hackathon – Phase 2 Submission

-------------------------------------------------------------------------------------------------------

🔖 Selected Problem Statement

Financial Health Assessment Platform for Small and Medium Enterprises (SMEs)

This project is strictly built based on the problem statement selected during Phase 1 of the hackathon.
No alternate or custom problem statements have been used.

---------------------------------------------------------------------------------------------------------

🌍 Live Deployed Links (Mandatory)
Frontend (Public URL)

https://reliable-lokum-f733f8.netlify.app/

Backend API (Public URL)

https://financial-health-backend-sa69.onrender.com

Backend Swagger Documentation

https://financial-health-backend-sa69.onrender.com/docs

📦 GitHub Repository

🔗 https://github.com/Parinitha-08/financial-health-assessment-tool

----------------------------------------------------------------------------------------------------------------

🧩 Problem Overview

Small and Medium Enterprises (SMEs) often lack access to tools that help them clearly understand their financial performance.
While financial data may be available, it is difficult for non-finance business owners to analyze and interpret.

This results in challenges in assessing:

Profitability

Cash flow health

Overall business risk

-------------------------------------------------------------------------------------------------------------------

💡 Solution Description

The SME Financial Health Assessment Tool is a web-based platform that allows SME owners to upload financial data in CSV format and instantly receive:

Key financial metrics

Visual comparison of revenue vs expenses

AI-generated insights and recommendations

Multilingual output for better regional accessibility

The solution simplifies financial analysis and makes insights understandable for non-finance users.

-----------------------------------------------------------------------------------------------------------------------

⚙️ Features Implemented

Upload CSV-based financial statements

Automatic calculation of:

Total Revenue

Total Expenses

Profit

Profit Margin

Cash Flow

Financial Health Score

Risk Level

Interactive charts for financial visualization

AI-generated financial insights

Multi-language support:

English

Hindi

Kannada

Swagger-based API documentation

------------------------------------------------------------------------------------------------------

🛠️ Technology Stack (As per Hackathon Rules)
Frontend

React.js

Recharts (Data Visualization)

Netlify (Deployment)

Backend

FastAPI

Python

Pandas

Uvicorn

Render (Deployment)

----------------------------------------------------------------------------------------------------------

🗂️ Project Structure
financial-health-assessment-tool/
│
├── backend/
│   ├── ai/
│   ├── analysis/
│   ├── i18n/
│   ├── main.py
│   ├── report.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
│
└── README.md

-------------------------------------------------------------------------------------------------------------

▶️ How to Run Locally
Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend URL:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

Frontend
cd frontend
npm install
npm start


Frontend URL:
http://localhost:3000

------------------------------------------------------------------------------------------------------------

👩‍💻 Author

Parinitha Reddy N
HCL × GUVI Hackathon Participant

--------------------------------------------------------------------------------------------------------------

🏁 Final Note

This project demonstrates a practical, scalable, and user-friendly approach to solving real-world financial analysis challenges faced by SMEs using modern web technologies and AI-driven insights.
