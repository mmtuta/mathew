import re
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name

def extract_email_from_resume(text):
    email = None

    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()

    return email

def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(\+\d{1,3}[-\.\s]??\d{1,4}[-\.\s]??\d{1,4}[-\.\s]??\d{1,4})\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number

def extract_skills_from_resume(text, skills_list):
    skills = []

    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills

def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education

def extract_experience_from_resume(text):
    experience = None

    # Use regex pattern to find total experience
    pattern = r"\b(\d+(?:\.\d+)?)\s*(?:years?|yrs?|yr|y)\b"
    match = re.search(pattern, text)
    if match:
        experience = match.group(1)

    return experience

def extract_designation_and_company_from_resume(text):
    designations = []
    companies = []

    # Use regex pattern to find designations and companies
    pattern = r"\b[A-Z][a-z]*(?:'[a-z]*)?\b\s*\-\s*\b[A-Za-z]+\b"
    matches = re.findall(pattern, text)
    for match in matches:
        designation, company = match.split(" - ")
        designations.append(designation.strip())
        companies.append(company.strip())

    return designations, companies

def extract_dates_from_resume(text):
    dates = []

    # Use regex pattern to find dates
    pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b"
    matches = re.findall(pattern, text)
    for match in matches:
        dates.append(match)

    return dates

if __name__ == '__main__':
    pdf_path = "path/to/your/resume.pdf"