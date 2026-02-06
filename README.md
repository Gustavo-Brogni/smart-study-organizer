# AI Note Complementer

A system that uses a local AI (in this case LM Studio) to complement class notes with additional information that may be relevant to the context.

## Current Status
In active development - This is a learning project

## Current Features
- Reading note files (currently .txt);
- Complementation via local AI (LM Studio);
- Generation of organized complementary file.

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
3. Run: 'python complement.py'
4. Result available in: 'notes_complemented.txt'