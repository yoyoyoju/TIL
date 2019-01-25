# Ch3 Mini MVC Tutorial
From HeadFirst Servlet&JSP Ch3: 

The development environment is to say:
    `~/MyProjects/beerV1/`

The deployment environment is to say:
    `~/tomcat/webapps/Beer-v1/`

#### 4a. deploy and test a simple html page
* html file
    1. create the opening page html in the development environment
        under ~/MyProjects/beerV1/web/
    2. copy the file into
        ~/tomcat/webapps/Beer-v1/WEB-INF/

* deployment descripter ([DD](web.xml))
    (maps between servletName - servletClass - url-pattern)
    3. create DD under /beerV1/etc/
    4. copy the file into tomcat/webapps/Beer-v1/WEB-INF

* to test
    5. Start Tomcat
    6. test the page (http://localhost:8080/Beer-v1/form.html)


* form.html file
    * has a form with action 
    * when the form is submitted, request URL is generated based on this information
    * from DD file the container looks up servlet by this URL-pattern
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


#### 4b. introduce a servlet as a controller

##### simplified flow how the servlet work
* as the form is submitted the browser generates the request URL:
    * `/Beer-v1/SelectBeer.do` 
    * the form action attribute "SelectBeer.do" is relative to the URL the page it's on
* the container looks up DD for matching servlet-class using both <servlet> and <servlet-name> tags
* the container starts a new thread to handle the request
    and passes the request to the thread
* the container sends the response back to the client

##### how to
* make a servlet code to acept the posted information
    * write a class extends HttpServlet
    * uses HttpServletRequest interface to 
        * getParameter("color"); (from the `<select name attribute>`)
    * uses HttpServletResponse interface to
        * setContentType("text/html");
        * getWriter();
```java
public class BeerSelect extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) 
        throws IOException, ServletException {

        /** 
         * to write into html file to send 
         * as the response back to the client
         **/
        
        // get the posted information from the request
        String c = request.getParameter("color");

        // make html as a response (using String c)
        response.setContentType("test/html");
        PrintWriter out = response.getWriter();
        out.println("Beer Selection Advice<br>");
        out.println("<br>Got beer color " + c);
    }
}
```
* compile with
    `javac -classpath /Users/tomcat/apache-tomcat-9.0.14/lib/servlet-api.jar:classes:. -d classes src/com/example/web/BeerSelect.java`
    * the path to the servlet-api.jar should be adjusted
    * run the commend in ~/MyProjects/beerV1
* deploy the servlet
    * make a copy of the class files into
    * /Beer-v1/WEB-INF/classes/com/example/web/
* restart tomcat
* go to `http://localhost:8080/Beer-v1/form.html`


#### 4c. 4d. Use model class
* in MVC(model view controller) design pattern,
  the model tends to be the 'back-end' of the application
* it should be in its own utility packages (not tied down to a single web app)
* create the java to deal with model
* edit servlet to use the model
    * simply add
```java
import com.example.model.*;
//...
// in the doPost method of the servlet add
BeerExpert be = new BeerExpert();
List result = be.getBrands(c);
// print the result with out
```

##### the specs for the model in our example:
* the package should be com.example.model
* directory structure whould be `/WEB-INF/classes/com/example/model`
* exposes one method `public List<String> getBrands(String color)`

##### the basic flow:
* build the test class for the model
* build and test the model
    * `javac -d classes src/com/example/model/BeerExpert.java`
* edit the servlet to use the BeerExpert
* recompile and deploy the class into tomcat


#### 4e. Use JSP view
* we want to use JSP to generate a page for the container 
 using the model
* request dispatching:
    * a mechanism to allow one container-managed component to call another
    * in this case our servlet calls the JSP to produce html
* there are three big parts: 
    * Model: BeerExpert class 
    * View: result.jsp 
    * Controller: BeerSelect extends HttpServlet

##### each part in our example
* *Model*: BeerExpert class has a method to be called and returns a List
```java
public class BeerExpert {
    public List<String> getBrands(String color) {
        List<String> brands = new ArrayList<>();
        //...
        return brands;
    }
}
```
* *Controller*: servlet has a method doPost(request, response), 
 which is called as the form.html page "POST"ed a form
* what the doPost does:
    * get parameter from the form using request.getParameter("color")
    * instantiate the BeerExpert and call the getBrands method
    * add the returned List to the request object 
    * dispatch the request to the JSP 
        * it means the servlet BeerSelect "calls" the JSP to produce output
```java
public class BeerSelect extends HttpServlet {
    public void doPost(HttpServletRequest request,
                    HttpServletResponse response)
            throws IOException, ServletException {
        // get the parameter from the form
        String c = request.getParameter("color")
        // create an instance of BeerExpert class
        BeerExpert be = new BeerExpert();
        // get the result from be
        List<String> result = be.getBrands(c);

        /**
         * JSP produces the output
         * below is added instead of writing into html directly using PrintWriter
        **/

        // add an attribute to the request object for the JSP to use
        // in JSP the result will be passed by
        // request.getAttribute("styles");
        request.serAttribute("styles", result); 

        //instantiate a request dispatcher for the JSP
        RequestDispatcher view = 
            request.getRequestDispatcher("result.jsp");
        
        // use the request dispatcher to ask the container
        // to crank up the JSP, sending it to the request and response
        view.forward(request, response);
    }
}
```
* *View*: JSP to produce html
    * in the development env: under /web/
    * in the deployment env: under /Beer-v1/
```JSP
<!--result.jsp file-->
<!--page directive-->
<%@ page import="java.util.*" %>
<html><body>
<%
  /**
   * scriptlet code: standard Java sitting inside <% tags 
  **/

  // get an attribute from the request object
  List<String> styles = (List) request.getAttribute("styles");
  Iterator it = styles.iterator();
  while (it.hasNext()) {
    out.print("<br>try: " + it.next());
  }
%>
</body></html>
```

----
HeadFirst Servlet & JSP
