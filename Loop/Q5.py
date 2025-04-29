
#CP5
def generate_pythagorean_triplets(limit):
    print(f"Pythagorean Triplets with side length ≤ {limit}:")
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c = (a*2 + b2)*0.5
            if c.is_integer() and c <= limit:
   
generate_pythagorean_triplets(30)
