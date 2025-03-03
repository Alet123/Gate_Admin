from django.shortcuts import render


# Other views for rendering templates
def graph_view(request):
    return render(request, 'graphs.html')


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
