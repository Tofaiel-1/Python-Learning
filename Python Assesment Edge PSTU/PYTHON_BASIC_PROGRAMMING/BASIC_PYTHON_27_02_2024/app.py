#food = ['Alltime', 'Pancake', 'Dancake', 'Honeycomb', 'Sandwich']

#food = ('Alltime', 'Pancake', 'Dancake', 'Honeycomb', 'Sandwich')



#c = course.replace('beginners' , 'Advance')




#c = len(course)

#c = course.find('b')






course = 'Python for beginners!'

print('n' in course)


loan_amount = 10000000

person_has_good_credit = False

person_has_good_income = False

installment1 = loan_amount / 30

installment2 = loan_amount / 20

installment3 = loan_amount / 10

if person_has_good_credit and person_has_good_income:

    print('The person is eligible for the installment of : ' + str(installment1) )

elif  person_has_good_credit or person_has_good_income:

    print('The person is eligible for the installment of : ' + str(installment2) )
else:

    print('The person is eligible for the installment of : ' + str(installment3) )

















