package com.example.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class MultiChoiceEx extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws IOException, ServletException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Your choices<br>");

        String animal = request.getParameter("animal");
        String color = request.getParameter("color");
        String[] adjectives = request.getParameterValues("adjectives");

        StringBuilder sb = new StringBuilder();

        // without checking null
        // when none of the check box was checked,
        // the code below loop (sb.append(color) and so on)
        // will not excute
        if (adjectives != null) {
            for (int x=0; x<adjectives.length; x++) {
                sb.append(adjectives[x]).append(" ");
            }
        }

        sb.append(color).append(" ");
        sb.append(animal);

        out.println(sb.toString());
    }
}
