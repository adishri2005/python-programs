print("Probability, Entropy & MC Simulation Assignment 1")

import pandas as pd
import numpy as np

# dataset
data = {
    "Mood": ["Chill","Stressed","Chill","Chill","Hyped","Chill","Stressed",
             "Hyped","Chill","Stressed","Chill","Hyped","Stressed","Chill"],
    "Weather": ["Sunny","Sunny","Rainy","Rainy","Overcast","Sunny","Overcast",
                "Rainy","Overcast","Sunny","Overcast","Rainy","Overcast","Sunny"],
    "Homework": ["Yes","No","Yes","No","Yes","Yes","No",
                 "Yes","Yes","Yes","No","No","Yes","No"],
    "Plays": ["Yes","No","Yes","No","Yes","Yes","No",
              "Yes","Yes","No","Yes","No","Yes","Yes"]
}
df = pd.DataFrame(data)

# classes
classes = df["Plays"].unique()

# priors
priors = df["Plays"].value_counts(normalize=True).to_dict()

# likelihoods with Laplace smoothing
def likelihoods(df, feature, alpha=1):
    result = {}
    categories = df[feature].unique()
    k = len(categories)
    for c in classes:
        subset = df[df["Plays"] == c]
        total = len(subset)
        result[c] = {}
        for v in categories:
            count = len(subset[subset[feature] == v])
            prob = (count + alpha) / (total + alpha * k)
            result[c][v] = prob
    return result

likelihood_tables = {}
for feature in ["Mood", "Weather", "Homework"]:
    likelihood_tables[feature] = likelihoods(df, feature)

# prediction function
def predict(row):
    scores = {}
    for c in classes:
        score = np.log(priors[c])
        for feature in ["Mood","Weather","Homework"]:
            score += np.log(likelihood_tables[feature][c][row[feature]])
        scores[c] = score
    return max(scores, key=scores.get)

# predictions for whole dataset
df["Predicted"] = df.apply(predict, axis=1)

# accuracy
accuracy = (df["Predicted"] == df["Plays"]).mean()

# confusion matrix
conf_matrix = pd.crosstab(df["Plays"], df["Predicted"], rownames=["Actual"], colnames=["Predicted"])

# results
print("Class Priors:\n", priors, "\n")
print("Likelihood Tables:")
for f, table in likelihood_tables.items():
    print(f, table, "\n")
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)

# step-by-step posterior for one row (e.g. Row 1)
row = df.iloc[0]
print("\nRow chosen:", dict(row[["Mood","Weather","Homework","Plays"]]))
scores = {}
for c in classes:
    prior = np.log(priors[c])
    likelihood_sum = 0
    for f in ["Mood","Weather","Homework"]:
        prob = likelihood_tables[f][c][row[f]]
        likelihood_sum += np.log(prob)
        print(f"P({f}={row[f]}|{c}) =", prob)
    score = prior + likelihood_sum
    scores[c] = score
    print(f"Log-score({c}) =", score)
# normalize to posterior
exp_scores = {c: np.exp(v) for c,v in scores.items()}
total = sum(exp_scores.values())
posteriors = {c: v/total for c,v in exp_scores.items()}
print("Posterior Probabilities:", posteriors)
print("Predicted Class:", max(scores, key=scores.get))
