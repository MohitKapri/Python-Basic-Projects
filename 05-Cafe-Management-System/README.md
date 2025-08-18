# 🍽️ Cafe Billing System

This is a simple **Cafe Billing System** built in Python.  
The program allows users to order items from a menu, add multiple items, and view the final bill with an order summary.  

---

## 📌 Features
- Predefined menu with item names and prices.  
- Users can order multiple items.  
- Keeps track of all ordered items.  
- Displays a full order summary before showing the total bill.  

---

## 🛠️ How It Works
1. The menu is displayed at the start.  
2. The user enters the item name they want to order.  
3. If the item is available in the menu:
   - It is added to the order list.  
   - The total bill is updated.  
4. If the item is not available:
   - A message is shown that the item is unavailable.  
5. After each order, the program asks if the user wants to add another item.  
6. When the user says **No**, the final order summary and total bill are displayed.  

---

## 📜 Example Output
```
WELCOME TO OUR CAFE
Pizza:Rs-100
Momo:Rs-80
Choumine:Rs-50
Burger:Rs-60
Spring roll:Rs-70

Enter the name of the item you want to order = Pizza
✅ Your item Pizza has been added to your order!
Do you want to add another thing to your list? (Yes/No): Yes
Enter the name of the item you want to order = Momo
✅ Your item Momo has been added to your order!
Do you want to add another thing to your list? (Yes/No): No

🧾 Your Order Summary:
- Pizza: Rs 100
- Momo: Rs 80

💰 The total amount you have to pay is Rs 180
```

---

## 🚀 Future Enhancements
- Add **quantity selection** (e.g., 2 Pizzas).  
- Apply **discounts/offers**.  
- Save bills to a **file**.  
- Add GST/Taxes.  
