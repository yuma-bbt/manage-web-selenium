var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;
var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .build();
driver.get('http://yahoo.co.jp');
driver.quit();
