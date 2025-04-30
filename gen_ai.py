def generate_feedback_gemini(resume_text, jd_text):
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyAyraabCrvV5wjMbqqZqIDLQScLNcAxFoA")

    model = genai.GenerativeModel('models/gemini-2.0-flash')
    prompt = f"""
Act as a resume advisor. Compare the following resume and job description.
Provide brief feedback on how well the resume fits the role, and what can be improved.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"