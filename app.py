from flask import Flask, render_template, request
from parser import extract_text_from_PDF
from matcher import get_match_score, extract_skills, compare_skills
from gen_ai import generate_feedback_gemini
from vector_databases import skill_list
from visuals import plot_skill_charts
import markdown
import os

# Initialize Flask App
app = Flask(__name__)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description_text = request.form['jd_text']
        
        if resume_file and job_description_text.strip():
            # Extract text from resume
            resume_text = extract_text_from_PDF(resume_file)
            
            # Calculate match score
            match_score = get_match_score(resume_text, job_description_text)

            # Extract skills
            resume_skills = extract_skills(resume_text, skill_list)
            job_description_skills = extract_skills(job_description_text, skill_list)
            matched_skills, missing_skills = compare_skills(resume_skills, job_description_skills)

            # Generate Gemini feedback
            feedback = generate_feedback_gemini(resume_text, job_description_text)
            feedback_html = markdown.markdown(feedback)

            # Visual graphs
            from visuals import plot_skill_charts

            plot_skill_charts(matched_skills, missing_skills,
                            pie_path="static/pie_chart.png",
                            bar_path="static/bar_chart.png")


            
            return render_template('result.html', 
                                   match_score=match_score,
                                   feedback=feedback_html,
                                   matched_skills=matched_skills,
                                   missing_skills=missing_skills,
                                   )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
