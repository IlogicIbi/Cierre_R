import os

# Obtener la ruta del escritorio
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Crear la ruta completa del archivo
file_path = os.path.join(desktop_path, "instalacion.txt")

# Pregunta el número de OT y si es NEBA
numero_ot = input("Introduce el número de OT: ")
es_neba = input("¿La instalación es NEBA? (s/n): ")

# Variable global retirar CM
retirar_cm = ""

#defines funcion para escribir
def global_cm():
    global retirar_cm




# Variable global retirar Deco HD
retirar_deco_hd = ""

# Definir una función global de retirar deco para llamar a la variable fuera del If
def global_deco_hd():
    # Acceder a la variable global
    global retirar_deco_hd

# Abrir el archivo en modo de escritura (si no existe, se crea)
with open(file_path, "w") as file:
    # Registrar número de OT y si es NEBA
    file.write(f"Número de OT: {numero_ot}\n")

    # Preguntar sobre la instalación precableada
    instalacion_precableada = input("¿La instalación es precableada? (s/n): ")

    sn_retro=input("¿Es retrofit? (s/n): ")
        
    if instalacion_precableada.lower() == "s":
        cableada_por = input("¿Quien precableo? ")
        file.write(f"Instalación precableada por {cableada_por}\n")

    # Preguntar sobre la reasignación del CTO
    reasignar_cto = input("¿Se reasigna la CTO? (s/n): ")
      
    if reasignar_cto.lower() == "s":
        cto_habia = input("¿Qué CTO había anteriormente? ")
        cto_nueva = input("¿Qué CTO se instala ahora? ")
        puerto = input("¿En qué puerto se reasigna? ")
        file.write(f"Se reasigna CTO de {cto_habia} a {cto_nueva} en el puerto {puerto}\n")

        # Preguntar sobre la acometida exterior
    if instalacion_precableada.lower() == "n":
        acometida_exterior = input("¿Se instala acometida exterior? (s/n): ")

        if acometida_exterior.lower() == "s":
            acometida_uso = input("¿Qué tipo de acometida se utilizó? (huawei/corning/zte): ")
            acometida_total = input("¿Cuántos metros era la acometida? ")
            acometida_utilizada = input("¿Cuántos metros de acometida se utilizaron? ")
            file.write(f"Se instala acometida exterior {acometida_uso} de {acometida_total} metros y se utilizan {acometida_utilizada} metros\n")
    
        if instalacion_precableada.lower() == "n" and acometida_exterior.lower() == "n":
            # Preguntar sobre la acometida interior
            acometida_total_interior = input("¿De cuantos metros era la acometida de interior? ")
            acometida_utilizada = input("¿Cuantos metros de acometidad de interior se utilizaron? ")
            file.write(f"Se instala acometida interior de {acometida_total_interior} metros y se utilizan {acometida_utilizada} metros\n")

    file.write("Se instalan equipos en ubicaciones indicadas por el cliente.\n")

    if es_neba.lower() == "s":
        # Preguntar sobre la ONT y el Router
        modelo_ont = input("Introduce el modelo de ONT: ")
        mac_ont = input("Introduce la MAC de la ONT: ")
        modelo_router = input("Introduce el modelo de Router: ")
        mac_router = input("Introduce la MAC del Router: ")
        serial_router = input("Introduce el serial del Router: ")
        file.write(f"Se instala ONT {modelo_ont} con MAC {mac_ont}.\n ")
        file.write(f"Se instala Router {modelo_router} con MAC {mac_router} y serial {serial_router}.\n")
    else:
        # Preguntar sobre la MAC y el serial del Router
        router_noneba =input("Dime el modelo del Router: ")
        mac_router = input("Introduce la MAC del Router: ")
        serial_router = input("Introduce el serial del Router: ")
        file.write(f"Se instala Router {router_noneba} con MAC {mac_router} y serial {serial_router}.\n")

    # Preguntar sobre la retirada de CM o Deco HD
    if sn_retro.lower()=="s":
        retirar_cm = input("¿Se retira un CM? (s/n): ")
    
        if retirar_cm.lower() == "s":
            modelo_cm = input("Introduce el modelo del CM: ")
            mac_cm = input("Introduce la MAC del CM: ")
            file.write(f"Se retira CM {modelo_cm} con MAC {mac_cm}.\n")

        retirar_deco_hd = input("¿Se retira un Deco HD? (s/n): ")

        if retirar_deco_hd.lower() == "s":
            modelo_deco_hd = input("Introduce el modelo del Deco HD: ")
            caid_deco_hd = input("Introduce el CAID del Deco HD: ")
            file.write(f"Se retira Deco HD {modelo_deco_hd} con CAID {caid_deco_hd}.\n")

    instalar_decodificador = input("¿Se ha instalado decodificador? (s/n): ")
    

    if instalar_decodificador.lower() == "s":
        modelo_decodificador = input("Introduce el modelo del decodificador: ")
        caid_decodificador = input("Introduce el CAID del decodificador: ")
        file.write(f"Se instala decodificador 4K {modelo_decodificador} con CAID {caid_decodificador}.\n")

    instalar_wifimesh = input("¿Se ha instalado WiFiMesh? (s/n): ")

    if instalar_wifimesh.lower() == "s":
        serial1_wifimesh = input("Serial WIFIMESH 1: ")
        serial2_wifimesh = input("Serial WIFIMESH 2: ")
        file.write(f"Se instala pareja WiFi Mesh con serial {serial1_wifimesh} y {serial2_wifimesh}.\n")

    conectar_tomas_telefono = input("¿Se dejan conectadas las tomas de teléfono? (s/n): ")

    if conectar_tomas_telefono.lower() == "no":
        file.write("No se dejan conectadas las tomas de teléfono a la ONT a petición del cliente.\n")
    else:
        file.write("Se dejan conectadas las tomas de teléfono a la ONT a petición del cliente.\n")

    instalar_cable_telefono = input("¿Se ha instalado cable de telefono? (s/n): ")

    if instalar_cable_telefono.lower() == "s":
        metros_cable = input("Introduce metros de cable de telefono: ")
        file.write(f"Se instala cable de telefono de {metros_cable} m.\n")

    instalar_cable_datos = input("¿Se ha instalado cable de datos? (s/n): ")

    if instalar_cable_datos.lower() == "s":
        metros_cable_datos = input("Introduce metros de cable de datos: ")
        file.write(f"Se instala cable de datos de {metros_cable_datos} m.\n")

    link_speedtest = input("Introduce el enlace del Speedtest: ")
    link_kiron_ftth = input("Introduce el enlace de Kiron FTTH: ")
    link_voip = input("Introduce el enlace de VoIP: ")
    file.write(f"Link Speedtest: {link_speedtest}\n")
    file.write(f"Link Kiron FTTH: {link_kiron_ftth}\n")
    file.write(f"Link VoIP: {link_voip}\n")

    if instalar_decodificador.lower() == "s":
        link_kirontv4k = input("Introduce el enlace de KironTV4K: ")
        file.write(f"Link KironTV4K: {link_kirontv4k}\n")
    
    file.write(f" \n")

    file.write(f"--------------------Aqui van los enlaces de ulises--------------------\n")
    
    file.write(f" \n")
    
    if es_neba.lower() == "s":
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?instalado={mac_router}&returnwa=instalado&nordenBC={numero_ot}\n")
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?instalado={mac_ont}&returnwa=instalado&nordenBC={numero_ot}\n")
    
    if instalar_decodificador.lower() == "s":
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?instalado={caid_decodificador}&returnwa=instalado&nordenBC={numero_ot}\n")
    
    if instalar_wifimesh.lower() == "s":
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?instalado={serial1_wifimesh}&returnwa=instalado&nordenBC={numero_ot}\n")
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?instalado={serial2_wifimesh}&returnwa=instalado&nordenBC={numero_ot}\n")
    
    if retirar_deco_hd.lower() == "s":
        global_deco_hd()
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?retirado={caid_deco_hd}&returnwa=masmovil&nordenBC={numero_ot}&TipoEquipoRetirado=1595&TipoRecogida=1\n")
    
    if retirar_cm.lower() == "s":
        global_cm()
        file.write(f"https://ulises2.obremo.es/obremowa/movil/mEquiposMundoRReportados.aspx?retirado={mac_cm}&returnwa=masmovil&nordenBC={numero_ot}&TipoEquipoRetirado=1595&TipoRecogida=1\n")

    # Mostrar un mensaje de confirmación
    print(f"El archivo '{file_path}' se ha generado exitosamente.")

