# Chapter5 Being a Web App
* HeadFirst Servlet & JSP, Chapter5 Being a Web App
* how to tie all the components together?
* how do you let components share information?
* how do you hide information?
* how do you make information threadsafe?


#### Objectives

1. initialization parameters:
    * servlet code to access initialization parameters
    * deployment descriptor elements to declare initialization parameters
2. fundamental servlet attribute scopes (request, session, and context)
    * servlet code to add, retrieve, and remove attributes
    * identify the proper scope for an attribute
    * identify multithreading issues associated with each scope
3. Web container request processing model:
    * filter, filter chain, request and response wrappers, and web resource
4. Web container lifecycle event model for requests, sessions, and web applications
    * listener class, scope attribute listener, proper attribute listener
5. requestDispatcher mechanism
    * servlet code to
        * create a request dispatcher
        * forward or include the target resource


### Init Parameters
* initialization parameters
    * deploy-time constants
    * one cannot set them
    * to change it, one should re-deploy the web-app
* for some people, 'init parameter' refers to 'servlet init parameter'
* only String can be the parameter


#### servlet init parameters
* init parameters available only to a single servlet
    * ServletConfig is one per servlet
    * each servlet has its own ServletConfig
* `ServletConfig`
    * configure some parameters (for example e-mail address to show)
        * but do not want to hard-code it inside the servlet class
        * to change the parameter, modify only the Deployment Descriptor (web.xml) (not the servlet code)
        * when the web app is deployed, the parameter is read from the Deployment Descriptor
        * but still should be redeployed
            * there is a hot redeploy, one doesn't have to restart the server
        * if the values will be frequently changed, better to have a servlet method to read from a file or database
    * HOW TO USE IT:
        * in the deployment descriptor (web.xml) file:
            * INSIDE the <servlet> element
            ```xml
            <servlet>
                <servlet-name>BeerParamTests</servlet-name>
                <servlet-class>TestInitParams</servlet-class>

                <init-param>
                    <param-name>adminEmail</param-name>
                    <param-value>example@example.com</param-value>
                </init-param>
            </servlet>
            ```
        * in the servlet code
            * every servlet inherits a getServletConfig() method
            * getServletConfig() returns servletConfig
            * servletConfig has getInitParameter() method
            ```java
            out.println(getServletConfig().getInitParameter("adminEmail"));
            ```
    * NOTES:
        * servletConfig is available only after initialization
            * getServletConfig, cannot called in constructor
            * in `init(ServletConfig)`, the servlet gets its ServletConfig object
            * when container initializes a servlet, the container does followings:
                * reads the Deployment Descriptor for this server
                    * including the servlet init parameters (<init-param>)
                * creates a new ServletConfig instance for this servlet
                * creates a name String and a value String for each servlet init parameter
                    * assume we have only one
                * gives the ServletConfig the references to the name/value init parameters
                * creates a new instance of the servlet class
                * calls the servlet's init method with arguments (`init(ServletConfig)`)
                    * passing the reference to the ServletConfig 
        * the servlet init parameters are read only ONCE
            * when the container initializes the servlet
        * two `init` methods
            * `init(ServletConfig)` is called by container
            * the `init` method calles no-arg `init()` method
            * it is recommended to override `init()`, not `init(ServletConfig)`
            * but when the `init(ServletConfig)` is overriden, better call `super.init(ServletConfig)`
    * `ServletConfig` interface: methods
        * getInitParameter(String)
        * Enumeration getInitParameterNames()
        * getServletContext()
        * getServletName()  (rarely used)
    * Limitations
        * the parameters are only available to the servlet
        * to send the information to some other parts such as JSP,
            * have to use response
            * by `request.setAttribute(String name, Object o);`
    * Example code:
        * in the deployment descriptor
        ```xml
        <?xml version="1.0" encoding="ISO-8859-1" ?>
        <web-app xmlns="http://java.sun.com/xml/ns/javaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
            http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
            version="3.0">
            <servlet>
                <servlet-name>BeerParamTests</servlet-name>
                <servlet-class>com.example.TestInitParams</servlet-class>
                <init-param>
                    <param-name>adminEmail</param-name>
                    <param-value>example@example.org</param-value>
                </init-param>
                <init-param>
                    <param-name>mainEmail</param-name>
                    <param-value>main@example.org</param-value>
                </init-param>
            </servlet>
            <servlet-mapping>
                <servlet-name>BeerParamTests</servlet-name>
                <url-pattern>/Tester.do</url-pattern>
            </servlet-mapping>
        </web-app>
        ```
        * in a servlet class
        ```java
        package com.example;
        import javax.servlet.*;
        import javax.servlet.http.*;
        import java.io.*;

        public class TestInitParams extends HttpServlet {
            public void doGet(HttpServletRequest request, HttpServletResponse response)
                    throws IOException, ServletException {
                response.setContentType("text/html");
                PrintWriter out = response.getWriter();
                out.println("test init parameters<br>");

                java.util.Enumeration e = getServletConfig().getInitParameterNames();
                while(e.hasMoreElements()) {
                    out.println("<br>param name = " + e.nextElement() + "<br>");
                }
                out.println("main email is " + getServletConfig().getInitParameter("mainEmail"));
                out.println("<br>");
                out.println("admin email is " + getServletConfig().getInitParameter("adminEmail"));
            }
        }
        ```


#### context init parameters
* `ServletContext`
    * init parameters available to the entire webapp
        * any servlet and JSP in the app automatically has access to the context init parameters
        * ServletContext is one per web app
            * all the parts of the web app share it
            * if the application is distributed across multiple servers, one ServletContext per JVM
        * it is read only once, when the web-app is ployed
    * HOW TO USE IT:
        * in the deployment descriptor (web.xml) file:
            * OUTSIDE any <servlet> declaration
            * inside the <web-app>
            * use `<context-param>` element
            ```xml
            <web-app ....>
                <servlet>
                    <servlet-name>BeerParamTests</servlet-name>
                    <servlet-class>TestInitParams</servlet-class>
                </servlet>

                <context-param>
                    <param-name>adminEmail</param-name>
                    <param-value>admin@example.org</param-value>
                </context-param>
            </web-app>
            ```
        * in the servlet code:
            * every servlet inherits a getServletContext() method
            * getServletContext() returns a ServletContext object
            * ServletContext objects have getInitParameter(String)
            ```java
            out.println(getServletContext().getInitParameter("adminEmail"));
            ```
    * Web-app initialization: when the web app is deployed, the Container does followings
        * reads the deployment descriptor 
        * creates a name/value String pair for each <context-param>
        * creates a new instance of ServletContext
        * gives the ServletContext a reference to each name/value pair 
            * every servlet and JSP deployed as part of a single web app has access to that same ServletContext
    * `ServletContext` interface (javax.servlet.ServletContext): methods
        * getInitParameter(String)
        * getIniParameterNames()
        * getAttribute(String)  // returns Object: need to cast the return
        * getAttributeNames()
        * setAttribute(String, Object)
        * removeAttribute(String)
        * getMajorVersion()
        * getServerInfo()
        * getRealPath(String)
        * getResourceAsStream(String)
        * getRequestDispatcher(String)
        * log(String) : write server's log file(vendor-specific) or System.out
            * but it's more practical to use other way to log such as,
            * [Log4j](http://logging.apache.org/log4j) or loggin API(java.util.logging)
        * // more methods
    * to get the ServletContext
        * `getServletConfig().getServletContext().getInitParameter()`
            * a servlet's ServletConfig object always holds a reference to the ServletContext
            * if the class is not a servlet and a ServletConfig is passed, one can use this
        * `this.getServletContext().getInitParameter()`
            * `getServletContext()` method comes from GenericServlet
            * class, which inherits GenericServlet (or HttpServlet), can use this method



### Listener
* a class gets notified in the key events of ServletContext (initialization , destruction)
* the class can do:
    * when the context is initialized (the app is being deployed)
        * get the context init parameters from the ServletContext
        * use the init parameter lookup name to make a database connection
        * store the database connection as an attribute, so that all parts of the web app can access it
    * when the context is destroyed (the app is undeployed or goes down)
        * close the database connection
* **ServletContextListener** interface
    * contextInitialized(ServletContextEvent)
    * contextDestoryed(ServletContextEvent)
* how to use
    1. create a listener class (implements ServletContextListener)
        * gets the context init parameters
        * does things with the parameter
        * sets things as context attribute
    2. it can be deployed into `/WEB-INF/classes`
    3. put a `<listener>` element in the web.xml Deployment Descriptor
        * to tell the Container that we have a listener for this app
        ```xml
        <listener>
            <listener-class>
                com.example.MyServletContextListener
            </listener-class>
        </listener>
        ```
* example
    * the Listener
    ```java
    package com.example;

    import javax.servlet.*;

    // my Listener class implements javax.servlet.ServletContextListener
    public class MyServletContextListener implements ServletContextListener {
        public void contextInitialized(ServletContextEvent event) {
            /**
             * code to initialize the database connection
             * and store it as a context attribute
             **/

            // get ServletContext from event
            ServletContext sc = event.getServletContest();

            // get init parameter from the context
            String dogBreed = sc.getInitParameter("breed");

            // make new dog
            Dog d = new Dog(dogBreed);

            // use the context to set an attribute
            // (name/object) pair
            // now other parts of the app will be able to get the value of the attribute
            sc.setAttribute("dog", d);
        }

        public void contextDestroyed(ServletContextEvent event) {
            /**
             * code to close the database connection
             **/

            // the dog does not need to be cleaned up
        }
    }
    ```
    * the servlet to test the listener above
    ```java
    package com.example;

    import javax.servlet.*;
    import javax.servlet.http.*;
    import java.io.*;

    public class ListenerTester extends HttpServlet {
        public void doGet (HttpServletRequest request, HttpServletResponse response)
                throws IOException, ServletException {
            response.setContentType("text/html");
            PrintWriter out = response.getWrite();

            out.println("test context attributes set by listener<br>");
            out.prtinln("<br>");
            // use the dog created by Listener
            // getAttribute returns Object: need to cast the return
            Dog dog = (Dog) getServletContext().getAttribute("dog");
            out.println("Dog's breed is: " + dog.getBreed());
        }
    }
    ```
    * Deployment Descriptor
    ```xml
    <!-- /WEB-INF/web.xml -->
    <web-app ...>
        <servlet>
            <servlet-name>ListenerTester</servlet-name>
            <servlet-class>com.example.ListenerTester</servlet-class>
        </servlet>

        <servlet-mapping>
            <servlet-name>ListenerTester</servlet-name>
            <url-pattern>/ListenTest.do</url-pattern>
        </servlet-mapping>

        <context-param>
            <param-name>breed</param-name>
            <param-value>Great Dane</param-value>
        </context-param>

        <listener>
            <listener-class>
                com.example.MyServletContextListener
            </listener-class>
        </listener>
    </web-app>
    ```
