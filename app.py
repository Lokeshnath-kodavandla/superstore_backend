from flask import Flask, jsonify, request
from services.data_loader import load_data
from services.analytics import (
    get_kpis,
    profit_by_subcategory,
    sales_by_subcategory,
    sales_by_category,
    profit_by_category
)
from utils.filters import apply_filters
from flask import send_file
from services.reports import generate_csv, generate_pdf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data once
df = load_data()


@app.route("/")
def home():
    return "Backend is running"


@app.route("/api/kpis")
def api_kpis():
    region = request.args.get("region")
    state = request.args.get("state")

    filtered_df = apply_filters(df, region, state)
    return jsonify(get_kpis(filtered_df))


@app.route("/api/profit_by_subcategory")
def api_profit_by_subcategory():
    region = request.args.get("region")
    state = request.args.get("state")

    filtered_df = apply_filters(df, region, state)
    return jsonify(profit_by_subcategory(filtered_df))


@app.route("/api/sales_by_subcategory")
def api_sales_by_subcategory():
    region = request.args.get("region")
    state = request.args.get("state")

    filtered_df = apply_filters(df, region, state)
    return jsonify(sales_by_subcategory(filtered_df))


@app.route("/api/sales_by_category")
def api_sales_by_category():
    region = request.args.get("region")
    state = request.args.get("state")

    filtered_df = apply_filters(df, region, state)
    return jsonify(sales_by_category(filtered_df))


@app.route("/api/profit_by_category")
def api_profit_by_category():
    region = request.args.get("region")
    state = request.args.get("state")

    filtered_df = apply_filters(df, region, state)
    return jsonify(profit_by_category(filtered_df))


@app.route("/api/generate_report")
def generate_report():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    file_format = request.args.get("format", "csv")

    if not start_date or not end_date:
        return jsonify({"error": "start_date and end_date required"}), 400

    if file_format == "pdf":
        file_path = generate_pdf(df, start_date, end_date)
        return send_file(file_path, as_attachment=True, download_name="report.pdf")

    file_path = generate_csv(df, start_date, end_date)
    return send_file(file_path, as_attachment=True, download_name="report.csv")


if __name__ == "__main__":
    app.run(debug=True)
