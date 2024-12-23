class Settings3 ():

    def __init__(self):
        
        #configuracion de pantalla
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (0, 0, 255)


        #configuracion coete

        self.velocidad_cohete = 1



        #Configuración ballas
        
        self.bala_width = 15
        self.bala_heigth = 3
        self.bala_color = (255, 255, 255)
        self.bala_allowed = 5
    
        self.settings_dinamicos()
        self.valor_incremento = 1.2

    def settings_dinamicos(self):
        self.bala_speed_factor = 0.5
        self.velocidad_cuadro = 0.2
        

        
    def incrementar_speed(self):

        self.bala_speed_factor *= self.valor_incremento
        self.velocidad_cuadro *= self.valor_incremento
        