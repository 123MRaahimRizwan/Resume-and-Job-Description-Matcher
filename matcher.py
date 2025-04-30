import spacy
from sentence_transformers import SentenceTransformer, util

semantic_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_match_score(resume_text, job_description_text):
    embeddings = semantic_model.encode([resume_text, job_description_text], convert_to_tensor=True)
    similarity_score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(similarity_score[0][0]) * 100, 2)

def extract_skills(text, skill_keywords):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    return list(set([token.text for token in doc if token.text in skill_keywords]))

def compare_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    return matched, missing