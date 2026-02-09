# AI Notes Complementer

A system that uses a local AI (in this case LM Studio) to complement class notes with additional information that may be relevant given the context.

## Current Status
Under active development - This is a learning project

## Current Features
- Reading notes file (currently .txt);
- Complementation via local AI (LM Studio);
- Generation of organized complemented file.

## Technologies
- Python 3
- LM Studio (I'm using Mistral 3B)
- requests library

## Next Steps
- [ ] Process multiple files
- [ ] Google Drive integration
- [ ] Graphical interface
- [ ] OCR for physical notebooks

## How to Use
1. Have an LM Studio server running locally with an LLM model loaded;
2. Place your notes in a 'notes.txt' file;
3. Run: 'python complementer.py'
4. Result available in: 'complemented_notes.txt'