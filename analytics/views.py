import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
import io
import urllib, base64

def salary_distribution(request):
    # Sample dataset: Employee Salaries (with an outlier)
    data = [1,2,2, 3, 4, 5,6,6, 6]
    df = pd.DataFrame(data, columns=['Salary'])

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Histogram
    sns.histplot(df['Salary'], bins=10, kde=True, color='blue', ax=ax)
    ax.axvline(df['Salary'].mean(), color='red', linestyle='dashed', linewidth=2, label=f"Mean: {df['Salary'].mean():,.0f}")
    ax.axvline(df['Salary'].median(), color='green', linestyle='dashed', linewidth=2, label=f"Median: {df['Salary'].median():,.0f}")
    ax.set_title("Salary Distribution (Histogram) (In L)")
    ax.set_xlabel("Salary")
    ax.set_ylabel("Frequency")
    ax.legend()

    # Save the figure to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image in base64
    graphic = base64.b64encode(image_png).decode("utf-8")
    
    return render(request, "analytics/chart.html", {"graphic": graphic})
