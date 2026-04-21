import streamlit as st
import pandas as pd
import altair as alt
import snowflake.connector
from utils import queries

# -----------------------------
# Snowflake connection
# -----------------------------
@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse="COMPUTE_WH",
        database="CORTEX_FEEDBACK_DB",
        schema="GOLD"
    )

@st.cache_data
def run_query(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    df = cur.fetch_pandas_all()
    cur.close()
    return df

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Cortex Feedback Insights", layout="wide")
st.title("🧠 Snowflake Cortex – Feedback Insights Dashboard")

# KPIs
kpi_df = run_query(queries.GET_KPIS)
col1, col2 = st.columns(2)
col1.metric("Total Feedback", int(kpi_df["TOTAL_FEEDBACK"][0]))
col2.metric("Avg Rating", round(kpi_df["AVG_RATING"][0], 2))

st.divider()

# Sentiment distribution
sent_df = run_query(queries.GET_SENTIMENT_DISTRIBUTION)
sent_chart = (
    alt.Chart(sent_df)
    .mark_bar()
    .encode(
        x="SENTIMENT",
        y="COUNT",
        color="SENTIMENT"
    )
)
st.subheader("Sentiment Distribution")
st.altair_chart(sent_chart, use_container_width=True)

# Daily trends
trend_df = run_query(queries.GET_DAILY_TRENDS)
trend_chart = (
    alt.Chart(trend_df)
    .mark_line(point=True)
    .encode(
        x="DAY:T",
        y="TOTAL_FEEDBACK:Q"
    )
)
st.subheader("Daily Feedback Trends")
st.altair_chart(trend_chart, use_container_width=True)

# Top topics
topic_df = run_query(queries.GET_TOP_TOPICS)
topic_chart = (
    alt.Chart(topic_df)
    .mark_bar()
    .encode(
        x="FREQUENCY:Q",
        y=alt.Y("TOPIC:N", sort="-x")
    )
)
st.subheader("Top Topics")
st.altair_chart(topic_chart, use_container_width=True)

# Feedback table
st.subheader("Feedback Explorer")
table_df = run_query(queries.GET_FEEDBACK_TABLE)
st.dataframe(table_df, use_container_width=True)
