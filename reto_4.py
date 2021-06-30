def validar_clave (empleados: list):
    salida = []
    for empleado in empleados: 
        clave = ''
        for caracter in list(map(chr, list(map(int, empleado['clave'].split('-'))))):
            clave+=caracter
        cond = []
        cond.append(len(list(filter(lambda x: x.isupper(), list(clave))))>=2)
        cond.append(len(list(filter(lambda x: x.islower(), list(clave))))>=2)
        cond.append(len(list(filter(lambda x: x.isdigit(), list(clave))))>=2)
        num_se = []
        num = list(map(int, list(filter(lambda x: x.isdigit(), list(clave)))))
        for i in range(0,len(num)-1):
            if (num[i+1]-1 == num[i] or num[i+1]+1 == num[i]):
                num_se.append(True)
        cond.append(len(num_se)==0)
        cond.append(len(clave)==len(set(clave)))
        cond.append(len(list(filter(lambda x: not(x.isalnum()),list(clave))))>0)
        cond.append(len(clave)>=7)
        salida.append((empleado['cod_empleado'],all(cond)))
    return salida
    
empleados = [
{'cod_empleado': 'EMPL_001', 'clave': '65-76-64-114-53-55-109'},
{'cod_empleado': 'EMPL_002','clave': '68-80-38-99-48-57-116'}, 
{'cod_empleado':'EMPL_003', 'clave': '70-84-42-49-51-109-114'}
]


print(validar_clave(empleados))