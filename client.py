import pygame
import pygame.midi as midi 
import asyncio
import snapcast.control

### CONFIG 
server_ip = "10.42.0.190"
clientid_1 = "8e81967f-3259-44e7-8fae-110938afaf97"
# clientid_2
# clientid_3
# clientid_4
###

# init and check device is connected
midi.init()
if midi.get_count() == 0:
    exit()

# set up server and event loop.. 
loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, '10.42.0.190'))

# # print all client names 
# for client in server.clients:
#   print(client.friendly_name)

# set up object for midi input
things = midi.Input(device_id=0)

# the main event  
while True:
    if things.poll():
        Data1 = things.read(1000)[0:1][0][0]
        print(Data1)
        pygame.time.wait(10)
        knob = Data1.pop(1)
        value = Data1.pop(1)
        if knob == 1:
            loop.run_until_complete(server.client_volume(clientid_1, {'percent': value, 'muted': True}))

        

