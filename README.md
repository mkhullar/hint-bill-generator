Hint Bill Generator

by - Mayank Khullar (mkhullar@asu.edu)

dependencies:
1. Install python 3.6 (https://www.python.org/downloads/)

Instructions
1. Unzip hint_bill_generator.zip
2. Navigate to main.py.
3. Run python3 main.py.
4. Output will be displayed on console according to the test cases from main.py.
4. Enjoy!

Discussion
I used the following technologies: python3, PyCharm.

Requirements
1. Given a Plan and an array of Events, determine the deductible remaining (if any) on the plan. For example, given the example plan (included below) when called with an array consisting of a single event with a cost of $406.40 it should arrive at $1,093.60 remaining. When called with multiple events that total more than $1,500.00 it should arrive at $0.
2. Given a Plan, an array of Events and a period in months, determine the total cost to the patient over the time period. This includes all premiums, deductibles, and event costs. For example, given the example plan and events (still included below) and a period in months of 12, the result would be $10,535.44. ($6,000.00 for premiums + $1,500.00 for deductibles + $3,035.44 of patient event cost after deductibles)
3. With the same inputs as #3, determine each component of the cost, how much the patient paid in premiums, deductible, the patient's portion of the events and the insurance company's portion of the events.

Future Work.

1. Adding more test cases.
2. Further code refactoring.
