#!/usr/bin/env python3
"""
Simplified Healthcare Chatbot using AutoGen
"""

import os
import logging
from dotenv import load_dotenv
from autogen import ConversableAgent, GroupChat, GroupChatManager

# Suppress warnings from autogen.oai.client
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Please set your OPENAI_API_KEY in the .env file")
    exit(1)

# LLM Configuration
llm_config = {
    "config_list": [
        {
            "model": "gpt-4o", 
            "api_key": api_key
        }
    ],
    "timeout": 120,
    "cache_seed": 42
}

# Create AI Agents with distinct roles
patient_agent = ConversableAgent(
    name="Patient",
    system_message="You describe your emotions, symptoms, and health concerns in detail.",
    llm_config=llm_config
)

healthcare_facilitator = ConversableAgent(
    name="Healthcare_Facilitator",
    system_message="""You are the main healthcare facilitator. You:
    - Welcome users and understand their healthcare needs
    - Route questions to the appropriate specialist agents
    - Coordinate responses from multiple specialists
    - Ensure the conversation flows naturally
    - Provide a summary of recommendations at the end
    
    You're friendly, professional, and empathetic. Always maintain privacy standards.""",
    llm_config=llm_config
)

mental_health_specialist = ConversableAgent(
    name="Mental_Health_Specialist",
    system_message="""You are a mental health specialist with expertise in psychology and counseling. 
    You provide supportive, empathetic responses to mental health concerns. You can:
    - Offer coping strategies for anxiety, depression, and stress
    - Provide mindfulness and relaxation techniques
    - Suggest when to seek professional help
    - Offer general mental health education
    - NEVER provide diagnoses or replace professional care
    
    Always be compassionate, non-judgmental, and encourage users to seek licensed professionals for serious concerns.""",
    llm_config=llm_config
)

medical_advisor = ConversableAgent(
    name="Medical_Advisor",
    system_message="""You are a medical advisor with knowledge of symptoms, conditions, and general health information. You can:
    - Provide information about common symptoms and conditions
    - Offer general health advice and wellness tips
    - Suggest over-the-counter remedies for minor issues
    - Explain medical terms in simple language
    - Recommend when to see a healthcare provider
    - NEVER provide diagnoses, prescriptions, or emergency advice
    
    Always emphasize that you're not a substitute for professional medical care.""",
    llm_config=llm_config
)

safety_moderator = ConversableAgent(
    name="Safety_Moderator",
    system_message="""You are a safety moderator ensuring all medical advice follows ethical guidelines. You:
    - Flag potentially dangerous or inappropriate medical advice
    - Ensure disclaimers are present when discussing health topics
    - Prevent sharing of unverified or harmful information
    - Ensure responses respect privacy and ethical standards
    - Intervene when agents might be overstepping their boundaries
    
    Your role is crucial for maintaining a safe, responsible healthcare chatbot.""",
    llm_config=llm_config
)

# Create GroupChat for AI Agents
groupchat = GroupChat(
    agents=[healthcare_facilitator, mental_health_specialist, medical_advisor, safety_moderator],
    messages=[], 
    max_round=6,  # Ensures the conversation doesn't stop too early
    speaker_selection_method="round_robin"
)

# Create GroupChatManager
manager = GroupChatManager(
    groupchat=groupchat,
    name="Manager",
    llm_config=llm_config
)

# Function to start the chatbot interaction
def start_healthcare_chat():
    """Runs a healthcare chatbot with multiple specialized agents."""
    print("\n" + "="*60)
    print("Welcome to the AI Healthcare Chatbot!")
    print("Type 'exit' to end the conversation at any time")
    print("="*60)
    
    while True:
        user_input = input("\nHow can I help you with your health today? ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Thank you for using our healthcare chatbot. Stay healthy!")
            break
        
        print("\n" + "-"*40)
        print("Processing your request...")
        print("-"*40)
        
        try:
            # Initiate conversation with the healthcare facilitator
            patient_agent.initiate_chat(
                manager, 
                message=user_input,
                max_turns=2
            )
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again or check your configuration.")

if __name__ == "__main__":
    start_healthcare_chat()