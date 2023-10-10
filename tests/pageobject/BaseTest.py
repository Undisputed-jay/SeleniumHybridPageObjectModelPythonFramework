# In this, we will be removing @pytest.mark.usefixtures("setup_and_teardown")
# we will be setting the BaseTest as the parent class for all the test files (test_search, test_register, test_login)

import pytest
from datetime import datetime

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    
    def test_generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ayodele"+time_stamp+"@gmail.com"