# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    print (s)

    client = s.create_client("bill-union","cn-beijing-6",use_ssl=False)

    print (client.describe_bill_summary_by_pay_mode(BillBeginMonth="2020-06",BillEndMonth="2020-06"))
    print (client.describe_bill_summary_by_product(BillBeginMonth="2020-06",BillEndMonth="2020-06"))
    print (client.describe_bill_summary_by_project(BillBeginMonth="2020-06",BillEndMonth="2020-06"))
    print (client.describe_instance_summary_bills(BillMonth="2020-06",Page="1",Size="1"))
    print (client.describe_product_code())
    #print client.get_month_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")

    #print client.get_postpay_detail_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")
