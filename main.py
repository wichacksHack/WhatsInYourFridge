
import pandas as pd

food_list = pd.DataFrame(columns=['Name', 'Category', 'Ingredients', 'Rating', 'frequency'])

unchanged_food_list = pd.DataFrame(columns=['Name', 'Category', 'Ingredients', 'Rating', 'frequency'])

data = pd.read_csv('wiyf_dataset.csv')

food_list['Name'] = data['Recipe Name']
food_list['Ingredients'] = data['Ingredients']

unchanged_food_list['Name'] = data['Recipe Name']
unchanged_food_list['Ingredients'] = data['Ingredients']

import random

for i in range(len(food_list)):
    food_list.loc[i, "Rating"] = random.randint(1, 5)
    food_list.loc[i, "frequency"] = random.randint(0, 10)
    ing = food_list.loc[i, "Ingredients"].split(",")
    food_list.loc[i, "Ingredients"] = ing


import numpy as np

curr_fridge_items = set(np.concatenate((food_list.loc[5, "Ingredients"], food_list.loc[81, "Ingredients"],
                                        food_list.loc[369, "Ingredients"], food_list.loc[9245, "Ingredients"],
                                        food_list.loc[10438, "Ingredients"])))



possible_recipes = pd.DataFrame(columns=['Name', 'Category', 'Ingredients', 'Rating', 'frequency'])
for i in range(len(food_list)):
    if set(food_list.loc[i, "Ingredients"]).issubset(curr_fridge_items):
        possible_recipes.loc[len(possible_recipes.index)] = food_list.loc[i]


possible_recipes = possible_recipes.sort_values(["frequency", "Rating"], ascending=(False, False))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(unchanged_food_list['Ingredients'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_recommendations(name, cosine_sim=cosine_sim):
    idx = food_list.index[food_list['Name'].str.strip() == name][0]
    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    food_indices = [i[0] for i in sim_scores]
    return food_list['Name'].iloc[food_indices]


rec = get_recommendations('Lollipop Sugar Cookies Recipe')
