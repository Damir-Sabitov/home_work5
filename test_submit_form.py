from selene import browser, be, have

def test_submit():
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Snow')
    browser.element('#userEmail').type('example@mail.ru')
    browser.element('label[for="gender-radio-1"]').should(be.clickable).click()
    browser.element('#userNumber').type('5555555555')
    browser.element('#subjectsInput').type('Hist').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#uploadPicture').send_keys('/Users/damirsabitov/PycharmProjects/home_work5/my_file.png')

    browser.element('#submit').click()


    browser.element('.modal-content').should(be.visible)

    browser.element('.table-responsive').should(have.text('John Snow'))
    browser.element('.table-responsive').should(have.text('example@mail.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('5555555555'))
    browser.element('.table-responsive').should(have.text('History'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('my_file.png'))
    browser.element('.table-responsive')
