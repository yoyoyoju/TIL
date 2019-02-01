package com.example.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.*;
import com.example.model.BeerExpert;

// HttpServlet extends GenericServlet
// GenericServlet implements the Servlet interface
public class BeerSelect extends HttpServlet {
    // doPost to handle the HTTP request
    public void doPost(HttpServletRequest request,
            HttpServletResponse response)
            throws IOException, ServletException {
        // setContentType method from ServletResponse interface
        response.setContentType("text/html"); 
        PrintWriter out = response.getWriter();
        out.println("Beer Selection Advice<br>");
        // getParameter method from ServletRequest interface
        // the value "color" matches to the name attribute in <select> tag
        String c = request.getParameter("color");
        BeerExpert beerExpert = new BeerExpert();
        List<String> result = beerExpert.getBrands(c);

        request.setAttribute("styles", result);
        RequestDispatcher view = 
            request.getRequestDispatcher("result.jsp");
        view.forward(request, response);
    }
}

    
