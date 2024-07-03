import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the survey questions and corresponding labels
questions = [
    "Your company effectively integrates various marketing and customer engagement channels (e.g., campaigns, content, media, live commerce, and events) to create a seamless customer experience.",
    "Your company utilizes personalization techniques and CRM tools to tailor the customer experience and manage customer relationships.",
    "Your company optimizes commerce operations (e.g., eStore/eRetail, field force management, promotions, merchandising, display, and CRO) for efficiency and effectiveness.",
    "Your company is proficient in leveraging technology platforms (e.g., publishing, platform management, development, QA, OPS, security) to support omnichannel commerce.",
    "Your company is effective in fostering community and social engagement through channels such as social commerce, influencers, gaming, and rewards programs.",
    "Your company effectively implements foundational systems (e.g., strategy, data management, AI/automation, cloud implementation) and strategic planning (e.g., audit and health check, MMM/attribution) to support omnichannel commerce."
]

labels = [
    "Integrated Marketing and Customer Engagement",
    "Personalization and CRM",
    "Commerce Operations and Optimization",
    "Technology and Platform Management",
    "Community Building and Social Engagement",
    "Foundational Systems and Strategic Planning"
]

# Create the Streamlit application
st.title("Connected Commerce Maturity Assessment")

# Initialize an empty list to store the responses
responses = []

# Loop through the questions and create a slider for each
for i, question in enumerate(questions):
    response = st.slider(question, 1, 5, 3)
    responses.append(response)

# When the survey is submitted, display a radar chart
if st.button("Submit"):
    # Convert the responses to a DataFrame
    df = pd.DataFrame([responses], columns=labels)

    # Function to plot radar chart
    def plot_radar_chart(data, labels):
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        data = data + data[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, data, color='red', alpha=0.25)
        ax.plot(angles, data, color='red', linewidth=2)

        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        return fig

    # Plot the radar chart
    radar_chart = plot_radar_chart(responses, labels)
    st.pyplot(radar_chart)
