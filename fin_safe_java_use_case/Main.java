import model.Account;
import service.TransactionProcessor;
import exception.InSufficientFundsException;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Account Holder Name: ");
        String name = sc.nextLine();

        Account account = new Account(name, 0);
        TransactionProcessor processor = new TransactionProcessor(account);

        while (true) {
            System.out.println("\n1. Deposit\n2. Withdraw\n3. View History\n4. View Audit Log\n5. Exit");
            System.out.print("Choose option: ");

            if (!sc.hasNextInt()) {
                System.out.println("Error: Please enter a valid number.");
                sc.nextLine();
                continue;
            }

            int choice = sc.nextInt();

            try {
                switch (choice) {

                    case 1:
                        System.out.print("Enter deposit amount: ");
                        if (!sc.hasNextDouble()) {
                            System.out.println("Error: Please enter a valid amount.");
                            sc.nextLine();
                            break;
                        }
                        double dep = sc.nextDouble();
                        processor.deposit(dep);
                        break;

                    case 2:
                        System.out.print("Enter withdrawal amount: ");
                        if (!sc.hasNextDouble()) {
                            System.out.println("Error: Please enter a valid amount.");
                            sc.nextLine();
                            break;
                        }
                        double wd = sc.nextDouble();
                        processor.processTransaction(wd);
                        break;

                    case 3:
                        processor.printMiniStatement();
                        break;

                    case 4:
                        processor.printAuditLog();
                        break;

                    case 5:
                        System.out.println("Exiting...");
                        sc.close();
                        return;

                    default:
                        System.out.println("Invalid choice");
                }

            } catch (InSufficientFundsException | IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
}