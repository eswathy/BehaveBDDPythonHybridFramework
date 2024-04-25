from behave import *
from utilities import ExcelUtils
import logging


# logging.basicConfig(filename='configurations/test.log', level=logging.INFO)


@given(u'read the data from excel sheet')
def step_impl(context):
    #Read Data from excel
    # context.final_list = ExcelUtils.get_data_from_excel("ExcelFiles/CustomerCards.xlsx", "CardsData")
    # for row in context.final_list:
    #     logging.info(msg=row)

    ExcelUtils.generate_excel("ExcelFiles/CustomerCards.xlsx", "CardsData2",
                              ["name", "phone", "email"],
                              [{
                                  'name': 'swat1',
                                  'phone': '2532626598',
                                  'email': 'abc1@gmail.com'
                                  },
                                  {
                                      'name': 'swat2',
                                      'phone': '45265986256',
                                      'email': 'abc2@gmail.com'
                                  },
                                  {
                                      'name': 'swat3',
                                      'phone': '125625985',
                                      'email': 'abc3@gmail.com'
                                  }]
                              )
