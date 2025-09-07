#!/usr/bin/env python3
"""
Demo script showing symptom analysis with the AutoMed chatbot.
"""

import os
import sys
sys.path.append('..')

from main import AutoMedHealthcareChatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def symptom_checker_demo():
    """Run a demo symptom analysis consultation."""
    print("🌡️ AutoMed Symptom Checker Demo")
    print("=" * 40)
    
    # Initialize chatbot
    chatbot = AutoMedHealthcareChatbot()
    
    # Demo conversation about cold symptoms
    demo_messages = [
        "I've had a headache and sore throat for two days",
        "I also have a slight fever around 100°F",
        "What should I do to feel better?",
        "When should I consider seeing a doctor?"
    ]
    
    for message in demo_messages:
        print(f"\nUser: {message}")
        print("-" * 40)
        chatbot.start_chat(message)
        print("=" * 40)

if __name__ == "__main__":
    symptom_checker_demo()