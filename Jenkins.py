username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

caps = {
 'os': 'Windows',
 'os_version': '10',
 'browser': 'chrome',
 'browser_version': 'latest',
 'name': 'BStack-[Jenkins] Sample Test', # test name
 'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
 'browserstack.local': browserstack_local,
 'browserstack.localIdentifier': browserstack_local_identifier,
 'browserstack.user': username,
 'browserstack.key': access_key
}

driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=caps)
driver.get("http://flipkart.com")
print(driver.title)
driver.quit()
