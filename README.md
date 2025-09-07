# Multi-Agent Chatbot for Healthcare

A sophisticated multi-agent healthcare chatbot system built using Microsoft's AutoGen framework, this (AutoMed) is designed to provide preliminary healthcare guidance, mental health support, and medical information retrieval.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![AutoGen Version](https://img.shields.io/badge/autogen-0.2%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Agents](#agents)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Overview

AutoMed is a multi-agent healthcare chatbot system that leverages the power of Microsoft's AutoGen framework to create specialized AI agents that collaborate to provide comprehensive healthcare assistance. This system demonstrates how multiple AI agents with different specializations can work together to deliver more accurate and nuanced responses than a single AI model.

## Features

- **Multi-Agent Architecture**: Specialized agents for different healthcare domains
- **Mental Health Support**: Dedicated mental health assessment and support
- **Symptom Analysis**: Preliminary symptom checking and triage recommendations
- **Medical Information Retrieval**: Evidence-based medical information provision
- **Appointment Scheduling**: Integration with calendar systems for healthcare appointments
- **Privacy-Focused**: Designed with healthcare data privacy considerations
- **Extensible Framework**: Easy to add new specialized agents

## Architecture

The system employs multiple specialized agents:

1. **Healthcare Facilitator**: Coordinates interactions between user and specialized agents
2. **Mental Health Specialist**: Provides mental health support and assessment
3. **Medical Advisor**: Offers preliminary symptom analysis and medical information
4. **Appointment Coordinator**: Helps schedule healthcare appointments
5. **Safety Moderator**: Ensures responses adhere to medical safety guidelines

These agents collaborate through group chats managed by AutoGen's GroupChat manager, ensuring each query is handled by the most appropriate specialist.

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for GPT-4o models)
- (Optional) Azure OpenAI Service credentials

### Steps

1. Clone the repository:
```bash
git clone https://github.com/nambili-samuel/automed-healthcare-chatbot.git
cd automed-healthcare-chatbot
