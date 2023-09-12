import streamlit as st

# st.set_page_config(page_icon=':white_check_mark:')

st.markdown(
    """
    <style>
    /* Custom Streamlit theme styles */
    h1 {
        color: #0E8992; /* Blue color for h1 (title) */
        font-size: 55px; /* Increase font size for h1 */
        font-weight: bold; /* Bold font for h1 */
    }

    h2 {
        color: #E9A27C; /* orange color for h2 (header) */
        font-size: 28px; /* Increase font size for h2 */
        font-style: ; /* Italic style for h2 */
    }

    p {
        color: #333333; /* Dark gray color for text (p) */
        font-size: 14px; /* Increase font size for text (p) */
        font-weight: ; /* Bold text for paragraphs */
    }

    /* Style buttons with an elegant color */
    .elegant-button {
        background-color: #1976D2; /* Blue background for buttons */
        color: white; /* White text for buttons */
        font-weight: bold; /* Bold text for buttons */
        padding: 10px 20px; /* Padding for buttons */
        border: none; /* Remove button border */
        border-radius: 5px; /* Add button border radius */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Adding informative content to the page

st.title("About Diabetes")

st.markdown("""
**Diabetes** is a chronic medical condition characterized by high levels of glucose (sugar) in the blood.

It affects how our body uses energy from food. Insulin helps, but diabetes can lead to high blood sugar, this can lead to serious health problems, like heart disease and vision issues. While there's no cure, managing diabetes with a healthy lifestyle and medication can make a big difference.
""")

st.header("Types of Diabetes 🩸")
st.markdown("""
**There are several types of diabetes, including**:

- **Type 1 Diabetes:** Usually diagnosed in children and young adults. The immune system mistakenly attacks and destroys insulin-producing cells in the pancreas.

- **Type 2 Diabetes:** Most common type, often linked to lifestyle factors like obesity and physical inactivity. The body becomes resistant to insulin.

- **Gestational Diabetes:** Occurs during pregnancy and typically resolves after childbirth.
""")

st.header("Diabetes Management 💼")
st.markdown("""
**Effective diabetes management is crucial to prevent complications. It involves**:

- Monitoring blood sugar levels regularly.
- Medication or insulin therapy as prescribed by a healthcare provider.
- Following a balanced diet that controls carbohydrate intake.
- Engaging in regular physical activity.
- Maintaining a healthy weight.
""")

st.header("Risk Factors and Prevention 🔍")
st.markdown("""
**Common risk factors for diabetes include genetics, unhealthy eating habits, lack of physical activity, and obesity. You can reduce your risk by**:

- Maintaining a healthy weight.
- Eating a balanced diet with a focus on fruits, vegetables, and whole grains.
- Exercising regularly.
- Monitoring your blood sugar levels if you're at risk.
""")

st.header("Complications 📉")
st.markdown("""
**Uncontrolled diabetes can lead to serious complications, including:**

- Heart disease and stroke.
- Kidney disease.
- Neuropathy (nerve damage).
- Vision problems, including blindness.
- Foot problems, which can lead to amputation.
""")

st.header("Treatment Options 💊 ")
st.markdown("""
**Treatment options vary depending on the type and severity of diabetes. They may include:**

- Medications to lower blood sugar.
- Insulin therapy.
- Lifestyle changes, including diet and exercise.
- Regular check-ups with healthcare providers.
""")

st.header("Additional Information ℹ️")
st.markdown("""
For more information and support, consider visiting diabetes-related organizations and forums. Stay connected with healthcare providers for personalized guidance.
""")

