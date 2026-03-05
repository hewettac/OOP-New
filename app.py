import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Football Play Dashboard", layout="wide")
st.title("🏈 Football Playcalling Dashboard")
st.markdown("Analyze **Run vs Pass tendencies and play concepts by field position**")

# -------------------------
# Upload File
# -------------------------
uploaded_file = st.file_uploader("Upload Hudl Excel File", type=["xlsx","xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.lower().str.strip()

    # COLUMN MAP
    COLUMN_MAP = {
        "down": ["down", "dn"],
        "distance": ["dist", "togo", "yards to go", "ydstogo"],
        "yardline": ["yard ln", "spot", "ball on"],
        "concept": ["off play"],
        "play_type": ["play type", "playtype", "type"],
        "play_direction": ["play dir"],
        "gain_loss": ["gn/ls"]
    }

    rename_dict = {}
    for standard, variants in COLUMN_MAP.items():
        for col in df.columns:
            if col in variants:
                rename_dict[col] = standard
    df = df.rename(columns=rename_dict)

    df["yard_group"] = (df["yardline"] // 10) * 10

    # -------------------------
    # Filters
    # -------------------------
    st.sidebar.header("Filters")
    down_selected = st.sidebar.selectbox("Down", sorted(df["down"].dropna().unique()))
    df_down = df[df["down"] == down_selected]

    yard_choices = sorted(df_down["yard_group"].dropna().unique())
    yard_choice = st.sidebar.selectbox("Yard Group", yard_choices)

    # -------------------------
    # Field Scatter Plot (Football Field Style)
    # -------------------------
    summary = (
        df_down.groupby(["yard_group", "play_type"])
        .agg(count=("play_type", "count"))
        .reset_index()
    )
    totals = summary.groupby("yard_group")["count"].transform("sum")
    summary["percentage"] = summary["count"] / totals

    fig = px.scatter(
        summary,
        x="yard_group",
        y="percentage",
        size="count",
        color="play_type",
        color_discrete_map={"Run":"#2ecc71","Pass":"#e74c3c"},
        hover_data=["count"],
        title=f"Run vs Pass by Field Position ({down_selected} Down)"
    )

    # Make X-axis football field style
    field_ticks = list(range(0, 101, 10))
    field_labels = ["Own 0","10","20","30","40","50","40","30","20","10","Goal"]

    fig.update_layout(
        plot_bgcolor="#0b6623",
        paper_bgcolor="#111111",
        font=dict(color="white"),
        xaxis=dict(title="Field Position", tickmode="array", tickvals=field_ticks, ticktext=field_labels),
        yaxis=dict(title="Play Percentage")
    )
    fig.update_traces(marker=dict(line=dict(width=2, color="white")))

    selected_points = plotly_events(fig, click_event=True)
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # Handle Click
    # -------------------------
    if selected_points:
        yard_choice = int(selected_points[0]["x"])
    selected_plays = df_down[df_down["yard_group"] == yard_choice]

    # -------------------------
    # Metric Cards
    # -------------------------
    avg_gain = round(selected_plays["gain_loss"].mean(),1)
    max_gain = selected_plays["gain_loss"].max()
    min_gain = selected_plays["gain_loss"].min()
    col1, col2, col3 = st.columns(3)

    col1.metric("Average Gain", avg_gain)
    col2.metric("Max Gain", max_gain)
    col3.metric("Min Gain", min_gain)

    # -------------------------
    # Gain/Loss Bar Chart
    # -------------------------
    col1, col2 = st.columns(2)
    with col1:
        gain_summary = selected_plays.groupby("gain_loss").size().reset_index(name="plays").sort_values("gain_loss")
        gain_fig = px.bar(
            gain_summary,
            x="gain_loss",
            y="plays",
            labels={"gain_loss":"Yards Gained","plays":"Number of Plays"},
            title="Gain / Loss Distribution",
            template="plotly_dark"
        )
        st.plotly_chart(gain_fig, use_container_width=True)

    # -------------------------
    # Top Concepts
    # -------------------------
    with col2:
        top_concepts = (
            selected_plays.groupby(["concept","play_direction"])
            .size()
            .reset_index(name="count")
            .sort_values("count",ascending=False)
            .head(8)
        )
        concept_fig = px.bar(
            top_concepts,
            x="count",
            y="concept",
            color="play_direction",
            orientation="h",
            title="Top 8 Concepts",
            template="plotly_dark"
        )
        st.plotly_chart(concept_fig, use_container_width=True)

    # -------------------------
    # Raw Play Table
    # -------------------------
    st.subheader("Play Data")
    st.dataframe(selected_plays, use_container_width=True)