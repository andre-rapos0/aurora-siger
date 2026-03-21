TEMP_INT_MIN_C = 18
TEMP_INT_MAX_C = 35
TEMP_EXT_MIN_C = -5
TEMP_EXT_MAX_C = 30
BAT_VOLTAGE_MIN_V = 46
BAT_VOLTAGE_MAX_V = 52
BAT_CURR_MIN_A = 20
BAT_CURR_MAX_A = 120
BAT_SOC_PERC_MIN = 60
BAT_SOC_PERC_MAX = 100
BAT_CAPACITY_MIN_AH = 80
BAT_CAPACITY_MAX_AH = 120
POWER_LOAD_MIN_KW = 5
POWER_LOAD_MAX_KW = 25
ENERGY_LOSS_MIN_PERC = 2
ENERGY_LOSS_MAX_PERC = 8
TANK_PRESSURE_MIN_BAR = 95
TANK_PRESSURE_MAX_BAR = 145
EST_AUTONOMY_MIN_MINUTES = 45

def pronto_para_decolar(telemetria: dict) -> bool:
    """
    Verifica se a aeronave está pronta para decolar baseado em sua telemetria pre-decolagem.
    
    Args:
        telemetria (dict): Dados de telemetria da aeronave.
    
    Returns:
        pronto_para_decolar (bool): Booleano indicando se a aeronave está pronta para decolar.
    """
    if telemetria["telemetry_link_status"] == 0:
        return False

    if telemetria["structural_integrity"] == 0:
        return False

    if telemetria["critical_modules_status"] == 0:
        return False

    temp_int_c = telemetria["internal_temp_c"]
    if temp_int_c < TEMP_INT_MIN_C or temp_int_c > TEMP_INT_MAX_C:
        return False

    temp_ext_c = telemetria["external_temp_c"]
    if temp_ext_c < TEMP_EXT_MIN_C or temp_ext_c > TEMP_EXT_MAX_C:
        return False

    bat_voltage_v = telemetria["battery_voltage_v"]
    if bat_voltage_v < BAT_VOLTAGE_MIN_V or bat_voltage_v > BAT_VOLTAGE_MAX_V:
        return False
    
    bat_curr_a = telemetria["battery_current_a"]
    if bat_curr_a < BAT_CURR_MIN_A or bat_curr_a > BAT_CURR_MAX_A:
        return False
    
    bat_soc_perc = telemetria["battery_soc_percentage"]
    if bat_soc_perc < BAT_SOC_PERC_MIN or bat_soc_perc > BAT_SOC_PERC_MAX:
        return False
    
    bat_capacity_ah = telemetria["battery_capacity_ah"]
    if bat_capacity_ah < BAT_CAPACITY_MIN_AH or bat_capacity_ah > BAT_CAPACITY_MAX_AH:
        return False

    power_load_kw = telemetria["power_load_kw"]
    if power_load_kw < POWER_LOAD_MIN_KW or power_load_kw > POWER_LOAD_MAX_KW:
        return False

    tank_pressure_bar = telemetria["tank_pressure_bar"]
    if tank_pressure_bar < TANK_PRESSURE_MIN_BAR or tank_pressure_bar > TANK_PRESSURE_MAX_BAR:
        return False
    
    estimated_autonomy_min = telemetria["estimated_autonomy_min"]
    if estimated_autonomy_min < EST_AUTONOMY_MIN_MINUTES:
        return False
 
    return True
 

if __name__ == "__main__":
    non_anomaly_value = {
        "timestamp": "2026-03-21 18:52:49.861650",
        "internal_temp_c": 25.33515694993567,
        "external_temp_c": -1.2325490922224986,
        "battery_voltage_v": 51.10111596530898,
        "battery_current_a": 104.91509010963809,
        "battery_soc_percentage": 72.31047043952503,
        "battery_capacity_ah": 119.51826444680256,
        "power_load_kw": 20.136502100590548,
        "energy_loss_percent": 2.8663269828342055,
        "tank_pressure_bar": 138.9312426074094,
        "estimated_autonomy_min": 75.62266421586678,
        "structural_integrity": 1,
        "critical_modules_status": 1,
        "telemetry_link_status": 1,
        "is_anomaly": False,
        "energy_available_kwh": 4.416374051773404
    }

    print("Telemetria sem anomalia")
    if pronto_para_decolar(non_anomaly_value):
        print("PRONTO PARA DECOLAR")

    anomaly_value = {
        "timestamp": "2026-03-21 19:49:49.861650",
        "internal_temp_c": 30.598383950966202,
        "external_temp_c": 11.918259714044314,
        "battery_voltage_v": 49.14998227613003,
        "battery_current_a": 101.56128568994593,
        "battery_soc_percentage": 69.20588494301296,
        "battery_capacity_ah": 93.3714159680801,
        "power_load_kw": 11.484318204518203,
        "energy_loss_percent": 2.0917276301398458,
        "tank_pressure_bar": 142.30680898590666,
        "estimated_autonomy_min": 174.56062914654635,
        "structural_integrity": 1,
        "critical_modules_status": 1,
        "telemetry_link_status": 0,
        "is_anomaly": True,
        "energy_available_kwh": 3.1759988524375737
    }

    print("Telemetria com anomalia")
    if pronto_para_decolar(non_anomaly_value):
        print("DECOLAGEM ABORTADA")