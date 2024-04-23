from datetime import datetime
from dateutil.relativedelta import relativedelta

PAYMENT_TERM_IN_YEARS = 8


def format_date(date):
    date_format = "%d/%m/%Y"
    return date.strftime(date_format)


loan_amount = 1_000_000
loan_date = datetime.now()
installment_interval = relativedelta(months=1)
payment_term_years = relativedelta(years=PAYMENT_TERM_IN_YEARS)

total_month_count = PAYMENT_TERM_IN_YEARS * 12
installment_amount = loan_amount / total_month_count
initial_payment_date = loan_date + installment_interval
final_payment_date = initial_payment_date + payment_term_years

installment_number = 0
accumulated_amount = 0.0
installment_date = initial_payment_date

while installment_date < final_payment_date:
    installment_number += 1
    accumulated_amount += installment_amount
    print(
        f"{installment_number:3} |",
        f"{format_date(installment_date)} |",
        f"$ {accumulated_amount:,.2f}"
    )
    installment_date += installment_interval
