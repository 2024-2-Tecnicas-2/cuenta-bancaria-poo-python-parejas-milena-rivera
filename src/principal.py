if __name__ == '__main__':
    cuenta = CuentaBancaria('Isaac Rivera ', '507232755 ', 1000.0)

    print(f"Titular: {cuenta.get_titular()}")
    print(f"Número de cuenta: {cuenta.get_numero_cuenta()}")
    print(f"Saldo actual: {cuenta.get_saldo()}")

    cuenta.ingresar(500.0)
    print(f"Saldo después de ingresar 500.0: {cuenta.get_saldo()}")

    cuenta.retirar(300.0)
    print(f"Saldo después de retirar 300.0: {cuenta.get_saldo()}")

    try:
        cuenta.retirar(1500.0)
    except ValueError as e:
        print(e)

    cuenta.set_tipo_interes(2.0)
    saldo_con_interes = cuenta.calcular_interes()
    print(f"Saldo con el interés del 2% aplicado: {saldo_con_interes}")

    try:
        cuenta.set_tipo_interes(15.0)
    except ValueError as e:
        print(e)