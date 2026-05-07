# Redlined and Left Behind: Housing Unaffordability and Displacement Risk in Charlotte, NC
This was originally a final group project for Data Science Studio 2 (DTSC 2302), Spring 2026 at UNC Charlotte.  
I created this repository seperately to continue refining the project independent from the group and the University.

---

## Research Questions
- What neighborhood characteristics predict housing unaffordability in Charlotte, NC?
- Which neighborhoods are most at risk of displacement?
- Do historically redlined neighborhoods face disproportionately higher unaffordability and displacement risk today?

---

## Background
Charlotte has experienced rapid growth over the past decade, driving up housing costs and pushing long-term residents out of their neighborhoods. This pattern of displacement does not occur randomly. It follows decades of discriminatory housing policy, most notably the Home Owners' Loan Corporation (HOLC) redlining maps of the 1930s, which systematically denied mortgage access to Black and low-income communities.

This project uses publicly available neighborhood-level data to quantify the drivers of housing unaffordability and displacement risk across Charlotte's 458 Neighborhood Profile Areas (NPAs). A post-analysis overlays model predictions onto historical HOLC redlining boundaries to assess whether the legacy of redlining continues to shape housing outcomes today.

---

## Data Sources
| Dataset | Source | Use |
|---------|--------|-----|
| Charlotte Quality of Life Explorer | City of Charlotte ArcGIS REST API | Features for both models |
| NPA Boundaries | City of Charlotte ArcGIS REST API | Spatial join with HOLC zones |
| Vulnerability to Displacement by NPA | Charlotte Open Data Portal | Classification target variable |
| Mapping Inequality (HOLC Redlining Maps) | University of Richmond | Historical redlining grades (A–D) |

All sources merged through a SQLite database (`data/charlotte_housing.db`).

---

## Engineered Features
Three target and composite variables were engineered from raw data:
- **`housing_cost_burden`** — normalized composite index of rental and ownership affordability relative to neighborhood median income (regression target)
- **`displacement_risk`** — binary encoding of the city's vulnerability classification: 1 = High Risk, 0 = Low Risk (classification target)
- **`crime_total`** — composite of property and violent crime rates, normalized and averaged into a single index

---

## Models

### Regression — Housing Cost Burden
Predicts a continuous housing cost burden index (0–1 scale) across 458 NPAs.

**Final model features:** `household_income`, `home_ownership`, `food_nutrition`, `age_of_residents`

### Classification — Displacement Risk
Predicts binary displacement risk (Yes/No) across 458 NPAs. Recall prioritized — missing a high-risk neighborhood is worse than a false alarm.


---

## HOLC Post-Analysis
Both model outputs were overlaid onto Charlotte's historical HOLC grade boundaries. Key findings:

- 0% of A and B-graded neighborhoods are High Risk for displacement while 75% of C-graded and 61% of D-graded neighborhoods are High Risk
- Mean housing cost burden nearly doubles from grade A to grade C/D
- Kruskal-Wallis tests confirmed all differences are statistically significant (p < 0.05) across actual and model-predicted outcomes
- Neither model was trained with HOLC grade as a feature. The patterns emerged from neighborhood characteristics alone

---
