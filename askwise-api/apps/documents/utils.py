import os
import pypdf
import docx

def extract_text_from_file(file_path_or_object, file_name):
    """
    Extracts plain text from PDF, DOCX, TXT, and MD files.
    Works with both local file paths and Django uploaded file objects in memory.
    """
    ext = os.path.splitext(file_name)[1].lower()
    text = ""

    try:
        # Handle TXT and Markdown files
        if ext in ['.txt', '.md']:
            # Read bytes and decode to string
            content = file_path_or_object.read()
            text = content.decode('utf-8', errors='ignore')

        # Handle PDF files
        elif ext == '.pdf':
            reader = pypdf.PdfReader(file_path_or_object)
            page_texts = [page.extract_text() for page in reader.pages if page.extract_text()]
            text = "\n".join(page_texts)

        # Handle DOCX files
        elif ext == '.docx':
            doc = docx.Document(file_path_or_object)
            paragraphs = [p.text for p in doc.paragraphs if p.text]
            text = "\n".join(paragraphs)
            
    except Exception as e:
        # Fallback error string if a file is corrupted
        text = f"[Extraction Error: Unable to process file text. {str(e)}]"

    return text.strip()
