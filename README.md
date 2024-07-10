# Python-Flash-web-development
This is a web development done using Python flask module for creating a site for posting blogs. First create the project folder and name it say Python-flask-web-development. Inside this folder place the main.py and config.json files. In the config.json file add the email id and password for enabling the email services. You can customise project according to your requirement. Now follow the steps below and create 2 subfolders named templates, static and paste the appropriates files as described below. 

#. All the html files uploaded should be placed in the templates folder . These files are the client side software.

#. The file required for server side software should be placed in the static folder.

  @. Inside the static folder create 3 nos of subfolders and name it as 'assets', 'css', and 'js'.
  
    $. Inside the assets folder create a folder named image and store all the image files that you wish to assign to the html pages through jinja template. 
     The html is used to create the frame work of the web page. For making the html page dynamic, external variables and back end program logic of python can be incorporated into html through the jinja
     template. The jinja template is double curly braces "{{}}". For example to creating a backgroud image in your html file the code is
      <header class="masthead" style="background-image: url(' {{ url_for('static', filename='assets/img/about-bg.jpg') }} ')">.
      
    $. Inside the css folder place all the files will '.css' extension.
    
    $. Inside the js folder place files with '.js' extension.

The function of contact.html file is basically for uploading the user information into a database. The database used is Xamp. You can download this with link "https://www.apachefriends.org/download.html". After installation of Xamp you will be able to view the Xamp control panel. In the control panel start Apache and Mysql applications. Now if you enter "http://localhost/phpmyadmin" in your browser the phpadmin interface will be visible in your browser.

Steps for creating database:
1. Click on "New" to create a database
2. Write your database name.
3. Click create the database.

Steps for creating table:
1. Follow the above upto steps. Then in the resulting window we create table by giving name of table, no:of columns and click 'Go'.

Filling table:
1. The above step will create a empty table. Here addition of columns and changing the name of the table can be done if required.
2. Lets make the database for posts, by endering serial number (sno), title, content, datetime of posts published for column heading.
3. Then select the data type required in each field.
4. Give maximium length for each data set.
5. If datetime is not mentioned then automatically register current datetime by selecting CURRENT_TIME under default.
6. Auto increment (A_I) is given for sno. This field will automatically increment value and avoids duplication.
7. Finally we save.

We can add as many tables as required in the same database name and can be used for different purposes.
Alternately the '.sql' file may be taken from here and can be imported so that the tables with the feild names taken from the database will be created in your phpmyadmin.

