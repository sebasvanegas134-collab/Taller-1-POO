class Retencion:
    @staticmethod
    def calculo():
        horas = float(input("Ingrese las horas trabajadas: "))
        PHora = float(input("Ingrese el pago por hora: "))
        SBruto = horas * PHora
        RFuente = 0.125 * SBruto
        SNeto = SBruto - RFuente
        return SBruto, RFuente, SNeto


salario_bruto, retencion_fuente, salario_neto = Retencion.calculo()
print(f"Salario bruto: ${salario_bruto:,.2f}")
print(f"Retención en la fuente: ${retencion_fuente:,.2f}")
print(f"Salario neto: ${salario_neto:,.2f}")
