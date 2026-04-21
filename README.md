███████╗███╗   ██╗ ██████╗ ██╗    ██╗██╗  ██╗

██╔════╝████╗  ██║██╔═══██╗██║    ██║██║ ██╔╝

█████╗  ██╔██╗ ██║██║   ██║██║ █╗ ██║█████╔╝ 

██╔══╝  ██║╚██╗██║██║   ██║██║███╗██║██╔═██╗ 

███████╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║  ██╗

╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝



Snowflake Cortex Feedback Insights – Mini Project



\## 📌 Project Overview



Snowflake Cortex Feedback Insights is an end‑to‑end mini project demonstrating how to build an AI‑powered feedback analytics pipeline using:



\- Snowflake Cortex (sentiment, topics, summaries)

\- Medallion Architecture (Bronze → Silver → Gold)

\- Streamlit Dashboard (KPIs, charts, drill‑downs)

\- SQL pipeline + documentation

\- Notebook for exploration



This project showcases enterprise data architecture, practical AI integration, and business‑facing delivery.



\---



\## 🏗️ Architecture



The project follows a modern Medallion Architecture:



Raw → Bronze → Silver → Cortex Enrichment → Gold → Streamlit App



Detailed diagrams are available in:



\- `docs/data\_model.md`

\- `docs/pipeline\_flow.md`



\---



\## 📂 Repository Structure



snowflake-cortex-mini-project/

│

├── streamlit\_app/

│   └── app.py

│

├── sql/

│   ├── 01\_create\_objects.sql

│   ├── 02\_load\_bronze.sql

│   ├── 03\_clean\_silver.sql

│   ├── 04\_cortex\_enrichment.sql

│   └── 05\_gold\_views.sql

│

├── docs/

│   ├── data\_model.md

│   └── pipeline\_flow.md

│

├── notebooks/

│   └── exploration\_notebook.py

│

├── .github/workflows/

│   └── ci-basic.yml

│

├── requirements.txt

└── README.md



\---



\## ▶️ How to Run Locally



1\. Create `.streamlit/secrets.toml`:



\[snowflake]

user = "YOUR\_USER"

password = "YOUR\_PASSWORD"

account = "YOUR\_ACCOUNT"





2\. Install dependencies:



pip install -r requirements.txt



3\. Run the Streamlit app:



streamlit run streamlit\_app/app.py





\---



\## 🚀 Features



\- AI-powered sentiment analysis  

\- Topic extraction  

\- Cortex-generated summaries  

\- KPI dashboard  

\- Trend charts  

\- Topic frequency visualization  

\- Drill-down table  



\---



\## 🔮 Future Enhancements



\- Add embedding-based clustering  

\- Add NPS segmentation  

\- Add Snowpipe real-time ingestion  

\- Add dbt models  

\- Add unit tests  

\- Deploy as a Snowflake Native App  



\---











