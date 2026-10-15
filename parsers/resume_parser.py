def _extract_pdf(self, file_path: Path) -> str:
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2