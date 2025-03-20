from selenium import webdriver
from utils import Config, logger
import allure


def before_all(context):
    context.config = Config


def before_scenario(context, scenario):
    feature_tags = scenario.feature.tags if scenario.feature else []

    if "ui" in scenario.tags or "ui" in feature_tags:
        logger.info("Starting Chrome...")
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        context.driver = webdriver.Chrome(options=options)


def after_step(context, step):
    if step.status == "failed":
        if hasattr(context, "driver"):
            screenshot_path = "reports/allure-results/screenshot.png"
            context.driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Failed Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


def after_scenario(context, scenario):
    logger.info("Ending scenario: %s", scenario.name)
    if hasattr(context, "driver"):
        context.driver.quit()
