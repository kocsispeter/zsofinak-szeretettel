import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date

# Oldal konfigurálása
st.set_page_config(
    page_title="Karácsonyi Szeretet",
    page_icon="🎄",
    layout="wide"
)

# Karácsonyi CSS stílus
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#ff5c5c, #2e8b57);
    }
    .christmas-title {
        text-align: center;
        color: #2e8b57;
        font-size: 2.5em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        margin-bottom: 1em;
    }
    .christmas-card {
        background: #2e8b57;  /* Sötétebb zöld háttér */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin: 10px 0;
        color: white;  /* Fehér szöveg */
        border: 2px solid #ff5c5c;  /* Piros keret */
    }
    .christmas-card h4 {
        color: #ffd700;  /* Arany színű címek */
        margin-bottom: 10px;
        font-weight: bold;
    }
    .christmas-card p {
        color: white;  /* Fehér szöveg a jobb olvashatóságért */
        margin: 5px 0;
    }
    .christmas-card i {
        color: #ffeb99;  /* Világosabb arany az idézetekhez */
    }
    .countdown-box {
        background: #ff5c5c;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
        border: 2px solid #2e8b57;
    }
    .section-title {
        color: #ff5c5c;  /* Piros szín a szekció címekhez */
        font-weight: bold;
        font-size: 1.5em;
        margin-bottom: 1em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Főcím
st.markdown('<h1 class="christmas-title">🎄 Karácsonyi Szeretet 🎄</h1>', unsafe_allow_html=True)

# Karácsonyig hátralevő idő számláló
today = date.today()
christmas = date(today.year, 12, 25)
if today > christmas:
    christmas = date(today.year + 1, 12, 25)
delta = christmas - today

st.sidebar.markdown(
    '<div class="countdown-box">'
    f'<h3>Karácsonyig még</h3>'
    f'<h2>{delta.days} nap</h2>'
    '</div>',
    unsafe_allow_html=True
)

# Két oszlop létrehozása
col1, col2 = st.columns([2, 1])

# Karácsonyi aktivitások adatai
activities_data = {
    "activity": [
        "Karácsonyi sütés együtt",
        "Ajándékok közös becsomagolása",
        "Karácsonyi vásár látogatása",
        "Forró csoki készítése",
        "Karácsonyi filmek nézése",
        "Díszítés közösen",
        "Adventi kalendárium készítése",
        "Összebújás"
    ],
    "joy_level": [110, 106, 101, 103, 110, 102, 104, 108],
    "memory": [
        "Mézeskalács illata",
        "Csillogó szalagok",
        "Fények és fenyőillat",
        "Kávé és fahéj",
        "Meghitt pillanatok",
        "Csillogó díszek",
        "Meglepetések öröme",
        "Dallamok varázsa"
    ]
}

activities_df = pd.DataFrame(activities_data)

with col1:
    # Interaktív karácsonyi aktivitás vizualizáció
    chart_type = st.selectbox(
        "Válassz egy megjelenítési módot",
        ["Örömszint Diagram", "Karácsonyi Kördiagram", "Aktivitás Radar"]
    )

    if chart_type == "Örömszint Diagram":
        fig = px.bar(
            activities_df,
            x="activity",
            y="joy_level",
            title="Karácsonyi Aktivitások Örömszintje",
            color="joy_level",
            color_continuous_scale=["red", "green"]
        )
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Karácsonyi Kördiagram":
        fig = px.pie(
            activities_df,
            values="joy_level",
            names="activity",
            title="Karácsonyi Aktivitások Megoszlása",
            color_discrete_sequence=px.colors.sequential.Reds
        )
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Aktivitás Radar":
        fig = go.Figure(data=go.Scatterpolar(
            r=activities_df["joy_level"],
            theta=activities_df["activity"],
            fill='toself',
            line_color='red'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            title="Karácsonyi Aktivitások Radar Diagramja"
        )
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown('<h3 class="section-title">🎅 Karácsonyi Teendők</h3>', unsafe_allow_html=True)
    for _, row in activities_df.iterrows():
        st.markdown(f"""
        <div class="christmas-card">
            <h4>🎄 {row['activity']}</h4>
            <p><strong>Öröm szint:</strong> {row['joy_level']}%</p>
            <p><i>"{row['memory']}"</i></p>
        </div>
        """, unsafe_allow_html=True)

# Interaktív karácsonyi üzenet generátor
st.markdown('<h3 class="section-title">✉️ Karácsonyi Üzenet Generátor</h3>', unsafe_allow_html=True)
recipient = st.text_input("Kinek szeretnél üzenni?")
if recipient:
    message_type = st.selectbox(
        "Válassz egy üzenet típust",
        ["Romantikus", "Vicces", "Klasszikus"]
    )

    messages = {
        "Romantikus": f"Kedves {recipient}! A karácsony veled még varázslatosabb. Szeretlek! ❤️🎄",
        "Vicces": f"Hé {recipient}! Ki mondta, hogy a Mikulás nem létezik? Mi ketten bebizonyítjuk! 🎅😄",
        "Klasszikus": f"Kedves {recipient}! Áldott, békés karácsonyt kívánok neked! ✨🎄"
    }

    st.markdown(f"""
    <div class="christmas-card">
        <p>{messages[message_type]}</p>
    </div>
    """, unsafe_allow_html=True)

# Powered by szekció
st.sidebar.markdown("""
<div style="text-align: center; background: linear-gradient(45deg, #f3ec78, #af4261); padding: 10px; border-radius: 5px; color: white; margin-top: 20px;">
    <p style="margin: 0; font-size: 12px;">Powered by</p>
    <p style="margin: 0; font-weight: bold; font-size: 16px;">Kocsis Péter</p>
</div>
""", unsafe_allow_html=True)

# Lábléc
st.sidebar.markdown("---")
st.sidebar.markdown("Készült Streamlit-tel 🎄")