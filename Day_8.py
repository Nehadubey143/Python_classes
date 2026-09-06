# for loop
# for i in range(3):
# print(i)
# ➢ i → Loop variable
# ➢ Starting point → 0
# ➢ Ending point → 3(excluded) ➢ Range → 0–7
# ➢ Output → 0….7
# ➢ Note:By default starting point will be always 0
# ______________
# for i in range(0,3):
# print(i)
# ➢ Starting point → 0
# ➢ Ending point → 3 , which is always excluded
# ➢ Final range→ 0 – 2
# ➢ Final output → 0,1,2
# ______________
# for i in range(2,9):
# print(i)
# ➢ Output → 2,3,4,5,6,7,8
# ______________
# In C Language
# for(int i = 0 ; i <=3 ; i++){
# printf(i)
# }
# ➢ Step 1: initialization ( int i = 0 )
# ➢ Step 2: Condition check ( i <= 3 )
# ➢ Step 3: if condition is true , enter in the loop and execute the code
# ----print(i)-----
# ➢ Step 4: increment or Decrement i ( i++ )
# Loop Execution Steps:
# Phase1:
# ➢ Step 1: initialization ( int i = 0 )
# ➢ Step 2: Condition check ( i <= 3 ) , ( 0 <= 3 ) → True ➢ Step 3: condition is true , enter in the loop and execute the code print(i)
# output → 0
# ➢ Step 4: Increment or Decrement i ( i++ ) , 0++ => 1 → i becomes 1.
# ______________
# Phase2:
# ➢ Step 1: initialization ( i = 1 )
# ➢ Step 2: Condition check ( i <= 3 ) , ( 1 <= 3 ) → True
# ➢ Step 3: condition is true , enter in the loop and execute the code print(i)
# output →1
# ➢ Step 4: Increment or Decrement i ( i++ ) , 1++ → 1 → i becomes 2.
# ______________
# Phase3:
# ➢ Step 1: initialization ( i = 2 )
# ➢ Step 2: Condition check ( i <= 3 ) , ( 2 <= 3 ) → True
# ➢ Step 3: condition is true , enter in the loop and execute the code print(i)
# output → 2
# ➢ Step 4: Increment or Decrement i ( i++ ) , 2++ => 3 → i becomes 3.
# ______________
# Phase4:
# ➢ Step 1: initialization ( i = 3 )
# ➢ Step 2: Condition check ( i <= 3 ) , ( 3 <= 3 ) → False
# ➢ Step 3: we have to exit immediately from the loop because the condition
# is false .
# ______________
# for i in range(3,31,3):
# print(i) 3,6,9,12,15,18,21,24,27,30
# Output → 3,6,9,12,15,18,21,24,27,30
# Starting point → 3
# Ending point → 31 , excluded
# Gap = 3 , (N-1), 3-1 → 2 we have to skip 2 elements at each iteration
# ______________ Class Task:
# Task: write a program to print a table of 5.
# for i in range(5,51,5):
# print(i)
# ______________
# Task:
# 1. write a program to print the table of 39, 29,33
# 2. give me 3 example of while loop
# 3. write a program to print your name 5 times .
# 4. how to use a for loop in List and String .