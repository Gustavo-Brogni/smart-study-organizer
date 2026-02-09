from typing import Final

'''
Configuration file for Smart Study Organizer
'''

# LM Studio API Configuration
API_URL: str = "http://localhost:1234/v1/chat/completions"

# Languages available for output

LANGUAGES: Final[dict[str, str]] = {
    "pt": "Portuguese",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}

# Modes for the AI

MODES: dict[str, dict[str, str]] = {

    "complement": {
        "name": "Complement",
        "prompt": """You are a specialized educational assistant. Analyze these class notes and:

    1. Identify gaps, incomplete explanations, or shallow coverage in the notes and complement them with relevant, accurate technical information
    2. Add practical, real-world examples to illustrate abstract or complex concepts, making them more tangible
    3. Expand on key definitions and terminology by providing context, etymology when useful, and connections to related concepts
    4. Clarify ambiguous or poorly explained passages by rewriting them in a clear, pedagogically sound manner
    5. Where applicable, include diagrams descriptions, analogies, or step-by-step breakdowns to deepen understanding
    6. Add a dedicated "Common Misconceptions" section addressing frequent errors or misunderstandings related to the topics covered
    7. End with a "Suggested Resources" section listing specific topics to search for, recommended reading areas, and types of exercises to practice
    8. Preserve the original structure and flow of the notes — complement, do not replace
    9. The output needs to be in {language}

    NOTES:
    {notes}

    DETAILED COMPLEMENT"""

    },

    "summarize": {
        "name": "Summarize",
        "prompt": """You are a specialized educational assistant. Analyze these class notes and:

    1. Condense the content into a concise, well-structured summary preserving all key concepts, definitions, and main ideas
    2. Organize the summary using clear headings and bullet points for each major topic covered
    3. Highlight critical terms and their definitions in a dedicated "Key Terms" section
    4. Identify and list the core takeaways in a numbered "Main Ideas" section at the top
    5. Preserve any formulas, data, or factual details essential for exam preparation
    6. Remove redundancies, filler content, and tangential remarks while retaining academic rigor
    7. End with a brief "Connections & Context" note linking the summarized topics to broader subject themes
    8. The output needs to be in {language}

    NOTES:
    {notes}

    STRUCTURED SUMMARY"""
    },

    "quiz": {
        "name": "Quiz",
        "prompt": """You are a specialized educational assistant. Analyze these class notes and:

    1. Generate a comprehensive quiz covering all major topics, concepts, and details found in the notes
    2. Include a balanced variety of question types: Multiple Choice (4 options each), True/False, and Short Answer
    3. Organize questions into three difficulty tiers: Basic (recall and definitions), Intermediate (application and comprehension), and Advanced (analysis and critical thinking)
    4. Provide a minimum of 10 questions total, distributed proportionally across the difficulty tiers
    5. For Multiple Choice questions, ensure distractors are plausible and pedagogically meaningful
    6. After all questions, include a clearly separated "ANSWER KEY" section with correct answers and brief explanations for each
    7. Number all questions sequentially and label each with its type and difficulty level (e.g., "[MC | Intermediate]")
    8. The output needs to be in {language}

    NOTES:
    {notes}

    QUIZ OUTPUT"""

    },

    "flashcards": {
        "name": "Flashcards",
        "prompt": """You are a specialized educational assistant. Analyze these class notes and:

    1. Transform the content into flashcard-style question-answer pairs optimized for spaced repetition learning
    2. Create one flashcard for each key concept, definition, formula, process, or important fact in the notes
    3. Write the "Front" (question/prompt) to be specific and unambiguous, targeting a single piece of knowledge
    4. Write the "Back" (answer) to be concise yet complete, ideally one to three sentences
    5. Order flashcards from foundational concepts to more advanced topics to support progressive learning
    6. Use the following strict format for each card to ensure easy parsing and import into flashcard applications:
       --- CARD [number] ---
       FRONT: [question or prompt]
       BACK: [answer]
       TAGS: [comma-separated topic tags]
    7. Include a minimum of 15 flashcards covering the full breadth of the notes
    8. The output needs to be in {language}

    NOTES:
    {notes}

    FLASHCARD FORMAT"""

    }
}


# Processing configuration
MAX_CHARS: int = 8000
TEMPERATURE: float = 0.7
MAX_TOKENS: int = 2000

# Output Configuration
OUTPUT_FILE: str = "complemented_notes.txt"