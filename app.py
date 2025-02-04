from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

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
        # List the tour groups for the selected tour
        tourid = request.form.get("tourid")
        qstr = f"select tourgroupid, startdate from tourgroups where tourid={tourid};"
        cursor.execute(qstr)
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
    qstr = f"""SELECT c.customerid, c.firstname, c.familyname, c.dob, c.email, c.phone, t.tourid, t.tourname, tb.bookingid
                FROM customers AS c 
                JOIN tours AS t ON t.tourid={tourid} 
                JOIN tourbookings AS tb ON tb.tourgroupid = {tourgroupid} 
                ORDER BY c.firstname ASC, c.dob ASC;"""
    cursor.execute(qstr)
    customerlist = cursor.fetchall()
    return render_template("tourlist.html", tourname=tourname, startdate=startdate, customerlist=customerlist)


@app.route("/makebooking", methods=["GET", "POST"])
def makebooking():
    cursor = getCursor()
    if request.method == "POST":
        customerid = request.form.get('customerid')
        tourgroupid = request.form.get('tourgroupid')

        # Get customer dob
        qstr = "SELECT dob FROM customers WHERE customerid=%s;"
        cursor.execute(qstr, (customerid,))
        dob = cursor.fetchone()['dob']

        # Get tourgroup start date and tour age restriction
        qstr = "SELECT startdate, t.agerestriction FROM tourgroups tg JOIN tours t ON tg.tourid = t.tourid WHERE tg.tourgroupid=%s;"
        cursor.execute(qstr, (tourgroupid,))
        tour_info = cursor.fetchone()
        startdate = tour_info['startdate']
        agerestriction = tour_info['agerestriction']

        # Calculate customer age
        # from datetime import datetime
        # dob = datetime.strptime(dob, '%Y-%m-%d')
        # startdate = datetime.strptime(startdate, '%Y-%m-%d')
        age = (startdate - dob).days // 365

        # Check age restriction
        if age < agerestriction:
            return render_template("booking.html", error="Age restriction not met for this tour.")

        # Insert booking
        qstr = "INSERT INTO tourbookings (tourgroupid, customerid) VALUES (%s, %s);"
        cursor.execute(qstr, (tourgroupid, customerid))
        return redirect(url_for('Orders'))

    # GET method: Display booking form
    qstr = "SELECT customerid, firstname, familyname FROM customers;"
    cursor.execute(qstr)
    customers = cursor.fetchall()

    qstr = "SELECT tg.tourgroupid, t.tourname, tg.startdate FROM tourgroups tg JOIN tours t ON tg.tourid = t.tourid WHERE tg.startdate > CURDATE();"
    cursor.execute(qstr)
    tourgroups = cursor.fetchall()
    return render_template("booking.html", customers=customers, tourgroups=tourgroups)


@app.route("/customer_search")
def customer_search():
    # List customer details.
    cursor = getCursor()
    qstr = "SELECT * FROM customers ORDER BY customers.familyname, customers.dob ASC"
    cursor.execute(qstr)
    customers = cursor.fetchall()
    counts = len(customers)
    return render_template("customers.html", flag=1, counts=counts, customers=customers)


@app.route('/customer_new', methods = ['GET', 'POST'])
def customer_new():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        familyname = request.form.get('familyname')
        dob = request.form.get('dob')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cursor = getCursor()
        qstr = "INSERT INTO customers (firstname, familyname, dob, email, phone) VALUES (%s, %s, %s, %s, %s)"; 
        cursor.execute(qstr, (firstname, familyname, dob, email, phone))
        return redirect(url_for('customer_search'))
    else:
        return render_template("users.html", flag=1)


@app.route('/customer_edit', methods = ['GET', 'POST'])
def customer_edit():
    if request.method == 'POST':
        selected_user = request.form.get('edit_options')
        cursor = getCursor()
        qstr = f"SELECT * FROM customers WHERE customerid = {selected_user};"
        cursor.execute(qstr)
        customer = cursor.fetchone()
        return render_template("users.html", flag=2, customer=customer)
    else:
        cursor = getCursor()
        qstr = "SELECT * FROM customers;"
        cursor.execute(qstr)
        customers = cursor.fetchall()
        return render_template("users.html", flag=3, customers=customers)
    

@app.route('/customer_update', methods = ['POST'])
def customer_update():
    cursor = getCursor()
    firstname = request.form.get('firstname')
    familyname = request.form.get('familyname')
    dob = request.form.get('dob')
    email = request.form.get('email')
    phone = request.form.get('phone')
    customerid = request.form.get('customerid')
    qstr = "UPDATE customers SET firstname = %s, familyname = %s, dob = %s, email = %s, phone = %s WHERE customerid = %s;"
    cursor.execute(qstr, (firstname, familyname, dob, email, phone, customerid))
    return redirect(url_for('customer_search'))


@app.route("/Orders", methods=['GET', 'POST'])
def Orders():
    if request.method == 'POST':
        cursor = getCursor()
        customerid = request.form.get('customerid')
        # qstr = f"""SELECT tk.bookingid, tk.tourgroupid, tg.tourid, t.tourname, it.destinationid, dt.destinationname, tk.customerid, c.firstname, c.familyname, c.dob, 
        # c.email FROM tourbookings as tk JOIN customers as c ON tk.customerid = c.customerid JOIN tourgroups as tg ON 
        # tk.tourgroupid = tg.tourgroupid JOIN tours AS t ON tg.tourid = t.tourid JOIN itineraries AS it ON 
        # it.tourid = t.tourid JOIN destinations AS dt ON it.destinationid = dt.destinationid WHERE tk.customerid = {customerid} ORDER BY tk.bookingid ASC"""

        qstr = f"""select c.customerid, c.firstname, c.familyname, c.dob, c.email, tb.bookingid, t.tourid, t.tourname ,tg.startdate from tourbookings as tb 
                    join customers as c on c.customerid=tb.customerid
                    join tourgroups as tg on tg.tourgroupid = tb.tourgroupid 
                    join tours as t on t.tourid = tg.tourid
                    where c.customerid = {customerid}
                    order by c.familyname, c.dob asc;
                """
        cursor.execute(qstr)
        orders = cursor.fetchall()
        return render_template("customers.html", flag=4, orderlist=orders)
    else:
        cursor = getCursor()
        qstr = "SELECT tk.bookingid, tk.tourgroupid, tk.customerid, c.firstname, c.familyname, c.dob, c.email FROM tourbookings tk JOIN customers c ON tk.customerid = c.customerid ORDER BY tk.bookingid ASC;"
        cursor.execute(qstr)
        orders = cursor.fetchall()
        return render_template("customers.html", flag=2, orderlist=orders)


@app.route("/Searching")
def Searching():
    cursor = getCursor()
    qstr = "SELECT customerid, firstname, familyname FROM customers;"
    cursor.execute(qstr)
    customers = cursor.fetchall()
    return render_template("customers.html", flag=3, customers=customers)


@app.route("/booking/search", methods=['POST'])
def bookingSearch():
    user_id = request.form.get('customerid')
    cursor = getCursor()

    # qstr = f"""SELECT tk.bookingid, tk.tourgroupid, tg.tourid, t.tourname, it.destinationid, dt.destinationname, tk.customerid, c.firstname, c.familyname, c.dob, 
    # c.email FROM tourbookings as tk JOIN customers as c ON tk.customerid = c.customerid JOIN tourgroups as tg ON 
    # tk.tourgroupid = tg.tourgroupid JOIN tours AS t ON tg.tourid = t.tourid JOIN itineraries AS it ON 
    # it.tourid = t.tourid JOIN destinations AS dt ON it.destinationid = dt.destinationid WHERE tk.customerid = {user_id} ORDER BY tk.bookingid ASC"""
    qstr = f"""select c.customerid, c.firstname, c.familyname, c.dob, c.email, tb.bookingid, t.tourid, t.tourname ,tg.startdate from tourbookings as tb 
                join customers as c on c.customerid=tb.customerid
                join tourgroups as tg on tg.tourgroupid = tb.tourgroupid 
                join tours as t on t.tourid = tg.tourid
                where c.customerid = {user_id}
                order by c.familyname, c.dob asc;
            """
    cursor.execute(qstr)
    orders = cursor.fetchall()
    return render_template("customers.html", flag=4, orderlist=orders)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
