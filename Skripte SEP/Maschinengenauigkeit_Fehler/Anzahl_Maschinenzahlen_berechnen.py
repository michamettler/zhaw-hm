def calculate_max_machine_numbers(mantissa_bits, exponent_bits, base, vorzeichen):
    # Die erste Stelle der Mantisse ist immer 1, daher gibt es base^(mantissa_bits-1) Möglichkeiten für die Mantisse.
    # Es gibt 2 Möglichkeiten für das Vorzeichen (positiv und negativ).
    # Für den Exponenten gibt es base^exponent_bits Möglichkeiten, abzüglich 1, da die Null doppelt gezählt wird.
    # Schließlich fügen wir 1 hinzu für die Darstellung der Zahl 0.
    if vorzeichen: 
        mantissa_count = base ** (mantissa_bits)
    else:
        mantissa_count = base ** (mantissa_bits - 1)
    print(mantissa_count)
        
    if vorzeichen: 
        exponent_count = (base ** (exponent_bits+1)) - 1
    else:
        exponent_count = (base ** exponent_bits)
    print(exponent_count)

    total_numbers = (mantissa_count * exponent_count) + 1  # +1 für die Zahl 0

    return total_numbers, mantissa_count, exponent_count



# Beispielaufruf der Funktion mit der Basis 2 für das binäre System
number_of_machine_numbers, mantissa_count, exponent_count = calculate_max_machine_numbers(mantissa_bits=2, exponent_bits=1, base=2, vorzeichen=True)
print(f"Anzahl verschiedener Maschinenzahlen: {number_of_machine_numbers}, Anz. Mantissa {mantissa_count} * Anz. Mantissa {exponent_count} + 1 für die Zahl 0")
