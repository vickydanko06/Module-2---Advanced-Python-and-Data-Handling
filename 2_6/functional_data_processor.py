"""
Exercise: Functional Data Processor
Module 2 — Advanced Python & Data Handling
Estimated time: 35 minutes

Objective: Process a list of product dicts using ONLY functional patterns.

RULES:
  - No for-loops with .append() allowed
  - Use: list comprehensions, filter(), map(), sorted(), sum(), dict comprehensions
  - Do NOT modify the original `products` list
"""

products = [
    {"name": "Laptop",      "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price":  39.99, "category": "books",       "in_stock": True},
    {"name": "Headphones",  "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp",   "price":  29.99, "category": "home",        "in_stock": True},
    {"name": "AI Textbook", "price":  89.99, "category": "books",       "in_stock": True},
    {"name": "Monitor",     "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook",    "price":   4.99, "category": "office",      "in_stock": True},
    {"name": "Keyboard",    "price":  79.99, "category": "electronics", "in_stock": False},
]


# ============================================================
# Task 1 — Get all in-stock products
# Pattern: filter() keeps only items where the predicate returns True.
# filter() returns a lazy iterator — wrap in list() to materialise.
# ============================================================

# TODO: in_stock = list(filter( lambda ... , products ))
in_stock = list(filter(lambda p: p["in_stock"], products))

print("=" * 60)
print("Task 1 — In-stock products (filter)")
print("=" * 60)
for p in (in_stock or []):
    print(f"  {p['name']}")


# ============================================================
# Task 2 — Add a "discounted_price" field (10% off)
# Pattern: map() transforms every item.
# Use {**p, "discounted_price": ...} to create a NEW dict — do NOT mutate p.
# ============================================================

# TODO: discounted = list(map( lambda p: {**p, "discounted_price": ...}, products ))
discounted = list(map(lambda p: {**p, "discounted_price": p["price"] * 0.9}, products))

print("\n" + "=" * 60)
print("Task 2 — Discounted prices (map, no mutation)")
print("=" * 60)
for p in (discounted or []):
    print(f"  {p['name']:<15} original=${p['price']:>7.2f}  discounted=${p.get('discounted_price', '?'):>7}")


# ============================================================
# Task 3 — Only electronics under $200
# Pattern: filter() with TWO conditions in the lambda (use 'and').
# ============================================================

# TODO: cheap_electronics = list(filter( lambda p: ... and ... , products ))
cheap_electronics = list(filter(lambda p: p["category"] == "electronics" and p["price"] < 200, products))

print("\n" + "=" * 60)
print("Task 3 — Electronics under $200 (filter, two conditions)")
print("=" * 60)
for p in (cheap_electronics or []):
    print(f"  {p['name']:<15} ${p['price']:.2f}")


# ============================================================
# Task 4 — Sort all products by price, lowest first
# Pattern: sorted() with a key= lambda. sorted() never modifies the original.
# ============================================================

# TODO: by_price = sorted(products, key=lambda p: ...)
by_price = sorted(products, key=lambda p: p["price"]) 

print("\n" + "=" * 60)
print("Task 4 — All products sorted by price (sorted + key lambda)")
print("=" * 60)
for p in (by_price or []):
    print(f"  ${p['price']:>7.2f}  {p['name']}")


# ============================================================
# Task 5 — Total value of all in-stock products
# Pattern: sum() with a generator expression inside.
# A generator expression: sum(expression for item in iterable if condition)
# ============================================================

# TODO: total_value = sum( p["price"] for p in products if ... )
total_value = sum(p["price"] for p in products if p["in_stock"])

print("\n" + "=" * 60)
print("Task 5 — Total in-stock value (sum + generator expression)")
print("=" * 60)
print(f"  Total: ${total_value}" if total_value else "  Not implemented yet")


# ============================================================
# Task 6 — Group products by category
# Pattern: dict comprehension.
# Collect unique categories with a set comprehension first,
# then build a dict mapping each category to its list of products.
# ============================================================

# TODO:
# categories = {p["category"] for p in products}   # set comprehension
# grouped = {
#     cat: [p for p in products if p["category"] == cat]
#     for cat in sorted(categories)
# }
grouped = {cat: [p for p in products if p["category"] == cat] for cat in sorted({p["category"] for p in products})}

print("\n" + "=" * 60)
print("Task 6 — Products grouped by category (dict comprehension)")
print("=" * 60)
for cat, items in (grouped or {}).items():
    names = ", ".join(p["name"] for p in items)
    print(f"  {cat:<12}: {names}")

print(f"\nOriginal products list unchanged: {len(products)} items")