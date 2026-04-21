# ============================================================
# Snowflake Cortex Feedback Insights – Exploration Notebook
# Notebook-style Python script for local data exploration
# ============================================================

import pandas as pd
import altair as alt
import snowflake.connector

# ------------------------------------------------------------
# 1. Connect to Snowflake
# ------------------------------------------------------------
print("Connecting to Snowflake...")

conn = snowflake.connector.connect(
    user="YOUR_USER",
    password="YOUR_PASSWORD",
    account="YOUR_ACCOUNT",
    warehouse="COMPUTE_WH",
    database="CORTEX_FEEDBACK_DB",
    schema="GOLD"
)

cur = conn.cursor()
print("Connected.")

# ------------------------------------------------------------
# 2. Helper function to run SQL
# ------------------------------------------------------------
def run_query(sql):
    cur.execute(sql)
    return cur.fetch_pandas_all()

# ------------------------------------------------------------
# 3. Load enriched feedback
# ------------------------------------------------------------
print("Loading enriched feedback...")
df = run_query("""
    SELECT
        FEEDBACK_ID,
        CLEAN_TEXT,
        RATING,
        SOURCE,
        CREATED_AT,
        SENTIMENT,
        TOPICS,
        SUMMARY
    FROM CORTEX_FEEDBACK_DB.GOLD.FEEDBACK_ENRICHED
    ORDER BY CREATED_AT DESC;
""")

print("Loaded", len(df), "rows.")
print(df.head())

# ------------------------------------------------------------
# 4. Sentiment distribution
# ------------------------------------------------------------
print("\nSentiment distribution:")
sent_df = df.groupby("SENTIMENT").size().reset_index(name="COUNT")
print(sent_df)

# ------------------------------------------------------------
# 5. Daily trends
# ------------------------------------------------------------
print("\nDaily trends:")
df["DAY"] = pd.to_datetime(df["CREATED_AT"]).dt.date
trend_df = df.groupby("DAY").agg(
    TOTAL_FEEDBACK=("FEEDBACK_ID", "count"),
    AVG_RATING=("RATING", "mean")
).reset_index()
print(trend_df)

# ------------------------------------------------------------
# 6. Topic frequency
# ------------------------------------------------------------
print("\nTopic frequency:")
topic_rows = []

for _, row in df.iterrows():
    if isinstance(row["TOPICS"], list):
        for t in row["TOPICS"]:
            topic_rows.append({"TOPIC": t})

topic_df = pd.DataFrame(topic_rows)
topic_freq = topic_df.groupby("TOPIC").size().reset_index(name="FREQUENCY")
topic_freq = topic_freq.sort_values("FREQUENCY", ascending=False)
print(topic_freq)

# ------------------------------------------------------------
# 7. Example charts (saved locally)
# ------------------------------------------------------------
print("\nGenerating charts...")

sent_chart = (
    alt.Chart(sent_df)
    .mark_bar()
    .encode(x="SENTIMENT", y="COUNT", color="SENTIMENT")
)

sent_chart.save("sentiment_distribution.png")
print("Saved: sentiment_distribution.png")

trend_chart = (
    alt.Chart(trend_df)
    .mark_line(point=True)
    .encode(x="DAY:T", y="TOTAL_FEEDBACK:Q")
)

trend_chart.save("daily_trends.png")
print("Saved: daily_trends.png")

# ------------------------------------------------------------
# 8. Close connection
# ------------------------------------------------------------
cur.close()
conn.close()
print("\nNotebook exploration complete.")
