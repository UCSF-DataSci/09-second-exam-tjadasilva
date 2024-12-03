import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import f_oneway, ttest_ind
import matplotlib.pyplot as plt

# Step 1: Load data
data = pd.read_csv('ms_data.csv')
data['visit_date'] = pd.to_datetime(data['visit_date'])

# Step 2: Walking speed analysis
# Multiple regression with education and age
# Add education as a categorical variable
data['education_level'] = data['education_level'].astype('category')

# Build the regression model
walking_speed_model = smf.mixedlm(
    "walking_speed ~ age + education_level", 
    data, 
    groups=data['patient_id']
)
walking_speed_results = walking_speed_model.fit()

# Print regression results
print("Walking Speed Regression Results:")
print(walking_speed_results.summary())

# Test for significant trends
age_trend = sm.OLS(data['walking_speed'], sm.add_constant(data['age'])).fit()
print("\nAge Trend Regression Results:")
print(age_trend.summary())

# Step 3: Cost analysis
# Analyze effect of insurance type on costs
insurance_costs_anova = f_oneway(
    data[data['insurance_type'] == 'Basic']['visit_cost'],
    data[data['insurance_type'] == 'Premium']['visit_cost'],
    data[data['insurance_type'] == 'Platinum']['visit_cost']
)
print("\nANOVA Results for Insurance Type Effect on Visit Costs:")
print(f"F-statistic: {insurance_costs_anova.statistic:.2f}, p-value: {insurance_costs_anova.pvalue:.4f}")

# Effect size calculation (Cohen's d between Basic and Platinum)
def cohen_d(group1, group2):
    diff = np.mean(group1) - np.mean(group2)
    pooled_std = np.sqrt((np.var(group1, ddof=1) + np.var(group2, ddof=1)) / 2)
    return diff / pooled_std

effect_size = cohen_d(
    data[data['insurance_type'] == 'Basic']['visit_cost'],
    data[data['insurance_type'] == 'Platinum']['visit_cost']
)
print(f"\nEffect Size (Cohen's d) between Basic and Platinum Costs: {effect_size:.2f}")

# Box plot for cost analysis
data['insurance_type'] = pd.Categorical(
    data['insurance_type'], 
    categories=['Basic', 'Premium', 'Platinum'], 
    ordered=True
)
data.boxplot(column='visit_cost', by='insurance_type', grid=False)
plt.title("Visit Costs by Insurance Type")
plt.suptitle("") 
plt.xlabel("Insurance Type")
plt.ylabel("Visit Cost")
plt.savefig("visit_costs_boxplot.png")
plt.show()

# Step 4: Advanced analysis
# Interaction effects between education and age on walking speed
interaction_model = smf.ols(
    "walking_speed ~ age * education_level", 
    data=data
).fit()

# Print interaction results
print("\nInteraction Effects on Walking Speed:")
print(interaction_model.summary())

# Report key statistics and p-values
print("\nKey Interaction Statistics:")
for name, coef, pval in zip(interaction_model.params.index, interaction_model.params.values, interaction_model.pvalues):
    print(f"{name}: Coefficient = {coef:.3f}, p-value = {pval:.3f}")
