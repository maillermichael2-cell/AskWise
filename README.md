# AskWise API

<p align="center">
  <h1>🤖 AskWise API</h1>
  <p>
    An AI-powered Business Knowledge API that enables organizations to build intelligent assistants trained exclusively on their own data.
  </p>
</p>

---

## 📖 Overview

AskWise API is a backend platform that allows businesses to upload their knowledge base and instantly create an AI assistant capable of answering customer questions using only company-approved information.

Unlike a general-purpose chatbot, AskWise focuses on **domain-specific knowledge**. Every organization has its own isolated knowledge base, ensuring responses remain relevant, secure, and accurate.

Examples include:

- 🏥 Hospitals
- 🏫 Schools
- 🏢 Corporate Organizations
- 🏘️ Real Estate Companies
- 🛍️ E-commerce Businesses
- 🍽️ Restaurants
- 🏦 Financial Institutions
- ⚖️ Law Firms

---

# 🎯 Vision

Every business deserves an intelligent AI assistant without having to build an AI system from scratch.

AskWise provides the backend infrastructure that powers those assistants.

Instead of searching the internet, AskWise searches the business's own verified knowledge.

---

# 🚀 Features

## Authentication

- Email Registration
- Email Login
- OAuth Authentication
- Google OAuth
- GitHub OAuth
- Email Verification
- Password Reset
- Custom User Model
- Secure Session Management
- django-allauth Integration

---

## Organization Management

Businesses can:

- Create an organization
- Manage organization details
- Invite staff members (Future)
- Manage AI settings
- Configure assistant personality
- Manage API Keys (Future)

---

## Knowledge Base

Organizations can upload:

- PDF
- DOCX
- TXT
- Markdown

Future support:

- CSV
- Excel
- PowerPoint
- Websites
- Notion
- Google Docs

---

## AI Chat

Customers can ask:

> What are your business hours?

> Do you offer refunds?

> What is your admission process?

> How much does your premium plan cost?

The AI searches the company's knowledge base before responding.

---

## Conversation History

Store conversations including:

- User messages
- AI responses
- Timestamps
- Organization
- Conversation history

---

## Document Processing

Uploaded files are automatically:

- Stored
- Indexed
- Processed
- Prepared for AI retrieval

---

# 🏗 System Architecture

```
                Client Applications

             Mobile | Web | Dashboard

                       │

                       ▼

               Django REST API

                       │

      ┌────────────────┼─────────────────┐

      ▼                ▼                 ▼

 Authentication   Organization      Chat Service

      │                │                 │

      └────────────────┼─────────────────┘

                       ▼

              Knowledge Service

                       │

             AI Provider Layer

        ┌─────────┬──────────┬──────────┐

        ▼         ▼          ▼

      OpenAI   Anthropic   Gemini

                       │

                       ▼

                  PostgreSQL

```

---

# 📂 Project Structure

```
askwise-api/

│

├── apps/

│   ├── accounts/

│   ├── organizations/

│   ├── documents/

│   ├── chat/

│   ├── common/

│   └── core/

│

├── config/

├── requirements/

├── docker/

├── media/

├── static/

└── manage.py
```

---

# 📦 Technology Stack

## Backend

- Python
- Django
- Django REST Framework

## Database

- PostgreSQL

## Authentication

- django-allauth

## AI

- OpenAI API
- Anthropic API
- Google Gemini API

## Background Tasks (Future)

- Celery
- Redis

## Deployment

- Docker
- Nginx
- Render

---

# 🔐 Authentication Flow

```
User

↓

Register

↓

Email Verification

↓

Login

↓

Access Protected APIs

↓

Upload Documents

↓

Create Conversations

↓

Interact with AI
```

---

# 📁 Django Apps

## accounts

Responsible for:

- Authentication
- Registration
- OAuth
- User Management
- Email Verification

---

## organizations

Responsible for:

- Organizations
- Business Profiles
- Ownership

---

## documents

Responsible for:

- File Uploads
- Knowledge Base
- Document Management

---

## chat

Responsible for:

- Conversations
- Messages
- AI Requests

---

## common

Shared utilities.

---

## core

Project configuration.

---

# 📄 API Roadmap

## Phase 1

- Authentication
- Organizations
- Document Upload
- Conversation Models
- Swagger Documentation

---

## Phase 2

- AI Integration
- OpenAI
- Prompt Management
- AI Responses

---

## Phase 3

- Document Processing
- Retrieval Pipeline
- Semantic Search

---

## Phase 4

- Staff Management
- Permissions
- Organization Roles

---

## Phase 5

- Background Workers
- Redis
- Celery
- Notifications

---

## Phase 6

- API Keys
- Public API
- Rate Limiting
- Analytics

---

# 🔒 Security

- CSRF Protection
- OAuth Authentication
- Email Verification
- Environment Variables
- Secure Password Hashing
- Rate Limiting
- Input Validation
- Secure File Uploads

---

# 📈 Future Features

- Voice Assistant
- WhatsApp Integration
- Slack Integration
- Discord Integration
- Telegram Bot
- Website Widget
- AI Analytics
- Business Insights
- Multiple AI Providers
- Fine-tuned Models
- Live Chat
- Streaming Responses
- Multi-language Support

---

# 🎯 Target Users

- Small Businesses
- Schools
- Hospitals
- Law Firms
- Startups
- Government Agencies
- Customer Support Teams
- Real Estate Companies
- Financial Institutions

---

# 💡 Example Workflow

```
Business Owner

↓

Registers Account

↓

Creates Organization

↓

Uploads Company Documents

↓

AI Processes Knowledge

↓

Customers Ask Questions

↓

AskWise Retrieves Information

↓

AI Generates Accurate Response

↓

Conversation Stored
```

---

# 🌍 Long-Term Vision

AskWise aims to become a universal AI knowledge platform where businesses can create intelligent assistants without building custom AI infrastructure.

By combining secure authentication, scalable APIs, document management, and modern AI technologies, AskWise empowers organizations to deliver instant, reliable, and context-aware responses to customers.

---

## 👨‍💻 Author

**Michael Adeyanju**

Backend Engineer | Python • Django • PostgreSQL • Docker • AI Integration

---

## 📜 License

This project is released under the MIT License.