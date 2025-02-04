# Assignment: Web Application Development for ATL Project

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
- **Template Design:** For editing functionality, I chose to use the same template with conditional statements (like Jinja2's {% if %}) to toggle between display and edit modes. This decision was made to reduce code duplication and to simplify the template management. It allows me to have a single template file that can handle both viewing and editing data, making the app more efficient.
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
- **Error Handling:** I implemented custom error pages and messages to enhance user experience. This includes handling common errors like 404 (page not found) and 500 (server error), providing users with clear and helpful feedback.

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
- **Modularization:** I modularized my Flask app by creating separate modules for different functionalities. This not only makes the codebase more organized but also makes it easier to scale and maintain.

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
### 5.2 Image Source
> For the images used in my app, I sourced them from the following locations:

#### 5.2.1 Home Page Splash image
- **New Zealand Trip Pictures**
  ![alt text](static/images/hqdefault.jpg)
#### 5.2.2 New Zealand City List Image
  - **Milford**
  ![alt text](static/images/Milford.jpg)
  - **Queenstown**
  ![alt text](static/images/Queenstown.jpg)
  - **Rotorua**
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
