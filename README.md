# Smart Study Organizer

An intelligent system that uses a local AI (LM Studio) to enhance class notes with complementary information, summaries, quizzes, and flashcards based on context and user preferences.

<!-- Language -->
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)

<!-- Status -->
![Status](https://img.shields.io/badge/status-active-success.svg)

<!-- Licença -->
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Current Status
Active development - Educational learning project

## Motivation

Built as a learning project to organize my class notes while also exploring Python development, AI integration, Git and
software architecture best practices.

## Current Features
- Reading multiple note files (.txt format)
- 4 processing modes:
  - **Complement**: Expand notes with detailed explanations, examples, and additional context
  - **Summarize**: Create structured summaries with key terms and main ideas
  - **Quiz**: Generate comprehensive quizzes with multiple difficulty levels
  - **Flashcards**: Convert notes into spaced-repetition flashcard format
- Language selection (Portuguese, English, Spanish, French, German)
- Local AI processing via LM Studio
- Organized output file generation


## Technologies
- Python 3
- LM Studio (tested with Mistral 3B)
- requests library

## Roadmap
- [ ] Support for additional file formats (.pdf, .docx)
- [ ] Google Drive integration
- [ ] Graphical user interface (GUI)
- [ ] OCR for physical notebooks
- [ ] Export to flashcard applications

## How to Use
1. Ensure LM Studio is running locally with an LLM model loaded
2. Run: `python complementer.py`
3. Select:
   - Number of files to process
   - File names/paths
   - Processing mode (1-4)
   - Output language
4. View results in: `complemented_notes.txt`

## Project Structure
- `complementer.py` - Main processing module
- `config.py` - Configuration and prompt templates
- `.gitignore` - Git ignore rules

## License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

## Author

**Gustavo Brogni**

- GitHub: [@Gustavo-Brogni](https://github.com/Gustavo-Brogni)
- Email: gustavobrg22@protonmail.com
