# Architecture Overview – Snowflake Cortex Feedback Insights

This document explains the end‑to‑end architecture for the Snowflake Cortex Feedback Insights mini‑project. The design follows a modern **Medallion Architecture** (Bronze → Silver → Gold) and integrates **Snowflake Cortex** for AI‑powered text enrichment.

---

## 1. High‑Level Flow

1. **Raw feedback ingestion**  
   CSV/JSON files are loaded into the **Bronze** layer with minimal transformation.

2. **Data cleaning & standardization**  
   The **Silver** layer applies:
   - Type casting  
   - Null handling  
   - Text normalization  
   - Basic transformations  

3. **Cortex enrichment**  
   The Silver table is enriched using Snowflake Cortex functions:
   - Sentiment classification  
   - Topic/theme extraction  
   - Summarization  

4. **Gold layer aggregation**  
   Business‑friendly tables and views:
   - Sentiment trends  
   - Top themes  
   - Product/channel breakdowns  
   - Drill‑down enriched feedback  

5. **Streamlit dashboard**  
   A lightweight UI for:
   - KPIs  
   - Charts  
   - Filters  
   - Drill‑down exploration  

---

## 2. Medallion Layers

### Bronze Layer (Raw)
- Stores raw feedback exactly as received.
- No transformations except ingestion.
- Useful for audits and reprocessing.

**Example columns:**
- `raw_text`
- `rating`
- `source`
- `created_at`

---

### Silver Layer (Cleaned)
- Standardized and typed data.
- Removes noise and prepares for enrichment.

**Transformations include:**
- Trim whitespace  
- Normalize casing  
- Convert timestamps  
- Validate ratings  
- Remove empty feedback  

---

### Gold Layer (Enriched + Aggregated)
- Adds Cortex outputs:
  - `sentiment`
  - `topics`
  - `summary`
- Adds business metrics:
  - `sentiment_score`
  - `theme_frequency`
  - `daily_trends`

This is the layer consumed by the Streamlit app.

---

## 3. Cortex Integration

The project uses Snowflake Cortex functions such as:

- `SNOWFLAKE.CORTEX.SENTIMENT()`  
- `SNOWFLAKE.CORTEX.SUMMARIZE()`  
- `SNOWFLAKE.CORTEX.TOPICS()`  

These functions are applied in the **Silver → Gold** transformation step.

---

## 4. Streamlit Application

The Streamlit UI connects to the **Gold** layer and provides:

- KPI cards  
- Sentiment distribution  
- Topic frequency charts  
- Time‑series trends  
- Drill‑down table with raw + enriched feedback  

The app uses:
- `snowflake-connector-python`
- `pandas`
- `altair`
- `streamlit`

---

## 5. Architecture Diagram

See `architecture/medallion-diagram.mmd` for the Mermaid diagram.

A PNG version can be exported if needed.

---

## 6. Benefits of This Architecture

- Clear separation of concerns  
- Easy debugging and reprocessing  
- Cortex enrichment isolated to Silver → Gold  
- Streamlit UI decoupled from pipeline  
- Portfolio‑ready and enterprise‑aligned  

---

## 7. Next Steps

- Add CI/CD for SQL + Python  
- Add more Cortex use cases  
- Add multi‑product segmentation  
