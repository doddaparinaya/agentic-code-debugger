# Agentic-Code-Debugger
Built an Agentic AI-based debugging system using LangGraph that detects, explains, and fixes code issues autonomously using LLMs with structured outputs and confidence scoring.
# Prerequisites
  Python 3.8+ (3.10+ preferred)
  Ollama installed and running
# Architecture (WorkFlow)
                ┌────────────────────┐
                │   Input Code       │
                └─────────┬──────────┘
                          ↓
            ┌────────────────────────────┐
            │ Syntax Analyzer Agent      │
            │ - Detects errors           │
            │ - Identifies line numbers  │
            └─────────┬──────────────────┘
                      ↓
            ┌────────────────────────────┐
            │ Explanation Agent          │
            │ - Explains root cause      │
            │ - Assigns severity         │
            └─────────┬──────────────────┘
                      ↓
            ┌────────────────────────────┐
            │ Fix Generator Agent        │
            │ - Generates corrected code │
            │ - Improves structure       │
            └─────────┬──────────────────┘
                      ↓
            ┌────────────────────────────┐
            │ Confidence Evaluator       │
            │ - Scores fix reliability   │
            └────────────────────────────┘
  
