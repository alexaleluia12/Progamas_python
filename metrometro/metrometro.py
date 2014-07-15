from threading import Thread
#import winsound
import time
class Metrometro(Thread):

    def __init__(self, frequencia):
        self.frequencia = frequencia
        Thread.__init__(self)
        self.pare = True

 
    def run(self):    
        while self.pare:
            winsound.Beep(1000, 100)
                    
            time.sleep(60.0/self.frequencia)
            


def testeMetrometro():
    metrometro = Metrometro(30)
    metrometro.start()
    input('enter to stop')
    metrometro.pare = False
    


if __name__ == '__main__':
    testeMetrometro()
    
        
