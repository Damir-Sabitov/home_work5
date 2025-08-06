import os, time
from selene import browser, be, have

def test_submit():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'my_file.png'))

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Snow')
    browser.element('#userEmail').type('example@mail.ru')
    browser.element('label[for="gender-radio-1"]').should(be.clickable).click()
    browser.element('#userNumber').type('5555555555')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="4"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1995"]').click()

    browser.element('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()


    browser.element('#subjectsInput').type('Hist').press_enter()

    target = browser.element('[for="hobbies-checkbox-1"]')
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
    target.should(be.visible).should(be.clickable).click()

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('test street address')

    browser.element('#submit').click()

    browser.element('.modal-content').should(be.visible)

    browser.element('.table-responsive').should(have.text('John Snow'))
    browser.element('.table-responsive').should(have.text('example@mail.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('5555555555'))
    browser.element('.table-responsive').should(have.text('History'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('my_file.png'))
    browser.element('.table-responsive').should(have.text('test street address'))
    browser.element('.table-responsive').should(have.text('15 May,1995'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))