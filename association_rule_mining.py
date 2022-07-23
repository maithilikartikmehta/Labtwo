# %% import dataframe from pickle file
import pandas as pd
from sklearn import datasets

df = pd.read_pickle("UK.pkl")

df.head()
# %% convert dataframe to invoice-based transactional format

dataset = []
for inv_number, subset in df.groupby("InvoiceNo"):
    dataset.append(subset["Description"].tolist() )


# %% apply apriori algorithm to find frequent items and association rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
new_df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(new_df, min_support=0.01, use_colnames=True)


# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items
length = frequent_itemsets["itemsets"].apply(len)
frequent_itemsets["length"] = length
frequent_itemsets   

# %%
(frequent_itemsets["length"] > 1).sum()

#%%
(frequent_itemsets["length"] > 2).sum()

# %%
(frequent_itemsets["length"] > 3).sum()

# %%
(frequent_itemsets["length"] == frequent_itemsets["length"].max()).sum()


# %% top 10 lift association rules
from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, min_threshold=0.5)
rules.sort_values("lift", ascending=False).head(10)


# %% scatterplot support vs confidence
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["confidence"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Support vs Confidence")


# %% scatterplot support vs lift
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["lift"], alpha=0.1)
plt.xlabel("Support")
plt.ylabel("lift")
plt.title("Support vs lift")

# %%
