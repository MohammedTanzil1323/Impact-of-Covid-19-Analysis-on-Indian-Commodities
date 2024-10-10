import pandas as pd
#for i in range(29)
# Load your Excel file into a DataFrame
df = pd.read_excel('Report_Data_Commoditywise_with_variation (0).xlsx',header=2)

# Concatenate "2/02" to the values in the "States" column
df['States/UTs'] = df['States/UTs'] + ' 2/02'
print(df)