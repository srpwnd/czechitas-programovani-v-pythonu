# Pokud pečete podle anglických receptů, 
# často se po váš požaduje rozehřát troubu na uvedenou teplotu. 
# Pokud si ovšem neuvědomíte, že Američané používají pro měření teploty 
# stupně Fahrenheita namísto Celsia, bude vás na konci pečení čekat nemilé překvapení.

# Nastudujte si na České Wikipedii jak se převádějí stupně Fahrenheita na stupně Celsia 
# a napište program, který takový převod provede. Váš program se zeptá uživatele na teplotu 
# ve stupních Fahrenheita a vypíše její ekvivalent ve stupních Celsia.

fahrenheit = float(input("Zadej teplotu ve stupnich Fahrenheita: "))

celsius = (fahrenheit - 32) * 5/9

print(f"Teplota {fahrenheit}°F odpovida teplote {celsius}°C")