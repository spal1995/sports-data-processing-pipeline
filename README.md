# Sports Data Processing Pipeline

This project builds a data processing pipeline using Python and Pandas to clean, standardize, and analyze badminton tournament datasets.

The pipeline processes raw match data stored as CSV files and generates insights about player performance, tournament intensity, and match outcomes.

---

## Project Architecture

Raw CSV Data
        ↓
Data Cleaning & Normalization
        ↓
Entity Resolution (Fuzzy Matching)
        ↓
Data Transformation & Aggregation
        ↓
Analytics & Visualization

---

## Tech Stack

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
FuzzyWuzzy  

---

## Key Data Engineering Tasks

• Data cleaning and normalization of player names  
• Entity resolution using fuzzy string matching  
• Data transformations using Pandas groupby and aggregations  
• Feature engineering for performance metrics  
• Visualization of match momentum and tournament trends  

---

## Key Insights Generated

### Most Dominant Singles Player
Calculated win rate for players with at least 100 matches.

### Country Dominance in Doubles
Aggregated doubles match results by nationality.

### Tournament Intensity Analysis
Compared number of sets across tournament tiers.

### Retirement Pattern Analysis
Examined frequency of player retirements across tournament levels.

### Match Momentum Visualization
Plotted score progression of final matches to analyze momentum shifts.

---

## Example Visualization

Example: Score momentum of a championship match.

![Score Momentum](visualizations/match_momentum.png)

---

## Repository Structure
