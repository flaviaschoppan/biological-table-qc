from qc.loader import load_table
from qc.checks import (
    check_missing_values,
    check_invalid_pvalues,
    check_negative_expression,
    check_non_numeric_log2fc,
    check_extreme_expression,
)
from qc.report import build_qc_report
from qc.plots import plot_expression_distribution, plot_log2fc_distribution


def main():
    df = load_table("data/example_results.csv")

    results = {
        "Missing values per column": check_missing_values(df),
        "Invalid p-values": check_invalid_pvalues(df),
        "Negative mean expression": check_negative_expression(df),
        "Non-numeric log2FC": check_non_numeric_log2fc(df),
        "Extreme expression values": check_extreme_expression(df),
    }

    report = build_qc_report(results)

    print(report)

    with open("qc_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nQC report saved to qc_report.txt")

    plot_expression_distribution(df)
    plot_log2fc_distribution(df)

    print("QC plots saved:")
    print(" - expression_distribution.png")
    print(" - log2fc_distribution.png")

if __name__ == "__main__":
    main()
