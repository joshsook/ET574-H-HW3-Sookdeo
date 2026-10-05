import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Students {

    public static void main(String[] args) {

        // Create a HashMap to store the students.
        // The student's name is the key.
        // The value is another HashMap containing major and GPA.
        HashMap<String, HashMap<String, String>> students = new HashMap<>();

        try {
            // Open the CSV file.
            File file = new File("students.csv");
            Scanner input = new Scanner(file);

            // Skip the first line because it contains column names.
            input.nextLine();

            // Read each student from the CSV file.
            while (input.hasNextLine()) {

                String line = input.nextLine();

                // Split the line into three pieces:
                // Name, Major, GPA
                String[] parts = line.split(",");

                String name = parts[0];
                String major = parts[1];
                String gpa = parts[2];

                // Create a HashMap for this student's information.
                HashMap<String, String> studentInfo = new HashMap<>();

                studentInfo.put("major", major);
                studentInfo.put("gpa", gpa);

                // Add the student to the main HashMap.
                students.put(name, studentInfo);
            }

            input.close();

        } catch (FileNotFoundException e) {
            System.out.println("Could not find students.csv.");
            return;
        }

        // Calculate the total GPA.
        double totalGPA = 0.0;

        for (String name : students.keySet()) {
            double gpa = Double.parseDouble(students.get(name).get("gpa"));
            totalGPA = totalGPA + gpa;
        }

        // Calculate the average GPA.
        double averageGPA = totalGPA / students.size();

        // Display all students.
        System.out.println("Student Information");
        System.out.println("-------------------");

        for (String name : students.keySet()) {

            String major = students.get(name).get("major");
            double gpa = Double.parseDouble(students.get(name).get("gpa"));

            System.out.println(
                name + " - " + major + " - GPA: " + gpa
            );
        }

        // Display the average GPA.
        System.out.println();
        System.out.printf("Average GPA: %.2f%n", averageGPA);

        // Display students above the average.
        System.out.println();
        System.out.println("Students Above Average");
        System.out.println("----------------------");

        for (String name : students.keySet()) {

            double gpa = Double.parseDouble(students.get(name).get("gpa"));

            if (gpa > averageGPA) {
                System.out.println(name + " - " + gpa);
            }
        }

        // Predict scholarship winners.
        //
        // Based on the examples:
        //
        // Biology:
        // 2.75 or higher = scholarship
        //
        // Math:
        // 3.57 or higher = scholarship
        //
        // Computer Science:
        // 3.50 or higher = scholarship
        //
        // The Computer Science rule is an assumption because
        // the original examples do not give a Computer Science
        // scholarship example.

        System.out.println();
        System.out.println("Predicted Scholarship Winners");
        System.out.println("-----------------------------");

        for (String name : students.keySet()) {

            String major = students.get(name).get("major");
            double gpa = Double.parseDouble(students.get(name).get("gpa"));

            boolean scholarship = false;

            if (major.equals("Biology") && gpa >= 2.75) {
                scholarship = true;
            }

            if (major.equals("Math") && gpa >= 3.57) {
                scholarship = true;
            }

            if (major.equals("Computer Science") && gpa >= 3.50) {
                scholarship = true;
            }

            if (scholarship) {
                System.out.println(
                    name + " - " + major + " - " + gpa
                    + " - Scholarship: YES"
                );
            } else {
                System.out.println(
                    name + " - " + major + " - " + gpa
                    + " - Scholarship: NO"
                );
            }
        }
    }
}
