import websockets
import logging
import asyncio

#Que necesito
#Inicializar el servidor con websockets
#Recibimos el comando en el socket -> Display en caso de que se ejecute ->
async def server(s):
    cmd = await s.recv()
    (exitcode, output) = subprocess.getstatusoutput(cmd) #If negative -> Has finished
    print(f"CMD> {output}")
    #
    await s.send(str(exitcode))


async def main():
    async with s.serve(server,"127.0.0.1" , port=4444):
        await asyncio.Future()


