def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> list[str]:
    """
    Splits text into overlapping chunks, trying to break on sentence
    boundaries where possible rather than mid-word.

    chunk_size: target max characters per chunk
    overlap: characters repeated from the end of one chunk at the start of the next
    """
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        if end >= text_length:
            chunk = text[start:text_length]
            chunks.append(chunk.strip())
            break

        search_window = text[start:end]
        last_period = search_window.rfind('. ')
        last_newline = search_window.rfind('\n')
        break_point = max(last_period, last_newline)

        if break_point == -1 or break_point < chunk_size * 0.5:
            actual_end = end
        else:
            actual_end = start + break_point + 1

        chunk = text[start:actual_end].strip()
        if chunk:
            chunks.append(chunk)

        start = actual_end - overlap
        if start < 0:
            start = actual_end

    return chunks
