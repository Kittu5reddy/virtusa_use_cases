package service;

import model.Account;
import exception.InSufficientFundsException;
import java.util.ArrayList;

public class TransactionProcessor {

    private Account account;
    private ArrayList<Double> transactions;
    private ArrayList<String> auditLog;

    public TransactionProcessor(Account account) {
        this.account = account;
        this.transactions = new ArrayList<>();
        this.auditLog = new ArrayList<>();
    }

    /**
     * Processes withdrawal transaction with validation
     */
    public void processTransaction(double amount) throws InSufficientFundsException {

        if (amount < 0) {
            addAuditEntry("Rejected withdrawal request: negative amount " + amount);
            throw new IllegalArgumentException("Amount cannot be negative");
        }

        if (amount > account.getBalance()) {
            addAuditEntry("Rejected withdrawal request: insufficient funds for amount " + amount);
            throw new InSufficientFundsException("Insufficient funds");
        }

        account.withdraw(amount);

        addTransaction(-amount);
        addAuditEntry("Withdrawal processed: " + amount + ", balance now " + account.getBalance());

        System.out.println("Withdrawal successful. Balance: Rs" + account.getBalance());
    }

    /**
     * Deposit money into account
     */
    public void deposit(double amount) {
        if (amount < 0) {
            addAuditEntry("Rejected deposit request: negative amount " + amount);
            throw new IllegalArgumentException("Amount cannot be negative");
        }

        account.deposit(amount);

        addTransaction(amount);
        addAuditEntry("Deposit processed: " + amount + ", balance now " + account.getBalance());

        System.out.println("Deposit successful. Balance: Rs" + account.getBalance());
    }

    /**
     * Maintain last 5 transactions
     */
    private void addTransaction(double amount) {
        if (transactions.size() == 5) {
            transactions.remove(0);
        }
        transactions.add(amount);
    }

    private void addAuditEntry(String message) {
        auditLog.add(message);
    }

    /**
     * Print last 5 transactions
     */
    public void printMiniStatement() {
        addAuditEntry("Mini statement viewed");
        System.out.println("\n--- Last 5 Transactions ---");

        if (transactions.isEmpty()) {
            System.out.println("No transactions yet.");
            return;
        }

        for (double t : transactions) {
            System.out.println("RS" + t);
        }
    }

    public void printAuditLog() {
        System.out.println("\n--- Audit Log ---");

        if (auditLog.isEmpty()) {
            System.out.println("No audit entries yet.");
            return;
        }

        for (String entry : auditLog) {
            System.out.println(entry);
        }
    }
}