package com.example.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class OutstreamEx extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        // set the content type for an image
        response.setContentType("image/jpeg");

        // use outputstream 
        ServletOutputStream out = response.getOutputStream();

        ServletContext ctx = getServletContext();
        //get input stream for the resource 
        InputStream is = ctx.getResourceAsStream("/example_picture.jpg");
        // the file is in the root (/ means the root)

        int read = 0;
        byte[] bytes = new byte[1024];

        // read the image bytes
        // write the bytes to the output stream
        OutputStream os = response.getOutputStream();
        while((read = is.read(bytes)) != -1) {
            os.write(bytes, 0, read);
        }
        os.flush();
        os.close();
    }
}
