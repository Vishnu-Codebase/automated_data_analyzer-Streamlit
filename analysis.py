import matplotlib.pyplot as plt

def run_analysis(df, category_column, value_column):

    summary = df.groupby(category_column)[value_column].sum()

    fig, ax = plt.subplots()

    summary.plot(kind="bar", ax=ax)

    ax.set_title("Category Analysis")

    ax.set_ylabel(value_column)

    return summary, fig