import put_in_function as pif

student_a, student_b, student_c = 0 , 0 , 0

pif.put_in_functions_a()
pif.put_in_functions_b()
pif.put_in_functions_c()


total_number_of_tests = 8
tests_passed = 0
a_tests = 0
b_tests = 0
c_tests = 0

try:
	import ps1a_in_function as student_a
except:
	print('Skipping Part A')
if student_a:
	print('----PART A Test 1----')
	print('RUNNING with salary: 112000, savings_percent: .17, total_cost: 750000')
	yearly_salary = 112000
	percent_to_save = .17
	home_cost = 750000
	actual = 63
	try:
		student = student_a.part_a(yearly_salary, percent_to_save, home_cost)
		if actual != student:
			print('FAILED')
			print("Part A test 1 failed. Correct answer:", actual, "Your answer:", student)
		else:
			print('PASSED')
			tests_passed += 1
			a_tests +=1
	except Exception as e:
		print("Part A test 1 failed.")
		print(e)


	print('----PART A Test 2----')
	print('RUNNING with salary: 65000, savings_percent: .20, total_cost: 400000')
	yearly_salary = 65000
	percent_to_save = .20
	home_cost = 400000
	actual = 50
	try:
		student = student_a.part_a(yearly_salary, percent_to_save, home_cost)
		if actual != student:
			print("FAILED")
			print("Part A test 2 failed. Correct answer:", actual, "Your answer:", student)
		else:
			print("PASSED")
			tests_passed += 1
			a_tests +=1
	except Exception as e:
		print("Part A test 2 failed.")
		print(e)


	print('----PART A Test 3----')
	print('RUNNING with salary: 350000, savings_percent: .3, total_cost: 10000000')
	yearly_salary = 350000
	percent_to_save = .3
	home_cost = 10000000
	actual = 130
	try:
		student = student_a.part_a(yearly_salary, percent_to_save, home_cost)
		if actual != student:
			print("FAILED")
			print("Part A test 3 failed. Correct answer:", actual, "Your answer:", student)

		else:
			print("PASSED")
			tests_passed += 1
			a_tests += 1
	except Exception as e:
		print("Part A test 3 failed.")
		print(e)


try:
	import ps1b_in_function as student_b
except:
	print('Skipping Part B')
if student_b:
	print('----PART B Test 1----')
	print('RUNNING with salary: 110000, savings_percent: .15, total_cost: 750000, raise_percentage: .03')
	yearly_salary = 110000
	percent_to_save = .15
	home_cost = 750000
	semi_annual_raise = .03
	actual = 63
	try:
		student = student_b.part_b(yearly_salary, percent_to_save, home_cost, semi_annual_raise)
		if actual != student:
			print("FAILED")
			print("Part B test 1 failed. Correct answer:", actual, "Your answer:", student)
		else:
			print("PASSED")
			tests_passed += 1
			b_tests +=1
	except Exception as e:
		print("Part B test 1 failed.")
		print(e)




	print('----PART B Test 2----')
	print('RUNNING with salary: 350000, savings_percent: .3, total_cost: 10000000, raise_percentage: .05')
	yearly_salary = 350000
	percent_to_save = .3
	home_cost = 10000000
	semi_annual_raise = .05
	actual = 97
	try:
		student = student_b.part_b(yearly_salary, percent_to_save, home_cost, semi_annual_raise)
		if actual != student:
			print("FAILED")
			print("Part B test 2 failed. Correct answer:", actual, "Your answer:", student)

		else:
			print("PASSED")
			tests_passed += 1
			b_tests += 1
	except Exception as e:
		print("Part B test 2 failed.")
		print(e)


try:
	import ps1c_in_function as student_c
except:
	print('Skipping Part C')
if student_c:
	number_of_months = 36
	total_house_cost = 750000
	down_payment_percentage = 0.25
	target_savings = total_house_cost*down_payment_percentage
	print('----PART C Test 1----')
	print('RUNNING with initial_amount: 65000')
	initial_amount = 65000
	actual_r = 0.3583984375
	actual_steps = 10
	try:
		student_r, student_steps = student_c.part_c(initial_amount)
		student_savings = initial_amount * (1 + student_r / 12) ** number_of_months
		if type(student_r) == str or (abs(student_savings - target_savings) > 100 or abs(student_steps - actual_steps) > 2):
			print("FAILED")
			print("Part C Test 1 failed. Either your r value", student_r, "does not produce the correct savings, or your algorithm takes too few or too many steps. Expected answer:", actual_r, "in", actual_steps, "steps")

		else:
			print("PASSED")
			tests_passed += 1
			c_tests += 1
	except Exception as e:
		print("Part C test 1 failed.")
		print(e)



	print('----PART C Test 2----')
	print('RUNNING with initial_amount: 187401')
	initial_amount = 187401
	actual_r = 0.06103515625
	try:
		student_r, student_steps = student_c.part_c(initial_amount)
		student_savings = initial_amount * (1 + student_r / 12) ** number_of_months
		if type(student_r) == str or (abs(student_savings - target_savings) > 100):
			print("FAILED")
			print("Part C Test 2 failed. Either your r value", student_r, "does not produce the correct savings, or your algorithm takes too few or too many steps. Expected answer:", actual_r, "in")

		else:
			print("PASSED")
			tests_passed += 1
			c_tests += 1
	except Exception as e:
		print("Part C test 2 failed.")
		print(e)



	print('----PART C Test 3----')
	print('RUNNING with initial_amount: 1000')
	initial_amount = 1000
	actual_r = None
	try:
		student_r, student_steps = student_c.part_c(initial_amount)
		if not student_r == actual_r:
			print("FAILED")
			print("Part C test 3 failed. Correct answer:", actual_r, "your_answer", student_r)

		else:
			print("PASSED")
			tests_passed += 1
			c_tests += 1

	except Exception as e:
		print("Part C test 3 failed.")
		print(e)

print("\n\n--END OF TEST SUITE--")
print("You have passed", tests_passed, "out of ", total_number_of_tests, "tests.")
print("PART A", a_tests, " out of 3")
print("PART B", b_tests, " out of 2")
print("PART C", c_tests, " out of 3")
