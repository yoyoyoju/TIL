package com.example.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class RedirectExample extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws IOException, ServletException {

        String whereTo = request.getParameter("where");
        if (whereTo.equals("Google")) {
            response.sendRedirect("http://www.google.com");
        } else if (whereTo.equals("Dog")) {
            // relative from the original request
            // /Example-v1/redirect.html
            response.sendRedirect("OutstreamEx.do");
        } else {
            // relative from the root of the container
            response.sendRedirect("/Example-v1/index.html");
        }

    }
}

