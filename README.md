# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is an AI-powered educational web application for students. It uses Google's Gemini API to explain academic topics, answer doubts, create quizzes, generate revision notes, and support study planning.

## Features
- AI doubt solving
- Topic explanations
- Quiz generation
- Revision notes
- Study-plan assistance
- Responsive web interface
- Secure server-side Gemini API call

## Tech Stack
- HTML
- CSS
- JavaScript
- Node.js
- Express
- Google Gemini API

## Run locally

1. Install Node.js.
2. Open this project folder in a terminal.
3. Run:

```bash
npm install
```

4. Create a `.env` file by copying `.env.example`.
5. Put your Gemini API key in `.env`:

```env
GEMINI_API_KEY=your_real_key
PORT=3000
```

6. Start:

```bash
npm start
```

7. Open `http://localhost:3000`

## GitHub / Render

Do NOT upload `.env` or your API key to GitHub.

On Render, create a Web Service, connect this GitHub repository, use:
- Build Command: `npm install`
- Start Command: `npm start`

Add `GEMINI_API_KEY` under Render Environment Variables.

## Project title

Google Gemini Powered Learning Assistant – EduGenie

## Academic purpose

This project demonstrates how generative AI can support students with interactive explanations, practice questions, revision and personalized learning assistance.
