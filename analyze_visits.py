import pandas as pd
import numpy as np

# Step 1: Load and prepare data
# Read the cleaned CSV file and convert visit_date to datetime
data = pd.read_csv('ms_data.csv')
data['visit_date'] = pd.to_datetime(data['visit_date'])
# Sort data by patient_id and visit_date for longitudinal consistency
data.sort_values(by=['patient_id', 'visit_date'], inplace=True)

# Step 2: Add insurance information
# Read insurance types and create a mapping for patients
insurance_types = pd.read_csv('insurance.lst')['insurance_type'].dropna().tolist()
np.random.seed(42)  
insurance_map = {pid: np.random.choice(insurance_types) for pid in data['patient_id'].unique()}
data['insurance_type'] = data['patient_id'].map(insurance_map)
# Save updated data back to ms_data.csv
data.to_csv('ms_data.csv', index=False)

# Calculate visit costs based on insurance type and add random variation
cost_map = {'Basic': 100, 'Premium': 200, 'Platinum': 400}
data['visit_cost'] = data['insurance_type'].map(cost_map) + np.random.normal(0, 50, len(data))
# Save updated data back to ms_data.csv
data.to_csv('ms_data.csv', index=False)

# Step 3: Check for missing data
# Summarize missing values for key columns
missing_data_summary = data[['age', 'education_level', 'walking_speed']].isnull().sum()
print("Missing Data Summary:")
print(missing_data_summary)

# Step 4: Calculate summary statistics
# Compute mean walking speed by education level
mean_speed = data.groupby('education_level')['walking_speed'].mean()
# Compute mean visit costs by insurance type
mean_costs = data.groupby('insurance_type')['visit_cost'].mean()

# Step 5: Analyze age effects on walking speed
# Define age groups and categorize data
bins = [18, 34, 49, 64, 79, np.inf]
labels = ['18-34', '35-49', '50-64', '65-79', '80+']
data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels)
# Calculate mean walking speed for each age group
age_group_effects = data.groupby('age_group')['walking_speed'].mean()

# Output results
print("Mean Walking Speed by Education Level:\n", mean_speed)
print("Mean Costs by Insurance Type:\n", mean_costs)
print("Walking Speed by Age Group:\n", age_group_effects)