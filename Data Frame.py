import os, json
import pandas as pd
from RedditAPI import  Author_cnt, comments_cnt, Author_time, All_Nouns


Author_final = {key: value for key,value in Author_cnt.items() if key in All_Nouns}
Comments_final = {key: value for key, value in comments_cnt.items() if key in All_Nouns}

Author_List = list(Author_final.items())
Comments_List = list(Comments_final.items())

Comments_df = pd.DataFrame(Comments_List, columns = ["Nouns", "Occurences"])
Comments2_df = pd.DataFrame(Comments_List, columns = ["Nouns", "Occurences"]).set_index("Nouns").sort_values(by = ["Occurences"], ascending = False)
print(Comments_df)

print(Comments_df[Comments_df["Nouns"].isin(["dominion", "election", "biden", "immigrant", "antifa", "russia"])])
print(Comments2_df)



