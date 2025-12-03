def speed():
    print("\n--- Calculate Speed (v = d / t) ---")
    d = float(input("Enter distance (meters): "))
    t = float(input("Enter time (seconds): "))
    if t == 0:
        print("Time cannot be zero!")
    else:
        v = d / t
        print("Speed = ", v, "m/s")

def force():
    print("\n--- Calculate Force (F = m * a) ---")
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    F = m * a
    print("Force = ", F, "Newtons")

def kinetic_energy():
    print("\n--- Calculate Kinetic Energy (KE = 1/2 * m * v²) ---")
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    KE = 0.5 * m * (v ** 2)
    print("Kinetic Energy = ", KE, "Joules")

def ohms_law():
    print("\n--- Calculate Voltage (V = I * R) ---")
    I = float(input("Enter current (Amps): "))
    R = float(input("Enter resistance (Ohms): "))
    V = I * R
    print("Voltage = ", V, "Volts")

def density():
    print("\n--- Calculate Density (ρ = m / V) ---")
    m = float(input("Enter mass (kg): "))
    V = float(input("Enter volume (m³): "))
    if V == 0:
        print("Volume cannot be zero!")
    else:
        D = m / V
        print("Density = ", D, "kg/m³")


# ---------------- MAIN PROGRAM ----------------

while True:
    print("\n===== PHYSICS FORMULA CALCULATOR =====")
    print("1. Speed (v = d / t)")
    print("2. Force (F = m * a)")
    print("3. Kinetic Energy (KE = 1/2 * m * v²)")
    print("4. Ohm's Law (V = I * R)")
    print("5. Density (ρ = m / V)")
    print("6. Exit")

    choice = input("\nSelect a formula (1–6): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
