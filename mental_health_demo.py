#!/usr/bin/env python3
"""
Demo script showing mental health consultation with the AutoMed chatbot.
"""

import os
import sys
sys.path.append('..')

from main import AutoMedHealthcareChatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def mental_health_demo():
    """Run a demo mental health consultation."""
    print("🧠 AutoMed Mental Health Demo")
    print("=" * 40)
    
    # Initialize chatbot
    chatbot = AutoMedHealthcareChatbot()
    
    # Demo conversation about anxiety and sleep issues
    demo_messages = [
        "I've been feeling really anxious lately and having trouble sleeping",
        "I worry about work constantly and it's affecting my sleep",
        "What are some techniques to manage this anxiety?",
        "How can I improve my sleep quality?"
    ]
    
    for message in demo_messages:
        print(f"\nUser: {message}")
        print("-" * 40)
        chatbot.start_chat(message)
        print("=" * 40)

if __name__ == "__main__":
    mental_health_demo()