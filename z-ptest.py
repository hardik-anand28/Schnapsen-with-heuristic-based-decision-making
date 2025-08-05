from statsmodels.stats.proportion import proportions_ztest
# Data from your experiments
k1 = 194  # Wins by HeuristicBot
N1 = 1000  # Total games HeuristicBot played
k2 = 65  # Wins by RandomBot
N2 = 1000  # Total games RandomBot played
# Perform the z-test
zscore, pval = proportions_ztest([k1, k2], [N1, N2])
# Output the results
print(f"HeuristicBot vs. RDeepBot Wins: {k1}/{N1} ({k1 / N1:.2%})")
print(f"RandomBot vs. RDeepBot Wins: {k2}/{N2} ({k2 / N2:.2%})")
print(f"Z-Score: {zscore}")
print(f"P-Value: {pval}")
# Interpretation
if pval < 0.05:
    print("There is a significant difference in win rates between HeuristicBot and RandomBot when playing against RDeepBot.")
else:
    print("There is no significant difference in win rates between HeuristicBot and RandomBot when playing against RDeepBot.")
