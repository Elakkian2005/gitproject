budget = float(input("Enter total monthly budget: "))

total_expenses = 0

while True:
    entry = input("Enter expense amount (or type done to stop): ")

    if entry == "done":
        break

    total_expenses += float(entry)

balance = budget - total_expenses

print("------------------------------")
print(f"Total Budget  : {budget:.2f}")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Remaining     : {balance:.2f}")
print("------------------------------")

if balance < 500:
    print("⚠️  Warning: Low Funds")
else:
    print("✅ Budget is healthy")
```

---

## ✅ Output — Normal Balance
```
Enter total monthly budget: 10000

Enter expense amount (or type done to stop): 2000
Enter expense amount (or type done to stop): 3500
Enter expense amount (or type done to stop): 1000
Enter expense amount (or type done to stop): done

------------------------------
Total Budget  : 10000.00
Total Expenses: 6500.00
Remaining     : 3500.00
------------------------------
✅ Budget is healthy
```

---

## ✅ Output — Low Funds Warning
```
Enter total monthly budget: 5000

Enter expense amount (or type done to stop): 2000
Enter expense amount (or type done to stop): 1500
Enter expense amount (or type done to stop): 1200
Enter expense amount (or type done to stop): done

------------------------------
Total Budget  : 5000.00
Total Expenses: 4700.00
Remaining     : 300.00
------------------------------
⚠️  Warning: Low Funds
```

---

## ✅ Output — Zero Balance
```
Enter total monthly budget: 3000

Enter expense amount (or type done to stop): 1000
Enter expense amount (or type done to stop): 1000
Enter expense amount (or type done to stop): 1000
Enter expense amount (or type done to stop): done

------------------------------
Total Budget  : 3000.00
Total Expenses: 3000.00
Remaining     : 0.00
------------------------------
⚠️  Warning: Low Funds