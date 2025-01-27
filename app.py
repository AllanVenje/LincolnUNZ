from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import date, datetime, timedelta
import mysql.connector
import mysql.connector.pooling
import connect

app = Flask(__name__)

dbconn = None
connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="atl", user=connect.dbuser, \
                                                              password=connect.dbpass, host=connect.dbhost, \
                                                              database=connect.dbname, autocommit=True)
connection = None


def getCursor():
    global dbconn
    global connection
    if connection is None:
        connection = connection_pool.get_connection()
    if dbconn is None:
        dbconn = connection.cursor(dictionary=True)
    return dbconn


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tours", methods=["GET", "POST"])
def tours():
    cursor = getCursor()
    if request.method == "GET":
        # Lists the tours        
        qstr = "select tourid, tourname from tours;"
        cursor.execute(qstr)

        tours = cursor.fetchall()
        return render_template("tours.html", tours=tours)
    else:
        tourid = request.form.get("tourid")
        qstr = "select tourgroupid, startdate from tourgroups where tourid=%s;"
        cursor.execute(qstr, (tourid,))
        tourgroups = cursor.fetchall()
        return render_template("tours.html", tourid=tourid, tourgroups=tourgroups)


@app.route("/tours/list", methods=["POST"])
def tourlist():
    tourid = request.form.get('tourid')
    tourgroupid = request.form.get('tourgroupid')
    # Display the list of customers on a tour
    cursor = getCursor()
    qstr = f"SELECT * FROM tours WHERE tourid={tourid};"
    cursor.execute(qstr)
    tourname = cursor.fetchone()['tourname']  # update to get the name of the tour
    qstr = f"SELECT startdate FROM tourgroups WHERE tourgroupid={tourgroupid};"
    cursor.execute(qstr)
    startdate = cursor.fetchone()['startdate']
    qstr = f"SELECT c.customerid, c.firstname, c.familyname, c.dob FROM customers c JOIN tourbookings tb ON c.customerid=tb.customerid WHERE tb.tourgroupid={tourgroupid} ORDER BY c.firstname, c.dob DESC;"
    cursor.execute(qstr)
    customerlist = cursor.fetchall()
    return render_template("tourlist.html", tourname=tourname, startdate=startdate, customerlist=customerlist)


@app.route("/customers")
def customers():
    # List customer details.
    cursor = getCursor()
    qstr = "SELECT * FROM customers;"
    cursor.execute(qstr)
    customers = cursor.fetchall()
    return render_template("customers.html", customers=customers)


@app.route("/booking/add")
def makebooking():
    # Make a booking
    return render_template()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
