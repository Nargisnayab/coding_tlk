break`**: Exits the loop immediately.  
- **`continue`**: Skips the rest of the code in the current iteration and goes to the next one.  

🔹 **Example using `break` and `continue`:**  
```python
for num in range(1, 6):
    if num == 3:
        continue  # Skip printing 3
    if num == 5:
        break  # Stop the loop when num is 5
    print(num)
```
🔹 **Output:**  
```
1  
2  
4  
```

---
