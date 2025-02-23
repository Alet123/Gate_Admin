from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from io import BytesIO
import base64


# View for fetching updated graph data in JSON format
def get_updated_graph_data(request):
    # Sample data for Call and Put prices
    nifty_values = [150, 120, 140, 800, 100]
    call_prices = [95, 120, 145, 175, 210]
    put_prices = [510, 720, 530, 340, 440]

    # Compute the average price for both Call and Put
    call_avg = np.mean(call_prices)
    put_avg = np.mean(put_prices)

    # Return the JSON response with categories and average prices
    return JsonResponse({
        'categories': ['Call', 'Put'],
        'call_prices': [call_avg],
        'put_prices': [put_avg],
    })


# View for rendering the plot graph (dynamic plot)
def plot_graph(request):
    # Example time categories
    times = ['08:00 AM', '09:00 AM']

    # Data for the bar charts
    bar1_values = [100, 200]  # Bar chart 1 with 2 values
    bar2_values = [150, 250]  # Bar chart 2 with 2 values

    # Create the plot (Matplotlib)
    fig, ax = plt.subplots()

    # Plotting the bar charts
    ax.bar(times, bar1_values, label='Bar 1', color='b', alpha=0.6, width=0.4, align='center')
    ax.bar(times, bar2_values, label='Bar 2', color='r', alpha=0.6, width=0.4, align='edge')

    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    ax.set_title('Sample Bar Chart Comparison')
    ax.legend()

    # Save the plot to a BytesIO buffer in PNG format
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the PNG image to base64
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the base64 image to the template
    context = {
        'times': times,
        'bar1_values': bar1_values,
        'bar2_values': bar2_values,
        'plot_image': img_base64  # Pass the plot image as base64
    }

    return render(request, 'graph.html', context)


# Other views for rendering templates
def login(request):
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def trade_graph(request):
    return render(request, "trade_graph.html")


def portfolio(request):
    return render(request, "portfolio.html")


def trading_accounts(request):
    return render(request, "trading_accounts.html")


def create_trading_accounts(request):
    return render(request, "create_trading_accounts.html")


def group_accounts(request):
    return render(request, "group_accounts.html")


def create_group_accounts(request):
    return render(request, "create_group_accounts.html")


def master_accounts(request):
    return render(request, "master_accounts.html")


def create_master_accounts(request):
    return render(request, "create_master_accounts.html")


def api(request):
    return render(request, "api.html")
