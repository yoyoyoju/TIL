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

* from the request to the Servlet 
    * as the form is submitted the browser generates the request URL:
        * `/Beer-v1/SelectBeer.do` 
        * the form action attribute "SelectBeer.do" is relative to the URL the page it's on
    * the container looks up DD for matching servlet-class using both <servlet> and <servlet-name> tags
    * the container starts a new thread to handle the request
        and passes the request to the thread
    * the container sends the response back to the client

* First Version of the controller servlet:

----
HeadFirst Servlet & JSP
