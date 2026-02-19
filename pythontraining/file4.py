from docx import Document

doc = Document("h:\\hello.docx")

for para in doc.paragraphs:
    print(para.text)