import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_expression_distribution(df: pd.DataFrame, output_path="outputs/expression_distribution.png"):
    expr = pd.to_numeric(df["mean_expression"], errors="coerce")

    plt.figure(figsize=(7, 5))
    sns.histplot(expr.dropna(), bins=30, kde=True)

    plt.title("Distribution of Mean Expression Values")
    plt.xlabel("Mean expression")
    plt.ylabel("Number of genes")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_log2fc_distribution(df: pd.DataFrame, output_path="outputs/log2fc_distribution.png"):
    logfc = pd.to_numeric(df["log2FC"], errors="coerce")

    plt.figure(figsize=(7, 5))
    sns.histplot(logfc.dropna(), bins=30, kde=True)

    plt.title("Distribution of log2 Fold-Change Values")
    plt.xlabel("log2 Fold-change")
    plt.ylabel("Number of genes")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_expression_boxplot(df: pd.DataFrame, output_path="outputs/expression_boxplot.png"):
    expr = pd.to_numeric(df["mean_expression"], errors="coerce")

    plt.figure(figsize=(6, 4))
    sns.boxplot(x=expr)

    plt.title("Boxplot of Mean Expression (Outlier Detection)")
    plt.xlabel("Mean expression")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
