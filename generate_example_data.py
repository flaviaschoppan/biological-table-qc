import numpy as np
import pandas as pd

def generate_example_data(n_genes=3000, output_path="data/example_results.csv"):
    np.random.seed(42)

    # Generate gene names
    genes = [f"GENE_{i:04d}" for i in range(n_genes)]

    # Generate realistic distributions
    log2fc = np.random.normal(loc=0, scale=2, size=n_genes)
    p_values = np.random.uniform(0, 1, size=n_genes)
    mean_expression = np.random.lognormal(mean=4, sigma=1, size=n_genes)

    df = pd.DataFrame({
        "gene": genes,
        "log2FC": log2fc,
        "p_value": p_values,
        "mean_expression": mean_expression,
    })

    # ------------------------------------------------
    # Inject controlled "errors" for QC to detect
    # ------------------------------------------------

    # 1) Missing values
    df.loc[5, "log2FC"] = np.nan
    df.loc[25, "mean_expression"] = np.nan

    # 2) Invalid p-values
    df.loc[10, "p_value"] = 1.5
    df.loc[11, "p_value"] = -0.3

    # 3) Negative expression (biologically impossible)
    df.loc[50, "mean_expression"] = -100

    # 4) Non-numeric values in numeric column
    df.loc[80, "log2FC"] = "not_a_number"

    # 5) Extreme outliers
    df.loc[120, "mean_expression"] = 1e9
    df.loc[121, "mean_expression"] = 5e8

    # Save
    df.to_csv(output_path, index=False)

    print(f"Synthetic dataset generated at: {output_path}")
    print(f"Number of genes: {len(df)}")

if __name__ == "__main__":
    generate_example_data()
