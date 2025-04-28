{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1bed9bef-5a9a-4d19-aae9-c7fb090243e1",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected character after line continuation character (3516072018.py, line 74)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 74\u001b[1;36m\u001b[0m\n\u001b[1;33m    cd path\\to\\your\\folder\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected character after line continuation character\n"
     ]
    }
   ],
   "source": [
    "# Save this as app.py\n",
    "\n",
    "import streamlit as st\n",
    "import openai\n",
    "\n",
    "# Set your OpenAI API Key\n",
    "openai.api_key = \"YOUR_OPENAI_API_KEY\"\n",
    "\n",
    "# Function to call GPT and generate document\n",
    "def generate_document(document_type, inputs):\n",
    "    prompt = f\"\"\"\n",
    "You are an expert legal draftsman. Draft a {document_type} based on the following inputs:\n",
    "\n",
    "Party A Name: {inputs['party_a_name']}\n",
    "Party B Name: {inputs['party_b_name']}\n",
    "Date: {inputs['date']}\n",
    "Jurisdiction: {inputs['jurisdiction']}\n",
    "Term/Duration: {inputs['term']}\n",
    "Scope/Purpose: {inputs['purpose']}\n",
    "Additional Clauses: {inputs['additional_clauses']}\n",
    "\n",
    "Please write it in a professional legal tone.\n",
    "\"\"\"\n",
    "\n",
    "    response = openai.ChatCompletion.create(\n",
    "        model=\"gpt-4-turbo\",\n",
    "        messages=[\n",
    "            {\"role\": \"system\", \"content\": \"You are a legal documentation assistant.\"},\n",
    "            {\"role\": \"user\", \"content\": prompt}\n",
    "        ],\n",
    "        temperature=0.3\n",
    "    )\n",
    "    return response['choices'][0]['message']['content']\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"📝 Legal Document Generator\")\n",
    "st.write(\"Generate professional legal drafts easily!\")\n",
    "\n",
    "with st.form(\"doc_form\"):\n",
    "    st.subheader(\"Enter Document Details\")\n",
    "    document_type = st.selectbox(\"Select Document Type\", [\"NDA\", \"Lease Agreement\", \"Power of Attorney\"])\n",
    "    party_a_name = st.text_input(\"Party A Name\")\n",
    "    party_b_name = st.text_input(\"Party B Name\")\n",
    "    date = st.date_input(\"Date\")\n",
    "    jurisdiction = st.text_input(\"Jurisdiction\")\n",
    "    term = st.text_input(\"Term/Duration\")\n",
    "    purpose = st.text_area(\"Scope/Purpose\")\n",
    "    additional_clauses = st.text_area(\"Additional Clauses (Optional)\", \"\")\n",
    "\n",
    "    submitted = st.form_submit_button(\"Generate Document\")\n",
    "\n",
    "if submitted:\n",
    "    inputs = {\n",
    "        \"party_a_name\": party_a_name,\n",
    "        \"party_b_name\": party_b_name,\n",
    "        \"date\": date,\n",
    "        \"jurisdiction\": jurisdiction,\n",
    "        \"term\": term,\n",
    "        \"purpose\": purpose,\n",
    "        \"additional_clauses\": additional_clauses\n",
    "    }\n",
    "    with st.spinner(\"Generating your document...\"):\n",
    "        document_text = generate_document(document_type, inputs)\n",
    "\n",
    "    st.success(\"Document Generated Successfully!\")\n",
    "    st.download_button(\n",
    "        \"Download Document as Text\",\n",
    "        document_text,\n",
    "        file_name=f\"{document_type.replace(' ', '_')}_Draft.txt\"\n",
    "    )\n",
    "    st.subheader(\"📄 Preview:\")\n",
    "    st.text_area(\"Generated Document\", document_text, height=400)\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
