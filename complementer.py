"""
Smart Study Organizer - Main Processing Module

This module handles the core functionality of reading notes files,
processing them with AI (via LM Studio) and saving an enhanced output.

Author: Gustavo Brogni
Date: February 2026
"""


import requests
import sys
from typing import Optional
from config import API_URL, MAX_CHARS, TEMPERATURE, MAX_TOKENS, OUTPUT_FILE, LANGUAGES, MODES

def get_files() -> list[str]:
    """
    Prompt user for file paths to process.

    Returns:
        list[str]: List of file paths entered by user
    """

    file_list = []
    while True:   
        try:
            num_files = int(input("Enter how many files you wish to complement: "))
            break     
        except ValueError:
            print("Please insert a valid value.")
            
    for i in range(num_files):
        file_path = input(f"Enter the name of the {i + 1}º file: ")
        file_list.append(file_path)
        
    return file_list

def read_txt(file_path: str) -> str:
    """
    Reads contents from a .txt file.

    Args:
        file_path: Path to the .txt file.

    Returns:
        str: File content.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(file_path: str) -> str:
    """
    Reads content from a .pdf file.

    Args:
        file_path: Path to the .pdf file.

    Returns:
        str: Extracted text from PDF
    """

    file_content = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            file_content += text

    return file_content


def read_docx(file_path: str) -> str:
    """
    Reads contents from a .docx file.

    Args:
        file_path: Path to the .docx file.

    Returns:
        str: Extracted text from DOCX
    """
    doc = Document(file_path)
    file_content = ""

    for paragraph in doc.paragraphs:
        file_content += paragraph.text + "\n"
    return file_content



def read_files(file_list: list[str]) -> str:
    """
    Reads the files contents.

    Args:
        file_list: List of files user wants to ead.

    Returns:
        str: Concatenated content from all files.
    """

    notes_contents = ""

    for file in file_list:
        if Path(file).suffix == ".txt":
            txtcontent = read_txt(file)
            notes_contents += txtcontent + "\n\n"
        elif Path(file).suffix == ".pdf":
            pdfcontent = read_pdf(file)
            notes_contents += pdfcontent + "\n\n"
        elif Path(file).suffix == ".docx":
            docxcontent = read_docx(file)
            notes_contents += docxcontent + "\n\n"
        else:
            print(f"Warning: '{file}' has unsupported extension or does not exist. The file has been skipped.")

    return notes_contents

def select_language() -> str:
    """
    Prompts the user to select a language for the AI output.

    Returns:
        The language which the user selects.
    """

    while True:
        print("Select output language.")
        for code, name in LANGUAGES.items():
            print(f"{code}: {name}")

        choice = input("Answer: ").strip().lower()

        if choice in LANGUAGES:
            return LANGUAGES[choice]
        else:
            print(f"Invalid choice. Please select one of the available languages: {', '.join(LANGUAGES.keys())}")

def select_mode() -> str:
    """
    Prompts the user to select an available type of answer for the AI output.

    Returns:
        The mode which the user selects.
    """

    while True:
        print("Select processing mode: ")

        mode_list = list(MODES.keys())

        for i, mode_key in enumerate(mode_list, 1):
            mode_name = MODES[mode_key]["name"]
            print(f"{i} - {mode_name}")

        choice = input("Enter number (1-4): ").strip()

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(mode_list):
                return mode_list[choice_num - 1]
            else:
                print(f"Invalid choice. Please select 1-{len(mode_list)}")
        except ValueError:
            print("Please enter a valid number.")

def complement_with_ai(notes_contents: str, selected_language: str, selected_mode: str) -> Optional[str]:
    """
    Processes the notes with AI.

    Args:
        notes_contents: The content of the notes
        selected_language: The selected language
        selected_mode: The selected mode

    Returns:
        Optional[str]: AI-generated content if sucessful or None if connection fails.
    """

    if len(notes_contents) > MAX_CHARS:
        notes_contents = notes_contents[:MAX_CHARS]
        print(f"The content was condensed to {MAX_CHARS} characters to fit context.")

    prompt = MODES[selected_mode]["prompt"].format(language = selected_language, notes = notes_contents)

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }


    while True:

        print("🔄 Processing...")

        try:
            response = requests.post(API_URL, json=data)
            ai_response = response.json()['choices'][0]['message']['content']
            return ai_response
        except requests.exceptions.ConnectionError:
            print("Critical error: Couldn't connect to LM Studio.")
            print("Verify if LM Studio is running with the server started.")

            while True:
                retry = input("Do you wish to try again? (y/n): ")
                if retry.lower() == "y":
                    break
                elif retry.lower() == "n":
                    return None
                else:
                    print("You inserted an invalid value.")

def save_files(notes_contents: str, ai_response: str) -> None:
    """
    Save original notes and AI response to output file.

    Args:
        notes_contents: The original contents of the notes
        ai_response: AI-generated content

    """


    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("=== ORIGINAL NOTES ===\n")
        file.write(notes_contents)
        file.write("\n\n" + "="*50 + "\n")
        file.write("\n\n=== AI RESPONSE ===\n")
        file.write(ai_response)

    print("✅ Complemented file saved!")

notes: str = ""

while True:

    files = get_files()

    try:
        notes = read_files(files)
        break
    except FileNotFoundError:
        print(f"File not found. Try again.")
        continue

mode = select_mode()
language = select_language()
ai_content = complement_with_ai(notes, language, mode)

if ai_content is not None:
    save_files(notes, ai_content)
else:
    print("Couldn't generate AI response. Exiting...")
    sys.exit(1)