from suzi_core.document_parser import parse_pdf

# Use the filename exactly as it exists in suzi_core/data
pdf_text = parse_pdf("CV- francais.pdf")
if not pdf_text:
    print("No text extracted from PDF.")
else:
    print(pdf_text[:500])  # Първите 500 символа
