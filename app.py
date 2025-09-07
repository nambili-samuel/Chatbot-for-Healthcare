#!/usr/bin/env python3
"""
Flask web interface for the AutoMed Healthcare Chatbot.
"""

from flask import Flask, render_template, request, jsonify
import json
from main import AutoMedHealthcareChatbot
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
chatbot = None

@app.before_first_request
def initialize_chatbot():
    """Initialize the chatbot before first request."""
    global chatbot
    try:
        chatbot = AutoMedHealthcareChatbot()
        logger.info("AutoMed chatbot initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize chatbot: {e}")

@app.route('/')
def home():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # For demo purposes, we'll simulate a response
        # In a real implementation, you'd use the chatbot instance
        response = simulate_chatbot_response(message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

def simulate_chatbot_response(message):
    """
    Simulate chatbot response for demo purposes.
    In a real implementation, this would use the actual chatbot.
    """
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['anxious', 'stress', 'worry', 'depress']):
        return """I understand you're dealing with some difficult emotions. As your mental health specialist, I recommend:
        
1. Practice deep breathing exercises - inhale for 4 counts, hold for 4, exhale for 6
2. Try a 10-minute mindfulness meditation using an app like Calm or Headspace
3. Consider talking to a therapist who can provide personalized strategies
4. Maintain a regular sleep schedule and limit caffeine

Remember, I'm here for support, but for ongoing mental health concerns, please consult a licensed mental health professional."""

    elif any(word in message_lower for word in ['headache', 'fever', 'pain', 'sick']):
        return """As your medical advisor, I can suggest:

For headache and mild fever:
1. Rest and stay hydrated with water or electrolyte drinks
2. Over-the-counter pain relievers like acetaminophen may help (follow package instructions)
3. Use a cool compress on your forehead
4. Monitor your temperature - if it reaches 102°F or higher, consult a doctor

Please see a healthcare provider if symptoms worsen or persist beyond 3 days, or if you develop difficulty breathing, severe pain, or other concerning symptoms."""

    else:
        return """Thank you for sharing your health concerns. I'm connecting you with our healthcare specialists who can provide appropriate guidance.

As a reminder, I'm an AI assistant designed to offer general health information and support, but I cannot provide medical diagnoses or replace professional healthcare. For serious or emergency medical issues, please contact healthcare providers directly."""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)