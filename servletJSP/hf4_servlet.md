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

#### big lifecycle moments
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
            * constructor has no argument
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

##### Request interface
* **ServletRequest** interface
    * javax.servlet.ServletRequest
    * methods:
        * getAttribute(String): Object
        * getContentLength(): int
        * getInputStream(): ServletInputStream
            * an input stream from the request
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
            * the cookies associated with this request
        * getIntHeader(String): int
        * getHeader(String): String
            * the client's platform and browser info
        * getQueryString(): String
        * getSession(): HttpSession
            * the session associated with this client
        * getMehod(): String
            * the HTTP method of the request
        * // MANY more methods

##### Response interface
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


### Request

#### the HTTP Method
* HTTP 1.1 Methods and the correspondings
    * GET - doGet()
        * to get the thing(resource/file) at the requested URL
        * HTTP 1.1 spec declares GET idempotent
    * POST - doPost()
        * askes the server to accept the body info attached to the reqeust
        * and give it to the thing at the requested URL
    * HEAD - doHead()
        * askes for only the header part of whatever a GET would return
        * HTTP 1.1 spec declares HEAD idempotent
    * TRACE - doTrace()
        * askes for a loopback of the request message
        * so that the client can see what's being received on the other end
        * for testing or troubleshooting
    * OPTIONS - doOptions()
        * akses for a list of the HTTP methods to which the thing at the requested URL can respond
    * PUT - doPut()
        * says to put the enclosed info at the requested URL
        * HTTP 1.1 spec declares PUT idempotent
    * DELETE - doDelete()
        * says to delete the thing(resource/file) at the requested URL
    * CONNECT - no mechanism to handle this in servlet API
        * says to connect for the purposes of tunneling

* GET and POST
    * POST has a body
    * GET requests can be bookmarked; POST requests cannot
    * GET: the parameter shows up after URL
    * GET: only the request header info (no body to care about)
    * GET: for getting things (do not make any changes on the server)
    * POST: send data to be processed (to change somthing on the server)
    * GET: idempotent; POST: not idempotent
        * you can do the same thing over and over again, with no unwanted side effects

#### more about methods
* when I want to support both GET and POST from a single servlet
    * put logic in doGet() then have the doPost() delegate to the doGet() method if neccessary
    ```java
    public void doPost(...) throws ... {
        doGet(request, response);
    }
    ```
* InputStream
    * when the body is large
    * when the body holds textual or binary content to be processed
    * -> use getReader or getInputStream methods
    * these streams will only contain the body of the HTTP request (not the headers)
* getHeader and getIntHeader
    * getIntHeader: when we know the header value is an int (no step to parse)
    ```java
    String forwards = request.getHeader("Max-Forwards");
    int forwardsNum = Integer.parseInt(forwards);
    // can be done as
    int forwardsNum = request.getIntHeader("Max-Forwards");
    ```
* getServerPort(), getLocalPort(), getRemotePort()
    * getRemotePorst(): get the client's port (remote means client from servlet)
    * getServerPort(): to which port was the request originally sent?
        * the requests are sent to a single port (where the server is listening)
    * getLocalPort(): on which port did the request endup?
        * the server turns around and finds a different local port for each thread 
        * so that the app can handle multiple clients at the same time

#### GET or POST
* what determines whether the browser sends a GET or POST request?
* GET
    * a simple hyperlink always means a GET
    `<A HREF="httpL//www.example.com/index.html/">click here</A>`
    * default form is GET
    `<form action="SelectBeer.do">` when the mothod is not specified: GET request
* POST
    * form, wich method attribut is POST
    ```html
    <form method="POST" action="SelectBeer.do">
        <select name="color" size="1">
            <option>light
            <!--more options-->
        </select>
        <center>
            <input type="SUBMIT">
        </center>
    </form>
    ```
    

#### sending and using form examples
* a two parameter
    * HTML form
    ```html
    <form method="POST" action="SelectBeerTaste.do">
        Select beer characteristics<p>
        COLOR:
        <select name="color" size="1">
            <option>light
            <option>amber
            <option>brown
        </select>
        BODY:
        <select name="body" size="1">
            <option>light
            <option>medium
        </select>
        <center>
            <input type="SUBMIT">
        </center>
    </form>
    ```
    * HTTP POST request
        * it has both parameters in the body
    ```HTTP
    POST /advisor/SelectBeerTaste.do HTTP/1.1
    Host: www.example.com
    ...
    color=dark&body=heavy
    ```
    * Servlet class
    ```java
    public void doPost(HttpServletRequest request, HttpServletResponse response)
        throws IOException, ServletException {
        String colorParam = request.getParameter("color");
        String bodyParam = request.getParameter("body");
        // ...
    }
    ```
* multiple values for a single parameter
    * getParameterValues(): returns array
    * some form input types, like a set of checkboxes, can have more than one value
    ```html
    <!--html-->
    <form method=POST action="SelectBeer.do">
        Select beer characteristics<p>
        Can Sizes: <p>
        <input type=checkbox name=sizes value="12oz"> 12 oz.<br>
        <input type=checkbox name=sizes value="16oz"> 16 oz.<br>
        <input type=checkbox name=sizes value="22oz"> 22 oz.<br>
        <br><br>
        <center>
            <input type="SUBMIT">
        </center>
    </form>
    ```
    ```java
    // in servlet, under doPost method
    // use getParameterValues() method
    String one = request.getParameterValues("sizes")[0];
    String[] sizes = request.getParameterValues("sizes");
    // to See everything in the array
    String[] sizes = request.getParameterValuse("sizes");
    for(int x=0; x<sizes.length; x++) {
        // out is a PrintWriter from response
        out.println("<br>sizes: " + sizes[x]);
    }
    ```


### Response
* response: what goes back to the client
* the browser gets, parses, renders for the user
* typically,
    * set content type (setContentType())
    * get output stream (like a Writer) from the response object (getWriter())
    * use the output stream to write the HTML that goes back to the client
        ( doing I/O to write HTML like println())
* but there are other possible cases

#### send a JAR to the client
* instead of sending back an HTML page,
 the response contains the bytes representing the JAR
* need to: 
    * read the bytes fo the JAR file
    * write them to the response's output stream
* example scenario
    * `code.jar` link was clicked
        * the link refers to a servlet named `Code.do`
    * The Browser sends an HTTP request to the server with the name of the requeste servlet(Code.do)
    * The Container sends the request to the `CodeReturn` servlet
        * the `CodeReturn` servlet is mapped to `Code.do` in the DD
    * The `CodeReturn` servlet 
        * gets the bytes for the JAR
        * gets and output stream from the response
        * wrties out the bytes representing the JAR
    * The HTTP seponse now holds the bytes representing the JAR
    * the JAR starts downloading onto the client's machine
* `CodeReturn` servlet in the above scenario, to download the JAR
    ```java
    // imports code here

    public class CodeReturn extends HttpServlet {
        public void doGet(HttpServletRequest request, HttpServletResponse response)
                throws IOException, ServletException {
            // let the browser recognize that this is a JAR (not HTML)
            response.setContentType("application/jar");
            
            ServletContext ctx = getServletContext();
            // give me an input stream for the resource named bookCode.jar
            InputStream is = ctx.getResourceAsStream("/bookCode.jar");

            int read = 0;
            byte[] bytes = new byte[1024];

            OutputStream os = response.getOutputStream();
            // read the JAR bytes
            // then write the bytes to the output stream
            while ((read = is.read(bytes)) != -1) {
                os.write(bytes, 0, read);
            }
            os.flush();
            os.close();
        }
    }
    ```
* the JAR file location
    * `/`, represents the root of the web app
    * for example, if the web app's name is JarDownload, it is `JarDownload/bookCode.jar`
* content type: MIME type
    * `response.setContentType("application/jar");`
    * tell the browser what I am sending back, so the browser can do the right thing
    * it should be set BEFORE  the metods for the output stream (such as getWriter() or getOutputStream())
    * Common MIME type
        * text/html
        * application/pdf
        * video/quichtime
        * application/java
        * image/jpeg
        * application/jar
        * application/octet-stream
        * application/x-zip


#### two choices for output
* ServletResponse interface gives only two streams to choose from:
    * character data: PrintWriter
    * bytes: ServletOutputStream
* PrintWriter
    * it wraps the ServletOutPUtStream 
        * (it has a reference to the ServletOutputStream and delegates calls to it)
    * it adds higher-level character-friendly methods
    * use it for:
        * printing text data to a character stream
    * example
    ```java
    PrintWriter writer = response.getWriter();
    writer.println("some text and HTML");
    ```
* OutputStream
    * use it for:
        * writing anything else 
    * example
    ```java
    ServletOutputStream out = response.getOutputStream();
    out.write(aByteArray);
    ```

#### setHeader addHeader
* `response.addHeader("foo", "bar");`
    * if "foo" is not already in the response header:
        * add a new header "foo" and the value "bar"
    * if "foo" is already exist in the header
        * add "bar" as an additional value
* `response.setHeader("foo", "bar");`
    * if "foo" is not already in the response header:
        * add a new header "foo" and the value "bar"
    * if "foo" is already exist in the header
        * replace existing value with "bar"
* `response.setIntHeader("foo", 42);` for header with int value
    * if "foo" is not already in the response header:
        * add a new header "foo" and the value "bar"
    * if "foo" is already exist in the header
        * replace existing value with 42


#### Redirect
* redirect the request to a completely different URL
    * the servlet calls sendRedirect(aString) on the response
        `response.sendRedirect("http://www.google.com");`: redirect to google
        * sendRedirect takes a String, which is an URL
        * NOT URL object
    * the HTTP response has a status code "301" and a "Location" header with URL as its value
    * the brwser 
        * gets the 301 status code 
        * looks for the "Location" header 
        * makes a new request using the value of "Location" header URL
    * the user sees the new URL in the browser
* using relative URLs in sendRedirect()
    * starting with forward slash (`/`) : relative from root
    * starting without forward slash: relative from the original URL
    * example:
        * original request URL: `http://www.example.com/myApp/cool/bar.do`
        * `sendRedirect("foo/stuff.html");` : starts without `/`
            * `http://www.example.com/myApp/cool/foo/stuff.html`
        * `sendRedirect("/foo/stuff.html");` : starts with `/` (root)
            * `http://www.example.com/foo/stuff.html`
* throws IllegalStateException if you try to invoke it after the response has already been committed
    * 'committed': response has been sent, the data has been flushed to the stream
    * cannot write to the response and then call sendRedirect()


#### request dispatch
* the server do the work (not on the client side)
* example scenario
    * the servlet decides that the request should go to another part of the web app (like JSP)
    * the servlet calls
    ```java
    requestDispatcher view = request.getRequestDispatcher("result.jsp");
    view.forward(request, response);
    ```
    * the JSP takes over the response
    * the browser gets the response tin the usual way and renders it
    * the URL in the browser bar doesn't change
