# Task1 : Create a list called months that includes 'January', "March', and 'April'.
# Create another list named remaining months and add the rest of the months of the year to it.
# Insert 'February' into the months list in the correct order.
# Remove 'February' from the months list.
# Print the elements of the list that represent the time from "March' to "September'.

months = ['January', 'March', 'April']
remaining_months = ['May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months.insert(1, 'February')
months.remove('February')
combined_months = months + remaining_months
print(combined_months[1:8])

# start_index = combined_months.index('March')
# end_index = combined_months.index('September')
# print(combined_months[start_index:end_index + 1])