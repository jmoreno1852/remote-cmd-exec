import websockets
import asyncio
import subprocess
#Que necesito
#Inicializar el servidor con websockets
#Recibimos el comando en el socket -> Display en caso de que se ejecute ->
async def server(s):
    cmd = await s.recv()
    (exitcode, output) = subprocess.getstatusoutput(cmd) #If negative -> Has finished
    print(f"CMD> {output}")
    #
    await s.send(str(exitcode))




