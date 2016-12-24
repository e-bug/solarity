# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
        raise Exception("Invalid usage.\n\nRun: python idaweb_radiation_scraper.py <weather_param> <year>\n\n"
                        "Where weather_param is one of the following:\n"
                        "\t- circum-global_radiation\n"
                        "\t- global_radiation_std_dev\n"
                        "\t- global_radiation_ten_min_mean\n"
                        "\t- longwave_incoming_radiation_ten_min_avg\n"
                        "\t- longwave_outgoing_radiation_ten_min_avg\n"
                        "\t- shortwave_reflected_radiation_ten_min_avg\n"
                        "\t- uvb\n"
                        "\t- uvb_std\n"
                        "\t- photosynth_std\n"
                        "\t- diffuss\n"
                        "\t- photosynth\n"
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
'circum-global_radiation': '769',
'global_radiation_std_dev': '2119',
'global_radiation_ten_min_mean': '96',
'longwave_incoming_radiation_ten_min_avg': '175',
'longwave_outgoing_radiation_ten_min_avg': '1531',
'shortwave_reflected_radiation_ten_min_avg': '1871',
'uvb': '4810',
'uvb_std': '4811',
'photosynth_std': '4813',
'diffuss': '174',
'photosynth': '4812',
}



# =====================================================================================================================#
# ====================================================== MAIN =========================================================#
# =====================================================================================================================#
if __name__ == "__main__":

    weather_param, year = get_params()

    param_filename = logs_location + weather_param + '.log'

    # Define the quarters for the selected year (each quarter, an order)
    first_tertile = ['01.01.' + year, '31.03.' + year]
    second_tertile = ['01.04.' + year, '30.06.' + year]
    third_tertile = ['01.07.' + year, '30.09.' + year]
    fourth_tertile = ['01.10.' + year, '31.12.' + year]
    tertiles = [first_tertile, second_tertile, third_tertile, fourth_tertile]

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

        for idx, tertile in enumerate(tertiles):
            log.write("Time span: " + str(tertile) + "\n")

            # Search parameters ====================================================================================== #
            log.write("\tSetting search parameters..." + "\n")
            driver.get("https://gate.meteoswiss.ch/idaweb/system/orderWizard.do?method=parameter")
            driver.find_element_by_xpath("//option[@value='radiation']").click() # Param. Group = radiation
            driver.find_element_by_xpath("//option[@value='T']").click()         # Granularity = ten minutes
            driver.find_element_by_xpath("//input[@value='Search']").click()     # Search for these params

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
            driver.find_element_by_xpath("//input[@name='since']").send_keys(tertile[0])
            driver.find_element_by_xpath("//input[@name='till']").send_keys(tertile[1])

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
                    f.write(tertile[0] + " " + tertile[1] + " " + str(idx) + "\n")

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
