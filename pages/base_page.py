from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    WebDriverException,
)
from utils import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Open a given URL."""
        try:
            logger.info(f"Opening URL: {url}")
            self.driver.get(url)
        except WebDriverException as e:
            logger.error(f"Failed to open URL {url}: {e}")

    def find_element(self, locator, timeout=10, clickable=False):
        """Find an element with an explicit wait."""
        try:
            condition = (
                EC.element_to_be_clickable(locator)
                if clickable
                else EC.visibility_of_element_located(locator)
            )
            return WebDriverWait(self.driver, timeout).until(condition)
        except (TimeoutException, NoSuchElementException):
            logger.error(f"Element not found or not ready: {locator}")
            return None

    def find_elements(self, locator, timeout=10):
        """Find multiple elements."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except (TimeoutException, NoSuchElementException):
            logger.error(f"Elements not found: {locator}")
            return []

    def click(self, locator, timeout=10):
        """Click an element after ensuring it is clickable."""
        element = self.find_element(locator, timeout, clickable=True)
        if element:
            try:
                element.click()
            except (
                ElementClickInterceptedException,
                ElementNotInteractableException,
            ) as e:
                logger.warning(
                    f"Click failed for {locator}, using JavaScript. Error: {e}"
                )
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as e:
                logger.error(f"Unexpected error clicking {locator}: {e}")
        else:
            logger.error(f"Cannot click, element not found or not clickable: {locator}")

    def send_keys(self, locator, text, clear_first=True, timeout=10):
        """Send keys to an input field, waiting for it to be visible first."""
        element = self.find_element(locator, timeout)
        if element:
            try:
                if clear_first:
                    element.clear()
                    element.send_keys(Keys.CONTROL + "a")
                    element.send_keys(Keys.BACKSPACE)
                element.send_keys(text)
            except WebDriverException as e:
                logger.error(f"Failed to send keys to {locator}: {e}")
        else:
            logger.error(f"Cannot send keys, element not found: {locator}")

    def get_text(self, locator, timeout=10):
        """Get text from an element, waiting for it to be visible."""
        element = self.find_element(locator, timeout)
        try:
            return element.text if element else ""
        except WebDriverException as e:
            logger.error(f"Error retrieving text from {locator}: {e}")
            return ""

    def is_element_present(self, locator, timeout=5):
        """Check if an element is present, with an optional wait."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Wait until an element is clickable."""
        return self.find_element(locator, timeout, clickable=True)

    def scroll_to_element(self, locator, timeout=10):
        """Scroll to a specific element."""
        element = self.find_element(locator, timeout)
        if element:
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                    element,
                )
            except WebDriverException as e:
                logger.error(f"Error scrolling to element {locator}: {e}")

    def press_key(self, locator, key=Keys.ENTER, timeout=10):
        """Simulate pressing a key on an element."""
        element = self.find_element(locator, timeout)
        if element:
            try:
                element.send_keys(key)
            except WebDriverException as e:
                logger.error(f"Error sending keypress to {locator}: {e}")

    def get_attribute(self, locator, attribute, timeout=10):
        """Get an attribute value from an element."""
        element = self.find_element(locator, timeout)
        try:
            return element.get_attribute(attribute) if element else None
        except WebDriverException as e:
            logger.error(f"Error getting attribute '{attribute}' from {locator}: {e}")
            return None

    def take_screenshot(self, filename="screenshot.png"):
        """Take a screenshot and save it."""
        try:
            logger.info(f"Saving screenshot: {filename}")
            self.driver.save_screenshot(filename)
        except WebDriverException as e:
            logger.error(f"Error taking screenshot: {e}")

    def switch_to_frame(self, locator, timeout=10):
        """Switch to an iframe."""
        element = self.find_element(locator, timeout)
        if element:
            try:
                self.driver.switch_to.frame(element)
            except WebDriverException as e:
                logger.error(f"Error switching to iframe {locator}: {e}")

    def switch_to_default_content(self):
        """Switch back to the main content from an iframe."""
        try:
            self.driver.switch_to.default_content()
        except WebDriverException as e:
            logger.error(f"Error switching to default content: {e}")

    def accept_alert(self, timeout=5):
        """Accept an alert popup."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            logger.info("Alert accepted.")
        except TimeoutException:
            logger.error("No alert present to accept.")
        except WebDriverException as e:
            logger.error(f"Error handling alert: {e}")

    def dismiss_alert(self, timeout=5):
        """Dismiss an alert popup."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.driver.switch_to.alert.dismiss()
            logger.info("Alert dismissed.")
        except TimeoutException:
            logger.error("No alert present to dismiss.")
        except WebDriverException as e:
            logger.error(f"Error dismissing alert: {e}")
