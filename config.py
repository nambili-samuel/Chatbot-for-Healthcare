"""
Configuration settings for the AutoMed Healthcare Chatbot.
Contains agent configurations and setup utilities.
"""

import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API configuration
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Agent configurations
agent_configs = {
    "healthcare_facilitator": {
        "model": "gpt-4o",
        "temperature": 0.7,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}]
    },
    "mental_health_specialist": {
        "model": "gpt-4o",
        "temperature": 0.5,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}],
        "system_message": """You are a mental health specialist with expertise in psychology and counseling. 
        You provide supportive, empathetic responses to mental health concerns. You can:
        - Offer coping strategies for anxiety, depression, and stress
        - Provide mindfulness and relaxation techniques
        - Suggest when to seek professional help
        - Offer general mental health education
        - NEVER provide diagnoses or replace professional care
        
        Always be compassionate, non-judgmental, and encourage users to seek licensed professionals for serious concerns."""
    },
    "medical_advisor": {
        "model": "gpt-4o",
        "temperature": 0.3,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}],
        "system_message": """You are a medical advisor with knowledge of symptoms, conditions, and general health information. You can:
        - Provide information about common symptoms and conditions
        - Offer general health advice and wellness tips
        - Suggest over-the-counter remedies for minor issues
        - Explain medical terms in simple language
        - Recommend when to see a healthcare provider
        - NEVER provide diagnoses, prescriptions, or emergency advice
        
        Always emphasize that you're not a substitute for professional medical care and encourage users to consult doctors for medical concerns."""
    },
    "appointment_coordinator": {
        "model": "gpt-4o",
        "temperature": 0.5,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}],
        "system_message": """You help users schedule healthcare appointments and manage medical reminders. You can:
        - Help find appropriate healthcare providers based on symptoms
        - Suggest questions to ask during appointments
        - Set up medication or appointment reminders
        - Provide tips for preparing for medical visits
        - Explain different types of healthcare specialists
        
        Note: You don't actually book appointments but can guide users through the process."""
    },
    "safety_moderator": {
        "model": "gpt-4o",
        "temperature": 0.1,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}],
        "system_message": """You are a safety moderator ensuring all medical advice follows ethical guidelines. You:
        - Flag potentially dangerous or inappropriate medical advice
        - Ensure disclaimers are present when discussing health topics
        - Prevent sharing of unverified or harmful information
        - Ensure responses respect privacy and ethical standards
        - Intervene when agents might be overstepping their boundaries
        
        Your role is crucial for maintaining a safe, responsible healthcare chatbot."""
    },
    "manager": {
        "model": "gpt-4o",
        "temperature": 0.7,
        "timeout": 120,
        "cache_seed": 42,
        "config_list": [{"model": "gpt-4o", "api_key": api_key}]
    }
}

def configure_agents():
    """
    Create and configure all agents for the healthcare chatbot.
    Returns a dictionary of configured agents.
    """
    # Healthcare Facilitator - main coordinator
    healthcare_facilitator = AssistantAgent(
        name="Healthcare_Facilitator",
        system_message="""You are the main healthcare facilitator. You:
        - Welcome users and understand their healthcare needs
        - Route questions to the appropriate specialist agents
        - Coordinate responses from multiple specialists
        - Ensure the conversation flows naturally
        - Provide a summary of recommendations at the end
        
        You're friendly, professional, and empathetic. Always maintain HIPAA-like privacy standards.""",
        llm_config=agent_configs["healthcare_facilitator"],
        human_input_mode="NEVER"
    )
    
    # Mental Health Specialist
    mental_health_specialist = AssistantAgent(
        name="Mental_Health_Specialist",
        system_message=agent_configs["mental_health_specialist"]["system_message"],
        llm_config=agent_configs["mental_health_specialist"],
        human_input_mode="NEVER"
    )
    
    # Medical Advisor
    medical_advisor = AssistantAgent(
        name="Medical_Advisor",
        system_message=agent_configs["medical_advisor"]["system_message"],
        llm_config=agent_configs["medical_advisor"],
        human_input_mode="NEVER"
    )
    
    # Appointment Coordinator
    appointment_coordinator = AssistantAgent(
        name="Appointment_Coordinator",
        system_message=agent_configs["appointment_coordinator"]["system_message"],
        llm_config=agent_configs["appointment_coordinator"],
        human_input_mode="NEVER"
    )
    
    # Safety Moderator
    safety_moderator = AssistantAgent(
        name="Safety_Moderator",
        system_message=agent_configs["safety_moderator"]["system_message"],
        llm_config=agent_configs["safety_moderator"],
        human_input_mode="NEVER"
    )
    
    # User Proxy Agent
    user_proxy = UserProxyAgent(
        name="User_Proxy",
        human_input_mode="ALWAYS",  # Always take input from user
        max_consecutive_auto_reply=10,
        code_execution_config=False,
        system_message="A human user interacting with the healthcare chatbot system."
    )
    
    return {
        "user_proxy": user_proxy,
        "healthcare_facilitator": healthcare_facilitator,
        "mental_health_specialist": mental_health_specialist,
        "medical_advisor": medical_advisor,
        "appointment_coordinator": appointment_coordinator,
        "safety_moderator": safety_moderator
    }