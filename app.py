import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client properly
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_document(document_type, inputs):
    prompt = f"""
You are an expert legal draftsman. Draft a {document_type} based on the following inputs:

Party A Name: {inputs['party_a_name']}
Party B Name: {inputs['party_b_name']}
Date: {inputs['date']}
Jurisdiction: {inputs['jurisdiction']}
Term/Duration: {inputs['term']}
Scope/Purpose: {inputs['purpose']}
Additional Clauses: {inputs['additional_clauses']}

Please write it in a professional legal tone.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a legal documentation assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=2000
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("📝 Legal Document Generator")
st.write("Generate professional legal drafts easily!")

with st.form("doc_form"):
    st.subheader("Enter Document Details")
    document_type = st.selectbox("Select Document Type", ["NDA", "Lease Agreement", "Power of Attorney"])
    party_a_name = st.text_input("Party A Name")
    party_b_name = st.text_input("Party B Name")
    date = st.date_input("Date")
    jurisdiction = st.text_input("Jurisdiction")
    term = st.text_input("Term/Duration")
    purpose = st.text_area("Scope/Purpose")
    additional_clauses = st.text_area("Additional Clauses (Optional)", "")

    submitted = st.form_submit_button("Generate Document")

if submitted:
    inputs = {
        "party_a_name": party_a_name,
        "party_b_name": party_b_name,
        "date": date,
        "jurisdiction": jurisdiction,
        "term": term,
        "purpose": purpose,
        "additional_clauses": additional_clauses
    }
    with st.spinner("Generating your document..."):
        document_text = generate_document(document_type, inputs)

    st.success("Document Generated Successfully!")
    st.download_button(
        "Download Document as Text",
        document_text,
        file_name=f"{document_type.replace(' ', '_')}_Draft.txt"
    )
    st.subheader("📄 Preview:")
    st.text_area("Generated Document", document_text, height=400)
