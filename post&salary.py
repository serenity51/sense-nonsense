sal = 80000
sal1 = 90000
allowances1 = 0
deductions1 = 0
allowances = .1 * sal
deductions = .2 * sal
Nsalary = (sal + allowances - (deductions))
Nsalary1 = sal1
emp = ["e1", "e2", "e3", "e4"]
post = ["GM", "RM", "FM", "HM"]
def salary(emp, post):
 for i in emp:
    if post == "GM" or post == "RM":
        Nsalary = (sal + allowances - deductions)
        return Nsalary
    else:
        Nsalary1 = sal1 + allowances1 - deductions1
        return Nsalary1
print(salary("e1", "HM"))

#output
# e1,  FM ----90000
# e1, RM--- 72000
# e1  GM  72000
# e1 HM    90000