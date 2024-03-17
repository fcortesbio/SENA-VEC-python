import unittest
    
import numpy as np
from main import rand_clock, weapons
from scipy.stats import chisquare

# weapons = [".", "-", "+", "*", "T", "Y", "|", "W", "X", "M"]

# Pruebas para rand_clock()
class TestRandClock(unittest.TestCase):
    
    # Evaluar si la longitud de la cadena coincide con el parámetro especificado
    def test_lenght_(self):
        times = 20
        result = rand_clock(times)
        self.assertEqual(len(result), times)
        
    # Evaluar si todos los caracteres generados son válidos
    def test_validity(self):
        result = rand_clock(100)
        for character in result:
            self.assertIn(character, weapons)
    
    def test_character_distribution(self):
    # Evaluar la aleatoriedad a partir de la distribución de caracteres en una muestra aleatoria
        
        # generar una muestra de 100 caracteres
        sample = rand_clock(100)
        print(sample)
        
        # contar la frecuencia de cada caracter en la cadena generada
        char_counts = {char: sample.count(char) for char in set(sample)}
        print(char_counts)
        
        # calcular la frecuencia esperada asumiendo una distrubución uniforme
        expected_fq = len(sample) / len(char_counts)
        print(f"expected frequency: {expected_fq}")
        
        # calcular las frecuencias observadas y esperadas
        observed_fq = np.array(list(char_counts.values()))
        expected_fq_array = np.full_like(observed_fq, expected_fq)
        print(observed_fq)
        print(expected_fq_array)
                
        # Realizar la prueba Chi-cuadrado
        chi2_statistic, p_value = chisquare(observed_fq, f_exp=expected_fq_array)
        print(p_value, chi2_statistic)
        
        # Evaluar la significancia del p-valor por encima de 0.05
        self.assertGreater(p_value, 0.05) 
            

if __name__ == "__main__":
    unittest.main()
    
        
