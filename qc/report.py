import pandas as pd

def build_qc_report(results: dict):
    """
    Builds a text report from QC check results.
    """
    lines = []

    lines.append("QC REPORT")
    lines.append("=" * 40)

    for check_name, obj in results.items():
        lines.append(f"\n[{check_name}]")

        # Case 1: pandas DataFrame (rows flagged)
        if isinstance(obj, pd.DataFrame):
            n = obj.shape[0]
            lines.append(f"Number of flagged rows: {n}")

            if n > 0 and "gene" in obj.columns:
                lines.append("Affected genes:")
                for g in obj["gene"].astype(str).tolist():
                    lines.append(f" - {g}")

        # Case 2: pandas Series (summary per column)
        elif isinstance(obj, pd.Series):
            lines.append("Summary:")
            for idx, val in obj.items():
                lines.append(f" - {idx}: {val}")

        # Fallback: anything else
        else:
            lines.append(str(obj))

    return "\n".join(lines)

