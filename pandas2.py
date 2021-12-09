import numpy as np
import pandas as pd

 

""" 
    Create an 3x4 (3 rows x 4 columns) pandas DataFrame in which the columns are named Eleanor, Chidi, Tahani, and Jason. Populate each of the 12 cells in the DataFrame with a random integer between 0 and 100, inclusive.

    Output the following:
        the entire DataFrame
        the value in the cell of row #1 of the Eleanor column

    Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason.
"""

my_column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
#Numbers in dataset are random and integers. To change that you change np.random.randit to np.random.random
my_data = np.random.randint(low=0, high=101, size=(3, 4))

my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)
print(my_dataframe.head(3), '\n')
print("Here is first value of Eleanor: %d\n" % my_dataframe['Eleanor'][1])
my_dataframe['Janet'] = my_dataframe['Tahani'] + my_dataframe['Jason']
print(my_dataframe)

#You can also copy and reference to dataset as here:

df = my_dataframe

print("  Starting value of data frame: %d" % my_dataframe['Chidi'][0])
print("  Starting value of my_dataframe: %d\n" % df['Chidi'][0])

df.at[1, 'Jason'] = df['Jason'][1] + 13

print("  Updated value of data frame: %d" % my_dataframe['Jason'][1])
print("  Updated value of my_dataframe: %d\n" % df['Jason'][1])
