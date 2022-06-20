# nato-phonetic-alphabet

The idea is to return a list of words for each alphabet in the user-inputted word, which can then be used to distinguish similar sounding letters, during a telephone call for instance.

Letter and their associated codes are provided in csv file. 

These are converted to dictionary using pandas library. Dictionary has **Letter in UPPERCASE** as *KEY* and **Associated Word** as *VALUE*.

From this dictionary, a new list is formed which has associated word for each letter in the user inputted word

`Libraries imported` - [Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
