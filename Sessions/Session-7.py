# -----------------------------------------
# Name: Deepika M
# Date: 07-07-2026
# Task: The Secure Vault Gateway
# -----------------------------------------

# ==========================
# Task - 1
# The Secure Vault Gateway
# ==========================

def access_vault(user_id, *, pincode, biometric_id=None):
    """
    Grants access to the vault using a user ID and keyword-only credentials.
    """

    print(f"User ID      : {user_id}")
    print(f"Pincode      : {pincode}")

    if biometric_id is not None:
        print(f"Biometric ID : {biometric_id}")
        print("Vault Access Granted (Biometric Verification).")
    else:
        print("Vault Access Granted (Pincode Verification).")


# Test Cases
if __name__ == "__main__":

    print("===== Task - 1 =====")

    print("\nTest Case 1")
    access_vault("EMP101", pincode="1234")

    print("\nTest Case 2")
    access_vault("EMP102", pincode="5678", biometric_id="BIO789")

    print("\nTest Case 3")
    access_vault("", pincode="0000")

# ==========================
# Task - 2
# The Bulk Transfer Processor
# ==========================

def execute_bulk_transfer(sender_account, *amounts):
    """
    Processes multiple transfers from a sender account.

    Args:
        sender_account (str): Account number of the sender.
        *amounts (float): Variable number of transfer amounts.

    Returns:
        float: Remaining balance after all transfers.
    """

    balance = 10000

    print(f"Sender Account : {sender_account}")
    print(f"Starting Balance: ₹{balance}")

    for amount in amounts:
        print(f"Transferred ₹{amount}")
        balance -= amount

    return balance


# Test Cases
if __name__ == "__main__":

    print("===== Task - 2 =====")

    print("\nTest Case 1")
    remaining_balance = execute_bulk_transfer(
        "ACC1001", 1000, 1500, 2000
    )
    print(f"Remaining Balance: ₹{remaining_balance}")

    print("\nTest Case 2")
    remaining_balance = execute_bulk_transfer(
        "ACC1002", 5000
    )
    print(f"Remaining Balance: ₹{remaining_balance}")

    print("\nTest Case 3")
    remaining_balance = execute_bulk_transfer(
        "ACC1003"
    )
    print(f"Remaining Balance: ₹{remaining_balance}")

# ==========================
# Task - 3
# Dynamic Fee Policy
# ==========================

def calculate_net_amount(base_amount, **kwargs):
    """
    Calculates the final amount after applying
    multiple taxes or service fees.

    Args:
        base_amount (float): Initial amount.
        **kwargs: Tax or fee rates.

    Returns:
        float: Final amount after applying all taxes.
    """

    net_amount = base_amount

    print(f"Base Amount : ₹{base_amount}")

    for fee_name, fee_rate in kwargs.items():
        fee = base_amount * fee_rate
        net_amount += fee
        print(f"{fee_name} ({fee_rate * 100:.0f}%): ₹{fee:.2f}")

    return net_amount


# Test Cases
if __name__ == "__main__":

    print("===== Task - 3 =====")

    print("\nTest Case 1")
    amount = calculate_net_amount(
        1000,
        vat=0.15,
        service_fee=0.05
    )
    print(f"Net Amount : ₹{amount:.2f}")

    print("\nTest Case 2")
    amount = calculate_net_amount(
        5000,
        gst=0.18
    )
    print(f"Net Amount : ₹{amount:.2f}")

    print("\nTest Case 3")
    amount = calculate_net_amount(
        2500
    )
    print(f"Net Amount : ₹{amount:.2f}")


# ==========================
# Task - 4
# The Currency Arbitrage Scanner
# ==========================

def get_market_rates(ticker):
    """
    Returns the buy price, sell price, and spread
    for the given currency ticker.

    Args:
        ticker (str): Currency symbol.

    Returns:
        tuple: (buy_price, sell_price, spread)
    """

    market_data = {
        "USD": (83.20, 83.50),
        "EUR": (90.10, 90.60),
        "GBP": (105.40, 106.00)
    }

    buy_price, sell_price = market_data.get(ticker.upper(), (0.0, 0.0))
    spread = sell_price - buy_price

    return buy_price, sell_price, spread


# Test Cases
if __name__ == "__main__":

    print("===== Task - 4 =====")

    print("\nTest Case 1")
    buy, sell, spread = get_market_rates("USD")
    print(f"Buy Price  : ₹{buy:.2f}")
    print(f"Sell Price : ₹{sell:.2f}")
    print(f"Spread     : ₹{spread:.2f}")

    print("\nTest Case 2")
    buy, _, spread = get_market_rates("EUR")
    print(f"Buy Price  : ₹{buy:.2f}")
    print(f"Spread     : ₹{spread:.2f}")

    print("\nTest Case 3")
    buy, sell, spread = get_market_rates("JPY")
    print(f"Buy Price  : ₹{buy:.2f}")
    print(f"Sell Price : ₹{sell:.2f}")
    print(f"Spread     : ₹{spread:.2f}")

# ==========================
# Task - 5
# Account Validation Wrapper
# ==========================

def validate_account_status(account_id):
    """
    Returns the account status and KYC information.

    Args:
        account_id (str): Account ID.

    Returns:
        tuple: (status_code, (is_active, kyc_complete))
    """

    account_data = {
        "ACC101": (200, (True, True)),
        "ACC102": (200, (True, False)),
        "ACC103": (403, (False, False))
    }

    return account_data.get(account_id, (404, (False, False)))


# Test Cases
if __name__ == "__main__":

    print("===== Task - 5 =====")

    print("\nTest Case 1")
    status_code, (is_active, kyc_complete) = validate_account_status("ACC101")
    print(f"Status Code  : {status_code}")
    print(f"Is Active    : {is_active}")
    print(f"KYC Complete : {kyc_complete}")

    print("\nTest Case 2")
    status_code, (_, kyc_complete) = validate_account_status("ACC102")
    print(f"Status Code  : {status_code}")
    print(f"KYC Complete : {kyc_complete}")

    print("\nTest Case 3")
    status_code, (is_active, kyc_complete) = validate_account_status("ACC999")
    print(f"Status Code  : {status_code}")
    print(f"Is Active    : {is_active}")
    print(f"KYC Complete : {kyc_complete}")

# ==========================
# Task - 6
# The Auditor's Google-Style Docstring
# ==========================

def calculate_compound_interest(principal, rate, time, compounds_per_year):
    """
    Calculate the compound interest and final amount.

    Args:
        principal (float): Initial amount of money invested.
        rate (float): Annual interest rate (in decimal form).
        time (int): Investment period in years.
        compounds_per_year (int): Number of times interest is compounded per year.

    Returns:
        float: Final amount after compound interest is applied.

    Raises:
        ValueError: If the interest rate is negative.
    """

    if rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    amount = principal * (1 + rate / compounds_per_year) ** (
        compounds_per_year * time
    )

    return amount


# Test Cases
if __name__ == "__main__":

    print("===== Task - 6 =====")

    print("\nTest Case 1")
    print(
        f"Final Amount: ₹{calculate_compound_interest(10000, 0.10, 2, 4):.2f}"
    )

    print("\nTest Case 2")
    print(
        f"Final Amount: ₹{calculate_compound_interest(5000, 0, 3, 1):.2f}"
    )

    print("\nTest Case 3")
    try:
        calculate_compound_interest(10000, -0.05, 2, 4)
    except ValueError as error:
        print(error)

# ==========================
# Task - 7
# NumPy-Style Scientific Schema
# ==========================

def calculate_risk_score(data_points, sensitivity):
    """
    Calculate the overall risk score.

    Parameters
    ----------
    data_points : array-like
        A collection of numerical risk values.
    sensitivity : float
        A multiplier used to adjust the final risk score.

    Returns
    -------
    float
        The calculated risk score.

    Raises
    ------
    ValueError
        If sensitivity is negative or if data_points is empty.
    """

    if sensitivity < 0:
        raise ValueError("Sensitivity cannot be negative.")

    if not data_points:
        raise ValueError("Data points cannot be empty.")

    average = sum(data_points) / len(data_points)
    risk_score = average * sensitivity

    return risk_score


# Test Cases
if __name__ == "__main__":

    print("===== Task - 7 =====")

    print("\nTest Case 1")
    score = calculate_risk_score([10, 20, 30, 40], 1.5)
    print(f"Risk Score: {score:.2f}")

    print("\nTest Case 2")
    score = calculate_risk_score([50], 0)
    print(f"Risk Score: {score:.2f}")

    print("\nTest Case 3")
    try:
        score = calculate_risk_score([], 2.0)
        print(f"Risk Score: {score:.2f}")
    except ValueError as error:
        print(error)

# ==========================
# Task - 8
# The "Print vs. Return" Audit
# ==========================

def my_function():
    """
    Demonstrates the difference between print()
    and return().
    """

    total = 100 + 200
    print(f"Total = {total}")
    # Missing return statement


# Test Cases
if __name__ == "__main__":

    print("===== Task - 8 =====")

    print("\nTest Case 1")
    result = my_function()
    print("Value of result:", result)

    print("\nTest Case 2")
    if result is None:
        print("The function returned None because it has no return statement.")

    print("\nTest Case 3")

    def corrected_function():
        total = 100 + 200
        print(f"Total = {total}")
        return total

    corrected_result = corrected_function()
    print("Returned Value:", corrected_result)

# ==========================
# Task - 9
# Functional Pipeline Design
# ==========================

def clean_input(invoice):
    """
    Removes extra spaces and converts the amount to float.

    Args:
        invoice (tuple): (customer_name, amount)

    Returns:
        tuple: Cleaned customer name and amount.
    """

    customer_name = invoice[0].strip()
    amount = float(invoice[1])

    return customer_name, amount


def apply_discount(invoice):
    """
    Applies a 10% discount to the invoice amount.

    Args:
        invoice (tuple): (customer_name, amount)

    Returns:
        tuple: Customer name and discounted amount.
    """

    customer_name, amount = invoice
    discounted_amount = amount * 0.90

    return customer_name, discounted_amount


def format_currency(invoice):
    """
    Formats the amount as Indian Rupees.

    Args:
        invoice (tuple): (customer_name, amount)

    Returns:
        tuple: Customer name and formatted amount.
    """

    customer_name, amount = invoice

    return customer_name, f"₹{amount:.2f}"


def process_invoice(customer_name, amount):
    """
    Processes the invoice through all functions.

    Args:
        customer_name (str): Customer name.
        amount (float): Invoice amount.

    Returns:
        tuple: Final processed invoice.
    """

    invoice = (customer_name, amount)

    invoice = clean_input(invoice)
    invoice = apply_discount(invoice)
    invoice = format_currency(invoice)

    return invoice


# Test Cases
if __name__ == "__main__":

    print("===== Task - 9 =====")

    print("\nTest Case 1")
    result = process_invoice("  Deepika  ", 1000)
    print(result)

    print("\nTest Case 2")
    result = process_invoice("Rahul", 0)
    print(result)

    print("\nTest Case 3")
    result = process_invoice("Priya", 2500.50)
    print(result)

# ==========================
# Task - 10
# The Fail-Safe Dispatcher
# ==========================

def dispatch_payment(account_number, amount):
    """
    Dispatch a payment and return the operation result.

    This function follows the "Result Pattern", similar to Rust and Go,
    where the function returns a tuple instead of raising an exception
    for expected failures.

    Returns:
        tuple:
            (True, None)
                Payment completed successfully.

            (False, "Reason")
                Payment failed and the second element contains
                the error message.
    """

    if amount <= 0:
        return False, "Invalid payment amount."

    if account_number == "":
        return False, "Account number cannot be empty."

    return True, None


# Test Cases
if __name__ == "__main__":

    print("===== Task - 10 =====")

    print("\nTest Case 1")
    success, error = dispatch_payment("ACC101", 5000)
    print(f"Success : {success}")
    print(f"Error   : {error}")

    print("\nTest Case 2")
    success, error = dispatch_payment("ACC102", 0)
    print(f"Success : {success}")
    print(f"Error   : {error}")

    print("\nTest Case 3")
    success, error = dispatch_payment("", 1000)
    print(f"Success : {success}")
    print(f"Error   : {error}")