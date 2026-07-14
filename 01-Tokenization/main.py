# %%
"""
Task:
Write code to create a look-up-table that maps each token (a string) onto an integer.
Print out the look-up-table as in Figure
"""
lookup_table = {}
tokens = ["hello", "world", "this", "is", "a", "test"]
for i, token in enumerate(tokens):
    lookup_table[token] = i
print(lookup_table)


# %%
"""
Task:
Write code to tokenize (encode) the text by transforming it from a list of characters
into a sequence of integers, which you can print out.
"""
input_text = "hello world this is a test"
input_tokens = input_text.split()
token_ids = [lookup_table[token] for token in input_tokens]
print(token_ids)


# %%
"""
Task:
Visualize the token sequence in a plot like in Figure 2.3. The x-axis corresponds to
positional indices, and the y-axis corresponds to the token indices on the left and the
token strings on the right. Draw a box at the y-axis location of each token index.
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

# Draw a box (square marker) at each (position, token_id)
ax.plot(
    range(len(token_ids)),
    token_ids,
    "s",
    markersize=18,
    markerfacecolor=[0.7, 0.7, 0.9],
    markeredgecolor="black",
)

ax.set_xlabel("Positional index")
ax.set_ylabel("Token index")
ax.set_xticks(range(len(token_ids)))
ax.set_yticks(range(len(tokens)))
ax.grid(linestyle="--", axis="y")

# Right y-axis: token strings
ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks(range(len(tokens)))
ax2.set_yticklabels(tokens)
ax2.set_ylabel("Token")

plt.tight_layout()
plt.show()
