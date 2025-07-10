Test Personal Expense Tracker
    [Documentation]    This is a test case for the Personal Expense Tracker application.
    [Tags]    personal_expense_tracker

    # Test case 1: Login
    Login to application    testuser    testpassword
    Verify login success

    # Test case 2: Add transaction
    Add transaction    2022-01-01    100.00    Food    Lunch
    Verify transaction added

    # Test case 3: View transactions
    View transactions
    Verify transactions displayed

    # Test case 4: Edit transaction
    Edit transaction    2022-01-01    100.00    Food    Lunch
    Verify transaction edited

    # Test case 5: Delete transaction
    Delete transaction    2022-01-01    100.00    Food    Lunch
    Verify transaction deleted