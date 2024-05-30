from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromeBinary = '/home/iantitor/Downloads/chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/brave'
driver = webdriver.Chrome(chromeBinary, chrome_options=options)

driver.get('https://app.knowledgehook.com/app/student/e32b2f69-fb65-ee11-9761-0050568c42b6/')

def skipClick(x):
    while 1:
        try:
            name = driver.find_element_by_xpath(x)
            name.click()
            break
        except:
            pass


def skipType(x, y):
    while 1:
        try:
            code = driver.find_element_by_xpath(x)
            code.send_keys(y + Keys.ENTER)
            break
        except:
            pass


def question():
    while 1:
        try:
            questionElement = driver.find_element_by_xpath('//div[@class="RenderMath gameplayQuestionText"]//p[@class="ng-scope"]')
            break
        except:
            pass
    return questionElement.get_attribute('innerHTML')

skipType('//input[@placeholder="Class Code"]', '418867')
skipClick('//a[contains(text(), "Sequin")]')
skipType('//input[@ng-attr-type="{{ ShowPassword ? ' + "'text'" + " : 'password'" + ' }}"]', 'now23')
skipClick('//button[@ng-click="SetLocation(' + "'Home'" + ')"]')
skipClick('//a[@href="/app/student/e32b2f69-fb65-ee11-9761-0050568c42b6/gameplay/skill/924f96d1-2599-ee11-9a33-0050569ebc32?branchid=6fdc61fa-4acc-ea11-974a-0050568c42b6&courseid=99c54417-13ef-4b70-bdb0-019f8a422a57"]')
print('first skip')
skipClick('//button[@class="btn btn-lg btn-primary btnCloseWorkedExample"]')
print('second skip')
skipClick('//button[@class="btn btn-lg btn-primary wide-xxs btnCloseWorkedExample"]')
try:
    driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary wide-xxs btnCloseWorkedExample"]').click()
except:
    pass

question1 = question().replace('This model represents this addition; (', '').replace('(', '').replace(')', ''). replace('+ ', '').replace('−', '-').split(' ')
answer = int(question1[0]) + int(question1[1])
if answer == abs(answer):
    answer = '+' + str(answer)
else:
    answer = str(answer).replace('-', '–')

for x in range(4):
    answerElement = driver.find_element_by_id(f'McAnswer{x + 1}')
    potentialAnswer = driver.find_element_by_xpath(f'//div[@id="McAnswer{x + 1}"]//div[@ng-click="SelectMultipleChoiceAnswer(Choice)"]//table//tbody//tr//td[@class="gameplayAnswerValue"]//span//p')
    if answer == potentialAnswer.get_attribute('innerHTML'):
        answerElement.click()
submit = driver.find_element_by_id('GameplaySubmitSelected')
submit.click()

skipClick('//a[@ng-click="SkipUpload()"]')
skipClick('//a[@ng-click="Continue()"]')
skipClick('//a[@class="cursor text-lg"]')
skipClick('//button[@ng-click="CloseModal()"]')
skipClick('//button[@ng-click="CloseModal()"]')
try:
    driver.find_element_by_xpath('//button[@ng-click="CloseModal()"]').click()
except:
    pass
try:
    driver.find_element_by_xpath('//button[@ng-click="CloseModal()"]').click()
except:
    pass
answer = int(driver.find_element_by_id('MathJax-Span-8').get_attribute('innerHTML')) * int(driver.find_element_by_id('MathJax-Span-5').get_attribute('innerHTML'))
print(answer)
