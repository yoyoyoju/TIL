# try with resources statement
* try statement that declares one or more resources
    * resource: 
        * object that must be closed after the program is finished with it
        * any object that implements `java.lang.AutoCloseable` can be used as a resource
            * interface `java.io.Closeable` extends the AutoCloseable interface
    * example
        ```java
        static String readFirstLineFromFile(String path) throws IOException {
            try (BufferedReader br = new BufferedReader(new FileReader(path))) {
                return br.readLine();
            }
        }
        ```
        ```java
        public static void writeToFileZipFileContents(String zipFileName, String outputFileName)
                throws java.io.IOException {
            java.nio.charset.Charset charset = java.nio.charset.StandardCharsets.US_ASCII;
            java.nio.file.Path outputFilePath = java.nio.file.Paths.get(outputFileName);

            try (
                java.util.zip.ZipFile zf =
                    new java.util.zip.ZipFile(zipFileName);
                java.io.BufferedWriter writer =
                    java.nio.file.Files.newBufferedWriter(outputFilePath, charset)
            ) {
                for (java.util.Enumeration entries =
                        zf.entries(); entries.hasMoreElements();) {
                    String newLine = System.getProperty("line.separator");
                    String zipEntryName =
                        ((java.util.zip.ZipEntry)entries.nextElement()).getName() +
                        newLine;
                    writer.write(zipEntryName, 0, zipEntryName.length());
                }
            }
        }
        ```
        ```java
        public static void viewTable(Connection con) throws SQLException {
            String query = "select COF_NAME, SUP_ID, PRICE, SALES, TOTAL from COFFEES";

            try (Statement stmt = con.createStatement()) {
                ResultSet rs = stmt.executeQuery(query);

                while (rs.next()) {
                    String coffeeName = rs.getString("COF_NAME");
                    int supplierID = rs.getInt("SUP_ID");
                    float price = rs.getFloat("PRICE");
                    int sales = rs.getInt("SALES");
                    int total = rs.getInt("TOTAL");

                    System.out.println(coffeeName + ", " + supplierID + ", " + 
                                        price + ", " + sales + ", " + total);
                }
            } catch (SQLException e) {
                JDBCTutorialUtilities.printSQLException(e);
            }
        } 
        ```


---
reference [link](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html)
