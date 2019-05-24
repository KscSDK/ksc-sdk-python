# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("bill","cn-beijing-6",use_ssl=False)

    #print client.get_product_code()

    #print client.get_month_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")

    print client.get_postpay_detail_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")
