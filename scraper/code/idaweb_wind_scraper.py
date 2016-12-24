# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# import time
# from bs4 import BeautifulSoup
from datetime import datetime

import sys
import logging



# =====================================================================================================================#
# ================================================== FUNCTIONS ========================================================#
# =====================================================================================================================#
def get_params():
    """
    Retrieve from the command line the weather parameter and the year to be requested.
    """
    if len(sys.argv) == 3:
        return [str((sys.argv)[1]), str((sys.argv)[2])]
    else:
        raise Exception("Invalid usage.\n\nRun: python idaweb_wind_scraper.py <weather_param> <year>\n\n"
                        "Where weather_param the following:\n"
                        "\t- wind_scalar_10m_mean\n"
                        "And year is an integer value" + "\n")


def login_to_idaweb():
    """
    Login to IDAWEB by using the credentials specified in the file.
    """
    log.write("Logging in to IDAWEB..."+"\n")
    driver.get(login_url)

    if email=='' or password=='':
        log.write("Invalid credentials to log in to IDAWEB.\nExiting..." + "\n")
        raise Exception("Invalid credentials.\n\nPlease, insert your email and password to log in to IDAWEB.\n")

    else:
        driver.find_element_by_xpath("//input[@name='user']").send_keys(email)
        driver.find_element_by_id('password_input').send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



# =====================================================================================================================#
# =============================================== GLOBAL VARIABLES ====================================================#
# =====================================================================================================================#
email = ""
password = ""
login_url = "https://gate.meteoswiss.ch/idaweb/login.do"

# webdriver to be used (Firefox(), Chrome(), PhantomJS(), ...)
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
driver.implicitly_wait(5)

main_directory_location= "/home/ema/Dropbox/ada/solarity/scraper/"
program_files_location = main_directory_location + "scraper_data/"
logs_location = main_directory_location + "logs/"

log_filename = logs_location + 'execution_flow.log'
exception_log_filename = logs_location + 'exceptions.log'

parameter_checkbox_dict = {
'wind_scalar_10m_mean' : '196'
}



# =====================================================================================================================#
# ====================================================== MAIN =========================================================#
# =====================================================================================================================#
if __name__ == "__main__":

    weather_param, year = get_params()

    param_filename = logs_location + weather_param + '.log'

    # Define the months for year 2015 (each month, an order)
    first_month = ['01.01.' + year, '31.01.' + year]
    second_month = ['01.02.' + year, '1.03.' + year]
    third_month = ['02.03.' + year, '31.03.' + year]
    fourth_month = ['01.04.' + year, '30.04.' + year]
    fifth_month = ['01.05.' + year, '31.05.' + year]
    sixth_month = ['01.06.' + year, '30.06.' + year]
    seventh_month = ['01.07.' + year, '31.07.' + year]
    eighth_month = ['01.08.' + year, '31.08.' + year]
    ninth_month = ['01.09.' + year, '30.09.' + year]
    tenth_month = ['01.10.' + year, '31.10.' + year]
    eleventh_month = ['01.11.' + year, '30.11.' + year]
    twelfth_month = ['01.12.' + year, '31.12.' + year]
    months = [first_month, second_month, third_month, fourth_month, fifth_month, sixth_month,
              seventh_month, eighth_month, ninth_month, tenth_month, eleventh_month, twelfth_month]

    # Define the bimesters for the selected year (each month, an order)
    first_bimester = ['01.01.'+ year, '01.03.'+ year] # we ask until march 1 to avoid dealing with leap years
    second_bimester = ['02.03.' + year, '30.04.' + year]
    third_bimester = ['01.05.' + year, '30.06.' + year]
    fourth_bimester = ['01.07.'+ year, '31.08.'+ year]
    fifth_bimester = ['01.09.' + year, '31.10.' + year]
    sixth_bimester = ['01.11.'+ year, '31.12.'+ year]
    bimesters = [first_bimester, second_bimester, third_bimester, fourth_bimester, fifth_bimester, sixth_bimester]

    log = open(log_filename, "a")
    logging.basicConfig(filename=exception_log_filename)

    start = datetime.now()
    log.write("********************************************************************************"+"\n")
    log.write("START: " + str(start) + "\n")

    try:
        if main_directory_location == '':
            log.write("Full path to scraper folder missing.\nExiting..." + "\n")
            raise Exception("Missing path.\n\nPlease, insert the ull path to your scraper folder.\n")

        login_to_idaweb()
        log.write("Successfully logged in to IDAWEB..." + "\n")

        log.write("Weather parameter:" + weather_param + "\n")
        with open(param_filename, 'a') as f:
            f.write(year + "\n")

        periods = bimesters
        # if year == '2015':
        #     periods = months

        for idx, period in enumerate(periods):
            log.write("Time span: " + str(period) + "\n")

            # Search parameters ====================================================================================== #
            log.write("\tSetting search parameters..." + "\n")
            driver.get("https://gate.meteoswiss.ch/idaweb/system/orderWizard.do?method=parameter")
            driver.find_element_by_xpath("//option[@value='wind']").click()         # Param. Group = wind
            driver.find_element_by_xpath("//option[@value='T']").click()            # Granularity = ten minutes
            driver.find_element_by_xpath("//input[@value='Search']").click()        # Search for these params

            # Parameter preselection ================================================================================= #
            log.write("\tSelecting weather parameter..." + "\n")
            driver.find_element_by_xpath("//input[@value='" + parameter_checkbox_dict[weather_param] + "']").click()

            # Station preselection =================================================================================== #
            log.write("\tChoosing stations..." + "\n")
            driver.execute_script("javascript:setMethod('step');setState('station');submitCountValidated();")
            driver.find_element_by_xpath("//input[@value='Select all']").click()

            # Time preselection ====================================================================================== #
            log.write("\tSetting time span..." + "\n")
            driver.execute_script("javascript:setMethod('step');setState('criteria');submitCountValidated();")
            driver.find_element_by_xpath("//input[@name='since']").send_keys(period[0])
            driver.find_element_by_xpath("//input[@name='till']").send_keys(period[1])

            # Data inventory ========================================================================================= #
            log.write("\tSelecting data..." + "\n")
            driver.execute_script("javascript:setMethod('step');setState('inventory');submitCountValidated();")

            if check_exists_by_xpath("//div[@id='no_results']"):
                log.write("\tNo data available for the requested parameter in this time span..." + "\n")

            else:
                driver.find_element_by_xpath("//input[@value='Select all']").click()

                # Order ============================================================================================== #
                log.write("\tChecking the order..." + "\n")
                driver.execute_script("javascript:setMethod('step');setState('order');submitCountValidated();")
                ordername = weather_param + str(idx)
                driver.find_element_by_xpath("//input[@name='orderText']").send_keys(ordername)
                driver.find_element_by_xpath("//option[@value='data.format.csv']").click()

                # Summary ============================================================================================ #
                log.write("\tChecking the summary..." + "\n")
                driver.execute_script("javascript:setMethod('step');setState('summary');submitCountValidated();")

                # General Terms and Conditions ======================================================================= #
                log.write("\tAccepting the general terms and conditions..." + "\n")
                driver.execute_script("javascript:setMethod('step');setState('agb');submitCountValidated();")
                driver.find_element_by_xpath("//input[@name='acceptAgbs']").click()

                log.write("\tPlacing the order..." + "\n")
                driver.find_element_by_xpath("//input[@value='Order']").click()

                with open(param_filename, 'a') as f:
                    f.write(period[0] + " " + period[1] + " " + str(idx) + "\n")

        with open(param_filename, 'a') as f:
            f.write("\n")

        end = datetime.now()
        log.write('\nEND: ' + str(end) + '\n\n')

    except:
        now = datetime.now()
        logging.exception("main exception - " + str(now))
        log.write('\nEXCEPTION RAISED:' + str(now) + '\n\n')

    finally:
        # close driver and log file
        driver.quit()
        log.close()
