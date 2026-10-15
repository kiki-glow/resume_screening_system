# Resume Screening System - a freeCodeCamp inspo
The system takes a folder of resumes and a Job Description (JD) as input. It then processes each resume, extracts relevant info, and calculates a score based on how well the candidate matches the job requirements.

## Score formula
```math
Total Score = (Required Skills * 50\%) + 
(Preferred Skills * 25\%) + 
(Experience * 15\%) + (Keywords * 10\%)
```

## Project Structure
- **app.py** # Streamlit web interface
- **main.py** # Command-line interface
- **parsers/**
    - **resume_parser.py** # PDF/DOCX text extraction
    - **jd_parser.py** # Job description parsing
- **extractors/**
    - **keyword_extractor.py** # Skills and experience extraction
- **matcher/**
    - **scorer.py** # Scoring algorithm
- **data**
    - **config.json** # Scoring weights
    - **skills_taxonomy.json** # Skills database
- **requirements.txt** # Dependencies

## Setup the project
```bash
mkdir resume_screening_system
cd resume_screening_system
mkdir parsers extractors matcher data input output
python -m venv venv

# Windows
source venv/Scripts/activate || venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

pip install PyPDF2 python-docx streamlit pandas
```

---
## Author
**Kinya Glory**
GitHub: https://github.com/kiki-glow