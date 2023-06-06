"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е деллив со 3, 5, 3 и 5, 
а потоа ќе испечати соодветната порака."""

broj=int(input("Внесете еден број. "))
zbir=0
razlika=0
proizvod=1
if broj%3==0:
    print(f"Бројот {broj} е деллив со 3. ")
else:
    print(f"бројот {broj} не е деллив со 3. ")
if broj%5==0:
    print(f"Бројот {broj} е деллив со 5. ")
else:
    print(f"Бројот {broj} не е деллив со 5. ")
if broj%3==0 and broj%5==0:
    print(f"бројот {broj} е деллив со 3 и 5. ")
else:
    print(f"brojot {broj} ne e delliv so 3 i so 5. ")