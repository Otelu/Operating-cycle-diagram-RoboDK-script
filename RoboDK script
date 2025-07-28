from robodk import robolink 
import csv
import time 

RDK = robolink.Robolink() 
robot = RDK.Item('', robolink.ITEM_TYPE_ROBOT)

with open('diagram_6axe.csv', mode='w', newline='') as file: 
  writer = csv.writer(file) 
  writer.writerow(['Iteration', 'J1 [°]', 'J2 [°]', 'J3 [°]', 'J4 [°]', 'J5 [°]', 'J6 [°]']) 
  
  i = 1
  print("Regidtering robot positions. Press Ctrl+C to stop.") 
  try: 
      while True: 
            joints = robot.Joints().list() 
            print(f"Iteration {i}, positions: {joints}") 
            if len(joints) == 6: 
                writer.writerow([i] + joints)
                file.flush() 
                i += 1 
            time.sleep(0.5) 
    except KeyboardInterrupt: 
        print("\nRegistering was stopped.")   
print("Diagram saved as 'diagram_6axe.csv'")
