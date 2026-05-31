import fitz

pdf_path = r"C:\Users\Lenovo\OneDrive\Desktop\policy-gap-analysis\nist_framework.pdf.pdf"
doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text()

text = text.replace("\n", " ")

with open("nist_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("NIST PDF Parsed Successfully")