print('{:=^25}'.format('desafio14'))
#receba uma temperatura em °C e transforme para °K(kelvin) e °F(fahrenheit)
celsius = float(input('Digite a temperatura em graus Celsius(°C): '))
fahrenheit = (9/5 * celsius) +32
kelvin = 273.15 + celsius
print('-'*8)
print('Graus Celsius : {:.2f}°C\nGraus Kelvin : {:.2f}°K\nGraus fahrennheit : {:.2f}°F'.format(celsius, kelvin, fahrenheit))
print('-'*8)
