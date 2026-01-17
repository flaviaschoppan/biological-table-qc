import matplotlib.pyplot as plt
import pandas as pd

def plot_expression_distribution(df: pd.DataFrame, output_path="expression_distribution.png"):
    expr = pd.to_numeric(df["mean_expression"], errors="coerce")

    plt.figure(figsize=(6, 4))
    plt.hist(expr.dropna(), bins=20)
    plt.title("Distribution of mean expression")
    plt.xlabel("Mean expression")
    plt.ylabel("Number of genes")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_log2fc_distribution(df: pd.DataFrame, output_path="log2fc_distribution.png"):
    logfc = pd.to_numeric(df["log2FC"], errors="coerce")

    plt.figure(figsize=(6, 4))
    plt.hist(logfc.dropna(), bins=20)
    plt.title("Distribution of log2 fold-change")
    plt.xlabel("log2FC")
    plt.ylabel("Number of genes")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
