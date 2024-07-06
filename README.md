# Python-Flash-web-development
This is a web development done using Python flask module for creating a site for posting blogs.
#All the html files should be placed in a folder created and named as templates. These are the client side software. 
#The server side software should to placed in a folder created and named as static. 
  @Inside the static folder create 3 nos of subfolders and name it as 'assets', 'css', and 'js'. 
    $Inside the assets folder create a folder named image and store all the image file you vish to assign it to the html pages through jinja template. 
     The html inherently is passive and is hardcoded. Inorder to take variables and to run logic statements from the python program we will require the jinja               template. The jinja template is double curly braces "{{}}". For example to creating a backgroud image in your html file the code is                        
      <header class="masthead" style="background-image: url(' {{ url_for('static', filename='assets/img/about-bg.jpg') }} ')">.
    $Inside the css folder place all the files will '.css' extension.
    $Inside the js folder place files with '.js' extension.
