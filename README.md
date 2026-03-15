# Sports(Badminton) Data Processing Pipeline

This project builds a **data processing pipeline using Python and Pandas** to clean, standardize, and analyze badminton tournament datasets.

Badminton is a fast-paced racquet sport played indoors or outdoors, where two (singles) or four (doubles) players hit a shuttlecock (birdie) over a high net. The objective is to score points by landing the shuttle in the opponent's court, with matches typically played to 21 points across three sets.

---

# Analytical Questions Explored

The project answers the following **10 analytical badminton questions**:

### 1. Who is the most dominant singles player?
Find the player with the highest win rate among players with at least 100 matches played.

### 2. Which country dominates men's doubles tournaments?
Determine which national teams produce the most successful doubles pairs.

### 3. Does tournament level affect match intensity?
Analyze whether higher-tier tournaments produce more competitive matches.

### 4. Do retired matches skew tournament results?
Examine how often matches end due to player retirement.

### 5. Who scores the most consecutive points in a game?
Identify the player or team with the longest scoring streak.

### 6. How often does the team with fewer total points win?
Analyze cases where the losing team actually scored more total points.

### 7. How common are straight-set wins?
Determine the proportion of matches that end in two sets versus three sets.

### 8. Are certain months more intense in professional badminton?
Analyze tournament scheduling patterns across the year.

### 9. Which players improve performance in later rounds?
Identify players whose performance increases in semifinals or finals.

### 10. How does score momentum evolve during a match?
Visualize point-by-point score progression to analyze match momentum.

---

The pipeline processes raw match data stored as CSV files, performs **entity resolution using fuzzy matching**, and generates insights about **player performance, tournament intensity, and match dynamics**.

---

# Project Architecture

The project follows a simple data pipeline structure.

Raw Data (CSV)  
↓  
Data Cleaning  
↓  
Entity Resolution (Fuzzy Matching)  
↓  
Processed Data  
↓  
Analytical Queries & Visualizations  

Pipeline implementation:

data/raw  
↓  
data_cleaning.py  
↓  
entity_matching.py  
↓  
data/processed  
↓  
analysis.py  

![Pipeline Architecture](visualizations/pipeline.png)

---

# Repository Structure

```
sports-data-processing-pipeline
│
├── data
│   ├── raw
│   │   ├── ms.csv
│   │   └── md.csv
│   │
│   └── processed
│       ├── ms_clean.csv
│       └── md_clean.csv
│
├── notebooks
│   └── badminton_analysis.ipynb
│
├── src
│   ├── data_cleaning.py
│   ├── entity_matching.py
│   └── analysis.py
│
├── visualizations
│
├── requirements.txt
└── README.md
```

---

# Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- FuzzyWuzzy  

---

# Key Data Engineering Tasks

This project demonstrates several common data engineering tasks:

- Data ingestion from CSV datasets  
- Data cleaning and normalization  
- Entity resolution using fuzzy string matching  
- Data transformation using Pandas  
- Analytical querying  
- Visualization of match dynamics  

# Example Visualization

Example: Score progression of a championship match showing momentum shifts during the final set.

---

# How to Run the Project

### Clone the repository

```bash
git clone https://github.com/spal1995/sports-data-processing-pipeline.git
cd sports-data-processing-pipeline
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run data cleaning pipeline

```bash
python src/data_cleaning.py
```

This generates processed datasets in:

```
data/processed/
```

### Run analysis

```bash
python src/analysis.py
```

This executes all analytical queries and visualizations.

---

# Future Improvements

Possible extensions for this project:

- Convert the pipeline into a scheduled workflow using Apache Airflow  
- Store processed data in a relational database or data warehouse  
- Build dashboards using Power BI or Tableau  
- Automate data ingestion workflows  

---

# Author

**Shubhrajit Pal**

Data Engineering | Data Analytics | Machine Learning
