from celery import shared_task
from selenium_files.hesabro.club.update_customers_specifications import update_customers_specifications
from selenium_files.settings_selenium.run_app import run_hesabro

@shared_task
def run_update_customers_specifications():
    print("process 'update_customers_specifications' is running")
    driver, is_logged_in = run_hesabro()
    # print("this select")
    if is_logged_in:
        update_customers_specifications(driver)
    driver.close()
    # driver.quite()
    print("process 'update_customers_specifications' is complete")