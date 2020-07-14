# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("krtpay","cn-beijing-6",use_ssl=False,ks_access_key_id=ak,
                             ks_secret_access_key=sk)

    #res =  client.describe_product_code()
    #print json.dumps(res)

    #print client.describe_bill_summary(BillStartTime="2020-07-13 00:00:00",BillEndTime="2020-07-14 00:00:00")


    #print client.describe_bills(BillStartTime="2020-07-13 00:00:00",BillEndTime="2020-07-14 00:00:00",
    #                            ProductCode="KEC",Size=1)

    print client.describe_bill_detail(BillStartTime="2020-07-13 00:00:00",BillEndTime="2020-07-14 00:00:00",
                                ProductCode="KEC",Size=1,SettleCycle=3)

    #print client.get_month_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")

    #print client.get_postpay_detail_bill(BillStartMonth="2019-03", BillEndMonth="2019-03")
