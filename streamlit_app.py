import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config (This must be the first Streamlit command)
st.set_page_config(page_title="Miért Szeretem a Páromat", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#f6d8ac, #f1beb0);
    }
    .Widget>label {
        color: #462211;
        font-weight: bold;
    }
    .stButton>button {
        color: #4F8BF9;
        border-radius: 50%;
        height: 3em;
        width: 3em;
    }
    .stTextInput>div>div>input {
        color: #4F8BF9;
    }
    .powered-by {
        text-align: center;
        background: linear-gradient(45deg, #f3ec78, #af4261);
        padding: 10px;
        border-radius: 5px;
        color: white;
        margin-top: 20px;
    }
    .powered-by p {
        margin: 0;
        font-size: 12px;
    }
    .company-name {
        font-weight: bold;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Data
data = {
    "reason": [
        "Megértő és türelmes", "Remek humorérzék", "Támogató", "Jó hallgatóság",
        "Kedves és figyelmes", "Izgalmas és kalandvágyó", "Megbízható és lojális",
        "Intelligens beszélgetőpartner", "Vonzó külső", "Jól kiegészítjük egymást"
    ],
    "effect": [
        "Biztonság", "Nevetés", "Motiváció", "Megosztás", "Értékesség", "Új élmények",
        "Bizalom", "Stimuláció", "Fizikai vonzalom", "Harmónia"
    ],
    "value": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)

# Title
st.title("❤️ Miért Szeretem a Páromat ❤️")

# Sidebar for chart selection
chart_type = st.sidebar.selectbox(
    "Válassz egy diagram típust",
    ["Bar Chart", "Pie Chart", "Radar Chart", "Line Chart"]
)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Vizualizáció")

    if chart_type == "Bar Chart":
        fig = px.bar(df, x="reason", y="value", title="Okok és Értékek")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie Chart":
        fig = px.pie(df, values="value", names="reason", title="Okok Megoszlása")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Radar Chart":
        fig = go.Figure(data=go.Scatterpolar(
            r=df["value"],
            theta=df["reason"],
            fill='toself'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False,
            title="Okok Radar Diagramja"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Line Chart":
        fig = px.line(df, x="reason", y="value", title="Okok Trendje")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Részletes Lista")
    for _, row in df.iterrows():
        st.markdown(f"❤️ **{row['reason']}:** {row['effect']} ({row['value']})")

# Add an interactive element
st.subheader("Interaktív Elem")
selected_reason = st.selectbox("Válassz egy okot a részletekért", df["reason"])
selected_data = df[df["reason"] == selected_reason].iloc[0]
st.write(f"**Ok:** {selected_data['reason']}")
st.write(f"**Hatás:** {selected_data['effect']}")
st.write(f"**Érték:** {selected_data['value']}")

# Add a metric
st.sidebar.metric(label="Átlagos Érték", value=f"{df['value'].mean():.2f}")

# Add the fancy "Powered by" section
st.sidebar.markdown("""
<div class="powered-by">
    <p>Powered by</p>
    <p class="company-name">Kocsis Péter</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Készült Streamlit-tel ❤️")