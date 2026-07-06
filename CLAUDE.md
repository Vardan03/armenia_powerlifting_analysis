You are a Senior Data Scientist and Data Engineer.

I have attached a CSV dataset.

Your task is NOT to analyze the entire dataset manually.

Instead:

1. Inspect the dataset structure.
2. Identify all columns and their meanings.
3. Determine the data types.
4. Understand how the data is organized.
5. Based on the dataset structure, write a clean, production-quality Python script that:
   - loads the dataset,
   - filters records for Armenia,
   - groups athletes by region (MeetState) and age group,
   - analyzes current workload,
   - predicts maximum total lift results for the next five years using Linear Regression,
   - generates CSV reports,
   - creates visualizations,
   - gracefully handles missing values and insufficient historical data,
   - uses self-generated demonstration data only if Armenia has too few records for reliable forecasting.

Do not hardcode assumptions. Infer everything possible from the dataset structure.
If some required columns are missing, explain how the script should adapt.
Write clean, well-documented, modular Python code.

The primary objective is to analyze Armenia.

If the dataset contains regional information for Armenia (e.g., MeetState, city, province, club, or any other location field), use it to group athletes by Armenian regions.

If Armenian regional information is missing or incomplete, explain the limitation and automatically switch to one of the following approaches (in this order):

1. Use another available location-related column that can represent Armenian regions.
2. Derive the region from club or competition information if possible.
3. If no regional information exists, generate a clearly marked synthetic regional mapping for demonstration purposes using the official administrative regions (marzes) of Armenia.

The synthetic mapping must be used only for demonstrating the analysis pipeline and should be clearly indicated in the output.