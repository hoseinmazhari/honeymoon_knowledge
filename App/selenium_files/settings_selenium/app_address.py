

hesabro_domain = "https://hesabro.ir/@hm"
honeymoonatr_domain = "https://honeymoonatr.com"
aradpayamak_domain = "http://aradpayamak.net"
class file_locations():
    cookies = "cookies"
    
class urls_hesabro():
    
    class user_detail():
        coin = f"{hesabro_domain}/customer/coin?id="
    class product():
        create_product = f"{hesabro_domain}/product-main/add-variety?copy_id=0&referrer=https%3A%2F%2Fhesabro.ir%2F%40hm%2Fproduct"
        product_view_detail = f'{hesabro_domain}/product/view?id='
        product_view_uniq_barcodes = f'{hesabro_domain}/product-method/view-unique?id='
        product_update = f'{hesabro_domain}/product-main/update-variety?id='
    class create_report():
        birthday = f"{hesabro_domain}/report-customer/index"
    class random_page():
        pages = {
            "random":{
                "1" : "/tags",
                "2" : "/settings/index?category=1",
                "3" : "/version/index",
                "4" : "/sms-report/index",
                "5" : "/ipg",
                "6" : "/comments-type",
                "7" : "/education-course",
                "8" : "/factor-report/sale",
                "9" : "/product/sale-report",
                "10" : "/product/buy-sale-review-report?factor_type=4"}
            }


class urls_honeymoonatr():
    
    class products():
        all_products = "https://honeymoonatr.com/wp-admin/edit.php?post_type=product"
        step_one_product = "https://honeymoonatr.com/wp-admin/post.php?post="
        step_tow_product = "&action=edit"
        next_page = "https://honeymoonatr.com/wp-admin/edit.php?post_type=product&paged="
class urls_arad():
    
    class phone_book():
        contact_groups = "http://aradpayamak.net/APPs/SMS/?cmp=PhoneBook&st=PhoneBookCategory"
        send_sms = 'http://aradpayamak.net/APPs/SMS/?cmp=SendDynamic&st=SendDynamic&action=sendSMSI'
    class simple_send_sms():
        send_page = 'http://aradpayamak.net/APPs/SMS/?cmp=Send&st=SendSMS'

# urls={
#     "user_detail":{
#         "coin": f"{hesabro_domain}/customer/coin?id="
#     },
#     "product":{
#     "create_product" : f"{hesabro_domain}/product-main/add-variety?copy_id=0&referrer=https%3A%2F%2Fhesabro.ir%2F%40hm%2Fproduct"
#     },
#     "birthday":{
#         "create_rpt": f"{hesabro_domain}/report-customer/index"
#     }
#     ,
#     "random":{
#         "1" : "/tags",
#         "2" : "/settings/index?category=1",
#         "3" : "/version/index",
#         "4" : "/sms-report/index",
#         "5" : "/ipg",
#         "6" : "/comments-type",
#         "7" : "/education-course",
#         "8" : "/factor-report/sale",
#         "9" : "/product/sale-report",
#         "10" : "/product/buy-sale-review-report?factor_type=4"
#     }
# }
# def get_address(part,element,id):
    # return f"{urls[part][element]}{id}"
# def get_rnd_page(element):
#     element = str(element)
#     return f"{hesabro_domain}{urls['random'][element]}"
