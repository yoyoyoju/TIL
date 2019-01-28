# Servlet
* note from *headfirst servlet&JSP* chapter 4. request and respond

* **servlet**s live to service clients
    * take a client's **request**
    * send back a **response**

* the servlet technology model: what you have to understand in Ch4.
    * for each of the  HTTP methods (GET, POST, HEAD, ...)
        * the purpose of the methods
        * the technical characteristics of the method protocol
        * what triggers the methods
        * the corresponding HttpServlet
    * HttpServletRequest interface
        * retrieve HTML form parameters from the request
        * retrieve HTTP request header infromation
        * retrieve cookies from the request
    * HttpServletReponse interface
        * set an HTTP response header
        * set the content type of the response
        * acquire a text stream for the response
        * acquire a binary stream for the response
        * redirect an HTTP request to another URL
        * add cookies to the response
    * purpose and event sequence of the servlet lifecycle
        1. servlet class loading
        2. servlet instantiation
        3. call the init() method
        4. call the service() method
        5. call the destroy() method


#### Servlet's life and container
1. user clicks a link that has a URL to a servlet
2. the container sees that the request is for a servlet,
so the container creates two objects:
    1. HttpServletResponse response
    2. HttpServletRequest request
3. The container does following:
    1. finds the correct servlet based on the URL in the request
    2. creates or allocates a thread for that request
    3. calls the servlet's `service(request, response)` method 
        * passing the request and response obects as arguments
4. the `service` method figures out which servlet method to call
    * based on the HTTP Method (GET,POST,etc.) sent by client
        * if the client sent an HTTP GET request,
        * `service` method calls the servlet's `doGet(request, response)`
            * passing the request and response objects as argument
5. The servlet uses the response object to write out the response to the client.
The response goes back through the container.
6. The `service` method completes,
    * the thread either dies or returns to a container-managed theread pool
    * the request and response object references fall out of scope
The client gets the response

#### servlet's life stages
* load class
* Instantiate servlet(constructor runs)
* init(): called only once in the servlet's life.
    * must complete before container can call service()
* service(): handle client requests, each request runs in a separate thread
* destroy(): to clean up before the servlet is killed 

#### servlet inheritance hierarchy
* **Servlet** interface
    * javax.servlet.Servlet
    * methods:
        * service(ServletRequest, ServletResponse
        * init(ServletConfig)
        * destory()
        * getServletConfig()
        * getServletInfo()
* abstract **GenericServlet** class implements Servlet
    * javax.servlet.GenericServlet
    * implements most of the basic servlet methods
    * methods:
        * service(ServletRequest, ServletResponse)
        * init(ServletConfig)
        * init()
        * destroy()
        * getServletConfig()
        * getServletInfo()
        * geInitParameter(String)
        * getInitPrameterNames()
        * getServletContext()
        * log(String)
        * log(String, Throwable)
* abstract **HttpServlet** class extends GenericServlet
    * javax.servlet.http.HttpServlet
    * implements the service() method to reflect the HTTPness
    * the methods takes an HTTP-specific request and response
    * methods:
        * service(HttpServletRequest, HttpServletResponse)
        * service(ServletRequest, ServletResponse)
        * doGet(HttpServletRequest, HttpServletResponse)
        * doPost(HttpServletRequest, HttpServletResponse)
        * doHead(HttpServletRequest, HttpServletResponse)
        * doOptions(HttpServletRequest, HttpServletResponse)
        * doPut(HttpServletRequest, HttpServletResponse)
        * doTrace(HttpServletRequest, HttpServletResponse)
        * doDelete(HttpServletRequest, HttpServletResponse)
        * getLastModified(HttpServletRequest)
* MyServlet class extends HttpServlet
    * com.example.foo (my own package)
    * customized servlet class that I write
    * most of the methods are handled by superclass methods
    * override the HTTP methods I need, 
        * such as doPost(HttpServletReqeust, HttpServletResponse)
