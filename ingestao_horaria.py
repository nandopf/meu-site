import os
import time
from datetime import datetime
from supabase import create_client

# --- CONFIGURAÇÕES ---
URL = "https://ptunjhmkickwuiyxufhv.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB0dW5qaG1raWNrd3VpeXh1Zmh2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1OTg1OTUsImV4cCI6MjA5MzE3NDU5NX0.ASh37T-ZHHnFTk_yWLQnWNv91l0AOeUW_1Tj9F-8KD0" 

supabase = create_client(URL, KEY)

def get_cpu_temp():
    try:
        res = os.popen('vcgencmd measure_temp').readline()
        if not res: return 0.0
        return float(res.replace("temp=","").replace("'C\n",""))
    except: return 0.0

def ler_sensores_quarto():
    return {"temperatura": 25.5, "humidade": 62.0}

def ler_sensores_fermentador():
    return {"sensor_1_temp": 18.2, "sensor_2_temp": 15.8}

def ler_sensores_hidroponia():
    # Placeholder para sensores de pH, Temp Água e Nutrientes
    return {"ph": 6.0, "temp_agua": 22.5, "nutrientes_ppm": 850}

def ler_sensores_lupulo():
    # Placeholder para sensores de Solo e Válvula
    return {"humidade_solo": 45.0, "temp_solo": 20.5, "valvula_status": False}

def enviar_dados():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{agora}] Executando envio agendado...")
    
    try:
        cpu = get_cpu_temp()
        
        # P1: Quarto
        dq = ler_sensores_quarto(); dq["cpu_temp"] = cpu
        supabase.table("temperatura_quarto").insert(dq).execute()
        
        # P2: Fermentador
        df = ler_sensores_fermentador(); df["cpu_temp"] = cpu
        supabase.table("temperatura_fermentador").insert(df).execute()

        # P3: Hidroponia
        dh = ler_sensores_hidroponia(); dh["cpu_temp"] = cpu
        supabase.table("hidroponia").insert(dh).execute()

        # P4: Lúpulo
        dl = ler_sensores_lupulo(); dl["cpu_temp"] = cpu
        supabase.table("lupulo").insert(dl).execute()
        
        print(f"[{agora}] ✅ Todos os projetos atualizados com sucesso!")
    except Exception as e:
        print(f"[{agora}] ❌ Erro: {e}")

if __name__ == "__main__":
    enviar_dados()
