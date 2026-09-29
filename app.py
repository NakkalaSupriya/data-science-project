import csv
import os
from statistics import mean


def load_data(file_path):
    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["sales"] = float(row["sales"])
            row["marketing_spend"] = float(row["marketing_spend"])
            row["customers"] = int(row["customers"])
            rows.append(row)
    return rows


def show_summary(rows):
    total_sales = sum(row["sales"] for row in rows)
    total_marketing = sum(row["marketing_spend"] for row in rows)
    total_customers = sum(row["customers"] for row in rows)
    average_sales = mean(row["sales"] for row in rows)
    best_month = max(rows, key=lambda row: row["sales"])

    print("\n===== DATA SCIENCE PROJECT =====")
    print(f"Number of records : {len(rows)}")
    print(f"Total sales       : {total_sales:.2f}")
    print(f"Marketing spend   : {total_marketing:.2f}")
    print(f"Total customers   : {total_customers}")
    print(f"Average sales     : {average_sales:.2f}")
    print(f"Best month        : {best_month['month']}")
    print(f"Best month sales  : {best_month['sales']:.2f}")


def show_marketing_analysis(rows):
    print("\n===== MARKETING ANALYSIS =====")
    for row in rows:
        roi = row["sales"] / row["marketing_spend"]
        print(f"{row['month']}: sales={row['sales']:.2f}, marketing={row['marketing_spend']:.2f}, ROI={roi:.2f}")


def main():
    file_path = os.path.join("data", "sales_data.csv")
    try:
        rows = load_data(file_path)
        show_summary(rows)
        show_marketing_analysis(rows)
        print("\nProject completed successfully.")
    except FileNotFoundError:
        print("ERROR: data/sales_data.csv was not found.")
    except ValueError:
        print("ERROR: The CSV contains an invalid numeric value.")


if __name__ == "__main__":
    main()
