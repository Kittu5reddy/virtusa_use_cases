# FinSafe Transaction Validator

## Overview

FinSafe is a console-based Java wallet application that validates every withdrawal request against the current account balance and keeps a short history of recent successful transactions.

The project demonstrates:

- Encapsulation with private account fields
- A custom checked exception for insufficient funds
- Validation for negative amounts and overdrafts
- A mini statement that stores the last 5 successful transaction amounts
- Basic auditing through console output

## Features

- Deposit money into an account
- Withdraw money with balance validation
- Reject negative transaction amounts
- Throw `InSufficientFundsException` when withdrawal exceeds the balance
- View the last 5 successful transactions
- Handle invalid console input without crashing

## Project Structure

- `Main.java` - console menu and user interaction
- `model/Account.java` - account data model
- `service/TransactionProcessor.java` - deposit, withdrawal, history, and audit logic
- `exception/InSufficientFundsException.java` - custom exception for insufficient balance

## Requirements Covered

1. Encapsulation
   - `Account` uses private fields for `accountHolder` and `balance`.

2. Custom Exception
   - `InSufficientFundsException` is thrown when a withdrawal is greater than the current balance.

3. Validation Logic
   - `processTransaction(double amount)` throws `IllegalArgumentException` for negative amounts.
   - It throws `InSufficientFundsException` when the amount is greater than the balance.

4. Transaction History
   - The last 5 successful transaction amounts are stored in an `ArrayList`.
   - `printMiniStatement()` prints the recent transaction history.

## How To Run

From the project root, compile the sources:

```bash
javac Main.java exception\InSufficientFundsException.java model\Account.java service\TransactionProcessor.java
```

Then run the application:

```bash
java Main
```

## Example Usage

1. Enter the account holder name.
2. Choose an action from the menu.
3. Deposit or withdraw an amount.
4. View the mini statement to see the last 5 successful transactions.

## Notes

- The application keeps transaction history and audit entries in memory only.
- Audit information is shown through console output and is not persisted to a file or database.
