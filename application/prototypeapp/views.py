from django.core.checks import Error
from django.shortcuts import render
import mysql.connector
from newsapi import NewsApiClient
from pprint import pprint
import pandas as pd

# Create your views here.

def home(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, 'trader_register.html')

def login(request):
    return render(request, 'login.html')

def viewindex(request):
    payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = payload[0]

    symbols = table['Symbol'].values.tolist()
    print(symbols)

    names = table['Security'].values.tolist()
    print(names)

    # list = [symbols, names]

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
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

def search(request):

    string = "\"" + "%" + request.GET.get("search") + "%" + "\""
    print(string)
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = 'SELECT symbol, name from stocks where name LIKE %s' % string
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'home.html', {"row": rows})

def regdata(request):

    try:
        fname = "\"" + request.POST.get('fname') + "\""
        lname = "\"" + request.POST.get('lname') + "\""
        email = "\"" + request.POST.get('email') + "\""
        gender = "\"" + request.POST.get('gender') + "\""
        city = "\"" + request.POST.get('city') + "\""
        country = "\"" + request.POST.get('country') + "\""
        pwd = "\"" + request.POST.get('password') + "\""

        conn = mysql.connector.connect(host="localhost", database="tradiction", user="root", password="toor")
        cursor = conn.cursor()

        query = "insert into tradiction.login (username,password) values (%s,%s)" % (email, pwd)
        cursor.execute(query)
        conn.commit()
        id = cursor.lastrowid

        query = "insert into tradiction.traderreg (firstname,lastname,gender,city,country,lid) " \
                "values (%s,%s,%s,%s,%s,%d)" % (fname, lname, gender, city, country, id)
        cursor.execute(query)
        conn.commit()
        msg = ("Registration Complete !!")
        return render(request, 'login.html', {'msg': msg})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()



def logindata(request):
    uname = request.GET.get('username')
    pwd = request.GET.get('password')
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "SELECT password,lid FROM login WHERE username= '%s'" % uname
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    loginpwd = rows[0][0]
    loginid = rows[0][1]
    request.session['lid'] = loginid

    if pwd == loginpwd:
        return render(request, "home.html")

    else:
        msg = "Either username or password is incorrect."
        return render(request, "login.html", {'msg': msg})
