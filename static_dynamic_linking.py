class CuentaBancaria:
    def abono(self):
        return "Abono a cuenta bancaria"
    
class CuentaAhorro(CuentaBancaria):
    def abono(self):
        return "Abono a cuenta ahorro"
    
class CuentaCorriente(CuentaBancaria):
    def abono(self):
        return "Abono a cuenta corriente"
    
b = CuentaBancaria()
a = CuentaAhorro()
c = CuentaCorriente()
a = b

print(b.abono())
print(a.abono())
print(c.abono())

"""  
Python uses a dinamic linking by default, but if we want to switch it to static we can override instances (See line 16).
Static linking -> which method declared it is decised based on the type of the variable explicited.
Dynamic linking -> which method declared it is decised based on type of value within a variable.
"""