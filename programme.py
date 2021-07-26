from threading import Thread, Condition
import time
import random
import sched, time
s = sched.scheduler(time.time, time.sleep)



queue = []
MAX_NUM=int(input("Entrer le nombre maximun d'élément à produire: "))
nombre_producteur=int(input("Entrer le nombre de producteur a initiliser: "))
nombre_consomateur=int(input("Entrer le nombre de consommateur a initiliser: "))

i_pro=0
i_cons=0
condition = Condition()

class Producteur(Thread):
    def run(self):
        nums = range(5)
        global queue
    
        while True:
            def do_something(sc):

                condition.acquire()
                if len(queue) == MAX_NUM:
                    # print ("Ma queu est remplit,le producteur est en attente")
                    condition.wait()
                    
                    # print ("Espace présent dans la queu, le consommateur notifie le producteur")
                else:

                    num = random.choice(nums)
                    queue.append(num)
                    print ("Production de ", num)
                # print("Queu après production : ",queue)
                condition.notify()
                condition.release()
                time.sleep(random.random())

                s.enter(2, 1, do_something, (sc,))
            s.enter(2, 1, do_something, (s,))
            s.run()



class Consomateur(Thread):
    def run(self):
        global queue
        
        while True:
            def do_something(sc): 
                condition.acquire()
                if not queue:
                    # print ("La queue est vide le consommateur attend")
                    condition.wait()
                    # print ("Le producteur vient de produit et le notifi au consommateur")
                num = queue.pop(0)
                print ("Conosmmation de :", num)
                # print("Queu après consommation : ",queue)
                condition.notify()
                condition.release()
                time.sleep(random.random())
                s.enter(6, 1, do_something, (sc,))
            s.enter(6, 1, do_something, (s,))
            s.run()


while i_pro<nombre_producteur:
    Producteur().start()
    i_pro=i_pro+1

while i_cons<nombre_consomateur:
    Consomateur().start()
    i_cons=i_cons+1

def do_something(sc): 
    global queue
    print("Le contenu de la queu est",queue)
    # do your stuff
    s.enter(1, 1, do_something, (sc,))
s.enter(1, 1, do_something, (s,))
s.run()

