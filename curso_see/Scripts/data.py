import pandas as pd

def get_transacciones_x_pais():
    transacciones = pd.read_excel('../Data/transacciones_202008.xlsx', sheet_name = 'Sheet1')
    transacciones["InvoiceDate"] = pd.to_datetime( transacciones["InvoiceDate"] )    
    transacciones['anio'] = transacciones.InvoiceDate.dt.year
    transacciones['mes'] = transacciones.InvoiceDate.dt.month
    transacciones['periodo'] = transacciones.InvoiceDate.dt.year * 100 + transacciones.InvoiceDate.dt.month
    transacciones['venta_usd'] = transacciones.Quantity * transacciones.UnitPrice
    paises = transacciones.groupby(['Country', 'anio']).apply(
        lambda x: (x.Quantity * x.UnitPrice).sum()
    ).reset_index(name='venta_usd')
    transacciones_x_pais = transacciones.groupby(['Country', 'anio', 'mes']).apply(
        lambda x: (x.Quantity * x.UnitPrice).sum()
    ).reset_index(name='venta_usd')
    
    return (paises, transacciones_x_pais)