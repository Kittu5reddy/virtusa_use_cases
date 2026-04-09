import java.util.Scanner;

public class PasswordValidator {

    // Method to validate password
    public static boolean validatePassword(String password) {
        boolean hasUpperCase = false;
        boolean hasDigit = false;

        // Check length
        if (password.length() < 8) {
            System.out.println(" Password too short (minimum 8 characters required)");
            return false;
        }

        // Loop through characters
        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);

            if (Character.isUpperCase(ch)) {
                hasUpperCase = true;
            }

            if (Character.isDigit(ch)) {
                hasDigit = true;
            }
        }

        // Feedback system
        if (!hasUpperCase) {
            System.out.println(" Missing an uppercase letter");
        }

        if (!hasDigit) {
            System.out.println(" Missing a digit");
        }

        // Final validation
        return hasUpperCase && hasDigit;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String password;

        System.out.println(" Welcome to SafeLog Password Validator");

        // Retry mechanism
        while (true) {
            System.out.print("Enter your password: ");
            password = scanner.nextLine();

            if (validatePassword(password)) {
                System.out.println(" Password is strong and valid!");
                break;
            } else {
                System.out.println(" Please try again.\n");
            }
        }

        scanner.close();
    }
}