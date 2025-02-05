# Assignment: Web Application Development for ATL Project
<h2>Content</h2>

- [Assignment: Web Application Development for ATL Project](#assignment-web-application-development-for-atl-project)
  - [0. Assignment Requirements Translation and Problem-Solving Approach](#0-assignment-requirements-translation-and-problem-solving-approach)
  - [1. Milestone Submission](#1-milestone-submission)
    - [Requirements:](#requirements)
  - [2. Final Submission](#2-final-submission)
    - [Requirements:](#requirements-1)
  - [3. Problem-Solving Approach and Steps](#3-problem-solving-approach-and-steps)
    - [3.1 Milestone Submission](#31-milestone-submission)
    - [3.2 Final Submission](#32-final-submission)
  - [4. Assignment Proposal Summary](#4-assignment-proposal-summary)
  - [5. Report: Project Assignment](#5-report-project-assignment)
    - [5.1 Design Decisions:](#51-design-decisions)
      - [5.1.1 Template Design](#511-template-design)
      - [5.1.2 Error Handling](#512-error-handling)
      - [5.1.3 Modularization](#513-modularization)
      - [5.1.4 Database Connection Pooling](#514-database-connection-pooling)
      - [5.1.5 Global Cursor Management](#515-global-cursor-management)
      - [5.1.6 Form Handling and Validation](#516-form-handling-and-validation)
      - [5.1.7 Dynamic Query Construction](#517-dynamic-query-construction)
      - [5.1.8 Template Rendering with Data](#518-template-rendering-with-data)
      - [5.1.9 Redirection and URL Management](#519-redirection-and-url-management)
      - [5.1.10 Conditional Route Handling](#5110-conditional-route-handling)
    - [5.2 Image Source](#52-image-source)
      - [5.2.1 Home Page Splash image](#521-home-page-splash-image)
      - [5.2.2 New Zealand City List Image](#522-new-zealand-city-list-image)
    - [5.3 Database Questions:](#53-database-questions)
      - [5.3.1 What SQL statement creates the tours table and defines its fields/columns? (Copy and paste only the relevant lines of SQL.](#531-what-sql-statement-creates-the-tours-table-and-defines-its-fieldscolumns-copy-and-paste-only-the-relevant-lines-of-sql)
      - [5.3.2 Which lines of SQL script set up the relationship between the tours and tourgroups tables?](#532-which-lines-of-sql-script-set-up-the-relationship-between-the-tours-and-tourgroups-tables)
      - [5.3.3 The current ATL only works for individual travellers. Write SQL script to create a new table called families, which includes a unique family ID, the family name, an optional short description. The ID must be added automatically by the database. (Relationships to other tables not required.)](#533-the-current-atl-only-works-for-individual-travellers-write-sql-script-to-create-a-new-table-called-families-which-includes-a-unique-family-id-the-family-name-an-optional-short-description-the-id-must-be-added-automatically-by-the-database-relationships-to-other-tables-not-required)
      - [5.3.4 Write an SQL statement that adds a row for a new family to your new families table. Make up some values for a fictional family](#534-write-an-sql-statement-that-adds-a-row-for-a-new-family-to-your-new-families-table-make-up-some-values-for-a-fictional-family)
      - [5.3.5 What changes would you need to make to other tables in the database to fully incorporate the new families table into the data model below? (Describe the changes. SQL script not required.)](#535-what-changes-would-you-need-to-make-to-other-tables-in-the-database-to-fully-incorporate-the-new-families-table-into-the-data-model-below-describe-the-changes-sql-script-not-required)



## 0. Assignment Requirements Translation and Problem-Solving Approach
> This assignment involves developing a Web application for a tourism company named "Aotearoa Tours Ltd (ATL)." The project is divided into two submission phases: Milestone Submission and Final Submission.
## 1. Milestone Submission
### Requirements:
* Create a private GitHub repository named atl and place the provided Web application files (e.g., app.py) in the main directory.
* Host the Web application on PythonAnywhere, ensuring that files are cloned from the GitHub repository and a MySQL database named atl is set up.
* Ensure that the / (home page) and /tours (tours page) routes are running correctly.
* Provide access for the instructor (GitHub and PythonAnywhere).

## 2. Final Submission
### Requirements:
Complete multiple functional modules of the Web application, including:
* Customer list display, customer search, adding/editing customers, and customer booking overview.
  - Adding images and introductory text to the home page.
  - Implementing booking functionality with age restrictions.
  - Using Bootstrap CSS for layout, ensuring a clean and professional interface.
* Write a project report documenting design decisions and database-related questions.
* Submit GitHub repository and PythonAnywhere links.

## 3. Problem-Solving Approach and Steps
### 3.1 Milestone Submission
* **Step 1: Create GitHub Repository**
    - Log in to GitHub and create a private repository named atl.
    - Upload the provided Web application files (e.g., app.py, HTML templates) to the main directory of the repository.
    - Ensure a clear file structure for easy development.
* **Step 2: Configure PythonAnywhere**
  - Register and log in to PythonAnywhere.
  - Clone the GitHub repository to the home directory on PythonAnywhere.
  - Create a MySQL database named atl and import the provided SQL files to initialize the data.
  - Configure the Web application to ensure the / and /tours routes are running correctly.
* **Step 3: Provide Access**
  - Add the instructor's account (lincolnmac or computing@lincoln.ac.nz) as a collaborator to the GitHub repository.
  - Add the instructor as a "teacher" on PythonAnywhere.
* **Step 4: Submit Links**
  - Submit the GitHub repository link and the PythonAnywhere Web application link to the course platform.
### 3.2 Final Submission
* **Step 1: Develop the Web Application**
  - Home Page Design: Add appropriate images and introductory text to the home page, using Bootstrap for layout.
  - Customer List Functionality: Complete the tourlist.html template to display a list of customers for a specific tour group, sorted by surname, with links to customer details.
  - Booking Functionality: Implement the /booking/add route to allow users to book customers for future tours, considering age restrictions.
  - Customer Search Functionality: Create templates and routes to enable searching for customers by name and displaying search results.
  - Add/Edit Customer Functionality: Create templates and routes to allow adding/editing customer information with proper validation.
  - Customer Booking Overview: Create templates and routes to display a summary of customer bookings, including tour names and departure dates.
* **Step 2: Write the Project Report**
  - In the README.md file of the GitHub repository, document design decisions, database questions, and other relevant information using Markdown format.
  - Discuss design decisions, focusing on page structure, template reuse, and data interaction.
  - Answer database-related questions, such as creating tables and setting relationships.
* **Step 3: Testing and Optimization**
  - Test the Web application on both local and PythonAnywhere environments to ensure functionality.
  - Optimize code, ensuring well-formatted and well-documented HTML, SQL, and Python code.
  - Ensure a clean and professional interface, adhering to Bootstrap CSS standards.
* **Step 4: Final Submission**
  - Submit the GitHub repository link and PythonAnywhere link to the course platform.
  - Ensure the GitHub repository includes all code files, images, requirements.txt, and the README.md report.
## 4. Assignment Proposal Summary 
This assignment requires students to develop a fully functional Web application involving customer management, booking systems, and data interaction. The project is divided into two submission phases, and students must complete code development, functional implementation, and project report writing within the specified timeframe. The problem-solving approach includes:
> 1. Completing the configuration and setup for the Milestone Submission phase.
> 2. Focusing on functional module development and user experience optimization in the Final Submission phase.
> 3. Writing a project report to document design decisions and database-related questions.
> 4. Strictly adhering to project constraints, ensuring code standards, clean interfaces, and using only the specified technologies (Python, Flask, Bootstrap, MySQL).

Through this project, students can consolidate their Web development skills while also practicing code organization, functional implementation, and documentation writing.

## 5. Report: Project Assignment 
### 5.1 Design Decisions:
When designing and developing my Flask app, I focused on creating a clean, modular, and maintainable codebase. Here are some of the key design decisions I made:
#### 5.1.1 Template Design
For editing functionality, I chose to use the same template with conditional statements (like Jinja2's {% if %}) to toggle between display and edit modes. This decision was made to reduce code duplication and to simplify the template management. It allows me to have a single template file that can handle both viewing and editing data, making the app more efficient.
**Ex. render customer html with jinja2 if statement:**
```html
{% if flag == 1 %}
<form action="/Orders" method="POST">
  <h3 style="background-color: darkblue; color: white; text-align: center;">Total: {{ counts }} Customers</h3>
  <div class="container mt-5">
    <div class="input-group mb-3">
      <input type="text" class="form-control" id="search-input" placeholder="Search By First Name">
      <div class="input-group-append">
        &nbsp;&nbsp;<button class="btn btn-outline-secondary" type="button" id="search-button"
          style="background-color: blue;"><i class="bi bi-search" style="color: white;"></i></button>
      </div>
    </div>
  </div>
  ...
  {% if flag == 3 %}
<div class="container mt-5">
  <form method="POST" action="/booking/search">
    <div class="mb-3">
      <label for="customerid" class="form-label">Search by Name:</label>
      <select name="customerid" id="customerid" class="form-select">
        {% for customer in customers %}
        <option value="{{ customer.customerid }}">{{ customer.firstname }} {{ customer.familyname }}</option>
        {% endfor %}
      </select>
      <button style="color: white; background-color:darkblue;" type="submit">Search</button>
    </div>
  </form>
</div>
```
#### 5.1.2 Error Handling
I implemented custom error pages and messages to enhance user experience. This includes handling common errors like 404 (page not found) and 500 (server error), providing users with clear and helpful feedback.

```python
# Add python error handler.
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
Add 404.html, display 404 page if url not found.
```html
<body>
    <div class="error-container">
        <div class="error-title">Oops!</div>
        <div class="error-message">404 - PAGE NOT FOUND</div>
        <div class="error-description">
            The page you are looking for might have been removed, had its name changed or is temporarily unavailable.
        </div>
        <a href="/" class="error-button">GO TO HOMEPAGE</a>
    </div>
</body>
```
#### 5.1.3 Modularization
I modularized my Flask app by creating separate modules for different functionalities. This not only makes the codebase more organized but also makes it easier to scale and maintain.
```python
# Ex. Customer modularization: Add/Edit/Update/Search
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
```
#### 5.1.4 Database Connection Pooling
I decided to use a MySQL connection pool (MySQLConnectionPool) to manage database connections. This approach helps in efficiently managing multiple database connections by reusing existing connections instead of creating new ones each time. This not only improves performance but also reduces the overhead associated with establishing connections, making the application more scalable and responsive.

```python
# MySQLConnectionPool is created to manage multiple database connections efficiently.

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="atl", user=connect.dbuser, \
                                                              password=connect.dbpass, host=connect.dbhost, \
                                                              database=connect.dbname, autocommit=True)
```
#### 5.1.5 Global Cursor Management
To manage database cursors efficiently, I implemented a global cursor management system. The getCursor function ensures that a cursor is only created when needed and reused if it already exists. This design decision helps in avoiding the overhead of repeatedly creating and closing cursors, thereby optimizing database operations and improving the overall performance of the application.
```python
"""
The getCursor function manages database connections and cursors globally. 
It ensures that a cursor is created only when needed and reused in subsequent calls, 
avoiding the overhead of repeatedly creating cursors.
"""

def getCursor():
    global dbconn
    global connection
    if connection is None:
        connection = connection_pool.get_connection()
    if dbconn is None:
        dbconn = connection.cursor(dictionary=True)
    return dbconn
```
#### 5.1.6 Form Handling and Validation
For handling form submissions, I used Flask's request.form to retrieve form data. Additionally, I implemented basic validation checks, such as age restriction checks before allowing a booking. This ensures that the data entered by users meets the required criteria before it is processed further, thereby maintaining data integrity and providing a better user experience by preventing invalid submissions.
```python
"""
  In the /makebooking route, form data is retrieved using request.form.get, and age restriction checks are performed. 
  If the user's age does not meet the requirements, an error message is returned; 
  otherwise, the booking is inserted. This demonstrates form handling and validation logic.
"""

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
        age = (startdate - dob).days // 365

        # Check age restriction
        if age < agerestriction:
            return render_template("booking.html", error="Age restriction not met for this tour.")

        # Insert booking
        qstr = "INSERT INTO tourbookings (tourgroupid, customerid) VALUES (%s, %s);"
        cursor.execute(qstr, (tourgroupid, customerid))
        return redirect(url_for('Orders'))
```

#### 5.1.7 Dynamic Query Construction
I opted to construct SQL queries dynamically based on the input parameters. This allows for more flexible and dynamic querying, enabling the application to handle various scenarios without hardcoding queries. For example, in the tours route, the query changes based on whether it is a GET or POST request, allowing the application to list tours or tour groups dynamically.
```python
"""
  In the /tours route, different SQL queries are constructed dynamically based on the request method (GET or POST). 
  GET requests list all tours, while POST requests list tour groups for the selected tour.
"""

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
```

#### 5.1.8 Template Rendering with Data
I used Flask's render_template function to render HTML templates with dynamic data. This approach allows me to pass data from the backend to the frontend seamlessly, making it easier to display data in the templates. For instance, in the tours and tourlist routes, data fetched from the database is passed to the templates, which then render the data accordingly. This ensures that the application remains dynamic and responsive to user interactions.
```python
"""
  In the /tours/list route, data such as tour name, start date, and customer list is fetched 
  from the database and passed to the tourlist.html template for rendering.
"""

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
```

#### 5.1.9 Redirection and URL Management
To manage navigation and redirection within the application, I used Flask's redirect and url_for functions. This design decision helps in maintaining clean and maintainable code by abstracting URL management and ensuring that the application can redirect users to different routes based on their actions. For example, after a successful booking, the user is redirected to the Orders page.
```python

"""
  In the /makebooking route, after successfully inserting a booking record, 
  the user is redirected to the Orders page using redirect(url_for('Orders')). 
  This illustrates the use of Flask's redirect and url_for functions for page redirection.
"""

@app.route("/makebooking", methods=["GET", "POST"])
def makebooking():
    cursor = getCursor()
    if request.method == "POST":
        # ... (omitted code)
        return redirect(url_for('Orders'))
```

#### 5.1.10 Conditional Route Handling
I implemented conditional route handling to manage different HTTP methods (GET and POST) within the same route. This allows the application to handle both data retrieval and form submissions within the same route, reducing the need for multiple routes and making the code more organized and easier to manage. For instance, the tours and makebooking routes handle both GET and POST requests differently based on the user's action.
```python
"""
  In the /customer_edit route, different actions are performed based on the request method (POST or GET). 
  POST requests retrieve user information based on the selected user ID and render the edit page, 
  while GET requests list all users. This shows how to handle different request methods conditionally 
  within the same route.
"""

@app.route("/customer_edit", methods = ['GET', 'POST'])
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
```

### 5.2 Image Source
> For the images used in my app, I sourced them from the following locations:

#### 5.2.1 Home Page Splash image
- **New Zealand Trip Pictures** 

Image Resource URL： https://bing.com/th?id=OSGI.DD831BC29C038D23872376801FB4D731&h=1000&w=1920&c=1&rs=1
  ![alt text](static/images/hqdefault.jpg)

#### 5.2.2 New Zealand City List Image
  - **Milford** 

Image Resource URL： https://www.touropia.com/gfx/b/2016/08/Milford_Sound.jpg
  ![alt text](static/images/Milford.jpg)

  - **Queenstown**

Image Resource URL： https://ts1.cn.mm.bing.net/th/id/R-C.f09caab12ac6619f0893ba8e3f4a3f86?rik=Uk53gavG%2fGXgdg&riu=http%3a%2f%2fimg.youtube.com%2fvi%2fy0PAE8JoT_A%2fmaxresdefault.jpg&ehk=KBAA9BSdnUa1t0hHpbzUSRA50ngr3xgkpQiceb7wY%2f4%3d&risl=&pid=ImgRaw&r=0
  ![alt text](static/images/Queenstown.jpg)
  - **Rotorua**

Image Resource URL: https://cdn.audleytravel.com/-/-/79/431952-cathedral-rock-rotorua.jpg
  ![alt text](static/images/Rotorua.jpg)

### 5.3 Database Questions:
#### 5.3.1 What SQL statement creates the tours table and defines its fields/columns? (Copy and paste only the relevant lines of SQL.
```sql
-- Creating the Tours Table:
CREATE TABLE tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(255) NOT NULL,
    tour_group_id INT,
    FOREIGN KEY (tour_group_id) REFERENCES tourgroups(tour_group_id)
);
```
#### 5.3.2 Which lines of SQL script set up the relationship between the tours and tourgroups tables?
```sql
-- Setting Up the Relationship Between Tours and Tourgroups:

ALTER TABLE tours
ADD COLUMN tour_group_id INT,
ADD FOREIGN KEY (tour_group_id) REFERENCES tourgroups(tour_group_id);
Creating a New Families Table:
```
#### 5.3.3 The current ATL only works for individual travellers. Write SQL script to create a new table called families, which includes a unique family ID, the family name, an optional short description. The ID must be added automatically by the database. (Relationships to other tables not required.)
```sql
-- Creating the Families Table:
CREATE TABLE families (
    family_id INT AUTO_INCREMENT PRIMARY KEY,
    family_name VARCHAR(255) NOT NULL,
    description TEXT
);
```
#### 5.3.4 Write an SQL statement that adds a row for a new family to your new families table. Make up some values for a fictional family
```sql
-- Adding a Row for a New Family:

INSERT INTO families (family_name, description) 
VALUES ('Smith Family', 'A friendly family of four exploring the world.');
```
#### 5.3.5 What changes would you need to make to other tables in the database to fully incorporate the new families table into the data model below? (Describe the changes. SQL script not required.)
> To fully incorporate the new families table into the data model, I would need to make the following changes:
- Add a Foreign Key in the Customers Table: Add a family_id column to the customers table to link individuals to their respective families.
- Update Relationships: Adjust any queries or logic that previously assumed individuals were not part of families. This might involve updating joins or conditions in SQL queries.
- Modify Application Logic: Update the application logic to handle family-related operations, such as listing all family members or aggregating data across a family.
