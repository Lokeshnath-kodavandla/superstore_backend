import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile
import os


def generate_csv(df, start_date, end_date):
    filtered = df[
        (df["Order Date"] >= start_date) &
        (df["Order Date"] <= end_date)
    ]

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    filtered.to_csv(temp_file.name, index=False)
    return temp_file.name


def generate_pdf(df, start_date, end_date):
    filtered = df[
        (df["Order Date"] >= start_date) &
        (df["Order Date"] <= end_date)
    ]

    total_sales = round(filtered["Sales"].sum(), 2)
    total_profit = round(filtered["Profit"].sum(), 2)
    total_orders = filtered["Order ID"].nunique()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp_file.name, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "E-Commerce Sales Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"From: {start_date}")
    c.drawString(50, 740, f"To: {end_date}")

    c.drawString(50, 700, f"Total Sales: {total_sales}")
    c.drawString(50, 680, f"Total Profit: {total_profit}")
    c.drawString(50, 660, f"Total Orders: {total_orders}")

    c.showPage()
    c.save()

    return temp_file.name
