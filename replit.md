# AI Love Compatibility Bot 💘

A fun and romantic web application that uses AI to generate compatibility reports between two people!

## Overview

This Flask web app uses Google's Gemini AI to analyze compatibility between two people based on their names, bios, and zodiac signs. The AI generates a humorous and creative compatibility report that includes:
- A love score out of 100 ❤️
- Zodiac compatibility commentary 🔮
- A unique "Love Aura Name" 💫
- A romantic poetic summary 💌

## Features

- Beautiful gradient UI (pink to purple) with floating heart animations
- Two-page flow: input form and results display
- Responsive design that works on all devices
- Clear, beginner-friendly code with extensive comments
- Secure API key management using Replit Secrets

## Project Structure

```
.
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html         # Input form page
│   └── result.html        # Results display page
├── static/
│   └── style.css          # Custom CSS styling
├── .gitignore             # Git ignore file
└── replit.md              # This documentation file
```

## Setup Instructions

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" or "Get API Key"
4. Copy the generated API key

### 2. Add API Key to Replit Secrets

**Good news!** Your `GOOGLE_API_KEY` is already configured in Replit Secrets, so you can skip this step and start using the app right away!

If you need to update or add the key:
1. In Replit, open the **Tools** menu in the left sidebar
2. Click on **Secrets**
3. Find `GOOGLE_API_KEY` or click **+ New Secret** to add it
4. Enter:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: Paste your API key from step 1
5. Click **Add Secret** or **Update**

### 3. Run the Application

The app is configured to run automatically! Just click the **Run** button at the top of Replit, and the Flask server will start on port 5000.

## How to Use

1. **Enter Person 1's Information**:
   - Name
   - Bio (hobbies, interests, personality)
   - Zodiac sign (optional)

2. **Enter Person 2's Information**:
   - Name
   - Bio (hobbies, interests, personality)
   - Zodiac sign (optional)

3. **Click "💘 Check Compatibility"**

4. **View the AI-Generated Report** with love score, zodiac commentary, and more!

5. **Try Another Match** by clicking the "Try Again" button

## Technology Stack

- **Backend**: Python 3.11 + Flask
- **AI**: Google Gemini API (gemini-1.5-flash model)
- **Frontend**: HTML5, CSS3 with custom animations
- **Templating**: Jinja2 (built into Flask)

## Code Highlights

### Flask Routes
- `/` - Homepage with input form
- `/generate` (POST) - Processes form and calls Gemini API

### Key Features
- Secure environment variable management
- Error handling for API failures
- Beautiful CSS animations (floating hearts)
- Responsive design
- User-friendly error messages

## Customization Ideas

- Add more zodiac signs and astrological features
- Store past compatibility checks in a database
- Add sharing functionality for results
- Create different compatibility algorithms
- Add user accounts and history

## Troubleshooting

**Problem**: "Gemini API key is not configured" error
- **Solution**: Make sure you've added `GEMINI_API_KEY` to Replit Secrets (see Setup Instructions above)

**Problem**: Changes not showing up
- **Solution**: Click the refresh button in the webview or restart the workflow

**Problem**: CSS not loading
- **Solution**: Clear your browser cache and hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

## Recent Changes

- **October 26, 2025**: Initial project creation
  - Created Flask application with Gemini AI integration
  - Designed romantic UI with gradient backgrounds and floating hearts
  - Implemented two-page flow (input form → results)
  - Added comprehensive error handling
  - Created beginner-friendly documentation

## User Preferences

- Clean, well-commented code for beginners
- Romantic and fun design aesthetic
- Emoji-rich user experience
- Secure API key management

## Security Notes

- API keys are stored in environment variables (never in code)
- Session secrets are managed via Replit Secrets
- No user data is stored permanently (privacy-first approach)

---

✨ **Enjoy discovering cosmic connections with AI magic!** ✨
