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


### Servlet lifecycle

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

#### Three big lifecycle moments
0. find and load the servlet classes
    * When it is done:
        * when the Container starts up
            * for example, when you run Tomcat
    * How it is done:
        * Finding the class: the Container does followings
            * looks for deployed web apps
            * starts searching for servlet class files
        * Loading the class
            * happens either on Container startup or first client use
            * the container loads the servlet class using normal Java class loading facilities
        * instantiating the class:
            * call the constructor to make an object
            * constructor should NOT be overwriten
            * (cannot be used until init() is called, though)
1. init()
    * When it is called:
        * after the servlet instance is created
        * before the servlet can service any client requests
            * it means. before the first call to service() method
        * it is called only once in a servlet's life
    * What it's for:
        * initialize your servlet before handling any client requests
        * it gets unique privileges like
            * the ability to use its ServletContext reference
                * to get information from the container
                * log events, get references to other resources, store attributes
    * Do you override it?
        * possibly
        * if you have initialization code
        * if it is not overriden, the one from GenericServlet runs
    * Parameters:
        * ServletConfig object
            * one ServletConfig object per servlet
            * to pass deploy-time information to the servlet
                * (for example, a database or enterprise bean lookup name)
            * to access the ServletContext
            * configured in the Deployment Descriptor
2. service()
    * When it is called:
        * when the first client request comes in
        * the container starts a new thread or allocates a thread from the pool
        * and causes the servlet's service method to be invoked
    * What it's for:
        * this method looks at the request
        * determines the HTTP method (GET, POST, etc)
        * invokes the matching method (doGET(), doPOST(), etc) on the servlet
    * Do you override it?
        * No. very unlikely
        * let the service() method from the HttpServlet run
    * Parameters:
        * HttpServletRequest object, HttpServletResponse object
3. doGet() and/or doPost() (etc.)
    * When it is called:
        * the service() method invokes doGet() or doPost() based on the HTTP method from the request
    * What it's for:
        * this is where your code begins!
        * I can write what my web app should do when certain HTTP method is called
        * can call other methods on other objects, if needed
    * Do you override it?
        * ALWAYS at least ONE of them
        * if not overriden, then you are telling the container that this servlet does not support that request
    * Parameters:
        * HttpServletRequest object, HttpServleteResponse object


#### each request runs in a separate thread
* basically (except SingleThreadModel), one instance per servlet
* a pair of a response and a request objects per a request
* one thread per a request
* and per each thread, service() method is called
* so a instance of servlet can have multiple threads


#### ServletConfig and ServletContext
* ServletConfig
    * one ServletConfig object per servlet
    * to pass deploy-time information to the servlet
    * use it to access the ServletContext
    * parameters are configured in the Deployment Descriptor
    * the parameters won't change for as long as this servlet is deployed and running
    * to change the parameters, you'll have to redeploy the servlet
* ServletContext
    * one ServletContext per web app
    * should be named as AppContext
    * Use it to access web app parameters
    * configured in the Deployment Descriptor
    * use it as a kind of application bulletin-board
        * can put up message (called attributes)
        * other parts of the application can access
    * use it to get server info, including the name and version of the Container, etc.


### Request and Response
* request and response are the arguments to service(), doGet(), doPost(), etc.

#### the inheritance hierarchy

##### Request
* **ServletRequest** interface
    * javax.servlet.ServletRequest
    * methods:
        * getAttribute(String): Object
        * getContentLength(): int
        * getInputStream(): ServletInputStream
        * getLocalPort(): int
        * getParameter(String): String
        * getParameterNames(): Enumeration
        * //Many more methods
* **HttpServletRequest** interface extends ServletRequest
    * javax.servlet.http.HttpServletRequest
    * about HTTP things like cookies, headers and sessions
    * add methods relate to the HTTP protocol
    * methods:
        * getContextPath(): String
        * getCookies(): Cookie[]
        * getHeader(String): String
        * getQueryString(): String
        * getSession(): HttpSession
        * getMehod(): String
        * // MANY more methods

##### Response
* **ServletResponse** interface
    * javax.servlet.ServletResponse
    * methods:
        * getBufferSize(): int
        * setContentType(String): void
        * setContentLength(int): void
        * getOutputStream(): ServletOutputStream
        * getWriter(): PrintWriter
        * // MANY more methods
* **HttpServletResponse** interface extends ServletResponse
    * javax.servlet.http.HttpServletResponse
    * adds methods about HTTP, such as errors, cookies and headers
    * methods:
        * addCookie(Cookie): void
        * addHeader(String name, String value): void
        * encodeRedirectURL(STring url): String
        * sendError(int): void
        * setStatus(int): void
        * // MANY more methods


#### the HTTP Method
* HTTP 1.1 Methods and the correspondings
    * GET - doGet()
        * to get the thing(resource/file) at the requested URL
    * POST - doPost()
        * askes the server to accept the body info attached to the reqeust
        * and give it to the thing at the requested URL
    * HEAD - doHead()
        * askes for only the header part of whatever a GET would return
    * TRACE - doTrace()
        * askes for a loopback of the request message
        * so that the client can see what's being received on the other end
        * for testing or troubleshooting
    * OPTIONS - doOptions()
        * akses for a list of the HTTP methods to which the thing at the requested URL can respond
    * PUT - doPut()
        * says to put the enclosed info at the requested URL
    * DELETE - doDelete()
        * says to delete the thing(resource/file) at the requested URL
    * CONNECT - no mechanism to handle this in servlet API
        * says to connect for the purposes of tunneling

* GET and POST
    * POST has a body
    * GET requests can be bookmarked; POST requests cannot
    * GET: the parameter shouws up after URL
    * GET: for getting things (do not make any changes on the server)
    * POST: send data to be processed (to change somthing on the server)
