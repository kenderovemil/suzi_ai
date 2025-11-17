# python
import os
from pdfminer.high_level import extract_text  # adjust to your parser if different

def parse_pdf(pdf_path: str) -> str:
    """Resolve the given pdf_path robustly and return extracted text.

    Resolution order (first existing candidate wins):
    - If pdf_path is absolute -> use it.
    - abspath(pdf_path)
    - If adding a leading '/' makes it absolute -> try that (fixes paths starting with 'media/...')
    - package data folder (suzi_core/data/<pdf_path>) for simple filenames
    """
    # quick guard
    if not pdf_path:
        print("[Suzi Parser] Грешка при парсване на PDF: empty path")
        return ""

    candidates = []

    # 1) exact absolute path
    if os.path.isabs(pdf_path):
        candidates.append(pdf_path)
    else:
        # 2) abspath(pdf_path) (treat as relative to CWD)
        candidates.append(os.path.abspath(pdf_path))

        # 3) try adding a leading slash (user may have copied an absolute path without the leading '/')
        if not pdf_path.startswith(os.sep):
            candidates.append(os.path.abspath(os.sep + pdf_path))

        # 4) treat as filename in package data folder
        candidates.append(os.path.join(os.path.dirname(__file__), "data", pdf_path))

    # Normalize candidates and pick the first that exists
    seen = set()
    full_path = None
    for c in candidates:
        if not c:
            continue
        norm = os.path.normpath(c)
        if norm in seen:
            continue
        seen.add(norm)
        if os.path.exists(norm):
            full_path = norm
            break

    if not full_path:
        # show attempted candidates for easier debugging
        tried = ", ".join([os.path.normpath(c) for c in candidates if c])
        print(f"[Suzi Parser] Грешка при парсване на PDF: no such file: '{tried}'")
        return ""

    # Extract text from the found PDF
    try:
        return extract_text(full_path)
    except Exception as e:
        print(f"[Suzi Parser] Грешка при извличане на текста от PDF: {e}")
        return ""
