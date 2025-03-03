class Polynomial:
    def __init__(self, coefficients):
        """
        Initialize the polynomial with a list of coefficients.
        coefficients[i] is the coefficient for the x^i term.
        """
        self.coefficients = coefficients

    def __repr__(self):
        """
        Return a string representation of the polynomial.
        """
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff != 0:
                terms.append(f"{coeff}*x^{power}")
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        """
        Add two polynomials.
        """
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                new_coeffs[i] += self.coefficients[i]
            if i < len(other.coefficients):
                new_coeffs[i] += other.coefficients[i]
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        """
        Subtract two polynomials.
        """
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                new_coeffs[i] += self.coefficients[i]
            if i < len(other.coefficients):
                new_coeffs[i] -= other.coefficients[i]
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        """
        Multiply two polynomials.
        """
        new_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, self_coeff in enumerate(self.coefficients):
            for j, other_coeff in enumerate(other.coefficients):
                new_coeffs[i + j] += self_coeff * other_coeff
        return Polynomial(new_coeffs)

    def evaluate(self, x):
        """
        Evaluate the polynomial at a given value of x.
        """
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

print(Polynomial([1, 2, 3]))  # 1*x^0 + 2*x^1 + 3*x^2