import pandas as pd
 
# intialise data of lists.
data = {'Parameters':['Distance', 'Difficulty', 'Condition', 'Priority'],
        'Values':[input("Distance"), input("Difficulty"), input("Condition"), input("Priority")]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)
