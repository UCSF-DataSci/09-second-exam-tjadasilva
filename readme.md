# DS-217 Final Exam: Thiago Junqueira Avelino da Silva

## Question 1: Data Preparation with Command-Line Tools (20 points)

### Steps Taken:
1. Generated raw data using `generate_dirty_data.py`.
2. Cleaned the data:
   - Removed comments, empty lines, and extra commas.
   - Extracted columns: `patient_id`, `visit_date`, `age`, `education_level`, `walking_speed`.
3. Created an `insurance.lst` file listing unique insurance types.

### Tools Used:
- `grep`, `sed`, `cut`, `awk`

### Summary:
- Total Visits: 15,416
- Walking Speed Range: 2.0 - 6.37

### Files:
- Cleaned Data: `ms_data.csv`
- Insurance Types: `insurance.lst`

## Question 2: Data Analysis with Python (25 points)

### Steps Taken:
1. Loaded and structured cleaned data.
2. Added insurance information:
   - Assigned consistent insurance types to patients.
   - Generated visit costs based on insurance type with random variation.
3. Verified missing data and calculated summary statistics.

### Tools Used:
- Python (`pandas`, `numpy`)

### Summary:
#### Mean Walking Speed by Education Level:
- Bachelors: 4.05 m/s
- Graduate: 4.43 m/s
- High School: 3.27 m/s
- Some College: 3.68 m/s

#### Mean Costs by Insurance Type:
- Basic: \$100.21
- Premium: \$200.17
- Platinum: \$399.75

#### Walking Speed by Age Group:
- 18-34: 4.61 m/s
- 35-49: 4.20 m/s
- 50-64: 3.71 m/s
- 65-79: 3.33 m/s
- 80+: 2.89 m/s

### Files:
- Updated Data: `ms_data.csv`

## Question 3: Statistical Analysis (25 points)

### Steps Taken:
1. Analyzed walking speed:
   - Mixed-effects regression with `age` and `education_level`.
   - Tested for significant age-related trends.
2. Analyzed visit costs:
   - ANOVA for insurance type effects.
   - Calculated Cohen’s d for effect sizes.
   - Generated box plot of costs by insurance type.
3. Conducted advanced analysis:
   - Investigated interaction between age and education level.

### Tools Used:
- Python (`pandas`, `numpy`, `statsmodels`, `matplotlib`)
- Statistical Methods: ANOVA, mixed-effects regression, OLS regression.

### Summary:
#### Walking Speed Analysis:
- **Age:** Walking speed decreases significantly with age (coef = -0.030, p < 0.001).
- **Education Level:**
  - Graduate: Faster speeds (+0.40 m/s).
  - High School: Slower speeds (-0.79 m/s).

#### Cost Analysis:
- **ANOVA:** Significant variation in costs (F = 47263.85, p < 0.001).
- **Cohen's d:** Large effect size (-5.95) between `Basic` and `Platinum`.

#### Advanced Interaction Analysis:
- No significant interactions between age and education level.

### Files:
- Updated Data: `ms_data.csv`
- Box Plot: `visit_costs_boxplot.png`

## Question 4: Data Visualization (30 points)

### Steps Taken:
1. **Walking Speed Visualizations:**
   - Scatter plot of age vs walking speed with regression line.
   - Box plot of walking speed by education level.
   - Line plot showing interaction effects of age and education on walking speed.

2. **Cost Visualizations:**
   - Bar plot of mean visit costs by insurance type with error bars.
   - Box plot showing distribution of visit costs by insurance type.

3. **Combined Visualizations:**
   - Pair plot for key variables.
   - Faceted plot of walking speed by insurance and education level.
   - Time trend analysis for walking speed over time.

4. **Bonus Visualizations:**
   - Polynomial regression for walking speed by age.
   - Interactive plot of education and age effects using Plotly.
   - Seasonal analysis of walking speed.

### Tools Used:
- Python Libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `plotly`

### Files:
#### Static Visualizations:
- `age_vs_walking_speed.png`
- `walking_speed_by_education.png`
- `education_age_interaction.png`
- `mean_costs_by_insurance.png`
- `cost_distribution_by_insurance.png`
- `pair_plot_key_variables.png`
- `faceted_walking_speed.png`
- `walking_speed_time_trends.png`
- `education_age_polynomial_regression.png`
- `seasonal_variation_walking_speed.png`

#### Interactive Visualization:
- `interactive_walking_speed.html`

### Summary:
The visualizations provide insights into:
- The decline in walking speed with age and differences by education level.
- The significant effect of insurance type on visit costs.
- Interaction effects and seasonal patterns in walking speed.