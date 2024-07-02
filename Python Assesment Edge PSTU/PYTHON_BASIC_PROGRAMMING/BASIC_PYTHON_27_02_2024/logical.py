has_good_credit = True

has_criminal_record = False

has_smart_salary = True

if has_good_credit and has_criminal_record:
    print('Eligible for loan')
elif has_smart_salary and has_good_credit:
    print('Installment will be 50% TK')
else:
    print('Not Eligible For Loan.')