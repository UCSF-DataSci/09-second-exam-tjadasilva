# Step 1: Generate raw data
# Use the provided script to create a raw data file
python3 generate_dirty_data.py

# Step 2: Clean data
# Remove comment lines, empty lines, and extra commas
grep -v '^#' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,*/,/g' > temp_data.csv
# Extract relevant columns: patient_id, visit_date, age, education_level, walking_speed
cut -d',' -f1,2,4,5,6 temp_data.csv > ms_data.csv

# Step 3: Generate insurance type file
# Create a file listing insurance types (one per line)
echo -e "insurance_type\nBasic\nPremium\nPlatinum" > insurance.lst

# Step 4: Summarize cleaned data
# Count the total number of visits (excluding the header)
echo "Total visits: $(wc -l < ms_data.csv | awk '{print $1 - 1}')"
# Display the first few rows of the cleaned data
echo "First few records:"
head -n 10 ms_data.csv

# Verify walking speed range
# Find the minimum and maximum walking speeds
min_speed=$(awk -F',' 'NR > 1 {if (min == "" || $5 < min) min = $5} END {print min}' ms_data.csv)
max_speed=$(awk -F',' 'NR > 1 {if (max == "" || $5 > max) max = $5} END {print max}' ms_data.csv)
echo "Minimum walking speed: $min_speed"
echo "Maximum walking speed: $max_speed"