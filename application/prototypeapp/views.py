from django.core.checks import Error
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import mysql.connector
from newsapi import NewsApiClient
from pprint import pprint
import pandas as pd


# Create your views here.

def registration(request):
    return render(request, 'trader_register.html')


def expertregistration(request):
    return render(request, 'expert_register.html')


def stocks(request):
    return render(request, 'stocks.html')


def news(request):
    return render(request, 'news.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def watchlist(request):
    return render(request, 'watchlist.html')


def help(request):
    return render(request, 'help.html')


def login(request):
    return render(request, 'login.html')


def tradinghistory(request):
    return render(request, 'tradinghistory.html')


def index(request):
    payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = payload[0]

    symbols = table['Symbol'].values.tolist()
    print(symbols)

    names = table['Security'].values.tolist()
    print(names)

    # list = [symbols, names]

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='admin1', password='Admin123')
    cursor = conn.cursor()
    query = 'TRUNCATE `tradiction`.`stocks`'
    cursor.execute(query)
    for i, j in zip(symbols, names):
        i = "\"" + i + "\""
        j = "\"" + j + "\""
        print(i, j)
        query = 'INSERT INTO stocks (`symbol`, `name`) VALUES (%s, %s)' % (i, j)
        cursor.execute(query)

    conn.commit()
    # lid = int(request.session.get('lid'))
    news = NewsApiClient(api_key='17338a8016484433bcd67895a6a6ed95')

    # /v2/top-headlines
    top_headlines = news.get_top_headlines(
        category='business',
        language='en',
        country='us')
    print("topheadlines:", top_headlines)
    articles = top_headlines['articles']
    pprint(articles)

    titles = []
    for singlearticle in articles:
        titles.append(singlearticle.get('title'))

    pprint(titles)
    return render(request, 'home.html', {'articles': articles})


"""def search(request):

    string = "\"" + "%" + request.GET.get("search") + "%" + "\""
    print(string)
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = 'SELECT symbol, name from stocks where name LIKE %s' % string
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'home.html', {"row": rows})"""


def addtrader(request):

        fname = "\"" + request.POST.get('fname') + "\""
        lname = "\"" + request.POST.get('lname') + "\""
        email = "\"" + request.POST.get('email') + "\""
        address = "\"" + request.POST.get('address') + "\""
        city = "\"" + request.POST.get('city') + "\""
        state = "\"" + request.POST.get('state') + "\""
        phono = "\"" + request.POST.get('phono') + "\""
        ssnno = "\"" + request.POST.get('ssnno') + "\""
        # bankst = request.FILES['bankst']
        routingno = "\"" + request.POST.get('routingno') + "\""
        accno = "\"" + request.POST.get('accno') + "\""
        pwd = "\"" + request.POST.get('password') + "\""

        conn = mysql.connector.connect(host="localhost", database="tradiction", user="admin1", password="Admin123")
        cursor = conn.cursor()

        """if request.method == 'POST' and request.FILES['bankstatement']:
            fs = FileSystemStorage()

            # Bank Statement

            filename = bankst.name
            extension = filename.split(".")
            upload_file_name = fname + lname + "_bankstatement." + extension[1]
            filename = fs.save(upload_file_name, bankst)
            bankstatement_url = "\"" + fs.url(filename) + "\""   """

        query = "insert into tradiction.login (username,password) values (%s,%s)" % (email, pwd)
        cursor.execute(query)
        conn.commit()
        id = cursor.lastrowid

        query = "insert into tradiction.traderreg (firstname, lastname, address, city, state, phoneno, ssnno, bankst, routingno, accountno, lid) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)" % (
                fname, lname, address, city, state, phono, ssnno, '"sa"', routingno, accno, id)

        cursor1 = conn.cursor()
        cursor1.execute(query)
        conn.commit()
        msg = "Registration Complete !!"
        return render(request, 'login.html', {'msg': msg})


def logindata(request):
    uname = request.GET.get('username')
    pwd = request.GET.get('password')
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='admin1', password='Admin123')
    cursor = conn.cursor()
    query = "SELECT password,lid FROM login WHERE username= '%s'" % uname
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    loginpwd = rows[0][0]
    loginid = rows[0][1]
    request.session['lid'] = loginid

    if pwd == loginpwd:
        return index(request)

    else:
        msg = "Either username or password is incorrect."
        return render(request, "login.html", {'msg': msg})
