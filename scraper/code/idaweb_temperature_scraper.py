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
        raise Exception("Invalid usage.\n\nRun: python idaweb_radiation_scraper.py <weather_param> <year>\n\n"
                        "Where weather_param is the following:\n"
                        "\t- temp_2_m_current_val\n"
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
driver.implicitly_wait(1)

main_directory_location= "/home/ema/Dropbox/ada/solarity/scraper/"
program_files_location = main_directory_location + "scraper_data/"
logs_location = main_directory_location + "logs/"

log_filename = logs_location + 'execution_flow.log'
exception_log_filename = logs_location + 'exceptions.log'

parameter_checkbox_dict = {
'temp_2_m_current_val' : '91'
}

new_stations_2015_dict = {
'Bergün / Latsch': '18575,91,1,20.03.2015 07:20:00',
'Bivio': '4379,91,1,28.04.2015 06:00:00',
'Col des Mosses': '18626,91,1,10.04.2015 06:00:00',
'Courtelary': '18621,91,1,17.03.2015 07:00:00',
'Flühli, LU': '18562,91,1,19.03.2015 08:00:00',
'Frutigen': '18889,91,1,18.08.2015 06:00:00',
'Gersau': '18604,91,1,10.03.2015 08:00:00',
'Lachen / Galgenen': '18609,91,1,27.10.2015 07:00:00',
'Les Marécottes': '18883,91,1,24.08.2015 15:10:00',
'Mottec': '18615,91,1,15.04.2015 05:00:00',
'Nottwil / SPZ': '18854,91,1,12.05.2015 06:40:00',
'Oberriet, SG': '18568,91,1,05.05.2015 06:00:00',
'Otemma': '12081,91,1,10.12.2015 13:30:00',
'Vals': '18580,91,1,01.04.2015 05:00:00',
'Vevey / Corseaux': '18876,91,1,07.09.2015 13:00:00'
}


# =====================================================================================================================#
# ====================================================== MAIN =========================================================#
# =====================================================================================================================#
if __name__ == "__main__":

    weather_param, year = get_params()

    param_filename = logs_location + weather_param + '.log'

    # Define the months for year 2015 (each month, an order)
    first_month_1 = ['01.01.' + year, '15.01.' + year]
    first_month_2 = ['16.01.' + year, '31.01.' + year]
    second_month_1 = ['01.02.' + year, '15.02.' + year]
    second_month_2 = ['16.02.' + year, '01.03.' + year]
    third_month_1 = ['02.03.' + year, '15.03.' + year]
    third_month_2 = ['16.03.' + year, '31.03.' + year]
    fourth_month_1 = ['01.04.' + year, '15.04.' + year]
    fourth_month_2 = ['16.04.' + year, '30.04.' + year]
    fifth_month_1 = ['01.05.' + year, '15.05.' + year]
    fifth_month_2 = ['16.05.' + year, '31.05.' + year]
    sixth_month_1 = ['01.06.' + year, '15.06.' + year]
    sixth_month_2 = ['16.06.' + year, '30.06.' + year]
    seventh_month_1 = ['01.07.' + year, '15.07.' + year]
    seventh_month_2 = ['16.07.' + year, '31.07.' + year]
    eighth_month_1 = ['01.08.' + year, '15.08.' + year]
    eighth_month_2 = ['16.08.' + year, '31.08.' + year]
    ninth_month_1 = ['01.09.' + year, '15.09.' + year]
    ninth_month_2 = ['16.09.' + year, '30.09.' + year]
    tenth_month_1 = ['01.10.' + year, '15.10.' + year]
    tenth_month_2 = ['16.10.' + year, '31.10.' + year]
    eleventh_month_1 = ['01.11.' + year, '15.11.' + year]
    eleventh_month_2 = ['16.11.' + year, '30.11.' + year]
    twelfth_month_1 = ['01.12.' + year, '15.12.' + year]
    twelfth_month_2 = ['16.12.' + year, '31.12.' + year]
    months = [first_month_1, first_month_2, second_month_1, second_month_2, third_month_1, third_month_2,
              fourth_month_1, fourth_month_2, fifth_month_1, fifth_month_2, sixth_month_1, sixth_month_2,
              seventh_month_1, seventh_month_2, eighth_month_1, eighth_month_2, ninth_month_1, ninth_month_2,
              tenth_month_1, tenth_month_2, eleventh_month_1, eleventh_month_2, twelfth_month_1, twelfth_month_2]

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
            driver.find_element_by_xpath("//option[@value='temperature']").click()  # Param. Group = temperature
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

                if year == '2015':
                    # Go over all the remaining pages to see if there is any of the new stations
                    iterate = True
                    while iterate:
                        for new_station in sorted(new_stations_2015_dict):
                            stat_xpath = "//input[@value='" + new_stations_2015_dict[new_station] + "']"
                            if (check_exists_by_xpath(stat_xpath)):
                                driver.find_element_by_xpath(stat_xpath).click() # Deselect station
                        if (check_exists_by_xpath("//img[@src='/idaweb/images/arrowrightblack.gif']")):
                            # No more pages left
                            iterate = False
                        else:
                            driver.find_element_by_xpath("//a[@title='Next']").click()

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
