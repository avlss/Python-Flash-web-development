# Python-Flash-web-development
This is a web development done using Python flask module for creating a site for posting blogs. First create the project folder and name it say Python-flask-web-development. Inside this folder place the main.py and config.json files. Now follow the steps below and create 2 subfolders named templates, static and paste the appropriates files as described below. 

#All the html files uploaded should be placed in the templates folder . These files are the client side software.

#The file required for server side software should be placed in the static folder.

  @Inside the static folder create 3 nos of subfolders and name it as 'assets', 'css', and 'js'.
  
    $Inside the assets folder create a folder named image and store all the image files that you wish to assign to the html pages through jinja template. 
     The html is used to create the frame work of the web page. For making the html page dynamic, external variables and back end program logic of python can be incorporated into html through the jinja
     template. The jinja template is double curly braces "{{}}". For example to creating a backgroud image in your html file the code is
      <header class="masthead" style="background-image: url(' {{ url_for('static', filename='assets/img/about-bg.jpg') }} ')">.
      
    $Inside the css folder place all the files will '.css' extension.
    
    $Inside the js folder place files with '.js' extension.
