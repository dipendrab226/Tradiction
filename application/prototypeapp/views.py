from django.core.mail import EmailMessage
from django.template.context_processors import csrf
from get_all_tickers import get_tickers as gt
from django.core.checks import Error
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import mysql.connector
from newsapi import NewsApiClient
from pprint import pprint
import pandas as pd
import yfinance as yf
from .sentimenttwitter import query_twitter
from django.contrib.messages.storage import session
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import datetime
import hashlib

# Create your views here.


def registration(request):
    return render(request, 'registration/trader_register.html')


def expertregistration(request):
    return render(request, 'registration/expert_register.html')


def portfolio(request):
    lid = request.session.get('lid')
    print(lid)
    if lid is not None:
        lid = int(request.session.get('lid'))
    if lid:
        return render(request, 'portfolio.html')
    else:
        return login(request)


def help(request):
    return render(request, 'help.html')


def login(request):
    return render(request, 'registration/login.html')


def tradinghistory(request):
    lid = int(request.session.get('lid'))
    if lid:
        return render(request, 'tradinghistory.html')
    else:
        return login(request)


def logout(request):
    lid = int(request.session.get('lid'))
    print(lid)
    del request.session['lid']
    return index(request)


def between(request):
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    lid = int(request.session.get('lid'))
    bid = int(request.session.get('bid'))
    total = request.session.get('total')
    sid = request.session.get('sid')
    query = "SELECT firstname,username,phoneno FROM traderreg join login on traderreg.lid= login.lid where login.lid ='%d' ;" % lid
    print("between", query)
    cursor.execute(query)
    rows = cursor.fetchall()
    print("between rows", rows)
    return render(request, 'between.html', {'rows': rows, 'total': total, 'bid': bid})


def Home(request):
    MERCHANT_KEY = "dORgZtd2"
    key = "dORgZtd2"
    SALT = "pu96lYOYtR"
    PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"

    action = "https://sandboxsecure.payu.in/_payment"
    posted = {}
    # Merchant Key and Salt provided y the PayU.
    for i in request.POST:
        posted[i] = request.POST[i]
    hash_object = hashlib.sha256(b'randint(0,20)')
    txnid = hash_object.hexdigest()[0:20]
    hashh = ''
    posted['txnid'] = txnid
    hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
    posted['key'] = key
    hash_string = ''
    hashVarsSeq = hashSequence.split('|')
    for i in hashVarsSeq:
        try:
            hash_string += str(posted[i])
        except Exception:
            hash_string += ''
        hash_string += '|'
    hash_string += SALT

    hashh = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
    action = PAYU_BASE_URL
    if (posted.get("key") != None and posted.get("txnid") != None and posted.get("productinfo") != None and posted.get(
            "firstname") != None and posted.get("email") != None):
        # return render_to_response('current_datetime.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"'https://sandboxsecure.payu.in/_payment" }))
        return render(request, 'current_datetime.html',
                      {"posted": posted, "hashh": hashh, "MERCHANT_KEY": MERCHANT_KEY, "txnid": txnid,
                       "hash_string": hash_string, "action": "https://sandboxsecure.payu.in/_payment"})
    else:
        return render(request, 'current_datetime.html',
                      {"posted": posted, "hashh": hashh, "MERCHANT_KEY": MERCHANT_KEY, "txnid": txnid,
                       "hash_string": hash_string, "action": "."})


@csrf_protect
@csrf_exempt
def success(request):
    c = {}
    c.update(csrf(request))
    status = request.POST["status"]
    # status = '1'
    firstname = request.POST["firstname"]
    amount = request.POST["amount"]
    txnid = request.POST["txnid"]
    posted_hash = request.POST["hash"]
    key = request.POST["key"]
    productinfo = request.POST["productinfo"]
    print("productinfo", productinfo)
    result = productinfo.split(",")
    bid = result[0]
    lid = result[1]
    request.session['lid'] = lid
    email = request.POST["email"]
    salt = "c7GRmpi4Yb"
    date = datetime.datetime.now().strftime("%c")

    try:
        additionalCharges = request.POST["additionalCharges"]
        # additionalCharges = '0'
        retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + bid + '|' + amount + '|' + txnid + '|' + key
    except Exception:
        retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + bid + '|' + amount + '|' + txnid + '|' + key
    hashh = hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
    if (hashh != posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ", txnid)
        print("We have received a payment of Rs. ", amount, ". Your order will soon be shipped.")
    # return render_to_response('sucess.html',RequestContext(request,{"txnid":txnid,"status":status,"amount":amount}))

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "INSERT INTO payment (bid,tranid,status,date) VALUES('%s','%s','%s','%s')" % (bid, txnid, status, date)
    cursor.execute(query)
    conn.commit()
    query = "UPDATE buystocks SET status='payment successful' where bid=%s" % bid
    cursor.execute(query)
    conn.commit()
    subject = "PAYMENT SUCCESSFUL"
    Body = "HELLO " + firstname + ", Congratulations. Your Payment is successful."

    try:
        email = EmailMessage(subject, Body, to=[email])
        email.send()
        print("sent")

    except Error as e:
        print(e)

    return portfolio(request)


@csrf_protect
@csrf_exempt
def failure(request):
    c = {}
    c.update(csrf(request))
    # status=request.POST["status"]
    status = '0'
    firstname = request.POST["firstname"]
    amount = request.POST["amount"]
    txnid = request.POST["txnid"]
    posted_hash = request.POST["hash"]
    key = request.POST["key"]
    productinfo = request.POST["productinfo"]
    result = productinfo.split(",")
    bid = result[0]
    lid = result[1]
    email = request.POST["email"]
    date = datetime.datetime.now().strftime("%c")
    salt = "c7GRmpi4Yb"
    try:
        # additionalCharges=request.POST["additionalCharges"]
        additionalCharges = '0'
        retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
    except Exception:
        retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key

    hashh = hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
    if (hashh != posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ", txnid)
        print("We have received a payment of Rs. ", amount, ". Your order will soon be shipped.")
        # return render_to_response("Failure.html",RequestContext(request,c))
        return render(request, 'Failure.html')

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "INSERT INTO payment (bid,tranid,status,date) VALUES('%s','%s','%s','%s')" % (
        bid, txnid, status, date)
    cursor.execute(query)
    conn.commit()
    query = "UPDATE buystocks SET status='payment successful' where bid=%s" % bid
    cursor.execute(query)
    conn.commit()
    return portfolio(request)


def index(request):

    lid = request.session.get('lid')
    if lid is not None:
        lid = int(lid)
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
    return render(request, 'home.html', {'articles': articles, 'lid': lid})


def search(request):

    try:
        conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
        cursor = conn.cursor()
        query = 'select count(*) from stocks'
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        if rows is None:

            payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
            table = payload[0]

            symbols = table['Symbol'].values.tolist()
            print(symbols)

            names = table['Security'].values.tolist()
            print(names)

            query = 'TRUNCATE `tradiction`.`stocks`'
            cursor.execute(query)
            for i, j in zip(symbols, names):
                i = "\"" + i + "\""
                j = "\"" + j + "\""
                print(i, j)
                query = 'INSERT INTO stocks (`symbol`, `name`) VALUES (%s, %s)' % (i, j)
                cursor.execute(query)

        string = "\"" + "%" + request.GET.get("search") + "%" + "\""
        print(string)
        query = 'SELECT stocksymbol, stockname from stocks where stockname LIKE %s' % string
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return render(request, 'stocks.html', {"row": rows})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


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
        pwd = "\"" + request.POST.get('pwd') + "\""
        cpwd = "\"" + request.POST.get('cpwd') + "\""

        conn = mysql.connector.connect(host="localhost", database="tradiction", user="root", password="toor")
        cursor = conn.cursor()

        """if request.method == 'POST' and request.FILES['bankstatement']:
            fs = FileSystemStorage()

            # Bank Statement

            filename = bankst.name
            extension = filename.split(".")
            upload_file_name = fname + lname + "_bankstatement." + extension[1]
            filename = fs.save(upload_file_name, bankst)
            bankstatement_url = "\"" + fs.url(filename) + "\""   """

        if (pwd == cpwd):
            query = "insert into tradiction.login (username,password) values (%s,%s)" % (email, pwd)
            cursor.execute(query)

            id = cursor.lastrowid

            query = "insert into tradiction.traderreg (firstname, lastname, address, city, state, phoneno, ssnno, bankst, routingno, accountno, lid) " \
                    "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)" % (
                    fname, lname, address, city, state, phono, ssnno, '"bankstatement.pdf"', routingno, accno, id)

            cursor1 = conn.cursor()
            cursor1.execute(query)
            conn.commit()
            msg = "Registration Complete !!"
            return render(request, 'registration/login.html', {'msg': msg})

        else:
            msg = "Passwords do not match"
            return render(request, 'registration/trader_register.html', {'msg': msg})


def addexpert(request):

    fname = "\"" + request.POST.get('fname') + "\""
    lname = "\"" + request.POST.get('lname') + "\""
    email = "\"" + request.POST.get('email') + "\""
    address = "\"" + request.POST.get('address') + "\""
    city = "\"" + request.POST.get('city') + "\""
    state = "\"" + request.POST.get('state') + "\""
    postalcode = "\"" + request.POST.get('postalcode') + "\""
    phono = "\"" + request.POST.get('phono') + "\""
    ssnno = "\"" + request.POST.get('ssnno') + "\""
    pwd = "\"" + request.POST.get('pwd') + "\""
    cpwd = "\"" + request.POST.get('cpwd') + "\""

    conn = mysql.connector.connect(host="localhost", database="tradiction", user="root", password="toor")
    cursor = conn.cursor()

    if pwd == cpwd:
        query = "insert into tradiction.login (username,password) values (%s,%s)" % (email, pwd)
        cursor.execute(query)
        id = cursor.lastrowid

        query = "insert into tradiction.expertreg (firstname, lastname, address, city, state, postalcode, phoneno, ssnno, expertcertificate, loid) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)" % (
                    fname, lname, address, city, state, postalcode, phono, ssnno, '"certificate.pdf"', id)

        cursor.execute(query)
        conn.commit()
        return login(request)

    else:
        msg = "Passwords do not match"
        return render(request, 'registration/expert_register.html', {'msg': msg})


def logindata(request):

    uname = request.GET.get('username')
    pwd = request.GET.get('password')

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "SELECT password,lid FROM login WHERE username= '%s'" % uname
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

    if rows:
        loginpwd = rows[0][0]
        loginid = rows[0][1]
        request.session['lid'] = loginid

        if pwd == loginpwd:
            return index(request)

        else:
            msg = "Entered Password is incorrect!!!"
            return render(request, "registration/login.html", {'msg': msg})

    else:
        msg = "Given username does not exist!!!"
        return render(request, "registration/login.html", {'msg': msg})


def news(request):

    topnews = NewsApiClient(api_key='17338a8016484433bcd67895a6a6ed95')

    # /v2/top-headlines
    top_headlines = topnews.get_everything(
        q='market',
        language='en')
    articles = top_headlines['articles']

    top_headlines = topnews.get_everything(
        q='stock',
        language='en')
    articles.extend(top_headlines['articles'])

    top_headlines = topnews.get_top_headlines(
                      category='business',
                      language='en',
                      country='us')

    articles.extend(top_headlines['articles'])
    pprint(articles)
    return render(request, 'news.html', {'articles': articles})


def loadstocks(request):
    list_of_tickers = gt.get_tickers()
    pprint(list_of_tickers)
    name = []
    for i in list_of_tickers:
        symbol = yf.Ticker(i)
        name.append(symbol.info['longName'])

    pprint(name)


def stocks(request):
    lid = request.session.get('lid')
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    if lid is not None:
        lid = int(lid)
        query = "SELECT symbol FROM watchlist where logid = %d" % lid
        cursor.execute(query)
        rows1 = cursor.fetchall()
        print(rows1)
        symbols = []
        for i in rows1:
            symbols.append(i[0])

    query = "SELECT * FROM stocks"
    cursor.execute(query)
    rows = cursor.fetchall()

    if lid:
        return render(request, 'stocks.html', {'rows': rows, 'symbols': symbols, 'lid': lid})
    else:
        return render(request, 'stocks.html', {'rows': rows})


def stockdetails(request):

    lid = request.session.get('lid')
    if lid is not None:
        lid = int(lid)

    ticker = request.GET.get("stock")
    symbol = yf.Ticker(ticker)
    details = symbol.info
    pprint(details)
    ans = query_twitter(details['longName'], 100)
    pprint(ans)

    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "SELECT wid FROM watchlist where symbol='%s' and logid = '%d'" % (ticker, lid)
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        flag = 1
    else:
        flag = 0
    query = "SELECT sid from stocks where stocksymbol='%s'" % ticker
    cursor.execute(query)
    sid = cursor.fetchone()
    return render(request, 'details.html', {'details': details, 'twitter': ans, 'flag': flag, 'sid': sid})


def addtowatchlist(request):

    lid = request.session.get('lid')
    print(lid)
    if lid is not None:
        lid = int(lid)
        symbol = request.GET.get('symbol')
        print(symbol)
        conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
        cursor = conn.cursor()
        query = "INSERT INTO watchlist (logid, symbol) values ('%d','%s') on duplicate " \
                "key update wid=LAST_INSERT_ID(wid=0)" % (lid, symbol)
        cursor.execute(query)
        conn.commit()
        return stocks(request)

    else:
        return login(request)


def watchlist(request):
    lid = request.session.get('lid')
    if lid is not None:
        lid = int(lid)
        conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
        cursor = conn.cursor()
        query = "SELECT wid,logid,stockname,stocksymbol FROM watchlist join stocks on watchlist.symbol = stocks.stocksymbol where watchlist.logid = %d" % lid
        cursor.execute(query)
        rows = cursor.fetchall()
        return render(request, 'watchlist.html', {'rows': rows, 'lid': lid})
    else:
        return login(request)


def removefromwatchlist(request):

    lid = int(request.session.get('lid'))
    symbol = request.GET.get('symbol')
    print(symbol)
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()
    query = "DELETE FROM watchlist where symbol='%s' and logid=%d" % (symbol, lid)
    cursor.execute(query)
    conn.commit()
    return stocks(request)


def addstocks(request):

    sid = int(request.GET.get('id'))
    ticker = request.GET.get('symbol')
    lid = int(request.session.get('lid'))
    symbol = yf.Ticker(ticker)
    details = symbol.info
    pprint(details)
    buyprice = details['previousClose']
    name = details['longName']
    details = [name, buyprice, sid]
    return render(request, 'buystocks.html', {'details': details, 'lid': lid})


def buystocks(request):
    sid = request.POST.get('sid')
    print(sid)
    cprice = request.POST.get('cprice')
    sname = request.POST.get('sname')
    quantity = request.POST.get('quantity')
    total = request.POST.get('total')
    lid = int(request.session.get('lid'))
    date = datetime.datetime.now().strftime("%c")
    request.session['sid'] = sid
    request.session['total'] = total
    conn = mysql.connector.connect(host='localhost', database='tradiction', user='root', password='toor')
    cursor = conn.cursor()

    query = "insert into buystocks(lid,stid,sname,datetime,buyprice,quantity,total,status) values ('%d','%s','%s','%s','%s','%s','%s','%s')" \
            % (lid, sid, sname, date, cprice, quantity, total, "pending")
    print("add stock", query)
    cursor.execute(query)
    conn.commit()
    bid = cursor.lastrowid
    request.session['bid'] = bid
    return between(request)
