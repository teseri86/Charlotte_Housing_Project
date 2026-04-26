# DTSC2302-Project3
# Housing Unaffordability and Displacement Risk in Charlotte, NC
Final Group Project for Data Science Studio 2 (DTSC 2302) — Spring 2026
 
---
 
## Questions
- What neighborhood characteristics predict housing unaffordability in Charlotte, NC?
- Which neighborhoods are most at risk of displacement?
- Do historically redlined neighborhoods face disproportionately higher unaffordability and displacement risk today?
---
 
## Background
Charlotte has experienced rapid growth over the past decade, driving up housing costs and pushing long-term residents — particularly in lower-income and minority communities — out of their neighborhoods. This pattern of displacement does not occur randomly. It is suspected that it follows decades of discriminatory housing policy, most notably the Home Owners' Loan Corporation (HOLC) redlining maps of the 1930s, which systematically denied mortgage access to Black and low-income communities.
 
This project uses publicly available neighborhood-level data to quantify the drivers of housing unaffordability and displacement risk across Charlotte's Neighborhood Profile Areas (NPAs). A secondary analysis overlays model predictions onto historical HOLC redlining boundaries to assess whether the legacy of redlining continues to shape housing outcomes today.
 
---
 
## Data Sources
| Dataset | Source | Use |
|--------|--------|-----|
| Charlotte Area Quality of Life (QoL) Explorer | City of Charlotte ArcGIS REST API | Features for both models |
| Vulnerability to Displacement by NPA | Charlotte Open Data Portal | Classification target variable |
| Mapping Inequality (HOLC Redlining Maps) | University of Richmond | Historical redlining grades (A–D) |
 
---
 
## Models
 
### Regression — Predicting Housing Cost Burden
Predicts a composite housing cost burden index derived from rental cost and home sales price relative to household income, weighted by neighborhood homeownership rate.
 
**Method:** Multiple Linear Regression
 
### Classification — Predicting Displacement Risk
Predicts binary displacement risk (Yes/No) using the City of Charlotte's Vulnerability to Displacement dataset.
 
**Methods:** Logistic Regression, kNN Classification, Random Forest
 
---
 
## Features
- **Socioeconomic:** Household income, employment rate, food & nutrition services, public health insurance
- **Housing:** Rental cost, home sales price, housing age, housing density, code violations, foreclosures, new construction
- **Demographics:** Age of residents, race
- **Safety:** Property crime, violent crime
- **Accessibility:** Proximity to transit, grocery stores, financial services
