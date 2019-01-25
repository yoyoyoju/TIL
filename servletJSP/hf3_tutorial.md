# Ch3 Mini MVC Tutorial
As the very first step:
deplay and test the opening page

The development environment is to say
    ~/MyProjects/beerV1/
The deployment environment is to say 
    ~/tomcat/webapps/Beer-v1/

* html file
1. create the opening page html in the development environment
    under ~/MyProjects/beerV1/web/
2. copy the file into
    ~/tomcat/webapps/Beer-v1/WEB-INF/

* deployment descripter ([DD](web.xml))
    (maps between servletName - servletClass - url-pattern)
3. create DD under /beerV1/etc/
4. copy the file into tomcat/webapps/Beer-v1/WEB-INF

5. Start Tomcat
6. test the page (http://localhost:8080/Beer-v1/form.html)


* html
In this example, the form.html file has a form with action
```html
<!--in some where in the body of html-->
<form method="POST"
    action="SelectBeer.do"> <!--html thinks the servlet is called-->
    <!--...-->
    <select name="color" size="1">
        <option value="light"> light </option>
        <!--more options-->
    </select>
    <input type="SUBMIT">
</form>
```

#### from the request to the Servlet 
    * as the form is submitted the browser generates the request URL:
        * `/Beer-v1/SelectBeer.do` 
        * the form action attribute "SelectBeer.do" is relative to the URL the page it's on
    * the container looks up DD for matching servlet-class using both <servlet> and <servlet-name> tags
    * the container starts a new thread to handle the request
        and passes the request to the thread
    * the container sends the response back to the client

#### First Version of the controller servlet:
* make a servlet code to acept the posted information
    * write a class extends HttpServlet
    * uses HttpServletRequest interface to 
        * getParameter("color"); (set the `<select name attribute>`)
    * uses HttpServletResponse interface to
        * setContentType("text/html");
        * getWriter();
* compile with
    `javac -classpath /Users/tomcat/apache-tomcat-9.0.14/lib/servlet-api.jar:classes:. -d classes src/com/example/web/BeerSelect.java`
    * the path to the servlet-api.jar should be adjusted
    * run the commend in ~/MyProjects/beerV1
* deploy the servlet
    * make a copy of the class files into
    * /Beer-v1/WEB-INF/classes/com/example/web/
* restart tomcat
* go to `http://localhost:8080/Beer-v1/form.html`


#### model class
* in MVC(model view controller) design pattern,
  the model tends to be the 'back-end' of the application
* it should be in its own utility packages (not tied down to a single web app)


* the specs for the model in our example:
    * the package should be com.example.model
    * directory structure whould be `/WEB-INF/classes/com/example/model`
    * exposes one method `public List<String> getBrands(String color)`
* build the test class for the model
* build and test the model
    * `javac -d classes src/com/example/model/BeerExpert.java`
* edit the servlet to use the BeerExpert
* deploy the class into tomcat


----
HeadFirst Servlet & JSP
