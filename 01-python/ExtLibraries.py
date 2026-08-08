import numpy as np

rolls = np.random.randint(low=1, high=6, size=10)
print(rolls)  # e.g. [5 1 4 2 5 3 1 6 2 4] (random)
print(np.mean(rolls))  # e.g. 3.3 (mean of rolls)
print(np.median(rolls))  # e.g. 3.0 (median of rolls)
print(rolls + 10)  # e.g. [15 11 14 12 15 13 11 16 12 14] (rolls + 10)
print(rolls <= 3)  # e.g. [False  True False  True False  True  True False  True False]

xlist = [
    [1, 2, 3],
    [2, 4, 6],
]
# Create a 2-dimensional array
x = np.asarray(xlist)
print(
    f"xlist = {xlist}\nx =\n{x}"
)  # xlist = [[1, 2, 3], [2, 4, 6]]; x = [[1 2 3]\n [2 4 6]]
print(type(x))  # <class 'numpy.ndarray'>

print(x[1, -1])  # e.g. 6 (last element of second row)
print(xlist[1][-1])  # e.g. 6 (last element of second row)


def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    new_labels = [f"${int(amt)}" for amt in ticks]
    graph.set_yticklabels(new_labels)
